from ..classes.query import Query
from googleapiclient.discovery import build
import os

def parse_youtube_link(link):
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
  
  video_id = link.split('/')[-1].split('=')[-1]
  youtube = build(
    "youtube",
    "v3",
    developerKey = os.getenv('YOUTUBE_API_KEY')
  )

  request = youtube.videos().list(
    part = "snippet",
    id = video_id
  )
  response = request.execute()

  return Query(
    response['items'][0]['snippet']['title'],
    media_type='song'
  )
