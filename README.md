## Setup

(Notera: Vi kommer skippa virutal environment för att smida på rättning även om det borde användas!)

Efter att ha forkat och sedan klonat repositoriet:
- Kör kommandot pip install pygame för att få hem pygame
- Kör koden i main.py för att starta programmet!

# Hur man spelar

"""
    In this game(minesweeper) you can reveal cells until you have revealed either all non bomb cells or you reveal too many bombs and lose
    You can only reveal 3 bombs before the 4th becomes the end of you!
    G00D LÜCK!

    !--------------HOW TO PLAY-----------------!
    !-PRESS THE ESCAPE BUTTON TO QUIT THE GAME-!
    !-PRESS ENTER TO RESTART THE GAME----------!
    !-GAME RESETS AUTOMATICALLY IF WIN/LOSE----!
    !--------------HOW TO PLAY-----------------!
"""


## Hur funkar spelet?
Kort och gott: Spelet består av en 16x16 matris
En cell (ruta) kan bestå av en bomb, klickar man en bomb förlorar man
Klickar man en cell och det INTE är en bomb får man en siffra som berättar hur många bomber som ligger brevid, målet är att ta alla rutor som inte är bomber

En cell kan maximalt ha 8 rutor brevid sig

Exempel:
Jag klickar på en cell som har 8 grannar, det är inte en bomb, jag får siffran 4
Detta innebär att det finns 4 bomber uppdelat mellan några av de 8 cellerna, det är upp till mig att identifiera vilka som är bomber och vilka som inte är det

Scenario 1: Klickar på en ruta och får bomb, jag fölorar
Scenario 2: Klickar på en ruta brevid men får INTE en bomb, jag kör vidare!

När alla rutor har klickats på som inte innehåller en bomb vinner man!



