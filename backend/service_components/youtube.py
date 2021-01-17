from ..classes.media import Media
from ..classes.query import Query
from ..proper_noun_extractor import proper_noun_extractor
from decouple import config
from urllib.parse import urlparse
from googleapiclient.discovery import build

# Not all vids are playable on Youtube Music (It'll 
# just open it, skip the vid and play a random playlist 
# if song/vid is not avalible on there)


class YouTube:

  SERVICE = 'youtube'
  NETLOCS = [
    'youtube.com',
    'www.youtube.com',
    'm.youtube.com',
    'music.youtube.com',
    'uk.youtube.com',
    'youtu.be',
    'kids.youtu.be',
    'www.youtu.be'
  ]

  @staticmethod
  def search(user_query, result_limit=1, **kwargs):
    '''Takes a user query and the 
    results limit returns the results
    of the query
    
    Parameters:
      user_query (Query): A query object
      result_limit (Int): The maximum number of results
      kwargs (Dict): Not used-additional filters for the search
    
    Returns:
      results (List(Media)): A list of Media objects
    '''
    
    out = []
    user_search = ''
    MUSIC_BASE_URL = "https://music.youtube.com/watch?v="
    YOUTUBE_BASE_URL = "https://youtube.com/watch?v="

    if (isinstance(user_query, Query)):
      user_search = user_query.title
    else:
      raise TypeError(f'Cannot submit query to spotify of type: \
                      {type(user_query)}')

    youtube = build(
      "youtube",
      "v3",
      developerKey = config('YOUTUBE_API_KEY')
    )

    request = youtube.search().list(
      q = user_search,
      part = "snippet",
      type = "video",
      maxResults = result_limit
    )

    response = request.execute()

    for item in response["items"]:
      try:
        tmp1 = Media(
          service='youtube',
          artist_name='',
          title=item["snippet"]["title"],
          link=YOUTUBE_BASE_URL + item["id"]["videoId"],
          image_url=item["snippet"]["thumbnails"]["medium"]["url"],
          media_type='song'
        )
        tmp2 = Media(
          service='youtube_music',
          artist_name='',
          title=item["snippet"]["title"],
          link=MUSIC_BASE_URL + item["id"]["videoId"],
          image_url=item["snippet"]["thumbnails"]["medium"]["url"],
          media_type='song'
        )
      except KeyError:
        raise RuntimeError(f'Could not get all information for the \
                             query from spotify')
      out.append(tmp1)
      out.append(tmp2)
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
    
    hygienic_url = urlparse(link)
    video_id = hygienic_url.query.split('=')[-1]

    youtube = build(
      "youtube",
      "v3",
      developerKey = config('YOUTUBE_API_KEY')
    )

    request = youtube.videos().list(
      part = "snippet",
      id = video_id
    )
    response = request.execute()
    title_tmp = response['items'][0]['snippet']['title']

    return Query(
      proper_noun_extractor(title_tmp),
      media_type='song'
    )