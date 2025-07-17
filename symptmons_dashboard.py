import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("cleaned_combined_symptoms.csv")
