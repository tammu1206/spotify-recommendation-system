import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with your Client ID and Client Secret
client_id = '67f9c1e869524435b695a515715863db'  # Replace with your actual Client ID
client_secret = 'ce11a38f6b774c2abecc64614dca2284'  # Replace with your actual Client Secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("Authentication successful!")

# Get user input
user_input = input("Enter a song or artist you like: ")

# Search for the input
results = sp.search(q=user_input, type='track', limit=1)

# Check if any results were found
if results['tracks']['items']:
    track_id = results['tracks']['items'][0]['id']
else:
    print("No results found. Please try another song or artist.")
    exit()

# Get recommendations based on the found track
recommendations = sp.recommendations(seed_tracks=[track_id], limit=10)

print("\nRecommended Songs:")
for idx, track in enumerate(recommendations['tracks']):
    print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")
