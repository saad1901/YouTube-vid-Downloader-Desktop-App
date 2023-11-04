import os
from pytube import Playlist

# Function to download a playlist
def download_playlist(playlist_url, output_path):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Iterate through the videos in the playlist and download them
        for video in playlist.videos:
            print(f"Downloading: {video.title}")
            video.streams.get_highest_resolution().download(output_path)
            print(f"{video.title} has been downloaded.")

        print("Playlist download complete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # URL of the YouTube playlist
    playlist_url = 'https://youtube.com/playlist?list=PL7vKef4lW0uYZAxzsqnVuUSqcBToFtI52&si=aPLiPjSPRYFK3nDk'

    # Output directory where the videos will be saved
    output_directory = r"D:\YT videos"

    # Download the playlist
    download_playlist(playlist_url, output_directory)
