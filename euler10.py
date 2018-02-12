from math import sqrt,floor

def is_prime(n):
    i=1
    for i in range(2,floor(sqrt(n))+1 ):
        if n%i == 0:
            return False
    return True

i=1
s=0
for i in range(1,2000000):
    if is_prime(i):
        s+=i
print(s-1)
