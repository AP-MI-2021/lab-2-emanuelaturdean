print("test")
print("emma's project")
'''
Dându-se numărul natural n, determină numerele prime p1 si p2 astfel încât n = p1 + p2 (verificarea conjecturii lui Goldbach), p1 minim și p2 maxim.
 Pentru ce fel de n există soluție?

Funcția principală: get_goldbach(n) -> Optional[(int, int)]
Funcția de test: test_get_goldbach()


functia is_prime returneaza 1 daca n este prim si 0 daca nu.

'''

def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 0
        return 1
    else:
        return 0

'''
functia get_golbach(n) returneaza
'''
def get_goldbach(n):
    p1=2
    while ( p1 < int(n / 2 + 1) ):
        copie=n
        if(is_prime(p1) == 1):
            p2=copie-p1
            if(is_prime(p2) == 1 ):
                return p1,p2
        p1 += 1
    return None

def test_goldbach():
    n = 30
    rezultat = get_goldbach(n)
    if rezultat is not None:
        p1,p2 = rezultat
        assert(p1 == 7)
        assert(p2 == 23)
def cmmdc(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
def get_cmmmc(a,b):
    return a*b / cmmdc(a,b)
def cmmmc(numbers):
    cel_mai_mic_multiplu_comun=numbers[0]
    for i in range(1,len(numbers)):
        cel_mai_mic_multiplu_comun=cmmmc(cel_mai_mic_multiplu_comun,numbers[i])
    return cel_mai_mic_multiplu_comun
def citire(numbers):
    n=int(input('cate numere sunt:'))
    for i in range(0,n):
        x=int(input())
        numbers.append(x)


if __name__ == '__main__':
    numbers=[]
    citire(numbers)
    print(get_cmmmc(numbers))
