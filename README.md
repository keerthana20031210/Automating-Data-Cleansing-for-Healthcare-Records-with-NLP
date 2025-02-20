# Healthcare Data Cleansing Tool 🏥
An automated tool for cleaning and standardizing healthcare records using Natural Language Processing (NLP) and machine learning techniques.

## Features ✨
- **Text Standardization**: Cleans and normalizes medical diagnoses and medication names
- **Duplicate Detection**: Removes duplicate patient records
- **Blood Pressure Validation**: Validates and standardizes blood pressure readings
- **Anomaly Detection**: Identifies and flags unusual values using machine learning
- **User Interface**: Easy-to-use web interface built with Streamlit
- **Batch Processing**: Support for CSV file uploads
- **Manual Entry**: Option to input individual records
- **Data Export**: Download cleaned data in CSV format

## Installation 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/healthcare-data-cleaner.git
    cd healthcare-data-cleaner
    ```

2. Create and activate a virtual environment:

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    python -m venv venv
    source venv/bin/activate
    ```

3. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```


## Usage 💻

### Running the Application

1. Start the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`

### Using the Web Interface

#### File Upload:
- Click "Upload CSV file"
- Select your healthcare data CSV file (Format should match the sample input structure)

#### Manual Entry:
- Fill in the form fields for individual records
- Click "Process Data" to clean the entry

#### Download Results:
- Click "Download Cleaned Data" to get the processed CSV file

## Input Data Format 📋

Your input CSV should have the following columns:

| Name            | DOB          | Diagnosis                               | Medication                     | BP      |
|-----------------|--------------|-----------------------------------------|---------------------------------|---------|
| John Smith      | 1985-03-15   | Type 2 diabetes with hypertension       | Metformin 500mg and Lisinopril  | 142/90  |
| Sarah Johnson   | 1992-07-22   | Chronic migraine headaches              | Sumatriptan 50mg tablets        | 118/75  |

### Sample Input File

```csv
Name,DOB,Diagnosis,Medication,BP
John Smith,1985-03-15,Type 2 diabetes with hypertension,Metformin 500mg and Lisinopril,142/90
Sarah Johnson,1992-07-22,Chronic migraine headaches,Sumatriptan 50mg tablets,118/75
Mike Wilson,1978-11-30,Upper respiratory infection acute,Amoxicillin 500mg,125/82
Sarah Johnson,1992-07-22,Asthma with bronchitis,Albuterol inhaler,300/95
Emily Brown,1989-04-10,anxiety disorder with insomnia,Sertraline 50mg daily,115/75
David Lee,1995-09-05,Lower back pain chronic,Ibuprofen 400mg as needed,80/50
```
### Expected Output
```csv
Name,DOB,Diagnosis,Medication,BP
John Smith,1985-03-15,type 2 diabetes hypertension,metformin 500mg lisinopril,142/90
Sarah Johnson,1992-07-22,chronic migraine headaches,sumatriptan 50mg tablets,118/75
Mike Wilson,1978-11-30,upper respiratory infection acute,amoxicillin 500mg,125/82
Emily Brown,1989-04-10,anxiety disorder insomnia,sertraline 50mg daily,115/75
```
### Data Cleaning Process 🧹
```bash
Text Standardization:
Converts text to lowercase
Removes special characters
Eliminates stop words
Standardizes medical terminology
Duplicate Removal:
Identifies duplicate records based on Name and DOB
Keeps the first occurrence of duplicates
Blood Pressure Validation:
Validates format (systolic/diastolic)
Checks for reasonable ranges
Flags anomalous readings
Anomaly Detection:
Uses Isolation Forest algorithm
Identifies unusual patterns in numerical data
Removes statistical outliers
```