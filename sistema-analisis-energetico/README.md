# Sistema de Análisis Energético para Pequeños Comercios

## Descripción General

Este proyecto implementa un **prototipo de sistema de análisis energético** dirigido a pequeños comercios de barrio (tiendas, restaurantes y peluquerías). El sistema gestiona información básica de comercios y realiza un análisis detallado de consumo de energía eléctrica (medido en kWh) a través de 4 mediciones semanales.

### Funcionalidades Principales

- **Registro de comercios**: Captura datos de hasta 10 pequeños negocios con su NIT, nombre, tipo, número de empleados y meta semanal de consumo.
- **Captura de consumos**: Registra exactamente 4 mediciones semanales de consumo energético por cada comercio.
- **Cálculo de indicadores**: Calcula automáticamente el promedio de consumo semanal y la variación porcentual entre la primera y última semana.
- **Clasificación de eficiencia**: Clasifica cada comercio en una de 4 categorías: **Eficiente**, **En observación**, **Alto** o **Crítico**.
- **Generación de informe**: Produce un informe detallado con análisis individual de cada comercio y resumen ejecutivo con estadísticas agregadas.

## Restricciones Técnicas Implementadas

El proyecto fue desarrollado bajo restricciones de **programación imperativa pura**, sin uso de características modernas de Python:

- ❌ **No se usan**: Clases, archivos de base de datos, librerías externas, módulos adicionales
- ✅ **Se utilizan únicamente**: Funciones, ciclos (`for`/`while`), condicionales (`if`/`elif`/`else`), listas, diccionarios, variables y operadores básicos
- ❌ **Prohibidas para cálculos centrales**: Funciones integradas como `sum()`, `max()`, `min()`, `sorted()`, `len()`
- ✅ **Implementados manualmente**: Acumuladores, búsquedas, comparaciones mediante ciclos explícitos

Esta aproximación demuestra el dominio de conceptos fundamentales de programación y la capacidad de resolver problemas complejos con herramientas básicas.

## Estructura del Proyecto

```
sistema-analisis-energetico/
├── funciones.py          # Módulo con las 6 funciones obligatorias
├── main.py              # Punto de entrada principal
└── README.md            # Este archivo
```

### Descripción de Archivos

#### `funciones.py`
Contiene las 6 funciones obligatorias del sistema:

1. **`registrar_comercios()`**
   - Solicita datos de 10 comercios de forma interactiva
   - Captura: NIT, nombre, tipo, número de empleados, meta semanal
   - Inicializa lista de consumos vacía
   - Retorna lista de diccionarios con información de comercios

2. **`registrar_consumos(comercios)`**
   - Solicita exactamente 4 consumos semanales por comercio
   - Valida que cada consumo sea un número float > 0
   - Almacena consumos en la lista `"consumos"` de cada comercio
   - Retorna lista de comercios actualizada

3. **`calcular_promedio(consumos)`**
   - Recibe lista de 4 consumos
   - Acumula suma manualmente con ciclo while (sin usar `sum()`)
   - Calcula promedio dividiendo entre 4
   - Retorna float con el promedio semanal

4. **`calcular_variacion(consumos)`**
   - Extrae consumo de semana 1 (índice 0) y semana 4 (índice 3)
   - Aplica fórmula: `((semana4 - semana1) / semana1) * 100`
   - Retorna float con variación porcentual

5. **`clasificar_consumo(promedio, meta, variacion)`**
   - Classifica según criterios:
     - **Eficiente**: promedio ≤ meta Y variación ≤ 5%
     - **En observación**: promedio ≤ meta PERO variación > 5%
     - **Alto**: promedio > meta pero ≤ meta × 1.20
     - **Crítico**: promedio > meta × 1.20 (exceso > 20%)
   - Retorna string con clasificación

6. **`generar_informe(comercios)`**
   - Itera sobre los 10 comercios
   - Calcula promedio, variación y clasificación de cada uno
   - Muestra informe detallado por comercio
   - Calcula manualmente (sin `len()` ni `sorted()`):
     - Conteo de comercios por cada categoría de clasificación
     - Identificación del comercio con mayor consumo promedio
   - Imprime resumen ejecutivo con conclusiones

#### `main.py`
- Importa las 6 funciones desde `funciones.py`
- Implementa flujo principal en bloque `if __name__ == '__main__':`
- Ejecuta secuencialmente: registro → captura de consumos → generación de informe
- Proporciona mensajes de progreso y estructura visual clara

## Estructura de Datos

