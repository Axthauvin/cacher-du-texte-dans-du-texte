### :fr: Comment j'ai caché du texte dans du texte
C'est une façon en manipulant les bits de cacher du texte dans du texte.
Imaginons la chaine de caractère :
```
Hacker
```
Que je veux cacher dans le message :
```
Bonjour, je suis Axel Thauvin
``` 

- Dans un premier temps, on vient récupérer la **représentation décimale dans la table UTF-8** de chaque caractère de la chaine `Hacker`

  *Voici dans un tableau, la représentation décimale des 127 premiers caractères (aussi appelé tableau ASCII) :*
  
![Tableau ASCII](https://github.com/Axthauvin/cacher-du-texte-dans-du-texte/blob/main/UTF8-TABLElittle.png)

Pour l'exemple, nous allons prendre le caractère `H`.
Ici, sa représentation décimale est ***72*** (base 10).

- Ensuite nous allons convertir ce nombre en base 6 sur 4 'bits'
  # Pourquoi ?
  Si nous codons les lettres en base 6 sur 4 bits, nous aurons la représenation maximale de `5555` -> soit 6^4 -> 1296
  La valeur maximale que nous allons pouvoir exploiter dans ce tableau


### 🇬🇧 Comment j'ai caché du texte dans du texte
C'est une façon en manipulant les bits de cacher du texte dans du texte
