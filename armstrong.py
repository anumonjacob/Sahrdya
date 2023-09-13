n = int(input("Enter the number : ")) 
n1 = n
s = 0
rev = 0 
while n > 0:
	dig = n% 10
	s = s + dig * dig*dig 
	n = n // 10
if s == n1:
	print("Number is armstrong ") 
else:
	print("Number is not armstrong ")