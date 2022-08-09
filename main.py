import random
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import platform





########################
import kivy


print
print(kivy.platform)

if kivy.platform == 'win':
    filename='C:/Users/mkozharov/AppData/Local/Programs/Python/Python38/Scripts/eng/eng-rus-new.txt'
elif kivy.platform == 'android':
#    from android.permissions import request_permissions, Permission
#    from android.storage import primary_external_storage_path
#    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE]) # Даём разрешение на чтение и запись (в моём случае)
#    dir = primary_external_storage_path()
#    barscanner_dir_path = os.path.join(dir, 'PythonFiles')

    
#          from android.permissions import request_permissions, Permission
#          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
#          app_folder = os.path.dirname(os.path.abspath(__file__))
#          PATH = "/storage/emulated/0" #app_folder
#        content.ids.filechooser.path = PATH

    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    dir = primary_external_storage_path()
    dir_path = os.path.join(dir, 'MK_Eng')
    filename='./eng-rus-new.txt'
################################





class New_EngApp(App):

    
    
    def build(self):
     
        superBox = BoxLayout(orientation ='vertical')

        o_text = TextInput(text='Output: ' + filename, readonly='True', foreground_color = 'black', line_height = 1, font_name = 'DejaVuSans.ttf')

        superBox.add_widget(o_text)




        return superBox
   
if __name__=="__main__":
    New_EngApp().run()

