#!/usr/bin/python3

import os

os.chdir('videos')

for f in os.listdir('.'):
    file_names, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = file_names.split('-')
    new_name = f'{f_num.strip()[1:].zfill(2)}-{f_title.strip()}{f_ext}'
    os.rename(f, new_name)