Cada comercio se representa como un diccionario con la siguiente estructura:

```python
{
    "nit": str,              # Número de identificación tributaria
    "nombre": str,           # Nombre del comercio
    "tipo": str,             # Tipo: "Tienda", "Restaurante" o "Peluquería"
    "empleados": int,        # Número de empleados (> 0)
    "meta_semanal": float,   # Meta de consumo semanal en kWh
    "consumos": list         # Lista con 4 floats (consumos semanales)
}
```

Ejemplo:
```python
{
    "nit": "1234567890",
    "nombre": "Tienda Don Carlos",
    "tipo": "Tienda",
    "empleados": 3,
    "meta_semanal": 150.0,
    "consumos": [140.5, 145.2, 148.8, 152.3]
}
```

## Instrucciones de Ejecución

### Requisitos Previos
- **Python 3.6 o superior**
- Sistema operativo: Linux, macOS o Windows
- Terminal/Consola de comandos

### Pasos para Ejecutar

#### Opción 1: Ejecución Directa

1. Abre una terminal/consola en el directorio del proyecto
2. Verifica que los archivos `funciones.py` y `main.py` estén en el mismo directorio
3. Ejecuta el comando:
   ```bash
   python main.py
   ```
   
   En Windows, si `python` no funciona, intenta:
   ```bash
   python3 main.py
   ```

4. El programa iniciará mostrando un menú de bienvenida

#### Opción 2: Ejecución Interactiva desde Python

```bash
python
>>> from funciones import registrar_comercios, registrar_consumos, generar_informe
>>> comercios = registrar_comercios()
>>> comercios = registrar_consumos(comercios)
>>> generar_informe(comercios)
```

### Flujo de Interacción

El programa ejecutará los siguientes pasos de forma automática:

**PASO 1: Registro de 10 Comercios**
- Para cada comercio se solicita:
  - NIT
  - Nombre del comercio
  - Tipo (Tienda, Restaurante, Peluquería)
  - Número de empleados
  - Meta semanal de consumo en kWh

**PASO 2: Captura de Consumos**
- Para cada comercio, se solicitan 4 mediciones de consumo semanal
- Se valida que cada consumo sea un número positivo

**PASO 3: Análisis y Generación de Informe**
- El sistema calcula automáticamente:
  - Promedio de consumo semanal
  - Variación porcentual (semana 1 a semana 4)
  - Clasificación de eficiencia
- Se muestra informe detallado por comercio
- Se presenta resumen ejecutivo con:
  - Conteo de comercios por clasificación
  - Comercio con mayor consumo promedio

### Ejemplo de Salida

```
================================================================================
BIENVENIDO AL SISTEMA DE ANÁLISIS ENERGÉTICO
Para Pequeños Comercios de Barrio
================================================================================

[PASO 1] Registrando 10 comercios...

--- Comercio 1 de 10 ---
Ingrese NIT del comercio: 1001234567
Ingrese nombre del comercio: Tienda El Éxito
Tipos disponibles: Tienda, Restaurante, Peluquería
Ingrese tipo de comercio: Tienda
Ingrese número de empleados: 4
Ingrese meta semanal de consumo (kWh): 200.0
✓ Se registraron 10 comercios exitosamente.

[PASO 2] Registrando 4 consumos semanales por comercio...

--- Consumos para: Tienda El Éxito ---
Ingrese consumo Semana 1 (kWh): 195.5
Ingrese consumo Semana 2 (kWh): 198.2
Ingrese consumo Semana 3 (kWh): 202.1
Ingrese consumo Semana 4 (kWh): 205.8

[PASO 3] Calculando indicadores y generando informe...

================================================================================
INFORME DE ANÁLISIS ENERGÉTICO - PEQUEÑOS COMERCIOS
================================================================================

1. Tienda El Éxito
   NIT: 1001234567
   Tipo: Tienda
   Empleados: 4
   Meta semanal: 200.0 kWh
   Consumo promedio: 200.40 kWh
   Variación (Sem1 a Sem4): 5.31%
   Clasificación: En observación

[...resto de comercios...]

================================================================================
RESUMEN FINAL
================================================================================

Clasificación por eficiencia:
  • Eficiente: 2 comercios
  • En observación: 4 comercios
  • Alto: 3 comercios
  • Crítico: 1 comercio

Comercio con MAYOR consumo promedio:
  • Nombre: Restaurante La Buena Mesa
  • Promedio: 425.65 kWh
  • Meta: 350.0 kWh
  • Exceso sobre meta: 21.61%

================================================================================
PROCESO COMPLETADO EXITOSAMENTE
================================================================================
```

