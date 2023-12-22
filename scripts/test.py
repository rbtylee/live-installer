#!/usr/bin/python3

import os
current_dir = os.path.dirname(os.path.realpath(__file__)) 
print(current_dir)
# Move up three levels in the directory hierarchy
target_dir = os.path.abspath(os.path.join(current_dir, '../usr/share/live-installer/slideshow//index.html'))

print(target_dir)
slideshow_main = 'file://' + os.path.join('/home/ylee/code/NOW/li/usr/share/live-installer/slideshow//index.html')

# python3 python3-gi gir1.2-webkit2-4.0 xapp
