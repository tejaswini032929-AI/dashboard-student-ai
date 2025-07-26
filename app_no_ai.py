
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")
st.title("📊 Student Performance Dashboard + 🤖 AI Insights")
st.markdown("**Note:** AI features are currently disabled due to OpenAI API quota limits.")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("students_performance_200.csv")
    return df

df = load_data()

# Dataset preview
st.subheader("📁 Dataset Preview")
st.dataframe(df.tail(10), use_container_width=True)

# Summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Gender-based average scores
st.subheader("📈 Average Scores by Gender")
avg_scores = df.groupby("gender")[["math score", "reading score", "writing score"]].mean()
st.bar_chart(avg_scores)

# Parental education level vs. scores
st.subheader("📚 Parental Education vs. Average Scores")
avg_by_parent_edu = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean()
st.line_chart(avg_by_parent_edu)

# Placeholder for AI Insights (disabled)
st.subheader("❌ AI Insights (Disabled)")
st.warning("AI-based question answering is disabled due to exceeded API quota. Please update your OpenAI API key with an active quota to enable this feature.")
