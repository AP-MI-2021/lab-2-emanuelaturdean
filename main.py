

print("test")
print("emma's project")
'''
Dându-se numărul natural n, determină numerele prime p1 si p2 astfel încât n = p1 + p2 (verificarea conjecturii lui Goldbach), p1 minim și p2 maxim.
 Pentru ce fel de n există soluție?

Funcția principală: get_goldbach(n) -> Optional[(int, int)]
Funcția de test: test_get_goldbach()


functia is_prime returneaza 1 daca n este prim si 0 daca nu.

'''
from typing import Optional

def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 0
        return 1
    else:
        return 0

'''
functia get_golbach(n)  verifica daca un numar poate fi scris ca suma de doua numere prime
iar daca conditia ceruta este ideplinita,functia returneaza cele doua valori care alcatuiesc,adunate,numarul initial n
in caz contrar,functia va returna valoarea None
'''
def get_goldbach(n)->Optional[list]:
    p1=2
    while ( p1 < int(n / 2 + 1) ):
        copie=n
        if(is_prime(p1) == 1):
            p2=copie-p1
            if(is_prime(p2) == 1 ):
                return p1,p2
        p1 += 1
    return None
''''
functia testeaza algoritmul functiei goldbach
'''
def test_get_goldbach():
    n = 30
    rezultat = get_goldbach(n)
    if rezultat is not None:
        p1,p2 = rezultat
        assert(p1 == 7)
        assert(p2 == 23)
''''
functia cmmdc realizeaza cmmdc a doua nr 
'''
def cmmdc(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
'''
functia get_cmmmc se foloseste de functia cmmmc pentru a cauta cmmmc aa tuturor nr. din lista,parcurgand
list
'''

def get_cmmmc(lista: list[int]) -> int:
    cmmmc_lista = 1
    for element in lista:
        cmmmc_lista = cmmmc_lista * element // cmmdc(cmmmc_lista, element)
    return cmmmc_lista

def test_get_cmmmc():
    listaDeTestat = [2,3,5]
    rez = get_cmmmc(listaDeTestat)
    assert(rez == 30)
    listaDeTestat = [6, 7, 8]
    rez = get_cmmmc(listaDeTestat)
    assert(rez == 168)

def printMenu():
    # am definit meniul cu toate functiile sale de apel,incluzand si o functie de exit ,spre incheierea programului
    print('0. Exit')
    print('1. Goldbach')
    print('2. Cmmc')
    print('3. Teste')

if __name__ == '__main__':
    printMenu()
    numar = int(input("Apeleaza un numar de comanda din lista de mai sus:"))
    while (numar != 0):
        if numar == 1:
            #goldbach
            numarDeTestat = int(input("Numar pentru Goldbach:"))
            print(get_goldbach(numarDeTestat))
        if numar == 2:
            #cmmmc
            lista = []
            numarElemente = int(input("Numar elemente lista:"))
            for i in range(0, numarElemente):
                lista.append(int(input("Valoare element lista:")))
            print(get_cmmmc(lista))
        if numar == 3:
            test_get_goldbach()
            test_get_cmmmc()
            print('Am rulat testele')
        printMenu()
        numar = int(input("Apeleaza un numar de comanda din lista de mai sus:"))


