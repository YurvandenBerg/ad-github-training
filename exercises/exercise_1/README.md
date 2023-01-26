Je kent vast het 'like' van Facebook en andere social media. We willen de text creëren die in je scherm komt als je 
likes hebt ontvangen van al je vrienden, collega's en bots. Implementeer een functie die een list aanneemt die de namen
van mensen bevat die jouw gave nieuwe katten foto leuk vinden. Begin met een functie die maximaal twee namen aanneemt 
en de volgende output terugstuurt.

```
[]                                --> "no one likes this"
["Niels"]                         --> "Niels likes this"
["Sven", "Yur"]                   --> "Sven en Yur like this"
```

Één iemand uit jouw groep 'forked' de repository naar zijn/haar GitHub pagina en deelt het scherm om samen door de stappen te lopen. De opdrachten zouden nu zichtbaar moeten zijn in de persoonlijke GitHub omgeving. De eigenaar van de repo geeft toegang aan iedereen uit de groep. Ga naar settings -> Collaborators en voeg je groepsgenoten toe. Ga daarna naar 'Branches' en voeg default branch protection rules toe. Iedereen uit de groep 'cloned' nu deze nieuwe geforkte repo naar je project in je IDE. Gebruik `git --init` in je terminal om git te initieren. Werk nu samen aan de bovenstaande opdracht, de eigenaar van de repo commit en pusht de eerste opdracht naar de repo toe. Doe dit met `git push`.

Teamgenoot 2 breidt de code nu uit naar 3 personen die de volgende output heeft:

```
[]                                --> "no one likes this"
["Niels"]                         --> "Niels likes this"
["Sven", "Yur"]                   --> "Sven and Yur like this"
["Sebas", "Wies", "Kirsty"]       --> "Sebas, Wies and Kirsty like this"
```

Maak een branch aan en noem hem 'three-persons'. Teamgenoot 2 commit en pusht de nieuwe code nu als branch naar GitHub, probeer deze nieuwe code nu via een pull request te mergen naar de main branch. Teamgenoot 1 ziet nu een pull request verschijnen. Deel je scherm en probeer samen de pull request te accepteren, of als de code niet goed is om feedback te geven. Ga door totdat de code klopt. Maak de functie nu samen af in een nieuwe branch die 'all-input' heet.

De output voor 3 of meer personen ziet er alsvolgt uit:

```
[]                                          --> "no one likes this"
["Niels"]                                   --> "Niels likes this"
["Sven", "Yur"]                             --> "Sven and Yur like this"
["Sebas", "Wies", "Kirsty"]                 --> "Sebas, Wies and Kirsty like this"
["Sjors", "Reinier", "Christiaan", "Mandy"] --> "Sjors, Reinier and 2 others like this" 
```

Waar voor 4 of meer namen het getal in `and 2 others` toeneemt. Merge de code naar de main branch.
