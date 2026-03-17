# Movie-Genre-Prediction
Machine Learning project to predict movie genres using NLP and classification models

 🎬 Movie Genre Prediction System

 🚀 Overview
This project is an end-to-end Machine Learning + NLP system that predicts the genre of a movie based on its title and structured features.  
It is designed with a **production-ready architecture**, including model training, API development, and deployment.

---

 🎯 Problem Statement
With the exponential growth of content in streaming platforms, automatically classifying movies into genres helps improve:
- Content organization  
- Recommendation systems  
- User experience  

This project aims to build a robust system to **predict movie genres using text and structured data**.

---

 🧠 Solution Approach

 🔹 Data Processing
- Handled missing values and cleaned dataset  
- Converted text fields to string format  
- Encoded categorical variables using Label Encoding  

 🔹 Feature Engineering
- Applied **TF-IDF Vectorization** on movie titles  
- Created structured features from dataset  

 🔹 Modeling
- **Linear SVM** for text classification  
- **Random Forest** for structured data  
- Stratified train-test split to handle class imbalance  

 🔹 Explainability
- Used **SHAP (SHapley Additive exPlanations)** to interpret model predictions  

 🔹 Deployment
- Built UI using **Streamlit**    

---

 🏗️ Project Structure

```
tv-movie-genre-prediction/
│
├── data/
├── notebooks/
├── src/
├── models/
├── app/
├── requirements.txt
└── README.md
```

---

 ⚙️ Installation

```bash
git clone https://github.com/your-username/tv-movie-genre-prediction.git
cd tv-movie-genre-prediction
pip install -r requirements.txt
```

---

 ▶️ Run the Project

 🔹 Train Model
```bash
python main.py
```

 🔹 Run Streamlit App
```bash
streamlit run app/app.py
```

---

 📊 Example

Input:
```
Movie Title: "Avengers Endgame"
```

Output:
```
Predicted Genre: Action
```

---

 ⚡ Challenges Faced
- Empty vocabulary issue in TF-IDF  
- Handling non-string text inputs  
- Long execution time in SHAP  

 ✅ Solutions
- Cleaned and validated text data  
- Used `min_df` in TF-IDF  
- Sampled data for faster SHAP computation  

---

 🚀 Future Improvements
- Use **BERT / Transformers** for better NLP performance  
- Build a **real-time recommendation system**  
- Add user authentication and logging  

---

 🧰 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLP (TF-IDF, SVM)  
- Streamlit  
- SHAP  

---

 📌 Key Highlights
✔ End-to-end ML pipeline  
✔ NLP + Structured data hybrid system  
✔ Production-ready architecture  
✔ Deployed UI  
✔ Explainable AI integration  

---

 👩‍💻 Author
**Akhila Lenka**  
Data Science Enthusiast | Python Developer  

---

 ⭐ If you like this project
Give it a ⭐ on GitHub and share your feedback!


