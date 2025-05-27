import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

st.markdown("""
<style>
    .stApp {
        background-color: black;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #333;
        color: white;
        caret-color: white;
    }
    .stTextArea > div > div > textarea {
        background-color: #333;
        color: white;
        caret-color: white;
    }
    .stTextArea textarea::placeholder {
        color: white !important;
        opacity: 0.7;
    }

    .stTextArea .st-ck {
        display: none !important;
    }
    /* Alternative selectors to hide the "Press Ctrl+Enter" text */
    .stTextArea [data-baseweb="textarea"] + div {
        display: none !important;
    }
    .css-1ms3v3l {
        display: none !important;
    }
    button {
        background-color: #8A2BE2 !important;
        color: white !important;
    }
    .stMarkdown {
        color: white !important;
    }
    header {
        background-color: black !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: white !important;
    }
    .css-1x8cf1d {
        color: white !important;
    }
    .css-10trblm {
        color: white !important;
    }
    .css-16idsys p {
        color: white !important;
    }
    .css-16idsys label {
        color: white !important;
    }
    small, .small {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

ps = PorterStemmer()

tfidf= pickle.load(open('vectorizer.pkl', 'rb'))
model= pickle.load(open('model.pkl', 'rb'))

def transform_text(text): 
    cleaned = ''
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned += char.lower()
    
    tokens = nltk.word_tokenize(cleaned)

    final_result = []
    for word in tokens:
        if word not in stopwords.words('english'):
            final_result.append(ps.stem(word))
    
    return " ".join(final_result)

st.title("Email Spam Classifier")


input_email = st.text_area("", placeholder="Type the message here to check if it is a spam or not...", key="email_input")

if st.button('Predict'):
    if input_email:
        transformed_email = transform_text(input_email)
        vector_input = tfidf.transform([transformed_email])
        result = model.predict(vector_input)[0]
        
        if result == 1:
            st.header("This Email is a spam")
        else:
            st.header("This Email is not a spam")

st.markdown("## Sample Messages")

spam_examples = [
    "URGENT: You have won a £1,000 cash prize! To claim call 09061701461. Claim code KL341. Valid 12 hours only.",
    "Congratulations! You've been selected for a free iPhone 13. Click here to claim your prize now before it expires!"
]

ham_examples = [
    "Hey, can we reschedule our meeting to tomorrow at 2pm? I have a conflict with the current time.",
    "Just a reminder that your dental appointment is scheduled for Friday at 10:30am. Please confirm if you can make it."
]

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4 style='color:white;'>Spam Examples</h4>", unsafe_allow_html=True)
    for i, example in enumerate(spam_examples):
        st.text_area(f"Spam Example {i+1}", example, key=f"spam_example_{i}", height=100)

with col2:
    st.markdown("<h4 style='color:white;'>Ham (Non-Spam) Examples</h4>", unsafe_allow_html=True)
    for i, example in enumerate(ham_examples):
        st.text_area(f"Ham Example {i+1}", example, key=f"ham_example_{i}", height=100)