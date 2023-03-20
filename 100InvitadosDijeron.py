from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.core.window import Window, Keyboard


class textInsert(FloatLayout):

    currentQuestion = 0
    def __init__(self, **kwargs):
        super(textInsert, self).__init__(**kwargs)
        self.super = []

        text = StringProperty()

        ########################################
        keyboard = Window.request_keyboard(self._keyboard_released, self)
        keyboard.bind(on_key_up=self._keyboard_released)

        ########################################
    #end def __init__

    def _keyboard_released(self, window, keycode):
        self.super = []
        if keycode[0] == 276:
             print(f"<- released {keycode[1]}")
             if self.currentQuestion < 1: 
                 self.currentQuestion = 0
             else:
                 self.currentQuestion -=1     
        elif keycode[0] == 275:
             print(f"-> released {keycode[1]}")
             if self.currentQuestion > 2: 
                 self.currentQuestion = 3
             else:
                 self.currentQuestion +=1
        elif keycode[0] == 13:
             print( f"Enter released")
             print(f"Current Question {self.currentQuestion}")
    
 

class ROOT(App):
   def build(self):
      return textInsert()

if __name__ == '__main__':
   ROOT().run()