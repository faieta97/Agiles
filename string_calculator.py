def add(numbers):
    if numbers == "":
        return 0
    
    numeros_limpios = numbers.replace("\n", ",")
    
    return sum(int(n) for n in numeros_limpios.split(","))