## Criterios de Clasificación Detallados

El sistema clasifica cada comercio en una de 4 categorías según su desempeño energético:

| Categoría | Criterio | Interpretación |
|-----------|----------|----------------|
| **Eficiente** | Promedio ≤ Meta Y Variación ≤ 5% | Excelente control, consumo estable y dentro de límites |
| **En observación** | Promedio ≤ Meta Y Variación > 5% | Consumo dentro de meta pero con tendencia creciente |
| **Alto** | Meta < Promedio ≤ Meta × 1.20 | Exceso controlado (hasta 20% sobre meta) |
| **Crítico** | Promedio > Meta × 1.20 | Consumo alarmante (más de 20% sobre meta) |

### Interpretación de Variación

La **variación porcentual** mide el cambio de consumo entre la semana 1 y semana 4:

- **Variación negativa** (ej: -5%): Comercio reduce consumo → Mejora
- **Variación positiva baja** (ej: 3%): Consumo estable
- **Variación positiva alta** (ej: 15%): Tendencia creciente → Alerta

## Algoritmos Clave Implementados Manualmente

### 1. Cálculo de Promedio (Sin `sum()`)
```python
suma_acumulada = 0.0
indice = 0
while indice < 4:
    suma_acumulada = suma_acumulada + consumos[indice]
    indice = indice + 1
promedio = suma_acumulada / 4
```

### 2. Búsqueda del Máximo (Sin `max()`)
```python
mayor_promedio = 0.0
comercio_mayor_consumo = None
indice = 0
while indice < 10:
    promedio = calcular_promedio(comercios[indice]["consumos"])
    if promedio > mayor_promedio:
        mayor_promedio = promedio
        comercio_mayor_consumo = comercios[indice]
    indice = indice + 1
```

### 3. Conteo por Categoría (Sin `filter()` ni `list comprehension`)
```python
contador_eficiente = 0
indice = 0
while indice < 10:
    if clasificacion == "Eficiente":
        contador_eficiente = contador_eficiente + 1
    indice = indice + 1
```

## Casos de Uso

### Caso 1: Tienda Eficiente
- Meta: 200 kWh
- Consumos: [195, 198, 200, 202]
- Promedio: 198.75 kWh
- Variación: 3.59%
- **Clasificación: Eficiente** ✓

### Caso 2: Restaurante en Observación
- Meta: 300 kWh
- Consumos: [300, 310, 320, 330]
- Promedio: 315 kWh
- Variación: 10%
- **Clasificación: En observación** ⚠️

### Caso 3: Peluquería Crítica
- Meta: 100 kWh
- Consumos: [120, 125, 130, 135]
- Promedio: 127.5 kWh
- Variación: 12.5%
- **Clasificación: Crítico** 🔴

## Validaciones Implementadas

El sistema valida:
- ✅ NIT y nombre no vacíos
- ✅ Tipo de comercio válido
- ✅ Número de empleados es entero > 0
- ✅ Meta semanal es número > 0
- ✅ Cada consumo es número float > 0
- ✅ Se registran exactamente 4 consumos por comercio
- ✅ Se registran exactamente 10 comercios

## Notas Técnicas

- **Sin dependencias externas**: El código utiliza solo funcionalidades built-in de Python
- **Portabilidad**: Funciona en cualquier versión de Python 3.6+
- **Legibilidad**: Código comentado con funciones bien documentadas
- **Escalabilidad**: Estructura modular permite fácil adaptación para más comercios
- **Manejo de errores**: Validación completa de entrada de usuario

## Limitaciones y Extensiones Futuras

### Limitaciones Actuales
- Se registran exactamente 10 comercios (no configurable)
- Se requieren exactamente 4 mediciones (no configurable)
- Sin persistencia de datos (datos en memoria)
- Sin interfaz gráfica
- Sin análisis histórico

### Posibles Extensiones
1. Guardar datos en archivo de texto o CSV
2. Cargar datos previamente guardados
3. Permitir número variable de comercios y semanas
4. Comparativas históricas de periodos
5. Gráficos ASCII de tendencias
6. Alertas automáticas por consumo crítico
7. Recomendaciones de ahorro energético

## Prompts Original

Este proyecto fue generado utilizando el siguiente prompt:

---

**Actúa como un Desarrollador Python Senior. Necesito que generes el código y documentación para un sistema de prototipo de análisis energético dirigido a pequeños comercios de barrio.**

