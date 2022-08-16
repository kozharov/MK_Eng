# не получилось читать текстовый файл с андроида


import random
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.utils import platform
import os
import stat



########################
import kivy


print
print(kivy.platform)

if kivy.platform == 'win':
    dirname='C:/MK_Eng/'
    filename='C:/MK_Eng/eng-rus-new.txt'

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
    dirname = os.path.join(dir, 'MK_Eng')
    filename='/storage/emulated/0/MK_Eng/eng-rus-new.txt'



################################



if not os.path.isdir(dirname):
    # Create Directory
    os.mkdir(dirname)
    print('Directory Created...')
    # Create txt-file
    f = open(filename, 'w')
    print('file created', file=f)
    f.close()
    print('File Created...')
else:
    if not os.path.isfile(filename):
        # Create txt-file
        f = open(filename, 'w')
        print('file created', file=f)
        f.close()
        print('File Created...')


print('Read')
read = os.access(filename, os.R_OK) # Check for read access
print('Write')
write = os.access(filename, os.W_OK) # Check for write access
os.chmod(filename, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
read1 = os.access(filename, os.R_OK) # Check for read access
print('Write')
write1 = os.access(filename, os.W_OK) # Check for write access

# check file contents

"""
print('length -', os.path.getsize(filename))
if os.path.getsize(filename) == 14:
    status = 'Empty file. TAking default data...'
else:
    status = 'reading customer\'s file...'




status = '1'


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

status = '2'

# Getting data from file
#filename='C:/Users/mkozharov/AppData/Local/Programs/Python/Python38/Scripts/eng/eng-rus-new.txt'

#print(filename)


s = open(filename).read()
lines = [line.strip() for line in open(filename)]


status = '3'

for i in range (0,len(lines)):
    num.append(i)
    line=lines[i].split(chr(9))
    column1.append(line[1])
    column2.append(line[0])
    column3.append(line[3])
    column4.append(line[2])
    column5.append(line[4])

word_list=column4
word_meaning=column3
example_list=column1
example_meaning=column2
real_example=column5


print('SUCCESS!!!!!')
print(example_list)



print(len(lines))
"""


class New_EngApp(App):

    
    
    def build(self):
     
        superBox = BoxLayout(orientation ='vertical')

#        o_text = TextInput(text='Output: ' + filename + ' ' + status + ' ' + str(dir_path), readonly='True', foreground_color = 'black', line_height = 1, font_name = 'DejaVuSans.ttf')
        o_text = TextInput(text = 'XXXXX' + str(read) + 'YYYYYY'+ str(write) + 'XXXXX' + str(read1) + 'YYYYYY'+ str(write1), readonly='True', foreground_color = 'black', line_height = 1, font_name = 'DejaVuSans.ttf')

        superBox.add_widget(o_text)




        return superBox
   
if __name__=="__main__":
    New_EngApp().run()

