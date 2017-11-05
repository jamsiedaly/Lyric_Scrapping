from bs4 import BeautifulSoup
import urllib.request
import os

class lyricBlobs():
	
	def create_files(self, song_URL, song_id, artist_name):
			os.makedirs(os.path.dirname(artist_name), exist_ok=True)
			song_file_name = artist_name + 'input' + '.txt'
			song_file = open(song_file_name, 'w+', encoding='utf8')
			return song_file
			
	def write_song(self, line, song_file):
		song_file.write(line+'\r\n'+'')	
		
	def scrap_song(self, song_URL, song_id, artist_name, song_file):
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
		song_page = opener.open(song_URL)
		song_soup = BeautifulSoup(song_page.read(), 'html.parser')
		song_page.close()
		lyrics = song_soup.find('div', {'id':'content_h'})
		first_line = lyrics.next
		log = []
		if(first_line.string[:1] != '['):
			log.append(first_line)
		lines = lyrics.find_all('br')
		for line in lines:
			current_line = (line.next).string
			if(current_line == None):
				log.append('\r\n')
			elif(current_line[:1] == '['):
				pass
			else:
				log.append(current_line)
		for entry in log:
			self.write_song(entry, song_file)
			
	if __name__ == '__main__':
		scrap_song(song_URL)
		
	
