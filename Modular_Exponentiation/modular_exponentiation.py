def base_expansion(n, b):
    q = n
    a = []
    while q != 0:
        a.append(q % b)
        q = q // b
    return a

""" Calculates Modular Exponentiation for base 2 """
def modular_exponentiation(b, n, m):
    a = base_expansion(n, 2) # calculate for base 2
    x = 1
    power = b % m
    for i in range(0, len (a)):
        if a[i] == 1:
            x = (x * power) % m
        power = (power * power) % m
    return x

if __name__ == '__main__':
    print 'Modular Exponentiation:\n'
    b = input('Enter starting integer eg. "3" in "3^644 mod 645"\n')
    n = input('Enter power integer eg. "644" in "3^644 mod 645"\n')
    m = input('Enter mod integer eg. "645" in "3^644 mod 645"\n')

    print '\nAnswer is: ',modular_exponentiation(b,n,m)

    # b = 3
    # n = 644
    # m = 645


    # import timeit
    # t1 = timeit.Timer('b=3;n=644;m=645; modular_exponentiation(b,n,m)','from __main__ import modular_exponentiation')
    # t2 = timeit.Timer('b=3;n=644;m=645; pow(b,n,m)')

    # print 't1', min(t1.repeat(3,100)*1000)
    # print 't2', min(t1.repeat(3,100)*1000)
