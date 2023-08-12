from sys import stdin

def merge(A, p, q, r, b):
    mitad_izquierda = A[p:q + 1]
    mitad_derecha = A[q + 1:r + 1]

    i = j = 0
    k = p

    while i < len(mitad_izquierda) and j < len(mitad_derecha):
        if mitad_izquierda[i] <= mitad_derecha[j]:
            b[k] = mitad_izquierda[i]
            i += 1
        else:
            b[k] = mitad_derecha[j]
            j += 1
        k += 1

    while i < len(mitad_izquierda):
        b[k] = mitad_izquierda[i]
        i += 1
        k += 1

    while j < len(mitad_derecha):
        b[k] = mitad_derecha[j]
        j += 1
        k += 1

    # Copiar los elementos de 'b' a A en las posiciones p a r
    for i in range(p, r + 1):
        A[i] = b[i]

def merge_sort_range(A, p, r, b):
    inversions = 0 #Contador de inversiones
    if p < r:
        q = (p + r) // 2
        inversions += merge_sort_range(A, p, q, B)
        inversions += merge_sort_range(A, q + 1, r, B)
        inversions += merge(A, p, q, r, B)

    return inversions

def lectura_entrada():
    A = []

    while not (0 in A):
        vals = list(map(int, stdin.readline().split()))
        A.extend(vals)
        n = len(A)
        b = [0] * n  # Crear el arreglo auxiliar B
        p = 0
        r = n - 1

        merge_sort_range(A, p, r, b)
        i = p
        q = (p + r) // 2
        j = q + 1
        inversions = 0
        # Ciclo que se repite mientras i y j sean menores o iguales que r
        while i <= q and j <= r:
            if A[i] <= A[j]:
                b[i + j - q - 1] = A[i]  # Copiar el elemento de A[i] en 'b'
                i += 1
            else:
                b[i + j - q - 1] = A[j]  # Copiar el elemento de A[j] en 'b'
                j += 1

        # Copiar los elementos restantes de la mitad izquierda si es necesario
        while i <= q:
            b[i + j - q - 1] = A[i]
            i += 1

        # Copiar los elementos restantes de la mitad derecha si es necesario
        while j <= r:
            b[i + j - q - 1] = A[j]
            j += 1

        # Copiar los elementos de 'b' a A en las posiciones p a r
        for i in range(p, r + 1):
            A[i] = b[i]
        inversions = merge_sort_range(A, p, r, b)
        print(inversions)
        return inversions

def main():
    lectura_entrada()
    #Al final quise declarar todas las variables dentro de lectura entrada
main()
