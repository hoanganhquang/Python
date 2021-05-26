import requests
from bs4 import BeautifulSoup
import spotipy

# client_ID = "4ba216a189ea4d27bb783b43f3453541"
# client_Secret = "e00407f891814f74b27943f10af5a092"
#
# prompt = input("Which year do you want to travel to? ")
#
# data_url = requests.get(url=f"https://www.billboard.com/charts/hot-100/{prompt}")
# response = data_url.text
#
# soup = BeautifulSoup(response, "html.parser")
# data = soup.find_all(name="span", class_="chart-element__information__song")
#
# name_song_lst = [item.getText() for item in data]
# print(name_song_lst)

user_id = "yw4unbo9s197ahpe3vpcugqwe"
spot_token = "BQBWdyxZ36EVmwiR9TNeVKMs"

# spot = spotipy.SpotifyOAuth(client_id=client_ID, client_secret=client_Secret)
spotify_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
headers = {
    "Authorization": "Bearer BQBWdyxZ36EVmwiR9TNeVKMs-1toRFuZecolU7si7z75di8st1C6iwUVn1MWxFNQpLqtozhlfj3kzedPGd4QeeJJf9IW9UCOOUVbJWqO4dDszNG_EeI-OdhIQBJuWZ0hMhi2EFoCIdYPckSLAQtgqVly24X_ilSpOvIBlYSaEhWpDt5YQr8UzfUTNiN_-Eo"
}

params = {
    "name": "Songs",
    "description": "100 Songs",
    "public": False
}

# answer = requests.post(url=spotify_url, json=params, headers=headers)

