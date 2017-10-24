c=[]
p=[]
i=1
r=input("\nenter the range:")
while i<=r:
	item=input("\nenter the elements:")
	c.append(item)
	i=i+1
print "list:",c
s=[item for item in c if item%2==0]
print "final list:",s
p=s[::-1]
print(p)

