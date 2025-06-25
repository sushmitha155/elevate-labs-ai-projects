# 🎬 Movie Recommendation System

This is a content-based movie recommendation system that suggests similar movies based on genre, keywords, and overview using Natural Language Processing (NLP) techniques. Built as part of the Elevate Labs internship using the TMDB 5000 Movies Dataset.

---

## 📌 Features

- 📄 Preprocessing of movie metadata (overview, genres, keywords)
- ✨ Combines text features into a unified representation
- 🔍 Uses TF-IDF and Cosine Similarity for recommendations
- 🖥️ Interactive Streamlit Web App
- ✅ No user history required (cold-start friendly)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (TF-IDF, Cosine Similarity)
- Streamlit
- Dataset: TMDB 5000 Movies (from Kaggle)

---

## 🗂️ Project Structure

Movie_Recommendation_System/
├── dataset/
│ └── tmdb_5000_movies.csv
├── app.py
├── movie_recommender.ipynb
├── Final_Report.pdf
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run the App

1. Clone this repo:
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

3. Run the Streamlit app:
streamlit run app.py

yaml
Copy
Edit

---

## 💡 Example

Select a movie like `Avatar` and see the system suggest similar titles based on content.

---

## ✨ Future Improvements

- Add poster images via TMDB API
- Improve UI/UX
- Add collaborative filtering for hybrid recommendations

---

## 👩‍💻 Author

- **Sushmitha Gundeboina** | AIML | MRECW | 2026 Batch