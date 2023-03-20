from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.window import Window, Keyboard
from kivy.properties import ObjectProperty

from Cuestionario import cuestionario
 
class Questions(Widget):
    pregunta = ObjectProperty(None)
    respuesta1: ObjectProperty(None)
    respuesta2: ObjectProperty(None)
    respuesta3: ObjectProperty(None)
    numero: ObjectProperty(None)

    currentQuestion = 0
    nextQuestion = 0
    def __init__(self, **kwargs):
        super(Questions, self).__init__(**kwargs)
        self.super = []

        text = StringProperty()

        ########################################
        keyboard = Window.request_keyboard(self._keyboard_released, self)
        keyboard.bind(on_key_up=self._keyboard_released)

        ########################################
    #end def __init__

    def _keyboard_released(self, window, keycode):
        self.super = []
        print(f"Key Id: {keycode[0]}")

        if keycode[0] == 276:
             print(f"<- released")
             if self.nextQuestion < 2: 
                 self.nextQuestion = 1
             else:
                 self.nextQuestion -=1     

             self.numero.text = str(self.nextQuestion)    
        elif keycode[0] == 275:
             print(f"-> released")
             if self.nextQuestion > 2: 
                 self.nextQuestion = 3
             else:
                 self.nextQuestion +=1
             self.numero.text = str(self.nextQuestion)    
        elif keycode[0] == 13:   #Enter
             self.currentQuestion = self.nextQuestion
             print( f"Enter released")
             print(f"Current Question Number: {self.currentQuestion}")

             self.pregunta.text = cuestionario[self.currentQuestion][0]
             
             self.respuesta1.text = cuestionario[0][1]
             self.respuesta2.text = cuestionario[0][2]
             self.respuesta3.text = cuestionario[0][3]

             

        elif keycode[0] == 49:         
             print(f"Primer respuesta")
             self.respuesta1.text =  cuestionario[self.currentQuestion][1]
        elif keycode[0] == 50:
                
             print(f"Segunda reapuesta")
             self.respuesta2.text =  cuestionario[self.currentQuestion][2] 
        elif keycode[0] == 51:  
             print(f"Tercera respuesta")
             self.respuesta3.text =  cuestionario[self.currentQuestion][3]
        
        

class ROOT(App):
   def build(self):
      return Questions()

if __name__ == '__main__':
   ROOT().run()