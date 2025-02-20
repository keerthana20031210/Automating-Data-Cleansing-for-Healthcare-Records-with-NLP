import nltk

def download_nltk_dependencies():
    """Download required NLTK data."""
    required_packages = ['punkt', 'stopwords', 'averaged_perceptron_tagger']
    for package in required_packages:
        try:
            nltk.download(package, quiet=True)
        except Exception as e:
            print(f"Error downloading {package}: {str(e)}")
            raise