import random
d= {1:'R',2:'P',3:'S'}
c=d[random.randint(1,3)]
p=input("enter 'R' or 'P' or 'S' :")
if(c==p):
	print("tie")
elif((c=='R'and p=='S') or (c=='P'and p=='R') or (c=='S'and p=='P')):
	print("computer wins")
else:
	print("player wins")
