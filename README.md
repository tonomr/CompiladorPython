# Compilador en Python
## Proyecto Final
 
### Equipo: 
### * Magaña Reynoso, Antonio - 218744856
### * Contreras Díaz, Paola Stephania - 215483822

### Fecha: 9/Diciembre/2021
### Materia: Seminario de Solucion de Problemas de Traductores II
### Profesor: López Franco, Michel Emanuel
### Sección: D02
### Carrera: INCO
### CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS EN INGENIERÍAS - Universidad de Guadalajara


## Requisitos del Proyecto:
- Python 3
- PLY (Biblioteca ya incluida)
- Archivo de texto con el código del lenguaje PL/0 (Archivo ya incluído)

## Ojetivo:
Generar un compilador en Python.

## Metodología

### Analizador Léxico:
Usando la biblioteca PLY, tenemos que definir en nuestro analizador léxico nuestra lista de palabras reservadas y tokens, además de las variables y funciones de estás últimas.
Con la documentación de la biblioteca, nos indica que hay que definir la expresión regular de las funciones definidas, por último, imprimir la lista de tokens que nuestro programa detecto.
El programa reconoce los espacios, tabulaciones y saltos de línea, pero los ignora para concentrarse en las listas antes definidas.


### Analizador Sintactico:
Con nuestro analizador sintactico verificamos que el programa este bien escrito. Usando las reglas de la gramática del lenguaje.
Por ejemplo, si nos falta un punto y coma o un paréntesis, está parte se encarga de informarlo.

### Analizador Semántico:
Este tercer analizador de encargará de generar el árbol sintactico y la tabla de símbolos, si no hubo error al analizar el programa en las dos etapas anteriores.




## Resultados:


## Conclusión:
Este proyecto nos hizo aprender más acerca de cómo funcionan los compiladores, ya que tuvimos que hacer las primeras etapas de uno.
La primera parte se encarga de que todos los caracteres, palabras o tokens se encuentren en el lenguaje que nosotros definimos, si hay algún token no reconocido, aquí nos marcará error de que ese token es inválido.
Y ese es el trabajo del analizador léxico, detectar los tokens y verificar que sean parte del lenguaje.

La segunda parte vigila que el programa está bien escrito, sin errores como que nos falte algún cierre de paréntesis por ejemplo.
De esta forma, podremos avanzar a la siguiente parte de nuestro compilador.


Ahora bien, la tercera parte nos genera el árbol sintactico y es capaz de generar la tabla de estados y las reducciones gramaticales.
Así podremos apreciar como nuestro programa está siendo construido y compilado y nos permite avanzar a las siguientes fases.

