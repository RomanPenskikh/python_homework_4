# Создать и заполнить файл с случайными целыми значениями 
# Выполнить сортировку содержимого файла по возрастанию
from array import array
from fnmatch import translate
from importlib.resources import path
import random
from subprocess import list2cmdline
from tkinter import N, Place


my_file = open ("new_file_4.1.txt", "w+")
array_new_file = []
array_new_file = [str(random.randint(0, 9)) for i in range(30)] 
print(array_new_file)

with open("new_file_4.1.txt", "a") as data:
    for listitem in array_new_file:
        data.writelines('%s\n'%listitem)
    data.close()

my_file_sort=[]

with open("new_file_4.1.txt", "r") as ins:
    my_file_sort = []
    for line in ins:
        my_file_sort.append(line)

my_file_sort_2=[]
for j in range (30):
    my_file_sort_2.append(my_file_sort[j])
    my_file_sort_2[j]=my_file_sort_2[j].replace('\n','')
    my_file_sort_2[j]=int(my_file_sort_2[j])
print(my_file_sort_2)
my_file_sort_2.sort()
print(my_file_sort_2)

data = open("new_file_4.1.txt", "a")
data.writelines(str(my_file_sort_2))
data.close()
