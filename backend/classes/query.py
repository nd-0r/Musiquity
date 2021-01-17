
FORBIDDEN_TITLE_PUNCTUATION = [
  "'",
  ",",
  '"',
  '?',
  '/'
  '\\',
  '`',
  '|',
  '&'
]

class Query:

  title = ''
  from_service = ''
  artist = ''
  media_type = ''

  def __init__(self, title, service = '', artist='', media_type=''):
    if not (isinstance(title, str)
            and isinstance(artist, str)
            and isinstance(media_type, str)
            and isinstance(service, str)):
      raise TypeError(f'Cannot instantiate query object with arguments of types: \
                        {type(title)}, {type(artist)}, {type(media_type)}, {type(service)}')
    self.title = Query.clean_title(title)
    self.from_service = service
    self.artist = artist
    self.media_type = media_type

  @staticmethod
  def clean_title(title):
    out = title
    for punc in FORBIDDEN_TITLE_PUNCTUATION:
      out = out.replace(punc, '')
    return out

  def is_song(self):
    return self.media_type == 'song'

  def is_album(self):
    return self.media_type == 'album'

  def has_artist(self):
    return not self.artist == ''

  def __str__(self):
    return f'<Query: {self.string()} {hex(id(self))}>'

  def __repr__(self):
    return f'Query("{self.string()}")'

  def string(self):
    return f'\ntitle: {self.title}\nservice: {self.from_service}\
            \nartist: {self.artist}\nmedia type: {self.media_type}\n'
