import nltk
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
from datetime import datetime
import logging
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def clean_medical_text(text):
    """Clean and standardize medical text."""
    if pd.isna(text) or not isinstance(text, str):
        return ""
    
    # Basic text cleaning
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Tokenize and remove stopwords
    try:
        tokens = nltk.word_tokenize(text)
        stop_words = set(nltk.corpus.stopwords.words('english'))
        cleaned_tokens = [token for token in tokens if token not in stop_words]
        return ' '.join(cleaned_tokens)
    except Exception as e:
        logger.error(f"Error in text cleaning: {str(e)}")
        return text

def preprocess_bp(bp):
    """Process blood pressure readings."""
    if not isinstance(bp, str):
        return None
    try:
        # Extract systolic BP from formats like "120/80"
        match = re.match(r'(\d{2,3})/\d{2,3}', bp)
        if match:
            systolic = int(match.group(1))
            if 70 <= systolic <= 220:  # Validate reasonable range
                return systolic
    except Exception as e:
        logger.error(f"Error processing BP: {str(e)}")
    return None

def clean_healthcare_data(df):
    """Main function to clean healthcare data."""
    try:
        # Create a copy of the dataframe
        df = df.copy()
        
        # Clean text fields
        text_columns = ['Diagnosis', 'Medication']
        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].apply(clean_medical_text)
        
        # Process blood pressure
        if 'BP' in df.columns:
            df['Systolic_BP'] = df['BP'].apply(preprocess_bp)
        
        # Remove duplicates
        if 'Name' in df.columns and 'DOB' in df.columns:
            df.drop_duplicates(subset=['Name', 'DOB'], keep='first', inplace=True)
        
        # Anomaly detection for blood pressure
        if 'Systolic_BP' in df.columns:
            systolic_data = df[['Systolic_BP']].dropna()
            if not systolic_data.empty:
                clf = IsolationForest(contamination=0.1, random_state=42)
                df['Anomaly'] = clf.fit_predict(systolic_data)
                df = df[df['Anomaly'] == 1]
                df.drop(columns=['Anomaly'], inplace=True)
        
        return df
    
    except Exception as e:
        logger.error(f"Error in data cleaning: {str(e)}")
        raise
