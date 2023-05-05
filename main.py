# import re 
from textblob import TextBlob
import pandas as pd

df = pd.read_csv('sentiments.csv')
df['blob'] = df['text'].apply(lambda x: TextBlob(x))
df['polarity'] = df['blob'].apply(lambda x: x.sentiment.polarity)
df['sentiment'] = df['polarity'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
for index, row in df.iterrows():
    print(f"Row {index+1}: {row['sentiment'].capitalize()}")
sentence = input("Enter a sentence: ")
blob = TextBlob(sentence)
polarity = blob.sentiment.polarity
sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
print(f"The sentiment of '{sentence}' is {sentiment}.")
# print(df)
