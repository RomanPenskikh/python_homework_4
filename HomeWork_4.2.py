# Дан список чисел. Создать список в который попадают числа. описывающие возрастающую последовательность и содержащее максимальное кол-во элементов
# ПРимер [1, 5, 2, 3, 4, 6, 1, 7 ] => [1,2,3,4,6,7]
# Динамическое программирование — способ решения задач путём разбиения их на подзадачи, которые, в свою очередь, используются для нахождения ответа исходной задачи. 

array_max = [1, 5, 2, 3, 4, 6, 1, 7]

array_up = []
array_dawn = []
j = 1
 
while j < len(array_max):
  i = j
  N = array_max[:]
  while i < len(N)-1:
    if N[i] < N[i+1]: 
      array_dawn.append(N[i])
      i += 1
    else:
      N.pop(i+1)
      
  j+=1
  if len(array_up) < len(array_dawn):
    array_up = array_dawn
  array_dawn=[]
 
if array_max[-1] > array_up[-1]:
  array_up.append(array_max[-1])
  
if array_max[0] < array_up[0]:
  array_up.insert(0, array_max[0])
print(array_max)
print(array_up)