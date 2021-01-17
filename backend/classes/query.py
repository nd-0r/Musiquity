class Query:

  link = None
  
  artist = None
  title = None
  media_type = None

  def __new__(input_link):
    link = input_link

  def parse_link(link):

