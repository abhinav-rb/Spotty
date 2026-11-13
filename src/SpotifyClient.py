import os

class SpotifyClient:
    
    def __init__(self, client_secret, access_token=None):
        self.client_id = '35ff953650854c458987bb06dc37326a'
        self.client_secret = client_secret
        self.access_token = access_token
    
    
    #Spotify API client needs to be able to acceess:
        # - Get user information
        # - Get playlist information
        # - Get track information
    
    def get_user_info(self,user_id):
        # Implement the logic to get user information from Spotify API
        pass
    
    def get_playlist_info(self, playlist_id):
        # Implement the logic to get playlist information from Spotify API
        pass
    
    def get_track_info(self, track_id):
        # Implement the logic to get track information from Spotify API
        pass
    
    