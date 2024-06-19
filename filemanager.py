#!/home/pydev/mobileApp/.venv/bin/python

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder 
from kivy.core.window import Window
import os


Window.size = (380, 600)

class FileManager(MDApp):

	filemanager = None

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.path = os.path.expanduser("~") or os.path.expanduser("/")
		self.filemanager = MDFileManager(
				select_path = self.select_path,
				exit_manager = self.close_filemanager,
			)


	def open_filemanager(self):
		self.filemanager.show(self.path)



	def select_path(self, path):

		print(path)

		self.close_filemanager()



	def close_filemanager(self, *args):
		self.filemanager.close()


	def build(self):
		return Builder.load_file('./filemanager.kv')


if __name__=="__main__":
	app = FileManager()
	app.run()