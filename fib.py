# Ian McLoughlin
# A program that displays Fibonacci numbers.
# Exercise 1

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