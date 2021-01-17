from urllib.parse import urlparse

def parse_url(url):
  '''
  takes a validated url pointing to an item on
  a supported streaming service and returns a 
  query to be used with other streaming services

  Parameters:
    url (str): the url to be parsed
  
  Returns:
    query (Query): the query object to be used
    with other streaming services
  '''
