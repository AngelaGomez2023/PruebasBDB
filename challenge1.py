#Dada una lista de n números con dígitos en el rango [0, S], donde n <= 100, invierte todas las posiciones de la lista en tiempo O(n).
#Si el número de entrada contiene un dígito mayor o igual a S, elimina dicho dígito del número. Por ejemplo, con S=6, 61 se convierte en 1 y 6 será eliminado de la lista. El resultado debe imprimirse en la consola/terminal. No utilices el método sort incorporado de tu lenguaje.

#Ejemplos con S=2:

#[1, 2, 3, 4, 5, 6] -> [5, 4, 3, 2, 1]
#[10, 20, 30, 40] -> [40, 30, 20, 10]
#[6] -> []
#[66] -> []
#[65] -> [5]
#[6, 2, 1] -> [1, 2]
#[60, 6, 5, 4, 3, 2, 7, 7, 29, 1] -> [1, 2, 2, 3, 4, 5, 0]


def reverse_and_remove(nums, S): 
    result = [] 
    for num in nums: 
        filtered_digits = [d for d in str(num) if int(d) < S]
        if filtered_digits:
            reversed_num = int("".join(filtered_digits[::-1]))
            if reversed_num !=0:
                result.append(reversed_num)
    return result[::-1] 

S = 3
nums = [10,20,30,40,60,6,5,4,3,2,29,1]

result = reverse_and_remove(nums, S)
print(result)
           
