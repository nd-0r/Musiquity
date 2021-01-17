from ..classes.media import Media

from googleapiclient.discovery import build

# Prints Title, Youtube Music Link, and Youtube Link
# Not all vids are playable on Youtube Music (It'll just open it, skip the vid and play a random playlist if song/vid is not avalible on there)

def search_Youtube(user_search):
    youtube = build("youtube", "v3", developerKey = api_key)
    request = youtube.search().list(
    q = user_search,
    part = "snippet",
    type = "video",
    maxResults = 5
    )
    response = request.execute()
    for item in response["items"]:
        print (item["snippet"]["title"])
        print ("https://music.youtube.com/watch?v=" + (item["id"]["videoId"]))
        print ("https://youtube.com/watch?v=" + (item["id"]["videoId"]))

search_Youtube("Midnight City")
