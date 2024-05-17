# Guide d'utilisation pour le jeu

## Comment jouer ?
Pour se déplacer, appuyez sur les flèches de votre clavier. Attention, vous de pouvez pas marcher sur les arbres et les batiments !
Si vous voulez ouvrir votre inventaire sur la carte, appuyez sur la touche i de votre clavier.

Lorsqu'un combat avec un pokemon sauvage est lancé, quatre options s'offrent à vous :
  - Attaque neutre
  - Attaque spéciale
  - Fuir
  - Changer de pokemon
Pour utiliser l'une des ces quatre options, appuyez sur les cases correspondantes.
En dehors de la fuite, chaque options mènent le pokemon adverse à attaquer, et donc vous recevez des dégats.

Lorsque vous gagnez un combat, le pokemon sauvage disparrait de la carte et s'ajoute à votre inventaire.

## Détails sur les dégats dans les combats

### Pour les attaques neutres
La formule utilisée est la suivante :
$$\frac{attaque * 15}{deffenseennemi}$$

### Pour les attaques spéciales
Chaques type à ses forces et ses faiblasses. Par exemple le type feu est fort face au type glace, mais faible face au type eau. Il existe donc des coefficients multiplicateurs à utiliser.
La formule utilisée est la suivante :
$$\frac{attaquespeciale * 15}{deffensespecialeennemi}$$

### Détails sur la réponse de l'adversaire
L'adversaire attaque "intelligemment" : si son type l'avantage par rapport au type de votre pokemon, il fera une attaque spéciale, s'il est désaventagé il lancera une attaque neutre.
Dans le cas où le pokemon adverse n'est ni avantagé ni désaavantagé, le pokemon adverse lancera de manière aléatoire soit une attaque neutre soit une attaque spéciale.
