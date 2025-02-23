# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

# Database Model
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50))
    conspiracy_score = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'headline': self.headline,
            'category': self.category,
            'conspiracy_score': self.conspiracy_score
        }

# Initialize NLP Model
model = AutoModelForSequenceClassification.from_pretrained('./best_model')
tokenizer = AutoTokenizer.from_pretrained('./best_model')
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def calculate_conspiracy_score(prediction):
    # Map model output to conspiracy score (0-100)
    if prediction['label'] == 'Conspiracy':
        return round(prediction['score'] * 100, 2)
    elif prediction['label'] == 'Clickbait':
        return round(prediction['score'] * 50, 2)
    return round(prediction['score'] * 20, 2)

# API Endpoints
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    result = classifier(data['headline'])[0]
    return jsonify({
        'score': calculate_conspiracy_score(result),
        'category': result['label'],
        'original_prediction': result
    })

@app.route('/articles', methods=['GET', 'POST'])
def handle_articles():
    if request.method == 'GET':
        return jsonify([article.to_dict() for article in Article.query.all()])

    if request.method == 'POST':
        new_article = Article(
            headline=request.json['headline'],
            category=request.json.get('category', 'Unknown'),
            conspiracy_score=request.json.get('score', 0)
        )
        db.session.add(new_article)
        db.session.commit()
        return jsonify(new_article.to_dict()), 201

@app.route('/articles/<int:id>', methods=['PUT', 'DELETE'])
def handle_article(id):
    article = Article.query.get_or_404(id)

    if request.method == 'PUT':
        article.headline = request.json.get('headline', article.headline)
        article.category = request.json.get('category', article.category)
        article.conspiracy_score = request.json.get('score', article.conspiracy_score)
        db.session.commit()
        return jsonify(article.to_dict())

    if request.method == 'DELETE':
        db.session.delete(article)
        db.session.commit()
        return '', 204

# Initialize Database with Sample Data
@app.before_first_request
def initialize_data():
    db.create_all()
    with open('news_headlines_large.json') as f:
        data = json.load(f)
        for item in data['articles']:
            if item['headline'].strip():
                db.session.add(Article(
                    headline=item['headline'],
                    category=item['category'],
                    conspiracy_score=50 if item['category'] == 'Conspiracy' else 30
                ))
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)