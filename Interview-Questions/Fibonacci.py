n = 10
first = 0
second = 1
print(first ," , ",second, end = " , ")
for i in range (1,  n-1):
  third = first + second
  first = second
  second = third 
  print(third, end = " , ")
