"""libraries we need for this project
tensorflow: to build and train model

wordcloud:visual representation of text data
pandas: load dataset and manipulation
nltk,genism:data cleaning ,natural language processing(remove stopwords and unnecessary words)
seaborn,matplotlib,plotly: data visualization
numpy:array manipulation
sklearn: to split testing and training data,to find accuracy of model and plot confusion matrix



"""

import tensorflow as tf
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plot
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import plotly
import nltk
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
# import keras
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional
from tensorflow.keras.models import Model
from jupyterthemes import jtplot
from nltk.corpus import stopwords
import plotly.express as pltexp
from sklearn.model_selection import train_test_split
from nltk import word_tokenize
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
jtplot.style(theme='monokai', context='notebook', ticks=True, grid=False)

nltk.download("punkt")
nltk.download("stopwords")
