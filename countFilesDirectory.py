#!/usr/bin/python3
import sys, os
import glob

"""
итерироваться по файлам в директории
считать кол-во файлов в дериктории
"""

# def dirTarget(*args):

#     dir_name = os.path.abspath('/home/kirill-n/Загрузки')
#     #if name == '':
#     #    print('Введите имя дериктории')
#     #else:
#     item_files = os.walk(dir_name)
#     for root, dirs, files  in item_files:
#         print(len(files))
class GetPathDirectory():
	path_dir1 = str(input('Введите путь до дериктории: '))

def dirListFilesGlob(*args):
	path_dir = GetPathDirectory.path_dir1
	allFiles = glob.glob(path_dir + '/*')
	# iterFiles = [i for i in allFiles]
	# print(iterFiles)
	nameExtention = str(input('Введите расширение файла: '))
	targetLists = glob.glob(path_dir + '/*.%s' % nameExtention)
	print('Найдено ' + str(len(targetLists)) + ' файлов с расширением %s'
	    % nameExtention)



if __name__ == "__main__":
    dirListFilesGlob()
