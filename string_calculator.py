def add(numbers):
    if numbers == "":
        return 0
    
    if "," in numbers:
       
        lista_numeros = numbers.split(",")
        
        return int(lista_numeros[0]) + int(lista_numeros[1])
    
    return int(numbers)
