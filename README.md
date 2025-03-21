# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

Job Role Recommendation Engine
Approach & Methodology
1.	Data Preparation:
o	A dataset was created with job roles and their respective required skills.
o	The data is stored in a dictionary and converted into a Pandas DataFrame for easy manipulation.
2.	Text Processing:
o	The skills for each job role are treated as a set of words (tokens).
o	CountVectorizer from Scikit-learn is used to convert these textual skills into a numerical format.
3.	Similarity Computation:
o	We use Cosine Similarity to measure the similarity between job roles based on their skills.
o	Cosine similarity calculates the angle between two skill vectors, making it a suitable choice for text-based comparisons.
4.	Recommendation System:
o	For a given input job role, we compute the similarity with all other job roles.
o	The roles are sorted in descending order of similarity.
o	The top three closest roles (excluding the input role itself) are recommended.

