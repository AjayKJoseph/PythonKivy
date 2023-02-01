from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
    

class MainWidget(Widget):
    pass

class TheLabApp(App): # Add app at the end of the name
    pass



TheLabApp().run() # ensure to add parathensis () and run to instantiate class and create an object
