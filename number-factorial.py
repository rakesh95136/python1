#Write a program to find the factorail of given number

x = 5
f = 1
def fun1(x):
	if x == 1:
		return 1
	else:
		f = x * fun1(x - 1)
		return f

		
d = fun1(x)
print(d)
		
		