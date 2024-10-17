#Escribe una función que reciba un arreglo no vacío de enteros ordenados de manera ascendente y devuelva un nuevo arreglo de la misma longitud con los cuadrados de los enteros originales, también ordenados en orden ascendente. Si el número resultante está fuera del rango [0, SS] (para S=6, el rango sería [0, 66]), elimínalo del arreglo resultante. No utilices el método sort incorporado de tu lenguaje.

#Ejemplos con S=3:
#c54e140a2dd945e845759e651c934738

#{"array": [1, 2, 3, 5, 6, 8, 9]} -> [1, 4, 9, 25, 36, 64]
#{"array": [-2, -1]} -> [1, 4]
#{"array": [-6, -5, 0, 5, 6]} -> [0, 25, 25, 36, 36]
#{"array": [-10, 10]} -> []

def ordered_squares (arr, S):#defino la funcioon
    
    squares = [x * x for x in arr]
    filtered_squares = [sq for sq in squares if 0 <= sq <= S * (S + 1)]
    sorted_squares = []
    for square in filtered_squares:
        inserted = False
        for i in range(len(sorted_squares)):
            if square < sorted_squares[i]:
                sorted_squares.insert(i, square)
                inserted = True
                break
        if not inserted:
            sorted_squares.append(square)
    return sorted_squares

S = 3
arr = [1,2,3,4,5,6,8,9]

print(ordered_squares(arr, S))



               