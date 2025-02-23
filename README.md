# 🚀 AI-Powered News Aggregator & FAQ Chatbot  

Welcome to the **AI-Powered News Aggregator** and **FAQ Chatbot** project! This repository contains two independent applications built using **React.js** for the frontend and **Python (Flask)** for the backend. Below, you'll find everything you need to get started with the project.  

---

## 📂 Project Overview  

### 1. **AI-Powered News Aggregator**  
A web application that processes news headlines, assigns a **Conspiracy Score (0-100%)**, and allows users to test custom headlines dynamically.  

#### Key Features:  
- **Dynamic Headline Analysis:** Enter any headline to get a real-time Conspiracy Score and classification.  
- **CRUD Operations:** Add, update, or delete headlines from the dataset.  
- **NLP Model:** Detects clickbait, misinformation, and neutral news using **TF-IDF** or **transformers**.  

---

### 2. **AI Chatbot for FAQs**  
An intelligent chatbot that provides FAQ responses while detecting and correcting biased or misleading answers in real-time.  

#### Key Features:  
- **Real-Time Bias Detection:** Automatically rephrases overly promotional or biased responses.  
- **FAQ Management:** Add, update, or delete FAQs using CRUD operations.  
- **NLP Similarity Matching:** Retrieves the most relevant FAQ based on user queries.  

---

## 🛠️ Installation  

### Prerequisites  
- **Node.js** (v16 or higher)  
- **Python** (v3.8 or higher)  
- **npm** (Node Package Manager)  

### Steps to Run the Project  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Frontend Dependencies**  
   Navigate to the `frontend` folder and install dependencies:  
   ```bash
   cd frontend
   npm install
   ```

3. **Install Backend Dependencies**  
   Navigate to the `backend` folder and install dependencies:  
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

4. **Run the Backend Server**  
   Start the Flask backend server:  
   ```bash
   python app.py
   ```

5. **Run the Frontend Application**  
   In a new terminal, navigate to the `frontend` folder and start the React app:  
   ```bash
   cd ../frontend
   npm start
   ```

6. **Access the Application**  
   Open your browser and go to:  
   ```bash
   http://localhost:3000
   ```

---

## 📂 Folder Structure  

```plaintext
your-repo-name/  
├── frontend/               # React.js frontend code  
├── backend/                # Flask backend code  
├── datasets/               # JSON datasets for news headlines and FAQs  
├── README.md               # Project documentation  
└── .gitignore              # Git ignore file  
```

---

## 🌐 API Endpoints  

### News Aggregator API  
- **POST /classify-headline**: Classify a headline and return the Conspiracy Score.  
- **GET /headlines**: Fetch all headlines from the dataset.  
- **POST /add-headline**: Add a new headline to the dataset.  
- **PUT /update-headline**: Update an existing headline.  
- **DELETE /delete-headline**: Delete a headline from the dataset.  

### FAQ Chatbot API  
- **POST /ask-question**: Retrieve the most relevant FAQ for a user query.  
- **GET /faqs**: Fetch all FAQs from the dataset.  
- **POST /add-faq**: Add a new FAQ to the dataset.  
- **PUT /update-faq**: Update an existing FAQ.  
- **DELETE /delete-faq**: Delete an FAQ from the dataset.  

---

## 🚀 Deployment  

To deploy the application, follow these steps:  
1. Build the React app:  
   ```bash
   cd frontend
   npm run build
   ```  
2. Deploy the backend using **Heroku**, **Vercel**, or **AWS**.  

---

## 📝 Notes  
- Ensure the backend server is running before starting the frontend.  
- Use the provided JSON datasets (`news_headlines_large.json` and `faq_data_large.json`) for testing.
