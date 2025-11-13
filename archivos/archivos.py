# Abrimos el archivo de entrada en modo lectura
with open("entrada.txt", "r") as entrada, open("salida_holas.txt", "w") as salida:
    for linea in entrada:
        nueva_linea = linea.strip().upper()  # quita saltos y convierte a mayúsculas
        #Solo vamos a escribir las lineas que tengan "Hola"
        print(linea)
        if "HOLA" in nueva_linea:
            salida.write(nueva_linea + "\n")
            print("Si esta")
        else:
            print("No esta")