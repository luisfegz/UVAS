import sys
from heapq import heappop,heappush

def cola_con_prioridad(lista):
    cola_sell = []
    cola_buy = []
    lista_ordenes = []
    i = 0
    j = 0

    for i in range(0, len(lista), 1): #voy metiendo a las colas segun vaya leyendo
        if lista[i][0] == 'sell':
            heappush(cola_sell,(lista[i][2],lista[i][1]))
        else:
            heappush(cola_buy,((lista[i][2])*(-1),lista[i][1]))
        """
        x = heappop(cola_buy)
        y = heappop(cola_sell)
        """
        z = 0
        for z in range(0, len(cola_sell),1):
            if (cola_buy[0][0])*(-1) == cola_sell[z][0]:
                x = heappop(cola_buy)
                heappush(lista_ordenes,x)
                listica = [ (lista_ordenes[0][0]*-1)]
            """"
            if (cola_buy[1][0])*(-1) == cola_sell[z][0]:
                x = heappop(cola_buy)
                #heappush(lista_ordenes,x)
                listica = [ (lista_ordenes[0][0]*-1)]

            if (cola_buy[2][0])*(-1) == cola_sell[z][0]:
                x = heappop(cola_buy)
                heappush(lista_ordenes,x)
                listica = [ (lista_ordenes[0][0]*-1)]
            """
    print(listica)

def main():
    line = sys.stdin.readline() #Bloques de acciones
    i = 0
    while ( i < int(line)):
        j = 0
        lista = []
        line2 = sys.stdin.readline() #numero de acciones
        while ( j < int(line2) ):
            line3 = sys.stdin.readline().split()
            order, number_actions, stock_price = line3[0],line3[1],line3[4]
            lista.append((line3[0],int(line3[1]),int(line3[4])))
            j+=1
        cola_con_prioridad(lista)
        i+=1



main()