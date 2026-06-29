import json

VOCALES = "AEIOU"


def linea_a_matriz(linea):
    linea = linea.strip()
    matriz = []
    for fila in range(3):
        fila_actual = []
        for col in range(3):
            fila_actual.append(linea[fila * 3 + col])
        matriz.append(fila_actual)
    return matriz


def mostrar_matriz(matriz):
    for fila in range(3):
        fila_str = ""
        for col in range(3):
            if col == 0:
                fila_str = matriz[fila][col]
            else:
                fila_str = fila_str + " " + matriz[fila][col]
        print(fila_str)
    print()


def generar_matriz_vocales(matriz):
    vocales_encontradas = []
    for fila in range(3):
        for col in range(3):
            if matriz[fila][col] in VOCALES:
                vocales_encontradas.append(matriz[fila][col])

    while len(vocales_encontradas) < 9:
        vocales_encontradas.append("*")

    nueva_matriz = []
    for fila in range(3):
        fila_actual = []
        for col in range(3):
            fila_actual.append(vocales_encontradas[fila * 3 + col])
        nueva_matriz.append(fila_actual)
    return nueva_matriz


def actualizar_estadisticas(matriz_vocales, estadisticas):
    for fila in range(3):
        for col in range(3):
            car = matriz_vocales[fila][col]
            if car in estadisticas:
                estadisticas[car] = estadisticas[car] + 1


def procesar_archivo(nombre_archivo):
    estadisticas = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    cant_matrices = 0

    archivo = open(nombre_archivo, "r")
    linea = archivo.readline()
    while linea != "":
        if len(linea.strip()) >= 9:
            matriz_original = linea_a_matriz(linea)

            print("Matriz original:")
            mostrar_matriz(matriz_original)

            matriz_vocales = generar_matriz_vocales(matriz_original)

            print("Matriz de vocales:")
            mostrar_matriz(matriz_vocales)

            actualizar_estadisticas(matriz_vocales, estadisticas)
            cant_matrices = cant_matrices + 1

        linea = archivo.readline()

    archivo.close()
    return cant_matrices, estadisticas


def mostrar_resultados(cant_matrices, estadisticas):
    total_vocales = 0
    for vocal in estadisticas:
        total_vocales = total_vocales + estadisticas[vocal]

    print("Matrices procesadas:", cant_matrices)
    print("Total de vocales encontradas:", total_vocales)
    for vocal in estadisticas:
        print(vocal + ":", estadisticas[vocal])


def guardar_estadisticas_json(cant_matrices, estadisticas, nombre_archivo):
    total_vocales = 0
    for vocal in estadisticas:
        total_vocales = total_vocales + estadisticas[vocal]

    datos = {
        "matrices_procesadas": cant_matrices,
        "total_vocales": total_vocales,
        "apariciones": estadisticas
    }

    archivo_json = open(nombre_archivo, "w")
    json.dump(datos, archivo_json, indent=4)
    archivo_json.close()

    print("Estadisticas guardadas en", nombre_archivo)


def main():
    cant_matrices, estadisticas = procesar_archivo("datos.txt")
    mostrar_resultados(cant_matrices, estadisticas)
    guardar_estadisticas_json(cant_matrices, estadisticas, "estadisticas.json")


main()