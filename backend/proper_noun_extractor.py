import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def proper_noun_extractor(text):
  out = ''
  words = nltk.word_tokenize(text)
  words = [word for word in words if word not in set(stopwords.words('english'))]
  tagged = nltk.pos_tag(words)
  for (word, tag) in tagged[:3]:
    if tag == 'NNP':
      out += word + ' '
  return out.strip()