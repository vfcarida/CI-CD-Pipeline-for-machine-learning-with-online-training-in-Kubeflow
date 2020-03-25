import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from seldon_core.seldon_client import SeldonClient
import dill
import sys, os

# This import may take a while as it will download the Spacy ENGLISH model
import ml_utils


class Model(object):

  def __init__(self, tfidf_vectorizer, lr):
    self.tfidf = tfidf_vectorizer
    self.lr = lr

  def predict_ranking(self, input_str, top=5):
    import ml_utils
    clean_text_transformer = ml_utils.CleanTextTransformer()
    spacy_tokenizer = ml_utils.SpacyTokenTransformer()

    clean_text = clean_text_transformer.transform([input_str])
    spacy_tokens = spacy_tokenizer.transform(clean_text)

    tfidf_features = self.tfidf.transform(spacy_tokens)
    print(tfidf_features)
    predictions = self.lr.predict_proba(tfidf_features)

    return predictions


def preprocess_and_train(train_data, eval_data, output):

  df_cols = ["body", "is_java"]

  TEXT_COLUMN = "body"
  CLEAN_COLUMN = "clean_body"
  TOKEN_COLUMN = "token_body"

  print("train_data: {}\noutput: {}".format(train_data, output))

  df = pd.read_csv(
      train_data,
      names=df_cols,
      skiprows=1,
      encoding="ISO-8859-1")

  x = df["body"].values
  y = df["is_java"].values
  x_train, x_test, y_train, y_test = train_test_split(
      x, y, stratify=y, random_state=42, test_size=0.1, shuffle=True)

  # Clean the text
  clean_text_transformer = ml_utils.CleanTextTransformer()
  x_train_clean = clean_text_transformer.transform(x_train)

  # Tokenize the text and get the lemmas
  spacy_tokenizer = ml_utils.SpacyTokenTransformer()
  x_train_tokenized = spacy_tokenizer.transform(x_train_clean)

  # Build tfidf vectorizer
  tfidf_vectorizer = TfidfVectorizer(
      max_features=10000,
      preprocessor=lambda x: x,
      tokenizer=lambda x: x,
      token_pattern=None,
      ngram_range=(1, 3))

  tfidf_vectorizer.fit(x_train_tokenized)

  # Transform our tokens to tfidf vectors
  x_train_tfidf = tfidf_vectorizer.transform(x_train_tokenized)

  # Train logistic regression classifier
  lr = LogisticRegression(C=0.1, solver="sag")
  lr.fit(x_train_tfidf, y_train)

  model = Model(tfidf_vectorizer, lr)

  # These are the models we'll deploy
  with open(output, "wb") as model_file:
    dill.dump(model, model_file)

  return model


if __name__ == '__main__':
  preprocess_and_train(train_data=sys.argv[1],
                       eval_data=sys.argv[2],
                       output=sys.argv[3])
