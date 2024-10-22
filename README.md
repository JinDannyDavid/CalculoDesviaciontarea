# Programa Calcular Promedio y Desviacion

Este programa calcula la media y la desviación estándar de una lista de números ingresados por el usuario. Primero, solicita al usuario que ingrese la cantidad de números que desea ingresar, luego pide cada número uno por uno, y finalmente realiza los cálculos y muestra los resultados.
## Requisitos
El programa consta de dos archivos principales:
- ejecutador.py - La interfaz de usuario y la lógica principal del programa.
- calculos.py - La clase Calculadora que contiene los métodos para calcular la media y la desviación estándar.
- test_calculos - Aqui se realizara todos los testeos del programa a fin de corregir todos los posibles errores.

## Estructura del proyecto
Calculodesviacion
- ├── main.py
- scr-> logica->  calculos.py
- tests -> test_calculos.py

## Clases y Métodos
### Clase Calculadora

"__init__(self, elementos)."

Constructor que inicializa la lista de elementos.

"media(self)."

Calcula la media de los elementos en la lista. Lanza una excepción NoSePuedeCalcular si la lista está vacía o contiene elementos no numéricos.

"desviacion_estandar(self)"

Calcula la desviación estándar de los elementos en la lista. Lanza una excepción NoSePuedeCalcular si la lista está vacía o contiene elementos no numéricos.

### Clase NoSePuedeCalcular

Excepción personalizada para manejar errores de cálculo cuando la lista está vacía.

## Funcionamiento del Programa

### Inicio del Programa:
  - El programa comienza ejecutando la función Ejecutador().

### Ingreso del Número de Elementos:
  - El programa solicita al usuario que ingrese la cantidad de números que desea ingresar.
  
  - Si el número ingresado es menor o igual a cero, se genera un ValueError.

### Ingreso de Números:
  - El programa solicita al usuario que ingrese cada número uno por uno.
  
  - Los números ingresados se almacenan en una lista llamada numeros.

### Cálculo de la Media y la Desviación Estándar:
  - Se crea una instancia de la clase Calculadora con la lista de números ingresados.
  
  - Se llaman los métodos media() y desviacion_estandar() para calcular los valores correspondientes.

### Manejo de Excepciones:
  - Si se genera un ValueError, se muestra un mensaje de error correspondiente.
  
  - Si se genera un NoSePuedeCalcular, se muestra un mensaje de error correspondiente.
  
  - Si se genera un TypeError, se muestra un mensaje de error correspondiente.

### Mostrar Resultados:
  - El programa imprime la media y la desviación estándar calculadas.
