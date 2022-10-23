def func1(a, b, c):
  maior = a
  if b > maior:
    maior = b
  if c > maior:
    maior = c  
  return maior

a = int(input())
b = int(input())
c = int(input())
m = func1(a, b, c)
 
print("O maior é", m)