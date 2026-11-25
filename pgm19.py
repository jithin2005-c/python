a=int(input("Enter first numbers :"))
b=int(input("Enter second numbers :"))
while b:
  a,b=b,a%b
  
print("GCD=",a)
