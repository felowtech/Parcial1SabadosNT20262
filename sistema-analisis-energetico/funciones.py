def registrar_comercios():
    """
    Solicita y registra 10 comercios con información básica.
    Retorna una lista de diccionarios con los datos de cada comercio.
    """
    comercios = []
    cantidad_comercios = 10
    contador = 0
    
    while contador < cantidad_comercios:
        print(f"\n--- Comercio {contador + 1} de {cantidad_comercios} ---")
        
        nit = input("Ingrese NIT del comercio: ").strip()
        nombre = input("Ingrese nombre del comercio: ").strip()
        
        print("Tipos disponibles: Tienda, Restaurante, Peluquería")
        tipo = input("Ingrese tipo de comercio: ").strip()
        
        empleados_valido = False
        empleados = 0
        while not empleados_valido:
            try:
                empleados = int(input("Ingrese número de empleados: "))
                if empleados > 0:
                    empleados_valido = True
                else:
                    print("El número de empleados debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        meta_valido = False
        meta_semanal = 0.0
        while not meta_valido:
            try:
                meta_semanal = float(input("Ingrese meta semanal de consumo (kWh): "))
                if meta_semanal > 0:
                    meta_valido = True
                else:
                    print("La meta debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        comercio = {
            "nit": nit,
            "nombre": nombre,
            "tipo": tipo,
            "empleados": empleados,
            "meta_semanal": meta_semanal,
            "consumos": []
        }
        
        comercios.append(comercio)
        contador = contador + 1
    
    print(f"\n✓ Se registraron {contador} comercios exitosamente.")
    return comercios


def registrar_consumos(comercios):
    """
    Para cada comercio, solicita exactamente 4 consumos semanales.
    Valida que cada consumo sea un número float mayor a 0.
    Retorna la lista de comercios actualizada con los consumos.
    """
    indice_comercio = 0
    
    while indice_comercio < 10:
        comercio_actual = comercios[indice_comercio]
        print(f"\n--- Consumos para: {comercio_actual['nombre']} ---")
        
        consumos_registrados = 0
        while consumos_registrados < 4:
            semana_num = consumos_registrados + 1
            consumo_valido = False
            
            while not consumo_valido:
                try:
                    consumo = float(input(f"Ingrese consumo Semana {semana_num} (kWh): "))
                    if consumo > 0:
                        comercio_actual["consumos"].append(consumo)
                        consumo_valido = True
                    else:
                        print("El consumo debe ser mayor a 0.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            consumos_registrados = consumos_registrados + 1
        
        print(f"✓ Se registraron 4 consumos para {comercio_actual['nombre']}")
        indice_comercio = indice_comercio + 1
    
    print(f"\n✓ Se registraron consumos para todos los comercios.")
    return comercios


def calcular_promedio(consumos):
    """
    Calcula el promedio de 4 consumos semanales manualmente.
    Acumula la suma mediante un ciclo sin usar sum().
    Retorna el promedio como float.
    """
    suma_acumulada = 0.0
    indice = 0
    cantidad_consumos = 4
    
    while indice < cantidad_consumos:
        suma_acumulada = suma_acumulada + consumos[indice]
        indice = indice + 1
    
    promedio = suma_acumulada / cantidad_consumos
    return promedio


def calcular_variacion(consumos):
    """
    Calcula la variación porcentual entre la semana 1 (índice 0) y semana 4 (índice 3).
    Fórmula: ((semana4 - semana1) / semana1) * 100
    Retorna la variación como float.
    """
    semana1 = consumos[0]
    semana4 = consumos[3]
    
    variacion = ((semana4 - semana1) / semana1) * 100
    
    return variacion


def clasificar_consumo(promedio, meta, variacion):
    """
    Clasifica el consumo energético del comercio según tres criterios:
    - Eficiente: promedio <= meta Y variación <= 5%
    - En observación: promedio <= meta PERO variación > 5%
    - Alto: promedio > meta pero <= meta * 1.20
    - Crítico: promedio > meta * 1.20
    
    Retorna la clasificación como string.
    """
    if promedio <= meta:
        if variacion <= 5:
            clasificacion = "Eficiente"
        else:
            clasificacion = "En observación"
    else:
        limite_alto = meta * 1.20
        if promedio <= limite_alto:
            clasificacion = "Alto"
        else:
            clasificacion = "Crítico"
    
    return clasificacion


def generar_informe(comercios):
    """
    Genera un informe detallado de todos los comercios.
    Calcula promedio, variación y clasificación para cada uno.
    Muestra un resumen final con conteos por clasificación y el comercio
    con mayor consumo promedio.
    """
    print("\n" + "="*80)
    print("INFORME DE ANÁLISIS ENERGÉTICO - PEQUEÑOS COMERCIOS")
    print("="*80)
    
    contador_eficiente = 0
    contador_observacion = 0
    contador_alto = 0
    contador_critico = 0
    
    mayor_promedio = 0.0
    comercio_mayor_consumo = None
    indice = 0
    
    while indice < 10:
        comercio = comercios[indice]
        
        promedio = calcular_promedio(comercio["consumos"])
        variacion = calcular_variacion(comercio["consumos"])
        clasificacion = clasificar_consumo(promedio, comercio["meta_semanal"], variacion)
        
        print(f"\n{indice + 1}. {comercio['nombre']}")
        print(f"   NIT: {comercio['nit']}")
        print(f"   Tipo: {comercio['tipo']}")
        print(f"   Empleados: {comercio['empleados']}")
        print(f"   Meta semanal: {comercio['meta_semanal']} kWh")
        print(f"   Consumo promedio: {promedio:.2f} kWh")
        print(f"   Variación (Sem1 a Sem4): {variacion:.2f}%")
        print(f"   Clasificación: {clasificacion}")
        
        if clasificacion == "Eficiente":
            contador_eficiente = contador_eficiente + 1
        elif clasificacion == "En observación":
            contador_observacion = contador_observacion + 1
        elif clasificacion == "Alto":
            contador_alto = contador_alto + 1
        else:
            contador_critico = contador_critico + 1
        
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            comercio_mayor_consumo = comercio
        
        indice = indice + 1
    
    print("\n" + "="*80)
    print("RESUMEN FINAL")
    print("="*80)
    print(f"\nClasificación por eficiencia:")
    print(f"  • Eficiente: {contador_eficiente} comercios")
    print(f"  • En observación: {contador_observacion} comercios")
    print(f"  • Alto: {contador_alto} comercios")
    print(f"  • Crítico: {contador_critico} comercios")
    
    if comercio_mayor_consumo:
        print(f"\nComercio con MAYOR consumo promedio:")
        print(f"  • Nombre: {comercio_mayor_consumo['nombre']}")
        print(f"  • Promedio: {mayor_promedio:.2f} kWh")
        print(f"  • Meta: {comercio_mayor_consumo['meta_semanal']} kWh")
        porcentaje_sobre_meta = ((mayor_promedio - comercio_mayor_consumo['meta_semanal']) / comercio_mayor_consumo['meta_semanal']) * 100
        print(f"  • Exceso sobre meta: {porcentaje_sobre_meta:.2f}%")
    
    print("\n" + "="*80)
