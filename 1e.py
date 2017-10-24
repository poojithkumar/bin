def findmax(t):
	if(len(t)==1):
		return t[0]
	else:
		if(t[0]>findmax(t[1:])):
			return t[0]
		else:
			return findmax(t[1:])

s=[]
n=int(input("Enter No. of Elements in the list: "))
i=1
print ("Enter the Elements:-")
while (i<=n):
	inp=int(input())
	s.append(inp)
	i=i+1
print ("Entered Elememts are: ",s)
print ("Maximum Element is %d\n"%(int(findmax(s))))

