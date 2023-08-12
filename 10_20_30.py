from sys import stdin
def leer_enteros():
    baraja = []
    while not (0 in baraja):
        vals = list(map(int, stdin.readline().split()))
        baraja.extend(vals)
        if 52 - len(baraja) <= 0:
            ganar_perder_empate(baraja[0:52])
            baraja = baraja[52:]




def ganar_perder_empate(baraja):
    print(baraja)

    #repartir: funcion 7 mazos de 3 cartas de izquierda a derecha
    #jugar

def repartir(baraja):
    i = 0
    j = 0
    k = 0
    n = 0
    m = 0
    l = 0
    c = 0
    mazo1 = []
    mazo2 = []
    mazo3 = []
    mazo4 = []
    mazo5 = []
    mazo6 = []
    mazo7 = []

    for i in range(0, len(baraja),6):
        mazo1.extend(baraja[i])
    print(mazo1)

    for j in range(1, len(baraja),6):
        mazo2.extend(baraja[j])
    print(mazo2)

    for k in range(2, len(baraja),6):
        mazo3.extend(baraja[k])
    print(mazo3)

    for n in range(3, len(baraja),6):
        mazo4.extend(baraja[n])
    print(mazo4)

    for m in range(4, len(baraja),6):
        mazo5.extend(baraja[m])
    print(mazo5)

    for l in range(5, len(baraja),6):
        mazo6.extend(baraja[l])
    print(mazo6)


    for c in range (6, len(baraja),6):
        mazo7.extend(baraja[c])
    print(mazo7)

    mazoss = [ mazo1, mazo2, mazo3 ,mazo4, mazo5, mazo6, mazo7]
    print(mazoss)
def main():
    leer_enteros()
main()