def fibonacci(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   elif n > 1:
       return(fibonacci(n-1) + fibonacci(n-2))


nterms = int(input("Introduce un numero"))

while nterms <= 0:
    print("Please enter a positive integer")
    nterms = int(input("Introduce un numero"))

print("Fibonacci sequence:")
for i in range (nterms+1):
   print(fibonacci(i))
