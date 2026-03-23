import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "OMG!!! This is sooo cool 😂, I can't believe it!!!"

text = text.lower()

text = text.translate(str.maketrans("", "", string.punctuation))

words = word_tokenize(text)

filtered = [w for w in words if w not in stopwords.words('english')]

clean_text = " ".join(filtered)

print(clean_text)
