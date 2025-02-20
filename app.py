import streamlit as st
import pandas as pd
from scripts import data_cleaning
import setup

def main():
    try:
        # Download NLTK dependencies
        setup.download_nltk_dependencies()
        
        st.title("🏥 Healthcare Data Cleansing Tool")
        st.write("Upload your healthcare data or enter it manually for cleaning and standardization.")
        
        # File upload
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        
        # Manual data entry
        st.subheader("Or Enter Data Manually:")
        name = st.text_input("Patient Name")
        dob = st.date_input("Date of Birth")
        diagnosis = st.text_input("Diagnosis")
        medication = st.text_input("Medication")
        bp = st.text_input("Blood Pressure (e.g., 120/80)")
        
        if st.button("Process Data"):
            if uploaded_file:
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.DataFrame([{
                    "Name": name,
                    "DOB": dob.strftime("%Y-%m-%d") if dob else None,
                    "Diagnosis": diagnosis,
                    "Medication": medication,
                    "BP": bp
                }])
            
            with st.spinner("Cleaning data..."):
                cleaned_df = data_cleaning.clean_healthcare_data(df)
            
            st.success("✅ Data cleaning completed!")
            st.write("Cleaned Data:")
            st.dataframe(cleaned_df)
            
            # Download button
            st.download_button(
                label="Download Cleaned Data",
                data=cleaned_df.to_csv(index=False).encode("utf-8"),
                file_name="cleaned_healthcare_data.csv",
                mime="text/csv"
            )
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()