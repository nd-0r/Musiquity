from classes.media import Media
from classes.query import Query
from urllib.parse import urlparse
from parse_url import parse_url

def search(text):
  user_query = None
  if (uri_validator(text)):
    user_query = parse_url(text)
  else:
    user_query = Query(text)
  


def uri_validator(uri):
  try:
    result = urlparse(uri)
    return all([result.scheme, result.netloc, result.path])
  except ValueError:
    return False
    