import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def proper_noun_extractor(text, noun_limit=2):
  out = ''
  words = nltk.word_tokenize(text)
  words = [word for word in words if word not in set(stopwords.words('english'))]
  tagged = nltk.pos_tag(words)
  for (word, tag) in tagged[:noun_limit + 1]:
    if tag == 'NNP':
      out += word + ' '
  return out.strip()