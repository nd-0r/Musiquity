from ..classes.query import Query
import requests
import os

def parse_link(link):
  '''Takes as input a link to an entity on spotify
  and returns a Query object. The goal of this is
  to get as much data as possible on a best-effort
  basis, recognizing that all desired data might not
  be acquired; at the very least, however, we need
  a title!
  
  '''