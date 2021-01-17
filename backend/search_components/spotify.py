from ..classes.media import Media
from ..classes.query import Query
import requests
import os
import base64

# get the Oauth token
client_id = os.getenv('SPOTIFY_CLIENT')
client_secret = os.getenv('SPOTIFY_SECRET')
bytes_obj = bytes(client_id + ':' + client_secret, 'utf-8')
auth_string = base64.urlsafe_b64encode(bytes_obj)
head = {
    "Authorization": "Basic " + str(auth_string)[2:-1]
}
dat = {
  "grant_type": "client_credentials"
}
url = 'https://accounts.spotify.com/api/token'
temp = requests.request('POST', url, headers=head, data=dat)
os.environ['SPOTIFY_OAUTH'] = temp.json()['access_token']

def search_spotify(user_query, result_limit=1, **kwargs):
  '''Takes a user query and the 
  results limit returns the results
  of the query
  
  Parameters:
    user_query (Query): A query object
    result_limit (Int): The maximum number of results
    kwargs (Dict): Additional filters to apply to the query
      'album': specific text to look for in the album title
      'track': specific text to look for in the track title
      'artist': specific artist to look for
  
  Returns:
    results (List(Media)): A list of Media objects
  '''

  out = []
  BASE_URL = 'https://api.spotify.com/v1/search?'
  query = ''
  media_type = ''
  limit = 'limit=' + str(result_limit)

  if (isinstance(user_query, Query)):
    query = "q=" + user_query.get_title()
    if (query.is_song()):
      media_type = 'type=track'
    elif (query.is_album()):
      media_type = 'type=album'
    else:
      media_type = 'type=album,track'
    for k in kwargs.keys():
      query += '%20' + k + ':' + kwargs[k]
  else:
    raise TypeError(f'Cannot submit query to spotify of type: {type(user_query)}')

  try:
    head = {
        "Authorization": "Bearer " + os.getenv('SPOTIFY_OAUTH')
    }
  except EnvironmentError:
    raise RuntimeError(f'Cannot get environment variable $SPOTIFY_OAUTH')

  url = BASE_URL + query + '&' + media_type + '&' + limit
  query_response = requests.request('GET', url, headers = head)
  if (query_response.status_code != 200):
    raise RuntimeError(f'Cannot get information from Spotify API. Server returned \
                         status code: {query_response.status_code} with reason: \
                         {query_response.reason}')
  try:
    for album in query_response.json()['albums']['items']:
      try:
        tmp = Media('spotify',
          artist_name=album['artists'][0]['name'],
          title=album['name'],
          link=album['external_urls']['spotify'],
          image_url=album['images'][0],
          markets=album['available_markets'],
          media_type='album'
        )
      except KeyError:
        raise RuntimeError(f'Could not get all information for the query from spotify')
      out.append(tmp)
  except KeyError:
    pass
  try:
    for song in query_response.json()['tracks']['items']:
      try:
        tmp = Media('spotify',
          artist_name=song['artists'][0]['name'],
          title=song['name'],
          link=song['external_urls']['spotify'],
          image_url=song['images'][0],
          markets=song['available_markets'],
          media_type='song'
        )
      except KeyError:
        raise RuntimeError(f'Could not get all information for the query from spotify')
      out.append(tmp)
  except KeyError:
    pass
  return out