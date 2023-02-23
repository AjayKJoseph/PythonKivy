# https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=2

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# kivy.requre('1.9.0')

class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)
    
    # Create an instance outside of __init__ to capture Input Texts
    def press(self): 
        name = self.name.text # Line 19
        pizza = self.pizza.text
        color = self.color.text
        
        # Display name on the app
        # test =f'Hello {name}, you like {pizza} pizza, your favourite color is {color}'
        # self.add_widget(Label(text=test))
        
        print(f'Hello {name}, you like {pizza} pizza, your favourite color is {color}')
        
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        
class kivydesignlang(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    kivydesignlang().run()