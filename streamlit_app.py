import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def preprocess_data():
    job_roles = {
        "Data Scientist": "Python, Machine Learning, Statistics, Data Analysis, SQL",
        "ML Engineer": "Python, Deep Learning, TensorFlow, Model Deployment, NLP",
        "Data Analyst": "SQL, Python, Visualization, Business Intelligence, Excel",
        "AI Researcher": "Deep Learning, Neural Networks, Mathematics, Research, Pytorch",
        "Software Engineer": "Java, System Design, Databases, Algorithms, Backend"
    }
    return pd.DataFrame(list(job_roles.items()), columns=['Job Role', 'Skills'])

def compute_similarity(df):
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(", "))
    skill_matrix = vectorizer.fit_transform(df['Skills'])
    return cosine_similarity(skill_matrix)

def recommend_jobs(input_role, df, similarity_matrix):
    if input_role not in df['Job Role'].values:
        return ["Job role not found in the dataset."]
    index = df[df['Job Role'] == input_role].index[0]
    scores = sorted(enumerate(similarity_matrix[index]), key=lambda x: x[1], reverse=True)
    return [df.iloc[i[0]]['Job Role'] for i in scores[1:4]]

# Streamlit App
st.title("Job Role Recommendation Engine")
df = preprocess_data()
similarity_matrix = compute_similarity(df)
input_role = st.selectbox("Select a Job Role", df['Job Role'])
if st.button("Get Recommendations"):
    recommendations = recommend_jobs(input_role, df, similarity_matrix)
    st.write("### Recommended Job Roles:")
    for role in recommendations:
        st.write(f"- {role}")

