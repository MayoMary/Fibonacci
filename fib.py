# Ian McLoughlin
# A program that displays Fibonacci numbers.
# Exercise 1
# My name is Mary, so the first and last letters of my name (M + Y =13 + 25) give the number 38. The 38th Fibonacci number is 39088169.



def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 38
ans = fib(x)
print("Fibonacci number", x, "is", ans)



# Ian McLoughlin
# A program that displays Fibonacci numbers.
# Exercise 2
# My surname is McHale.
#The first letter is M and the number is 77.
# The last letter is e and the number is 101.
# Script returms the Fibonacci number for 178. 

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 178
ans = fib(x)
print("Fibonacci number", x, "is", ans)
