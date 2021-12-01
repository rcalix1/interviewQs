

def get_primes(N):
    primes = []
    is_primes =  [False, False] + [True]*(N-1)
    print(is_primes)
    for p in range(2, N+1):
        if is_primes[p]:
            primes.append(p)
            for j in range(p, N):
                multip = j*p
                #print(multip)
                if multip <= N:
                    is_primes[multip] = False
    print(primes)




N = 20
get_primes(N)
