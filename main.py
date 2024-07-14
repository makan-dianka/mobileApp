#!/home/makan/Projects/MobileApp/.venv/bin/python3


from kivy.app import App
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label



class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        # self.rows = 6


        # Create button 
        self.btn = Button(
            text='Soumettre', 
            font_size=32,
            size_hint_x=0,
            size_hint_y=0.3,
            # border=(1, 2, 3, 4),
            # background_normal='',
            background_color=(0.5, 0.8, 1, 1),
        )


        self.btn.bind(on_press=self.press)


        # Create label 
        self.label = Label(
            text=f"Bienvenue !", 
            font_size=20
        )

        
        # Create text input 
        self.name = TextInput(
            multiline=False,
            font_size=34,
            size_hint_x=2,
            size_hint_y=0.5,
        )


        # Create widgets
        self.add_widget(self.label)
        # self.add_widget(self.name)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 2
        self.bottom_layout.padding = (15, 0.2, 45, 180)
        self.bottom_layout.add_widget(Label(text='Username', font_size=30))
        self.bottom_layout.add_widget(self.name)
        
        self.add_widget(self.bottom_layout)

        self.add_widget(self.btn)


    def press(self, instance):
        pseudo = self.name.text

        # self.add_widget(Label(text=f"Bonjour {pseudo} !", font_size=20))

        # clear input field #name SSS
        self.name.text = ""




class Myapp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()


    def on_start(self):
        return Button(text="This method start kivy app")


    def on_stop(self):
        return Button(text="This method stop kivy app")



if __name__=='__main__':
    Myapp().run()