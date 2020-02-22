import folium
from geopy.geocoders import Nominatim
import ssl
import random
import math

geolocator = Nominatim(user_agent="MapFriends")
ssl._create_default_https_context = ssl._create_unverified_context


def build_map(data):
    """
    Get json data and return friends' location map as HTML string
    :param data: dict
    :return: str
    """
    map = folium.Map(min_zoom=3)

    fg = folium.FeatureGroup(name='Your friends\' location')
    locations_used = []
    for user in data["users"]:
        print(user, user["location"])
        location = geolocator.geocode(user["location"],
                                      language='en',
                                      timeout=3)
        if not location:
            continue
        lat = location.latitude
        long = location.longitude
        loc = (lat, long)
        while loc in locations_used:
            r_earth = 6378  # km
            dy = random.choice([-1, 1, 2, -2, 3, -3, 4, -4])
            dx = random.choice([-1, 1, 2, -2, 3, -3, 4, -4])
            new_latitude = loc[0] + (dy / r_earth) * (180 / math.pi)
            new_longitude = loc[1] + (dx / r_earth) * (180 / math.pi) \
                / math.cos(loc[0] * math.pi / 180)
            loc = (new_latitude, new_longitude)
        locations_used.append(loc)
        fg.add_child(folium.Marker(location=loc,
                                   popup=user["location"] +
                                   ":\n" + user["screen_name"],
                                   icon=folium.Icon(icon='pushpin'),
                                   ))
    map.add_child(fg)

    map.add_child(folium.LayerControl())
    map.save("templates/friends_data.html")
    with open('templates/friends_data.html', 'r') as f:
        html_string = f.read()
    return html_string
