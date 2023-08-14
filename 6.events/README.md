# Infografia_3_carrasco

El archivo que debe ejecutarse es **tank_game.py**

## Dinámica del juego

- Para controlar al Tanque Uno (el cual se encuentra en la parte inferior izquierda), se debe utilizar las siguientes teclas:

* A: Girar a la izquierda
* D: Girar a la derecha
* W: Avanzar hacia adelante
* S: Retroceder hacia atrás
* E: Disparar balas normales
* Q: Disparar una bala grande (causa más daño, pero solo se la puede usar 1 vez)

- Por otra parte, para controlar al Tanque Dos (el cual se encuentra en la parte superior derecha), se debe utilizar las siguientes teclas:

* J: Girar a la izquierda
* L: Girar a la derecha
* I: Avanzar hacia adelante
* K: Retroceder hacia atrás
* U: Disparar balas normales
* O: Disparar una bala grande (causa más daño, pero solo se la puede usar 1 vez)

- El juego se encuentra rodeado por una barrera, la cual impedirá que un jugador se aleje demasiado del limite de la pantalla.

- Se generan de forma aleatoria escondites de color rojo, en los cuales un jugador puede esconderse dentro o detrás de él para evitar recibir daño del tanque enemido (en caso de que el jugador se oculte dentro de él, no tendrá la capacidad de disparar, siempre y cuando su centro de encuentre dentro del escondite)

- El primer jugador que logre destruir al otro ganará (cuando uno de los jugadores caiga, se revelará por un mensaje quien fue el ganador. Luego de ello, el jugador deberá de **cerrar la pestaña del juego**. Si desea volver a jugar, tendrá que volver a ejecutar el archivo **tank_game.py**)

- Cabe mencionar que cada tanque tiene 5 puntos de vida. Además de que únicamente se podrá **causar daño a otro tanque**, si es que una bala normal o la bala grande impacta con el **escudo**, el cual es una esfera de color diferente que se encuentra rodeando al centro del tanque (el centro es el punto de color rojo)
