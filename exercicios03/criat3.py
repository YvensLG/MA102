from re import A


a=int(input())
x=a
b=0

while(x>0):
   b=10*b+x%10
   x=x//10

if(a==b): print("Capicua")
else: print("Não Capicua") 
