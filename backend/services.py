from service_components.spotify import Spotify
from service_components.youtube import YouTube

services = {
  'spotify': Spotify(),
  'youtube_music': YouTube(),
  'youtube': YouTube(),
}
