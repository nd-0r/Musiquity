class Media:

  service = ''
  artist_name = ''
  title = ''
  link = ''
  image_url = ''
  # markets = ''
  media_type = ''

  def __init__(self, service, **kwargs):
    if (isinstance(self.service, str)):
      self.service = service
    else:
      raise TypeError(f'Invalid type for service: {type(service)}')
    try:
      self.artist_name = kwargs['artist_name']
      self.title = kwargs['title']
      self.link = kwargs['link']
      self.image_url = kwargs['image_url']
      # self.markets = kwargs['markets']
      self.media_type = kwargs['media_type']
      assert (self.media_type in ['album', 'song'])
    except KeyError:
      raise ValueError(f'Media constructor received invalid \
                       or incomplete arguments: {kwargs.__str__()}')

  def is_song(self):
    return self.media_type == 'song'

  def is_album(self):
    return self.media_type == 'album'

  def check_market(self, market_id):
    return market_id in self.markets

  def __str__(self):
    return f'<Media: {self.string()} {hex(id(self))}>'

  def __repr__(self):
    return f'Media("{self.string()}")'

  def string(self):
    return f'{self.artist_name}, {self.title}, {self.media_type}'