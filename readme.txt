1. La base de todo: Las Mascotas (Clase Abstracta e Herencia)

Para empezar, creé una plantilla general llamada Mascota. Esta es una clase abstracta (por eso importé ABC arriba). Lo que significa es que es un modelo tan general que no puede crear una Mascota, ya que nadie va por la calle paseando un animal que se llame Mascota, o bien paseas a un perro o a un gato ( se puede pasear a otros animales, pero en este caso solo ocupe estos dos).
Todas las mascotas en mi sistema tienen tres datos que son nombre, edad y peso. Además, definí una acción llamada hacer_ruido. Como cada animal hace un ruido diferente (rugir, ladrar, maullar, etc), la dejé vacía (pass) para que cada uno la defina después."
Los animales de verdad (Hijos)
Luego, creé las clases Perro y Gato. Las dos heredan de Mascota (por eso están entre paréntesis). Esto significando que automáticamente ya tienen nombre, edad y peso gracias a la línea super().__init__, así que no tengo que volver a escribir ese código.
Al Perro le agregué un dato extra que consta de la raza y  le programé su ladrido: ¡Guau, guau!.
Al Gato le agregué el tipo_pelo y su maullido es ¡Miau, miau!.

2. Los actores del negocio: Veterinario y Consulta

También yo necesito gente que trabaje y ordene el negocio, así que creé dos clases más:
Veterinario: Guarda el nombre del doctor y su especialidad y consta de una función simple para mostrar su tarjeta de presentación: Dr. Joaquín Díaz (Especialidad: Perros y Gatos).
Consulta: Esta clase une todo. Cuando alguien va al doctor, la consulta junta a la mascota, al veterinario y el motivo de la visita. Aquí dentro hay una función clave: calcular_precio(). La consulta cuesta mínimo 15.000 pesos, pero si la mascota pesa más de 15 kilos, se le cobran 5.000 pesos extra por el tamaño.

3. El motor del programa: El Menú Principal

Como último, preparé la función menu_principal(), que es lo que el usuario ve en la pantalla. Es un ciclo (while ejecutando:) que no para de repetirse, hasta que escojas/elijas la opción de salir(4).
Aquí creé dos listas vacías para ir guardando la información en la memoria: una para las mascotas registradas y otra para las consultas, aparte contraté al veterinario de turno, el Dr. Juan Gómez.
En el menú tiene 4 opciones:
Opción 1 (Registrar): Le pregunta al usuario si es perro o gato, pide sus datos y, según la respuesta, crea el objeto (Perro o Gato) y lo guarda en la lista de mascotas.
Opción 2 (Mostrar): Revisa la lista. Si está vacía, avisa que no hay nadie. Si hay mascotas, hace una lista numerada mostrando los datos de cada una de estas.
Opción 3 (Crear Consulta): Te muestra las mascotas que has registrado para que elijas una mediante su número. Al elegir, le pregunta el motivo de la visita, calcula el precio según el peso del animal y te imprime en pantalla una boleta/factura completa con el nombre del paciente, el doctor, el ruido que hace el animal (ya sea ladrar con guau guau o maullar con miau miau) y el total a pagar.
Opción 4 (Salir): Cambia la variable a False, rompe el ciclo y cierra el programa.

Y la última línea de abajo (if __name__ == "__main__":) le dice a Python: Si ejecutas este archivo, arranca el menú principal altiro.