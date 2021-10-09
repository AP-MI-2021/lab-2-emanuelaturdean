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
    p1=2
    while ( p1 < int(n / 2 + 1) ):
        copie=n
        if(is_prime(p1) == 1):
            p2=copie-p1
            if(is_prime(p2) == 1 ):
                return p1,p2
        p1 += 1
    return None

def funct(n):
    return 1,n


def main():
    print(is_prime(25))
    return_value = get_golbach(60)
    if return_value is not None:
        p1,p2 = return_value
        print(p1)
        print(p2)





if __name__ == '__main__':
    main()
