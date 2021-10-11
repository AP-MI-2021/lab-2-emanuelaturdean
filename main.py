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
def get_cmmmc(numbers):
# max va fi nr.ales ca fiind cel mai mare,initial pornind de la 0 si va deveni cea mai mare
# valoare din lista
    max=0
    for x in numbers:
        if x > max:
            max = x
    ok1 = 0
    ok2 = 1
    while ( ok1 = 0):
        while ( ok2 = 1):
            for x in numbers:
                if ( max % x != 0):
                    ok2=0
        if (ok2 == 0):
            max += 1
        else:
            ok1 = 1
    return max


    while (True)
        for x in numbers:
        if (max % x != 0):
            break
        max +=1

    return max



def main():
    test_goldbach()
    print(get_cmmmc([1,2,3]))






if __name__ == '__main__':
    main()
