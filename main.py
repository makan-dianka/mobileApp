#!/home/makan/Projects/mobileapp/.venv/bin/python3


from kivy.app import App
from kivy.core.window import Window

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.properties import ObjectProperty

import random


class MisterNumber(FloatLayout):
    pass



class ButtonCancel(FloatLayout):
    pass




class MyLayout(Widget):
    
    first_btn = ObjectProperty(None)
    second_btn = ObjectProperty(None)
    thirth_btn = ObjectProperty(None)
    mist = ObjectProperty(None)



    def num_mister(self, miste):
        self.mist.text = miste




    def choice_number(self):

        numbers = [number for number in range(1, 500)]
        mister = []


        num_for_first_btn = str(random.choice(numbers))
        num_for_second_btn = str(random.choice(numbers))
        num_for_thirth_btn = str(random.choice(numbers))

        mister.append(num_for_first_btn)
        mister.append(num_for_second_btn)
        mister.append(num_for_thirth_btn)

        self.first_btn.text = num_for_first_btn
        self.second_btn.text = num_for_second_btn
        self.thirth_btn.text = num_for_thirth_btn

        self.num_mister(random.choice(mister))

        


    def reset(self):

        self.mist.text = "?"







kv = Builder.load_file('filemanager.kv')



class Myapp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return kv



if __name__=='__main__':
    Myapp().run()