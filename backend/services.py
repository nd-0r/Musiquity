from backend.service_components.spotify import Spotify
from backend.service_components.youtube import YouTube

services = {
  'spotify': Spotify(),
  'youtube_music': YouTube(),
  'youtube': YouTube(),
}
