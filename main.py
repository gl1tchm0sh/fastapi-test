from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    counter = 0
    tb1_state = BooleanProperty(False)
    my_text = StringProperty(f"{counter}")
    text_input_str = StringProperty("foo")


    # slider_value = 50
    # slider_state = BooleanProperty(False)
    # my_text2 = StringProperty(f"{slider_value}")

    def on_button_click(self):
        print("Button clicked")
        if self.tb1_state:
            self.counter += 1
        self.my_text = f"{self.counter}"

    def on_toggle_button_state(self, widget):
        print("toggle state " + widget.state) # normal / down
        widget.text = "ON" if widget.state == "down" else "OFF"
        self.tb1_state = True if widget.state == "down" else False

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        # self.slider_state = widget.active

    def on_slider_value(self,widget):
        print("Slider: " + str(int(widget.value)))
        # self.slider_value = f"{str(int(widget.value))}"
        # self.my_text2 = self.slider_value

    def on_text_validate(self,widget):
        self.text_input_str = widget.text

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b = Button(text="Z", size_hint=(.2,.2))
        self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = "vertical"
#         b1 = Button(text="A")
#         b2 = Button(text="B")
#         b3 = Button(text="C")
#         self.add_widget(b2)
#         self.add_widget(b3)
#         self.add_widget(b1)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()