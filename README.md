# Contenido

## Objetivos

Los objetivos del contenido de este repositorio son específicamente
pedagógicos y pueden ser concretados en los siguientes puntos:

* Servir en un curso básico de Criptografía como primer ejemplo de
  cifra en la que es posible poner en práctica de forma fácil todas
  las facetas del oficio: formateo del texto, cifrado, descifrado,
  cálculo de la clave de descifrado a partir de la descifrado y ataque
  exitoso en este caso.

* Exhibir un estilo de programación que sea modelo del que se pide en
  las prácticas.
  
* Mostrar las particularidades de la programación orientada a objetos
  en `Python` y muy especialmente algunos mecanismos de la herencia en
  dicho lenguaje.

## Estructura

La estructura del proyecto es la siguiente:
  
* Un fichero auxiliar `affine_alphabet.py` con: el alfabeto a usar,
  distintos parámetros correspondiéndole y diccionarios varios
  incluido el de frecuencias de las letras en monocase del español.
  
* El sistema de clases del proyecto codificado en el fichero
  `affine_classes.py` y que importa a `affine_alphabet.py`

* Un fichero principial `affine_cryptosystem.py` que codifica el uso
  de los auxiliares, importando `affine_classes.py`, y que sirve para
  llevar a cabo desde la línea de órdenes las posibles operaciones
  sobre texto relacionadas con la cifra según se explica en la
  siguiente sección.

* El código completo en formato `.ipynb` de todo lo dicho
  anteriormente para quien prefiera tener una visión global del
  proyecto en un cuaderno de Jupyter, con la funcionalidad que ello
  ofrece.

* El fichero `encipheringText.txt` que contiene el texto cifrado vía
  determinada clave afín y que corresponde al texto plano contenido en
  `plainText.txt`. Descubrir esa clave puede ser parte de un
  ejercicio.
  
El proyecto todo está codificado según `Python 3`.
  
## Ejemplos de Uso
	
* Cifrar el texto plano del fichero `plainText.txt` mediante la clave
  de decimación 21 y desplazamiento 13:

		python affine_cryptosystem.py plainText.txt 21 13 0

* Descifrar el texto cifrado del fichero `encipheringText.txt` a
  partir de la clave derivada de la de decimación 21 y desplazamiento
  13:
	
		python affine_cryptosystem.py encipheringText.txt 21 13 1

* Ataque para encontrar la clave de cifrado mediante la prueba
  Chi-cuadrado cuando `len(sys.argv) != 5`:

		python affine_cryptosystem.py encipheringText.txt 21 13 

		python affine_cryptosystem.py encipheringText.txt 21

  y la  mejor opción es: 

		python affine_cryptosystem.py encipheringText.txt


## Referencias

1. Koblitz, N. A Course in Number Theory and
Criptography. Springer-Verlag, 1994.
      
1. Kumanduri, R. and Romero, C. Number Theory with Computer
Applications. Prentice-Hall, 1998.
      
1. Menezes, A.J., van Oorschot, P.C., and Vanstone, S.A. Handbook of
Applied Cryptography. CRC Press, 1997.
