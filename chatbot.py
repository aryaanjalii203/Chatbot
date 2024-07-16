# -*- coding: utf-8 -*-
"""Chatbot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nKZp2Y6ZVgcacrGgrwR2nOYqEymltqot
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text="Natural language Processing is fascinating."
tokens=word_tokenize(text)
print(tokens)

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer=WordNetLemmatizer()
words=["running","ran","runs"]
lemmas=[lemmatizer.lemmatize(word, pos='v') for word in words]
print(lemmas)

from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words=set(stopwords.words('english'))
filtered_text=[word for word in tokens if word.lower() not in stop_words]
print(filtered_text)

import pandas as pd

data = pd.read_csv('/content/chatbot_dataset.csv', encoding='latin1')


nltk.download('punkt')
data['Question'] = data['Question'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower())))
print(data.head())

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(data['Question'])
print(X.shape)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data['Question'], data['Answer'], test_size=0.2, random_state=42)


model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
print("Model Training complete")

def get_response(question):
      question = ' '.join(nltk.word_tokenize(question.lower()))
      answer = model.predict([question])[0]
      return answer
print(get_response("What is NLP?"))

!pip install dash

# Now you can import dash
import dash

# Initialize the Dash app
app = dash.Dash(__name__)

from dash import dcc, html
# Define the layout
app.layout = html.Div([
html.H1("Chatbot", style={'textAlign': 'center'}),
dcc.Textarea(
id='user-input',value='Type your question here...',
style={'width': '100%', 'height': 100}
                                    ),
html.Button('Submit', id='submit-button', n_clicks=0),
html.Div(id='chatbot-output', style={'padding': '10px'})
])

from dash.dependencies import Input, Output
@app.callback(
    Output('output-div','childer'),
    Input('button','n_class'),
    [dash.dependencies.State('input-box','value')]
)
def update_output(n_clicks,value):
  if n_clicks is not None:
    return f'You have enetered: {value}'
    return ''

import dash
import dash_html_components as html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
        html.Div(children='''
                Dash: A web application framework for Python.
                    '''),
                    ])

# Define a simple callback (if needed)
@app.callback(
dash.dependencies.Output('output-div', 'children'),
[dash.dependencies.Input('input-div', 'value')]
)
def update_output(value):
  return f'You have entered: {value}'
  if __name__ == '__main__':
    app.run_server(debug=True)

app.layout = html.Div([
    html.H1("Chatbot", style={'textAlign': 'center'}),
    dcc.Textarea(
    id='user-input',
    value='Type your question here...',
    style={'width': '100%', 'height': 100}
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='chatbot-output', style={'padding': '10px'})
                                              ])

# Define callback to update chatbot response
@app.callback(
    Output('chatbot-output', 'children'),
    Input('submit-button', 'n_clicks'),
    [dash.dependencies.State('user-input', 'value')]
            )
def update_output(n_clicks, user_input):
  if n_clicks > 0:
    response = get_response(user_input)
    return html.Div([
        html.P(f"You: {user_input}", style={'margin': '10px'}),
        html.P(f"Bot: {response}", style={'margin': '10px', 'backgroundColor': '#f0f0f0', 'padding': '10px', 'borderRadius': '5px'})])
    return "Ask me something!"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)