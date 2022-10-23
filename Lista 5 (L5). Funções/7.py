def numPos(x):
  if x < 0:
    return False
  else:
    return True
   

def fat(n):
  j=1
  if numPos(n) == False:
    return "Não existe fatorial de número negativo"
  else:
    for i in range(1,n+1):
     j *= i
     i+=i
  return j

k = int(input("Descobrir o fatorial: "))

print(fat(k))