from bs4 import BeautifulSoup
import urllib.request
import os
from lyricBlobs import lyricBlobs

artist_name = 'kendrick_lamar/'
artist_URL = 'http://www.lyricsfreak.com/k/kendrick+lamar/'


def new_song(song_file):
		song_file.write('\r\n\r\n'+'')

def scrap_artist(artist_name, artist_URL, song_file):
	domain = 'http://www.lyricsfreak.com'
	loop = 0
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
	song_page = opener.open(artist_URL)
	song_soup = BeautifulSoup(song_page.read(), 'html.parser')
	lyrics = song_soup.find('table', {'name':'song'})
	song_links = lyrics.find_all('a')
	scraper = lyricBlobs()
	for link in song_links:
		href = link['href']
		if href != 'javascript:void(0)':
			new_song(song_file)
			print(href)
			loop += 1
			link_address = domain + href
			try:
				scraper.scrap_song(link_address, str(loop), artist_name, song_file)
			except:
				pass
	
artist_names = ['kendrick_lamar/',
				'aesop_rock/',
				'j_cole/',
				'scroobius_pip/',
				'lil_wayne/',
				'tupac/',
				'nas/',
				'dre/',
				#'eminem/',
				'kanye/',
				'rakim/',
				'outkast/',
				#'fabolous/',
				#'busta_ryhmes/',
				'jay-z']

artist_URLs = [	'http://www.lyricsfreak.com/k/kendrick+lamar/',
				'http://www.lyricsfreak.com/a/aesop+rock/',
				'http://www.lyricsfreak.com/j/j+cole/',
				'http://www.lyricsfreak.com/d/dan+le+sac+vs+scroobius+pip/',
				'http://www.lyricsfreak.com/l/lil+wayne/',
				'http://www.lyricsfreak.com/t/tupac+shakur/',
				'http://www.lyricsfreak.com/n/nas/',
				'http://www.lyricsfreak.com/d/dr+dre/',
				#'http://www.lyricsfreak.com/e/eminem/',
				'http://www.lyricsfreak.com/k/kanye+west/',
				'http://www.lyricsfreak.com/r/rakim/',
				'http://www.lyricsfreak.com/o/outkast/',
				#'http://www.lyricsfreak.com/f/fabolous/',
				#'http://www.lyricsfreak.com/b/busta+rhymes/',
				'http://www.lyricsfreak.com/j/jay+z/']

for i in range(0,100):
	scraper = lyricBlobs()
	song_file = scraper.create_files("rawBlobs/", "rawBlobs/", "rawBlobs/")
	for i, artist in enumerate(artist_names):
		try: 
			scrap_artist(artist, artist_URLs[i], song_file)
		except:
			scrap_artist(artist, artist_URLs[i], song_file)
