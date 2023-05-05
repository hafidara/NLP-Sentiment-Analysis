# import re 
from textblob import TextBlob
import pandas as pd

df = pd.read_csv('sentiments.csv')
df['blob'] = df['text'].apply(lambda x: TextBlob(x))
df['polarity'] = df['blob'].apply(lambda x: x.sentiment.polarity)

def get_sentiment(polarity):
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'
df['sentiment'] = df['polarity'].apply(get_sentiment)
for index, row in df.iterrows():
    print(f"Row {index+1}: {row['sentiment'].capitalize()}")
print(df)
sentence = input("Enter a sentence: ")
blob = TextBlob(sentence)
polarity = blob.sentiment.polarity
sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
print(f"The sentiment of '{sentence}' is {sentiment}.")

