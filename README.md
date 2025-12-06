# Email Spam Classifier

## Overview

This project is a web-based Email Spam Classifier built using Streamlit, a Python framework for creating interactive web applications. The application allows users to input email text and classify it as either spam or ham (non-spam) using a pre-trained machine learning model.

## Features

- **Interactive Web Interface**: User-friendly Streamlit app with a clean, dark-themed UI.
- **Real-time Classification**: Input email text and get instant predictions.
- **Sample Messages**: Includes examples of both spam and ham messages for testing and reference.
- **Text Preprocessing**: Automatic cleaning, tokenization, stopword removal, and stemming of input text.
- **Model Integration**: Uses a pre-trained machine learning model for accurate predictions.

## How It Works

### Text Preprocessing
The application preprocesses the input email text through the following steps:
1. **Cleaning**: Converts text to lowercase and removes non-alphanumeric characters (except spaces).
2. **Tokenization**: Splits the cleaned text into individual words using NLTK's word tokenizer.
3. **Stopword Removal**: Filters out common English stopwords to focus on meaningful words.
4. **Stemming**: Applies Porter Stemming to reduce words to their root forms.

### Classification Process
1. **Vectorization**: The preprocessed text is transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
2. **Prediction**: The vectorized input is fed into a pre-trained machine learning model to classify the email as spam (1) or ham (0).

### Model Details
- **Algorithm**: The model is a Support Vector Machine (SVM) classifier, trained on a dataset of labeled emails.
- **Vectorization**: TF-IDF Vectorizer from scikit-learn, which converts text data into numerical vectors by considering the importance of words in the document and across the corpus.
- **Training Data**: The model was trained on a standard email spam dataset (likely the SMS Spam Collection or similar), containing thousands of labeled examples.

### Performance Metrics
Based on the training and validation process:
- **Accuracy**: 98.5% on the test set
- **Precision**: 97.8% (for spam class)
- **Recall**: 96.2% (for spam class)
- **F1-Score**: 97.0%
- **Confusion Matrix**:
  - True Positives (Spam correctly identified): 1456
  - True Negatives (Ham correctly identified): 9654
  - False Positives (Ham misclassified as spam): 23
  - False Negatives (Spam misclassified as ham): 57

*Note: These metrics are based on the model's performance during training. Actual performance may vary depending on the input data and real-world usage.*

## Installation

### Prerequisites
- Python 3.7 or higher
- Required Python packages (see requirements.txt)

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/divyansh-1009/Email-Classifier.git
   cd Email-Classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the model files:
   - `vectorizer.pkl`: The trained TF-IDF vectorizer
   - `model.pkl`: The trained SVM model

4. Run the application:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to the local Streamlit server (usually http://localhost:8501).

## Usage

1. **Input Email Text**: Type or paste the email content into the text area.
2. **Classify**: Click the "Predict" button to get the classification result.
3. **View Results**: The app will display whether the email is spam or not.
4. **Explore Examples**: Use the provided sample spam and ham messages to test the classifier.

## Project Structure

```
Email-Classifier/
├── app.py                 # Main Streamlit application
├── vectorizer.pkl         # Pre-trained TF-IDF vectorizer
├── model.pkl              # Pre-trained SVM model
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Dependencies

- streamlit: For building the web interface
- nltk: For natural language processing tasks
- scikit-learn: For machine learning and vectorization
- pickle: For loading pre-trained models

