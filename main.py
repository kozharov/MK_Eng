"""
import kivy
kivy.require('2.1.0') # replace with your current kivy version !
import os
import stat

from kivy.app import App
from kivy.uix.label import Label


from kivy.utils import platform

my_text = 'X3'

if platform == "android":
    from android.permissions import request_permissions, Permission
#    from android.permissions import Permission, request_permissions, check_permission
    from android.storage import primary_external_storage_path


    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    dir = primary_external_storage_path()
    dirname = os.path.join(dir, 'MK_Eng')
###   filename='/storage/emulated/0/MK_Eng/eng-rus-new.txt'
###   access = 0o755
    os.mkdir(dirname)
###    os.chmod('/storage/emulated/0/MK_Eng/eng-rus-new.txt', stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)



#    if os.path.isdir('C:/MK_Eng') == True:
#        my_text = 'True'
#    else:
#        my_text = 'False'

#print(exec(dirname))

   
class MyApp(App):

    def build(self):
        return Label(text = my_text)


if __name__ == '__main__':
    MyApp().run()
"""


import random
import time
import os
import stat
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import platform
import kivy
import fileinput


global statistics_label_initial

screen_coeff=Window.size[0]/800
column1=[]
column2=[]
column3=[]
column4=[]
column5=[]
word_list=[]
word_meaning=[]
example_list=[]
example_meaning=[]
real_example=[]
num=[]
lines = []
statistics_label_initial = ''


if kivy.platform == 'win':
    dirname='C:/MK_Eng/'
    filename='C:/MK_Eng/eng-rus-new.txt'
elif kivy.platform == 'android':
    from android.permissions import request_permissions, Permission
    from android.storage import primary_external_storage_path
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
    dir = primary_external_storage_path()
    dirname = os.path.join(dir, 'MK_Eng')
    filename='/storage/emulated/0/MK_Eng/eng-rus-new.txt'


my_text=''

# check if directory and file exist
if not os.path.isdir(dirname):
    # Create Directory
    os.mkdir(dirname)
    while os.path.isdir(dirname) == False:
        time.sleep(0.1)
    print('Directory Created...')
    # Create txt-file
    my_text = my_text + 'Directory Created1'
    
    f = open(filename, 'w')
    print('file created', file=f)
    f.close()
    while os.path.isfile(filename) == False:
        time.sleep(0.1)
    print('File Created...')
    my_text = my_text + 'File Created1'
else:
    if not os.path.isfile(filename):
    # Create txt-file
        f = open(filename, 'w')
        print('file created', file=f)
        f.close()
        print('File Created...')
        my_text = my_text +'File Created2'


class MyApp(App):

    def build(self):
        return Label(text = my_text)


if __name__ == '__main__':
    MyApp().run()
