from ..classes.media import Media
from ..classes.query import Query
import requests
import json
from decouple import config
import base64

# get the Oauth token
client_id = config('SPOTIFY_CLIENT')
client_secret = config('SPOTIFY_SECRET')
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
SPOTIFY_OAUTH = temp.json()['access_token']


class Spotify:

  SERVICE = 'spotify'
  NETLOCS = [
    'open.spotify.com',
    'spotify.com',
    'play.spotify.com'
  ]

  @staticmethod
  def search(user_query, result_limit=1, **kwargs):
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
      query = "q=" + user_query.title
      if (user_query.is_song()):
        media_type = 'type=track'
      elif (user_query.is_album()):
        media_type = 'type=album'
      else:
        media_type = 'type=album,track'
      for k in kwargs.keys():
        query += '%20' + k + ':' + kwargs[k]
    else:
      raise TypeError(f'Cannot submit query to spotify of type: {type(user_query)}')

    try:
      head = {
          "Authorization": "Bearer " + SPOTIFY_OAUTH
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
            image_url=song['album']['images'][0],
            media_type='song'
          )
        except KeyError:
          raise RuntimeError(f'Could not get all information for the query from spotify')
        out.append(tmp)
    except KeyError:
      pass
    return out

  @staticmethod
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
    item_id = link.split('/')[-1]
    head2 = {
      "Authorization": "Bearer " + SPOTIFY_OAUTH
    }

    m_type = ''
    if ('album' in link):
      url = 'https://api.spotify.com/v1/albums/'
      m_type = 'album'
    elif ('track' in link):
      url = 'https://api.spotify.com/v1/tracks/'
      m_type = 'song'
    else:
      raise ValueError(f'"{link}" is not a valid spotify \
                        link to an album or song')

    url_to_submit = url + item_id
    query_response = requests.request('GET', url_to_submit, headers = head2)
    if (query_response.status_code != 200):
      print(json.dumps(query_response.json(), indent=1))
      raise RuntimeError(f'Cannot get information from Spotify API:')

    return Query(
      query_response.json()['name'],
      artist=query_response.json()['artists'][0]['name'],
      media_type=m_type
    )