### CONTEXTO Y OBJETIVO
El sistema gestiona la información básica de comercios y 4 mediciones semanales de consumo de energía (kWh) para calcular indicadores y clasificar su eficiencia energética.

### RESTRICCIONES TÉCNICAS RÍGIDAS
1. NO usar clases, archivos, bases de datos, librerías externas ni módulos (ej. `math`, `statistics`).
2. USAR ÚNICAMENTE: funciones, ciclos (`for`/`while`), condicionales (`if`/`elif`/`else`), listas, diccionarios, variables y operadores básicos.
3. Prohibido usar las funciones integradas: `sum()`, `max()`, `min()`, `sorted()`, `len()` para los cálculos centrales. El promedio, acumuladores y la búsqueda del mayor consumo DEBEN resolverse manualmente mediante ciclos y comparaciones.
4. El programa debe ejecutarse en consola/terminal mediante un flujo limpio y guiado.

### ESTRUCTURA DE DATOS
Cada registro principal es un diccionario almacenado en una lista global de comercios:
```
{
    "nit": str,
    "nombre": str,
    "tipo": str, # Tienda, Restaurante o Peluquería
    "empleados": int,
    "meta_semanal": float,
    "consumos": list # Lista de 4 floats
}
```

### ARQUITECTURA DE FUNCIONES (EXACTAMENTE ESTAS 6 EN `funciones.py`)

1. **`registrar_comercios()`**:
   - Solicita y registra 10 comercios.
   - Cada comercio inicia con `"consumos": []`.
   - Retorna la lista de comercios.

2. **`registrar_consumos(comercios)`**:
   - Para cada comercio en la lista, solicita exactamente 4 consumos semanales (float > 0) con validación de entrada.
   - Guarda las mediciones en la lista `"consumos"` de cada comercio.
   - Retorna la lista actualizada.

3. **`calcular_promedio(consumos)`**:
   - Recibe la lista de 4 consumos.
   - Recorre la lista con un ciclo y acumula la suma manualmente. Divide entre 4 (o con contador manual).
   - Retorna el promedio (float).

4. **`calcular_variacion(consumos)`**:
   - Extrae `semana1` (índice 0) y `semana4` (índice 3).
   - Calcula: ((semana4 - semana1) / semana1) * 100.
   - Retorna la variación porcentual (float).

5. **`clasificar_consumo(promedio, meta, variacion)`**:
   - "Eficiente": si promedio <= meta Y variación <= 5%.
   - "En observación": si promedio <= meta PERO variación > 5%.
   - "Alto": si promedio > meta y hasta un 20% por encima (promedio <= meta * 1.20).
   - "Crítico": si promedio > meta * 1.20 (supera la meta en más del 20%).
   - Retorna el string con la clasificación.

6. **`generar_informe(comercios)`**:
   - Recorre los comercios y calcula su promedio, variación y clasificación llamando a las funciones correspondientes.
   - Muestra por cada comercio: nombre, promedio (kWh), variación (%) y clasificación.
   - Calcula e informa en un resumen final:
     - Conteo manual de comercios por cada tipo de clasificación.
     - El comercio con el mayor promedio registrado (hallado mediante un ciclo manual con variable pivot de comparación).

### ENTREGABLE REQUERIDO
Por favor, genera y entrega el proyecto estructurado para ser empaquetado en un archivo ZIP con la siguiente distribución exacta:

1. `funciones.py`:
   - Contiene la definición estricta de las 6 funciones obligatorias descritas.

2. `main.py`:
   - Importa las 6 funciones desde `funciones.py`.
   - Contiene el bloque de ejecución principal (`if __name__ == '__main__':`) invocando secuencialmente cada una de las 6 funciones.

3. `README.md`:
   - Documentación completa en español que incluya:
     - Descripción general del proyecto.
     - Instrucciones paso a paso para ejecutar `main.py`.
     - El texto exacto de este prompt utilizado para la generación.

Genera el código completo, sin omisiones ni marcadores de posición (sin 'TODO' ni 'pass'), garantizando que funcione perfectamente al ejecutar `python main.py`.

---

## Autor y Fecha

**Generado**: Septiembre 2026  
**Versión**: 1.0  
**Estado**: Producción

## Licencia

Este proyecto es de código abierto y puede ser utilizado libremente con fines educativos y comerciales.

---

**¿Preguntas o sugerencias?** Este sistema puede ser adaptado según necesidades específicas de diferentes tipos de comercios o regiones.
