"""create a list of integers and find maxmum difference that exists between any number and any smaller number in list"""

l=[]
m=[]
n=int(input())
for i in range (n):
  a=int(input())
  l.append(a)

for i in range(len(l)):
  max=0
  for j in range(len(l)):
    if (j==i):
      continue
    elif (l[j]>max and (l[i]>l[j])):
      max=l[j]
  diff=l[i]-max
  if(max!=0):
      m.append(diff)

print(m)

    
    
  