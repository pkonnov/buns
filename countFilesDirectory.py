#!/usr/bin/python3
import sys
import os
import glob

"""
итерироваться по файлам в директории
считать кол-во файлов в дериктории
"""
path_dir = str(input('Введите путь до дериктории: '))
nameExtention = str(input('Введите расширение файла: '))

# def dirTarget(*args):

#     dir_name = os.path.abspath('/home/kirill-n/Загрузки')
#     #if name == '':
#     #    print('Введите имя дериктории')
#     #else:
#     item_files = os.walk(dir_name)
#     for root, dirs, files  in item_files:
#         print(len(files))


def dirListFilesGlob(*args):
    targetLists = glob.glob(path_dir + '/*.%s' % nameExtention)
    print('Найдено ' + str(len(targetLists)) + ' файлов с расширением %s'
            % nameExtention)



if __name__ == "__main__":
    dirListFilesGlob()
