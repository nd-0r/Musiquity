from ..classes.query import Query
import requests
import os

def parse_link(link):
  '''Takes as input a link to an entity on spotify
  and returns a Query object. The goal of this is
  to get as much data as possible on a best-effort
  basis, recognizing that all desired data might not
  be acquired; at the very least, however, we need
  a title!

  Parameters:
    link (string): the link to parse

  Returns:
    query (Query): a query object used to look up
    the item on other platforms
  '''

  if (not isinstance(link, str)):
    raise TypeError(f'Cannot parse link of type: {type(link)}')

  url = ''
  item_id = ''
  head2 = {
    "Authorization": "Bearer " + os.getenv('SPOTIFY_OAUTH')
  }

  if ('album' in link):
    url = 'https://api.spotify.com/v1/albums/'
  elif ('track' in link):
    url = 'https://api.spotify.com/v1/tracks/'
  else:
    raise ValueError(f'"{link}" is not a valid spotify \
                       link to an album or song')

  url_to_submit = url + item_id
  query_response = requests.request('GET', url_to_submit, headers = head2)
  print(query_response.json()['artists'][0]['name'])
  print(query_response.json()['name'])