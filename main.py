#!/home/makan/mobileApp/.venv/bin/python3

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder 
from kivy.core.window import Window
import os
from tcpip import client
from kivy.utils import platform

IP, PORT = os.getenv('host'), int(os.getenv('port'))


Window.size = (380, 600)

class FileManager(MDApp):

	filemanager = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		# current path 
		self.path = os.path.expanduser("~/Pictures") #or os.path.expanduser("/")
		self.whatsPath = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/media/WhatsApp Voice Notes/202425" # data for 2024/25

		self.filemanager = MDFileManager(
				select_path = self.select_path,
				exit_manager = self.close_filemanager,
			)

 
 
	def get_size(self, path):
		size = os.path.getsize(path) #size in bytes
		if size < 1024:
			return f"{size} bytes"
		elif size < pow(1024,2):
			return f"{round(size/1024, 2)} KB"
		elif size < pow(1024,3):
			return f"{round(size/(pow(1024,2)), 2)} MB"
		elif size < pow(1024,4):
			return f"{round(size/(pow(1024,3)), 2)} GB"
	   

	def navigate(self):
		if platform == 'android':
			path_content = os.listdir(self.whatsPath)
			print(f'elements in {self.path}: ', len(path_content))
			for file in path_content:
				path = os.path.join(f"{self.path}/{file}")
				if os.path.isfile(path):
					print(f"{file} [{self.get_size(path)}]")
					client.client_mode(IP, PORT, path)
		
		if platform == 'linux':
			if os.path.exists(self.path):
				path_content = os.listdir(self.path)
				print(f'elements in {self.path}: ', len(path_content))
				for file in path_content:
					path = os.path.join(f"{self.path}/{file}")
					if os.path.isfile(path):
						print(f"{file} [{self.get_size(path)}]")
						# client.client_mode(IP, PORT, path)
			



	def open_filemanager(self):

		self.filemanager.show(self.path)
		self.navigate() 




	def select_path(self, path):

		self.navigate()

		self.close_filemanager()


	def close_filemanager(self, *args):
		self.filemanager.close()


	def build(self):
		return Builder.load_file('./filemanager.kv')


if __name__=="__main__":
	app = FileManager()
	app.run()
