# 🎮 Conecta 4

¡Bienvenido a Conecta 4! 🎉 Este es un juego clásico de Conecta 4 implementado en Python usando Pygame para la interfaz gráfica y Tkinter para los controles adicionales. Dos jugadores pueden jugar turnándose para colocar fichas en el tablero. ¡Que gane el mejor! 🏆

## 📋 Características

- Tablero de 7x6 (7 columnas y 6 filas).
- Fichas Rojas y Amarillas. La primera partida la comienza siempre el jugador Rojo (alternando en cada partida).
- El juego detecta automáticamente victorias y empates.
- Guarda el número de partidas ganadas por cada jugador mientras la aplicación está en ejecución.
- Botones para reiniciar la partida y para resetear el contador de victorias.
- Interfaz gráfica con Pygame y controles adicionales con Tkinter.

## 🚀 Cómo jugar

1. **Iniciar el juego**: Al ejecutar el script, se abrirá una ventana con el tablero de Conecta 4.
2. **Colocar una ficha**: Haz clic en la columna donde deseas colocar tu ficha. La ficha caerá hasta la posición más baja disponible.
3. **Reiniciar partida**: Presiona `R` en el teclado o usa el botón "Reiniciar Partida" en la interfaz de Tkinter.
4. **Resetear contadores**: Presiona `C` en el teclado o usa el botón "Resetear Contadores" en la interfaz de Tkinter para reiniciar los contadores de victorias.

## 📦 Instalación

1. Asegúrate de tener Python y Pygame instalados. Puedes instalar Pygame con el siguiente comando:
    ```bash
    pip install pygame
    ```
2. Clona este repositorio:
    ```bash
    git clone https://github.com/DanielJaeger90/conecta4.git
    cd conecta4
    ```
3. Ejecuta el script principal:
    ```bash
    python conecta4.py
    ```

## 🖥️ Interfaz de usuario

El juego se presenta en una ventana de Pygame con el tablero de juego, y una pequeña ventana de Tkinter con botones para reiniciar la partida y resetear los contadores de victorias.

### Controles

- **Clic izquierdo**: Coloca una ficha en la columna seleccionada.
- **Tecla R**: Reinicia la partida actual.
- **Tecla C**: Resetea los contadores de victorias y reinicia la partida.

## 🏅 Ejemplos de uso

- **Inicio del juego**: El juego comienza con el tablero vacío y el jugador Rojo en primer turno.
    ![Inicio del juego](./screenshots/inicio.png)
- **Jugador Rojo gana**: Si el jugador Rojo consigue conectar cuatro fichas en línea.
    ![Jugador Rojo gana](./screenshots/rojo_gana.png)
- **Empate**: Si el tablero se llena y no hay ganador.
    ![Empate](./screenshots/empate.png)

## 🎉 ¡Diviértete!

Esperamos que disfrutes jugando a Conecta 4 tanto como nosotros disfrutamos desarrollándolo. Si tienes alguna sugerencia o encuentras algún problema, no dudes en abrir un issue en GitHub. ¡Que gane el mejor! 🤩

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. ¡Siéntete libre de usar y modificar el código!

---

Desarrollado con ❤️ por Daniel Jaeger
