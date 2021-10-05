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
def get_golbach(n):
    copie=n
    ok1=0
    ok2=0
    for i in range(2,int(n / 2) ):
        if (is_prime(i) == 1 ):
            p1=copie
            copie= copie - i
            ok1=1
        if (is_prime(copie) == 1 ):
            p2=copie
            ok2=1
        if( ok1 == 1 and ok2 == 1) :
            return p1 , p2

    return 0
def main():
n=13
print(get_golbach(n))