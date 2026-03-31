from textblob import TextBlob

reviews = [
    "This movie was amazing and fantastic",
    "I hated this movie, it was boring",
    "The film was okay, not great",
    "Absolutely loved the acting",
    "Worst movie ever"
]

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(review, "->", sentiment)
    