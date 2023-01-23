Je kent vast het 'like' van Facebook en andere social media. We willen de text creëren die in je scherm komt als je 
likes hebt ontvangen van al je vrienden, collega's en bots. Implementeer een functie die een list aanneemt die de namen
van mensen bevat die jouw gave nieuwe katten foto leuk vinden. Begin met een functie die maximaal twee namen aanneemt 
en de volgende output terugstuurt.

```
[]                                --> "no one likes this"
["Niels"]                         --> "Niels likes this"
["Sven", "Yur"]                   --> "Sven en Yur like this"
```

Één iemand uit jouw group kopieert `opdracht_1.py` naar de github folder van jouw team in `group_x` en commit + pusht 
de file. De file zou nu voor heel jouw team zichtbaar moeten zijn.

Teamgenoot 2 breidt de code nu uit naar 3 personen die de volgende output heeft:

```
[]                                --> "no one likes this"
["Niels"]                         --> "Niels likes this"
["Sven", "Yur"]                   --> "Sven and Yur like this"
["Sebas", "Wies", "Kirsty"]       --> "Sebas, Wies and Kirsty like this"
```

Teamgenoot 2 commit en pusht de nieuwe code nu naar de nieuwe branch. Teamgenoot 3 bouwt verder op deze code en maakt
de functie compleet. De output voor 3 of meer personen ziet er alsvolgt uit:

```
[]                                          --> "no one likes this"
["Niels"]                                   --> "Niels likes this"
["Sven", "Yur"]                             --> "Sven and Yur like this"
["Sebas", "Wies", "Kirsty"]                 --> "Sebas, Wies and Kirsty like this"
["Sjors", "Reinier", "Christiaan", "Mandy"] --> "Sjors, Reinier and 2 others like this" 
```
Waar voor 4 of meer namen het getal in `and 2 others` toeneemt. Teamgenoot 3 pusht commit en pusht deze code nu naar de
main branch.

Goed gedaan, je kan nu clonen, committen en pushen. Nu gaan we verder met branchen.



