from classes.media import Media
from classes.query import Query
from urllib.parse import urlparse
from parse_url import parse_url
from services import services

def search(text):
  user_query = None
  if (uri_validator(text)):
    out = {}
    user_query = parse_url(text)
    for service in services.keys():
      if user_query.service == service:
        continue
      if (user_query.has_artist()):
        out[service]=services[service].search(
          user_query, 
          artist=user_query.artist
        )
      else:
        out[service]=services[service].search(
          user_query
        )
    return out
  else:
    out = {}
    user_query = Query(text)
    for service in services.keys():
      out[service]=services[service].search(
        user_query
      )
    return out

def uri_validator(uri):
  try:
    result = urlparse(uri)
    return all([result.scheme, result.netloc, result.path])
  except ValueError:
    return False
