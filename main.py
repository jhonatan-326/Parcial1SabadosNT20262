# main.py
import funciones

def main():
    print("=== SISTEMA DE GESTIÓN Y CLASIFICACIÓN DE COMERCIOS ===")
    
    # Lectura del número de comercios
    while True:
        try:
            numero_comercios = int(input("Ingrese el número de comercios a registrar: "))
            if numero_comercios > 0:
                break
            else:
                print("El número de comercios debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            
    # 1. Registrar comercios
    lista_comercios = funciones.registrar_comercios(numero_comercios)
    
    # 2. Registrar consumos
    lista_comercios = funciones.registrar_consumo(lista_comercios)
    
    # 3. Calcular promedios
    lista_comercios = funciones.calcular_promedio(lista_comercios)
    
    # 4. Calcular variaciones
    lista_comercios = funciones.calcular_variacion(lista_comercios)
    
    # 5. Clasificar cada comercio
    for comercio in lista_comercios:
        comercio["clasificacion"] = funciones.clasificar_consumo(
            comercio["promedio"],
            comercio["meta"],
            comercio["variacion"]
        )
        
    # 6. Generar informe e imprimir resultados
    funciones.generar_informe(lista_comercios)

if __name__ == "__main__":
    main()