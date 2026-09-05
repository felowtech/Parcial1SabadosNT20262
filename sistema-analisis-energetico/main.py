from funciones import registrar_comercios, registrar_consumos, calcular_promedio, calcular_variacion, clasificar_consumo, generar_informe


def main():
    """
    Función principal que orquesta el flujo del sistema de análisis energético.
    Ejecuta secuencialmente las 6 funciones obligatorias.
    """
    print("\n" + "="*80)
    print("BIENVENIDO AL SISTEMA DE ANÁLISIS ENERGÉTICO")
    print("Para Pequeños Comercios de Barrio")
    print("="*80)
    
    print("\n[PASO 1] Registrando 10 comercios...")
    comercios = registrar_comercios()
    
    print("\n[PASO 2] Registrando 4 consumos semanales por comercio...")
    comercios = registrar_consumos(comercios)
    
    print("\n[PASO 3] Calculando indicadores y generando informe...")
    generar_informe(comercios)
    
    print("\n" + "="*80)
    print("PROCESO COMPLETADO EXITOSAMENTE")
    print("="*80 + "\n")


if __name__ == '__main__':
    main()
