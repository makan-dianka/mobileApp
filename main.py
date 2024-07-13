#!/home/makan/Projects/MobileApp/.venv/bin/python3


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition



class ScreenManagement(ScreenManager):
    pass


class HelloWorld(Screen):
    def sayHello(self):
        pass






kv = Builder.load_file('filemanager.kv')

class Myapp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        layout = kv
        return layout



if __name__=='__main__':
    Myapp().run()