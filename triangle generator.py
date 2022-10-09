def triangle1():
  size = int(input("enter size for triangle: "))
  start = 0
  triangle = "+"
  while start < size:
      print(triangle)
      start += 1
      triangle += "+"
  if start == size:
      triangle1()
triangle1()      
