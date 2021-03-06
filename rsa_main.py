from random import randrange
import base64

def findFactor(n):
    global prime_list
    result = []
    i = 0
    while not n == 1:
        if n % prime_list[i] == 0:
            result.append(prime_list[i])
            while n % prime_list[i] == 0:
                n //= prime_list[i]
        i += 1
    return result

def encryption(m, N, e):
  c = m**e % N
  return c
  
def decryption(c, N, d):
  m = c**d % N
  return m

MIN_PRIME = 2**7
MAX_PRIME = 2**12

erato_sieve = [0] + [1 for _ in range(MAX_PRIME-1)]
prime_list = []

# get prime_list by erastosthenes
for i in range(len(erato_sieve)):
    if erato_sieve[i] == 1:
        prime_list.append(i+1)
        for j in range(2, MAX_PRIME // (i+1) + 1):
            erato_sieve[(i+1) * j - 1] = 0

# get ranged_prime_list 
i = 0
while not prime_list[i] >= MIN_PRIME:
    i += 1
ranged_prime_list = prime_list[i:]
vi = len(prime_list) - 1
while not prime_list[i] <= MAX_PRIME:
    i -= 1
ranged_prime_list = ranged_prime_list[:i-1]
# print(ranged_prime_list)

# testable line
# print(findFactor(97))
# exit()

# main process
p = ranged_prime_list[randrange(len(ranged_prime_list))]
q = ranged_prime_list[randrange(len(ranged_prime_list))]
while p == q: # p != q
    q = prime_list[randrange(len(prime_list))]

N = p * q
pN = (p-1) * (q-1)
# get coprime num of pN
pN_factor = list(set(findFactor(p-1) + findFactor(q-1))) # for find coprime of pN
pN_non_coprime_list = set()
pN_coprime_list = range(1, pN+1)
for i in pN_factor:
    for j in range(pN // i):
        pN_non_coprime_list.add(i * (j+1)) # get non coprime num
pN_coprime_list = sorted(list(set(pN_coprime_list) - pN_non_coprime_list))

e = pN_coprime_list[randrange(len(pN_coprime_list))]

# find d
d_list = []
i = 1
while not len(d_list) >= 10:
    if i * e % pN == 1:
        d_list.append(i)
    i += 1
d = d_list[randrange(len(d_list))]
# for various test
#print(d_list)
print(f'p, q: {p}, {q}\nN, pN: {N}, {pN}');print();print(pN_factor);
print('N:',N)
print('e:',e)
print('d:',d)


public_key = (N, e)
private_key = (N, d)

m = int(input())
a =encryption(m, N, e)
print(a)
b = decryption(a, N, d)
print(b)
