import random

def NM(m, men):
    if m[i] < men:
      men = m[i]
      return men
    else:
      return men

i = 0
x = []

x.append (random.randint (1,10000))
menor = x[0]
for i in range(9):
  x.append(random.randint(1,10000))
  print(x[i], end=" ")
  NM(x, menor)
  menor = NM(x, menor)

print(f"O menor número é {menor}")