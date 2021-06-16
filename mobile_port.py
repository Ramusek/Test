import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import *
red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]
class Main(App):
    def build(self):
        global zeit
        global preis
        global aus
        global result_label
        layout = GridLayout(cols=1)
        colors = [red, green, blue, purple]
        Calculate = Button(text="Button 1",background_color=blue,size_hint=(.5, 1))
        self.zeit= TextInput(text="Zeit",size_hint=(.5, 1))
        self.preis=TextInput(text="0.19",size_hint=(.5, 1))
        self.aus=TextInput(text="2",size_hint=(.5, 1))
        self.result_label=Label(text="Ergebnis")
        layout.add_widget(self.zeit)
        layout.add_widget(self.preis)
        layout.add_widget(self.aus)
        layout.add_widget(Calculate)
        layout.add_widget(self.result_label)
        Calculate.bind(on_press=app.calculate)
        return layout
    def calculate(self,instance):
       global zeit
       global preis
       global aus
       zeit=self.zeit.text
       preis=self.preis.text
       aus=self.aus.text
       aus = float(aus)
       preis=float(preis)
       zeit=float(zeit)
       result = zeit * preis + aus
       resulte=round(result,2)
       resulte=str(resulte)
       self.result_label.text =(resulte)



       
if __name__ == "__main__":
    app = Main()
    app.run()