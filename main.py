#!/home/makan/Projects/MobileApp/.venv/bin/python3


from kivy.app import App
from kivy.core.window import Window

from kivy.uix.widget import Widget

from kivy.lang import Builder
from kivy.properties import ObjectProperty




class MyLayout(Widget):

    toplabel = ObjectProperty(None)
    name = ObjectProperty(None)


    def get_name_text(self):

        self.toplabel.text = f"Hello {self.name.text} !"
        self.name.text = ""
        



kv = Builder.load_file('filemanager.kv')



class Myapp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return kv



if __name__=='__main__':
    Myapp().run()