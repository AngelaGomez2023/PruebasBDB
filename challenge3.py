#Dado un arreglo de enteros positivos que representan los valores de monedas que posees, escribe
# una función que devuelva la cantidad mínima de cambio (la suma mínima de dinero) que NO puedes 
# dar como cambio. Las monedas pueden tener cualquier valor entero positivo y no son necesariamente 
# únicas (es decir, puedes tener varias monedas del mismo valor). Puedes usar el método sort
# incorporado de tu lenguaje.

#Pistas:

#Una forma de resolver este problema es intentar crear todas las cantidades posibles de cambio, comenzando desde 1 y subiendo hasta que ya no puedas crear una cantidad. Aunque este enfoque funciona, hay uno mejor.
#Comienza ordenando el arreglo de entrada. Ya que estás buscando la cantidad mínima de cambio que no puedes crear, tiene sentido considerar primero las monedas más pequeñas.
#Para entender el truco de este problema, considera el siguiente ejemplo: monedas = [1, 2, 4]. Con este conjunto de monedas, podemos crear 1, 2, 3, 4, 5, 6 y 7 centavos de cambio. Ahora, si agregáramos una moneda de valor 9, no podríamos crear 8 centavos. Sin embargo, si agregáramos una moneda de valor 7, podríamos crear 8 centavos y todas las cantidades de cambio desde 1 hasta 15.
#Ejemplos:

#{"coins": [5, 7, 1, 1, 2, 3, 22]} -> 20
#{"coins": [1, 1, 1, 1, 1]} -> 6
#{"coins": [1, 5, 1, 1, 1, 10, 15, 20, 100]} -> 55

def min_change_imposible_set(coins):
    coins.sort()
    min_change = 1

    for coin in coins:
        if coin > min_change:
            return min_change
        min_change += coin
    return min_change

coins = [5,7,1,1,2,3,22]
result = min_change_imposible_set(coins)
print("The minimum amount of change that cannot be formed is:", result)