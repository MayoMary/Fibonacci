# Mary McHale, 4th March 2018
# Topic 3 Collatz exercise
# https://en.wikipedia.org/wiki/Collatz_conjecture
# State where gor ! from GIVE LINK

n = input ("Please type a positive number between 1 and 100: ")
n=ord(n)
print (n)

while n != 1:
  if n % 2 ==0:
    p = n/2
    print (p)
  if n % 2 !=0:
    p = (n * 3 ) + 1
    print (p)
  n = p
  
