
import os
import splitter
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.title = ('IManip')
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.window.cols = 1 
        
        #image widget
        self.window.add_widget(Image(source='IManip.png'))

        #label widget
        self.greeting = Label(text = 'Podaj ścieżke do pliku: ')
        self.window.add_widget(self.greeting)

        #input widget 
        self.path_input = TextInput(multiline=False)
        self.window.add_widget(self.path_input)

        #label widget2
        self.greeting2 = Label(text = 'Podaj rozmiar tilea: ')
        self.window.add_widget(self.greeting2)

        #input widget2
        self.t_size_input = TextInput(multiline=False)
        self.window.add_widget(self.t_size_input)

        #button widget
        self.button = Button(text = "Procesuj")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, instance):
        path = self.path_input.text
        t_size = int(self.t_size_input.text)

        print(path)
        if os.path.isdir(path):
            files_list = os.listdir(path)
            for img in files_list:
                if img.endswith('.tif') or img.endswith('.jpg') or img.endswith('jpeg') or img.endswith('.png'):
                    splitter.split(img, path, t_size)
        else:
            splitter.split(os.path.basename(path), path + '\\..', t_size)

if __name__== "__main__":
    SayHello().run()