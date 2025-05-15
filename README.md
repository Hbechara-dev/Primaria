Aplicación de Cifrado y Descifrado con Tkinter
He desarrollado una aplicación completa de escritorio utilizando Tkinter que permite cifrar y descifrar números enteros de 6 dígitos según los requisitos especificados. La aplicación cuenta con tres ventanas principales y la funcionalidad de cifrado y descifrado solicitada.
Características principales
1. Ventana Principal

Muestra el título de la aplicación
Presenta información del autor (estudiante)
Incluye dos botones para navegar a las ventanas de cifrado y descifrado

2. Ventana de Cifrado

Permite al usuario ingresar un número entero de 6 dígitos
Implementa el algoritmo de cifrado:

Suma 7 a cada dígito y toma el residuo al dividir entre 10
Intercambia las posiciones (1º con 3º, 2º con 4º, 5º con 6º)


Muestra el número cifrado resultante

3. Ventana de Descifrado

Permite ingresar un número cifrado
Implementa el algoritmo de descifrado (proceso inverso)
Muestra el número original descifrado

Funcionamiento del algoritmo
Cifrado:

Se suma 7 a cada dígito y se calcula el residuo al dividir entre 10
Se intercambian las posiciones de los dígitos según lo especificado

Descifrado:

Se revierten los intercambios de posiciones
Se suma 3 a cada dígito y se calcula el residuo al dividir entre 10 (equivalente a restar 7 y ajustar para valores negativos)

Uso de la aplicación

Ejecuta el script Python
En la ventana principal, selecciona "Cifrar Número" o "Descifrar Número" según lo que necesites
Ingresa el número correspondiente (debe ser de 6 dígitos)
Haz clic en "Cifrar" o "Descifrar" según corresponda
Verás el resultado en la parte inferior de la ventana
