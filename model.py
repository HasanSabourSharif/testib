import torch
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from utils import AnswerPredictor

# Load the model state dictionary
model_state_dict = torch.load("./pytorch_model.bin", map_location=torch.device('cpu'))

# Create an instance of the model using its class definition
model = AutoModelForQuestionAnswering.from_pretrained("HooshvareLab/bert-fa-base-uncased", state_dict=model_state_dict)

# Optional: Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("HooshvareLab/bert-fa-base-uncased")

df = pd.read_csv('./data/QA.csv')

CONTEXT_LENGTH = 5

def getSimilarity(input_text):
    all_texts = df['question'].tolist()
    all_texts.append(input_text)

    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,3))

    # Fit and transform the texts
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)

    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    # Get the indices of the top 5 similar texts
    top_indices = cosine_similarities.argsort()[-CONTEXT_LENGTH:][::-1]

    # Retrieve the top 5 similar texts
    top_ = df.iloc[0]['answer']
    top_similar_texts = df.loc[top_indices, 'answer']
    
    return top_, top_similar_texts

def getContext(question):
    return '\n'.join(i for i in random.sample(getSimilarity(question)[1].to_list(), k=CONTEXT_LENGTH))


def getAnswer(question):
    context = getContext(question)
	
    predictor = AnswerPredictor(model, tokenizer, device="cpu", n_best=5)
    preds = predictor([question], [context] * 1, batch_size=1)

    lt = []
    for k, v in preds.items():
         lt.append(v)
    return lt
