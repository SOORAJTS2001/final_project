import telepot
import folium,time,random

# create map object
import os

# curr_lat_long = ()
# Set up your Telegram bot token
TOKEN = '6032631352:AAHk8jwne1WbqlXn4adDjgIn9JYBMPQQJYA'
bot = telepot.Bot(TOKEN)
# m = folium.Map(location=[8.913721,76.631944], zoom_start=20, tiles='OpenStreetMap')
# Define a function to handle location updates
def handle_location(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'location':
        lat = msg['location']['latitude']
        lon = msg['location']['longitude']
        # bot.sendMessage(chat_id, f"Your location: {lat}, {lon}")
        curr_lat_long = (lat,lon)
        with open('location.txt', 'w') as f:
            f.write(str(lat)+" "+str(lon))
        # folium.Marker(location=[lat,lon], popup='locations').add_to(m)
        # m.save('map.html')
        print('Map saved to map.html')
        print("your location is ", lat, lon)
        

# Start the bot and listen for updates
bot.message_loop(handle_location)

# Keep the bot running
while True:
    pass
