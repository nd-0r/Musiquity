class Query:

  title = ''
  artist = ''
  media_type = ''

  def __init__(self, title, artist='', media_type=''):
    if not (isinstance(title, str)
            and isinstance(artist, str)
            and isinstance(media_type, str)):
      raise TypeError(f'Cannot instantiate query object with arguments of types: \
                        {type(title)}, {type(artist)}, {type(media_type)}')
    self.title = title
    self.artist = artist
    self.media_type = media_type

  def is_song(self):
    return self.media_type == 'song'

  def is_album(self):
    return self.media_type == 'album'