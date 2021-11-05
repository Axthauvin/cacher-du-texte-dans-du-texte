

### [cacherdutexte.github.io](https://cacherdutexte.github.io)

This project contains : 
- Python modules (binary and decimal system 6) with a dedicated tkinter program to use it.
- A web version, which is actually hosted on *https://cacherdutexte.github.io*.


***I explain below how the project works, but an english version is available. [See directly the English explanation :uk:](#-how-did-i-hid-text-in-text)***



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
  <img src="https://github.com/Axthauvin/cacher-du-texte-dans-du-texte/blob/main/images/UTF8-TABLE.png" width = "800">


Pour l'exemple, nous allons prendre le caractère `H`.
Ici, sa représentation décimale est ***72*** (base 10).

- Ensuite nous allons convertir ce nombre en base 6 sur 4 'bits'
  # Pourquoi ?
  Si nous codons les lettres en base 6 sur 4 bits, nous aurons la représenation maximale de `5555` -> soit 6^4 -> 1296
  La valeur maximale que nous allons pouvoir exploiter dans ce tableau
  
  En fait nous avons 5 **caractères invisibles** qui vont correspondrent aux chiffres de ces bits, que nous allons *cacher* dans notre texte.
  - *Pour le 0 il n'y a pas de caractère caché*
  - *Pour le 1 c'est le caractère unicode \u200C*
  - *Pour le 2 c'est le caractère unicode \u200D*
  - *Pour le 3 c'est le caractère unicode \u200E*
  - *Pour le 4 c'est le caractère unicode \u200F*
  - *Pour le 5 c'est le caractère unicode \u034F*
  
  # Exemple avec le `H`
  
  Ici la représentation décimale de `H` est ***72***.
  Sa représentation en *base 6 sur 4 bits* est `0200`.
  Je vais donc : - Pas ajouter de caractère pour le 1er bit (car il vaut 0)
                 - Ajouter le caractère \u200D pour le 2ème bit (car il vaut 2)
                 - Pas ajouter de caractère pour le 3ème bit (car il vaut 0)
                 - Pas ajouter de caractère pour le 4ème bit (car il vaut 0)
  
  ***Reprenons la chaine initiale***
  J'ai `Bonjour, je suis Axel Thauvin`.
  Je vais donc écrire : **Bo`\u200D`nj** juste pour le H
  
  ***Et je fais pareil avec tous les caractères de `Hacker`.***
  Ce qui me donne : 
  `Bo‍njou‍r‏,‌ j‍e‏ ‎su‍i͏s͏ A‍x‏e͏l ‎T‌hauvin` (généré avec mon programme, vous pouvez l'essayer sur mon site)
  
  ***Voilà le résultat :***
  
  <img src="https://github.com/Axthauvin/cacher-du-texte-dans-du-texte/blob/main/images/VideoIllustration.gif" style="width: 100%">
  


### 🇬🇧 How did I hid text in text 
This is a bitwise way of hiding text within text.
Let's imagine the string :
```
Hacker
```
That I want to hide in the message:
```
Hello, I am Axel Thauvin
``` 

- First, we get the **decimal representation in the UTF-8 table** of each character in the `Hacker` string

  *Here is the decimal representation of the first 127 characters in an array (also called ASCII array):*
  <img src="https://github.com/Axthauvin/cacher-du-texte-dans-du-texte/blob/main/images/UTF8-TABLE.png" width = "800">


For the example, we will take the character `H`.
Here, its decimal representation is ***72*** (base 10).

- Then we will convert this number to base 6 on 4 'bits'
  # Why ?
  If we encode the letters in base 6 on 4 bits, we will have the maximum representation of `5555` -> that is 6^4 -> 1296
  The maximum value we can use in this table
  
  In fact we have 5 **invisible characters** which will correspond to the digits of these bits, which we will *hide* in our text.
  - For the 0 there is no hidden character*.
  - For 1 it is the unicode character \u200C*
  - For 2 it is the unicode character \u200D*
  - *For 3 it is the unicode character \u200E*
  - *For 4 it is the unicode character \u200F*
  - *For 5 it is the unicode character \u034F*
  
  # Example with `H`
  
  Here the decimal representation of `H` is ***72***.
  Its 4-bit *base-6* representation is `0200`.
  I will therefore : - Not add a character for the 1st bit (because it is 0)
                 - Add the character \u200D for the 2nd bit (because it is 2)
                 - Not add a character for the 3rd bit (because it is 0)
                 - Do not add a character for the 4th bit (because it is 0)
  
  ***Let's go back to the original string***.
  I have `Hello, I am Axel Thauvin`.
  So I'll write : **I'll write `He`\u200D`ll** just for the H
  
  ***And I do the same with all the characters in `Hacker`.
  Which gives me: 
  He‍llo,‍ ‏I‌ a‍m‏ ‎Ax‍e͏l͏ T‍h‏a͏uv‎i‌n` (generated with my program, you can try it on my website)
  
  ***Here is the result:***
  
  <img src="https://github.com/Axthauvin/cacher-du-texte-dans-du-texte/blob/main/images/VideoIllustration.gif" style="width: 100%">

