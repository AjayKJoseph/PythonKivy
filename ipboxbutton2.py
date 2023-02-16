# https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=2
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Create number of grids/col
        self.cols = 2
        
        # Add a Label
        self.add_widget(Label(text = "Name: "))
        # Create an Input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        # Add a Label
        self.add_widget(Label(text = "Favourite Pizza: "))
        # Create an Input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)
        
        # Add a Label
        self.add_widget(Label(text = "Fav colour : "))
        # Add an Input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)
        
        # Create a Submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the Button - does something with the button
        self.submit.bind(on_press=self.press) # Add a function
        self.add_widget(self.submit)
    
    # Create an instance outside of __init__ to capture Input Texts
    def press(self, instance): # instance is keyword comparable to event keyword in tkinter
        name = self.name.text # Line 19
        pizza = self.pizza.text
        color = self.color.text
        
        # Display name on the app
        test =f'Hello {name}, you like {pizza} pizza, your favourite color is {color}'
        self.add_widget(Label(text=test))
        
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()