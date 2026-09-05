# funciones.py

def registrar_comercios(numero_comercios):
    """
    1. Crear un ciclo for de N (numero_comercios) iteraciones.
    2. Crear un diccionario para registrar los comercios.
    3. Crear una lista vacía fuera del for y agregar cada diccionario a la lista.
    """
    lista_comercios = []
    
    for i in range(numero_comercios):
        print(f"\n--- Registro del Comercio {i + 1} ---")
        nombre = input("Nombre del comercio: ")
        meta = float(input("Meta de consumo del comercio: "))
        
        comercio = {
            "nombre": nombre,
            "meta": meta,
            "consumos": [],
            "promedio": 0.0,
            "variacion": 0.0,
            "clasificacion": ""
        }
        lista_comercios.append(comercio)
        
    return lista_comercios


def registrar_consumo(lista_comercios):
    """
    1. Crear un ciclo para ingresar 4 consumos.
    2. Crear un condicional if que valide que los datos ingresados sean mayores que 0.
    3. Almacenar los consumos en la lista consumos de cada diccionario.
    4. Retornar la lista actualizada.
    """
    for comercio in lista_comercios:
        print(f"\nIngreso de consumos para: {comercio['nombre']}")
        consumos = []
        semana = 1
        while semana <= 4:
            try:
                consumo = float(input(f"  Ingrese consumo de la semana {semana}: "))
                if consumo > 0:
                    consumos.append(consumo)
                    semana += 1
                else:
                    print("  [Error] El consumo debe ser mayor que 0. Intente nuevamente.")
            except ValueError:
                print("  [Error] Ingrese un número válido.")
        
        comercio["consumos"] = consumos
        
    return lista_comercios


def calcular_promedio(lista_consumo):
    """
    1. Crear un ciclo for que permite calcular el promedio.
    2. Crear una variable en 0 y por cada iteración del for sumar su valor y dividir en 4.
    3. Retornar la lista con el promedio actualizado.
    """
    for comercio in lista_consumo:
        suma = 0.0
        for c in comercio["consumos"]:
            suma += c
        promedio = suma / 4
        comercio["promedio"] = promedio
        
    return lista_consumo


def calcular_variacion(lista_consumo):
    """
    1. Crear un ciclo for que diferencie el porcentaje entre la primera y cuarta semana:
       ((semana4 - semana1) / semana1) * 100
    2. Retornar la variación porcentual actualizando la lista.
    """
    for comercio in lista_consumo:
        semana1 = comercio["consumos"][0]
        semana4 = comercio["consumos"][3]
        
        if semana1 != 0:
            variacion = ((semana4 - semana1) / semana1) * 100
        else:
            variacion = 0.0
            
        comercio["variacion"] = variacion
        
    return lista_consumo


def clasificar_consumo(promedio, meta, variacion):
    """
    1. Crear un condicional que permita clasificar (promedio, meta y variacion):
    2. Condición 1: si promedio <= meta Y variacion <= 5% -> Retornar "Eficiente"
    3. Condición 2: si promedio <= meta Y variacion > 5%  -> Retornar "En observación"
    4. Condición 3: si promedio <= meta * 1.20              -> Retornar "Alto"
    5. Sino cumple ninguna condición                       -> Retornar "Crítico"
    """
    if promedio <= meta and variacion <= 5:
        return "Eficiente"
    elif promedio <= meta and variacion > 5:
        return "En observación"
    elif promedio <= meta * 1.20:
        return "Alto"
    else:
        return "Crítico"


def generar_informe(lista_comercios):
    """
    1. Crear un ciclo for que recorra la lista comercios por comercio.
    2. Crear un condicional (if-elif-else) que evalúe la clasificación que tiene el comercio actual:
       ("Eficiente", "En observación", "Alto" o "Crítico").
    3. Crear un contador que dentro de la opción que resulte verdadera le sume 1 al contador correspondiente.
    4. Mostrar todo en la consola con print.
    """
    cont_eficiente = 0
    cont_en_observacion = 0
    cont_alto = 0
    cont_critico = 0
    
    print("\n==================================================")
    print("                INFORME GENERAL                   ")
    print("==================================================")
    
    for comercio in lista_comercios:
        clasif = comercio["clasificacion"]
        
        # Conteo según clasificación
        if clasif == "Eficiente":
            cont_eficiente += 1
        elif clasif == "En observación":
            cont_en_observacion += 1
        elif clasif == "Alto":
            cont_alto += 1
        elif clasif == "Crítico":
            cont_critico += 1
            
        # Imprimir detalles de cada comercio
        print(f"Comercio: {comercio['nombre']}")
        print(f"  - Meta: {comercio['meta']}")
        print(f"  - Consumos (Semanas 1-4): {comercio['consumos']}")
        print(f"  - Promedio: {comercio['promedio']:.2f}")
        print(f"  - Variación porcentual: {comercio['variacion']:.2f}%")
        print(f"  - Clasificación: {clasif}")
        print("-" * 50)
        
    print("\n--- RESUMEN Y CONTEO DE CLASIFICACIONES ---")
    print(f"Total Eficientes     : {cont_eficiente}")
    print(f"Total En observación : {cont_en_observacion}")
    print(f"Total Altos          : {cont_alto}")
    print(f"Total Críticos       : {cont_critico}")
    print("==================================================")