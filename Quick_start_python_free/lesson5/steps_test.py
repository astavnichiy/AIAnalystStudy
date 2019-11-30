import os
import psutil
import random
import sys
import shutil

import robot

#===============================================================================
# Тестирование шигов
#===============================================================================
dirname = input("укажите имя директории:")
file_list = os.listdir(dirname)
print(file_list)
for file_name in file_list:
    full_name = os.path.join(dirname, file_name)
    if full_name.endswith('.dupl'):
            os.remove(full_name)
    else:
        pass
