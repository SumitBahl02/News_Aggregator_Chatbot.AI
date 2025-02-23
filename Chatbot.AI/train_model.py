from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForSequenceClassification
from datasets import Dataset, DatasetDict
import json
from sklearn.model_selection import train_test_split

# Load dataset
with open('news_headlines_large.json') as f:
    data = json.load(f)

# Convert JSON to a structured dataset
headlines = [item['headline'] for item in data['articles']]
labels = [0 if item['category'] == 'Legitimate' else 1 for item in data['articles']]

# Split dataset into train and validation sets (80% train, 20% validation)
train_texts, val_texts, train_labels, val_labels = train_test_split(headlines, labels, test_size=0.2, random_state=42)

# Convert to Hugging Face Dataset
dataset = DatasetDict({
    "train": Dataset.from_dict({"text": train_texts, "label": train_labels}),
    "validation": Dataset.from_dict({"text": val_texts, "label": val_labels})
})

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

# Tokenization function
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# Tokenize datasets
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Load model
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",  # Now we have an eval dataset!
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],  # Added eval_dataset
)

# Train the model
trainer.train()
trainer.save_model('best_model')
