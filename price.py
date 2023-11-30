import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set a seed for reproducibility
np.random.seed(42)

# Generate random data for 10 years
years = list(range(2010, 2021))
pollution_levels = np.random.randint(50, 150, size=len(years))

# Create a DataFrame
data = pd.DataFrame({'Year': years, 'Pollution': pollution_levels})

# Streamlit app
st.title('Pollution vs. Year in India')

# Bar chart using Plotly Express
fig = px.bar(
    data,
    x='Year',
    y='Pollution',
    labels={'Pollution': 'Pollution Level'},
    title='Pollution vs. Year in India',
)

# Show the plot using Streamlit
st.plotly_chart(fig)
