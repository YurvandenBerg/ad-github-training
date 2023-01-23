Nu je kan clonen, committen en pushen gaan we met een branch werken. Iedereen uit je groepje
opent een branch op het functie bestand dat je in de vorige opdracht heb gemaakt. Maak een branch aan met de naam

opdracht_2_NAAM (NAAM is jouw naam). Dit doe je door gebruik te maken van `git branch opdracht_2_NAAM`. Nu typ je 
`git branch` om te kijken in welke branch je zit. Als het goed is staat het sterretje nog bij main. Je wilt nu navigeren
naar de branch die je net gemaakt hebt, type `git checkout opdracht_2_NAAM`. als je nu opnieuw `git branch` gebruikt 
bevind je je in de nieuwe branch. 

In deze nieuwe branch ga je aan de slag met de functie die je in de vorige opdracht gemaakt hebt. We hebben inmiddels
een functie die het aantal likes telt. De likes op je Facebook posts zijn zóóóó 2018 geworden. Het enige waar jij 
Facebook nog voor gebruikt is de verjaardag van je vrienden en collega's. 

Voeg een functie toe aan je huidige python bestand die een melding stuurt of jouw verjaardag vandaag is. De functie 
accepteert de input `name, date_of_birth` en de functienaam is `is_it_my_birthday`. Bonuspunten worden gescoord met
typehints en docstrings :). De output zou er alsvolgt uit moeten zien:

```
['Linus', '1969-12-28']  --> "Unfortunately, it is not your birthday"
['Gerda', '1980-02-27']  --> "Today is Gerda's birthday!"
```

Als je de output van de functie gecheckt hebt met voorbeelden kan je vervolgens de branch gaan pushen naar GitHub. 
Hiervoor moet je eerst je nieuwe veranderingen aan je commit toevoegen met `git status`. Dit geeft aan welke 
veranderingen je hebt gemaakt. Deze veranderingen voeg je vervolgens toe met `git add ...`. Je kan opnieuw met `git status`
checken of de veranderingen zijn doorgevoerd. Gebruik daarna `git commit -m "BESCHRIJVING"` om een beschrijving te geven
van je commit.

Gebruik `git push origin opdracht_2_NAAM` om de branch te pushen. Deze zou nu zichtbaar moeten zijn in de repository op 
GitHub. Om jouw nieuwe stukje code toe te voegen aan het totale project moet er nu een Merge van jouw branch naar de 
main branch plaatsvinden. Hoe dit gebeurt bespreken we weer met de totale groep.

Nu heb je geleerd om met branches te werken en kan je in je volgende projecten makkelijk met teamgenoten aan dezelfde 
projecten werken.
