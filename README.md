# LyricFreq 🎵
A command-line tool that tracks how often a word appears across an artist's songs and albums using the Genius API.
## Setup

Get a free API token at genius.com/api-clients
Install dependencies:

pip install lyricsgenius pandas matplotlib

Replace YOUR_GENIUS_TOKEN_HERE in the script with your token
Run:

python lyricfreq.py
## Usage

The CLI will prompt you to:

Search by album or song
Enter an artist name
Enter a word to track

After searching, you can view a summary table and a bar chart of total word mentions per album.
## Built With

LyricsGenius
pandas
matplotlib
