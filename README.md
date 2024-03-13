# Estructuras-de-datos-y-funciones-I

Pequeñas aplicaciones para aprender Python, con estructuras de datos y funciones

## Requisitos

Enumera los requisitos necesarios para ejecutar el proyecto, como versiones de software, bibliotecas, etc.

argumentos.py ==> Pequeña aplicación a modo de presentación de las personas.
Todo lo que se escriba después del nombre del script, corresponderá a los
argumentos siguientes.

efemerides.py ==> se realiza esta pequeña app utilizando un diccionario:
# definimos el diccionario
efemerides = {

 '1 de Enero': 'Año Nuevo',
 '27 de Febrero': 'Terremoto en Chile',
 '8 de Marzo': 'Día de la Mujer',
 '21 de Mayo': 'Glorias Navales',
 '18 de Septiembre': 'Fiestas Patrias',
 '19 de Septiembre': 'Glorias del Ejercito',
 '25 de Diciembre': 'Navidad'
 
 }

conversiones.py ==> una estructura de datos apropiada que permita
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar
mediante sys.argv en el siguiente orden: Sol, Peso Argentino, Dólar Americano.
Usando el siguiente script arrojará la información: python conversiones.py 0.0046 0.093 0.0013 10000 (import sys)


word_count.py es una app para contar las palabras y los carácteres del archivo entregado para este ejericicio, el lorem_ipsum.txt

## Instalación

Proporciona instrucciones paso a paso sobre cómo instalar y configurar el proyecto. 

```bash
git clone (nombre del proyecto que deseamos clonar)
cd tu_proyecto
pip install tabulate #para mostrar la información de conversiones en tablas
pip install 