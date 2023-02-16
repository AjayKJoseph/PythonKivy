# https://www.youtube.com/watch?v=TVnUxyEUVw0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=3
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Create number of grids
        self.cols = 1
        
        # Create a second GridLayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add a Label
        self.top_grid.add_widget(Label(text = "Name: "))
        # Create an Input box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        
        # Add a Label
        self.top_grid.add_widget(Label(text = "Test: "))
        # Create an Input box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        
        # Add a Label
        self.top_grid.add_widget(Label(text = "Test2: "))
        # Add an Input box
        self.pizza1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza1)
        
        # Add the new top_grid to our app.
        self.add_widget(self.top_grid)
        
        # Create a Submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the Button
        self.submit.bind(on_press=self.press) # Add a method
        self.add_widget(self.submit)
    
    # Create an instance outside of __init__ to capture Input Texts
    def press(self, instance):
        name = self.name.text # Line 19
        pizza = self.pizza.text
        pizza2 = self.pizza1.text
        
        # Display name on the app
        test =f'Hello {name}, you like {pizza} pizza, your favourite pizza2 is {pizza2}'
        self.add_widget(Label(text=test))
        
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.pizza1.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()