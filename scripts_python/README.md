# Guide d'utilisation pour le jeu
Auteurs :
- HERAUD Timothée
- LAGNEAUX Abigaëlle
- ZITO Nicolas

Versions utilisées :
  - Numpy : 1.24.4
  - Pyqt : 5.15.10

## Comment jouer ?
Pour lancer le jeu, veuillez lancer le fichier main.py.

Pour se déplacer, appuyez sur les flèches de votre clavier. 
Attention, vous ne pouvez pas marcher sur les arbres et les batiments !

Si vous voulez ouvrir votre inventaire sur la carte, appuyez sur la touche i de votre clavier.

Si vous voulez chanter le générique de Pokemon avec la voix de Johnny Hallyday, appuyez sur la touche c de votre clavier.

Lorsqu'un combat avec un pokemon sauvage est lancé, quatre options s'offrent à vous :
  - Attaque neutre
  - Attaque spéciale
  - Fuir
  - Changer de pokemon

Pour utiliser l'une des ces quatre options, appuyez sur les cases correspondantes.
En dehors de la fuite, chaque options mène le pokemon adverse à attaquer, et donc vous recevez des dégats.

Lorsque vous gagnez un combat, le pokemon sauvage disparaît de la carte et s'ajoute à votre inventaire.

## Règles misent en place
Le but du jeu est d'attrapper 200 pokemons sur les 300 de la carte via des combats entre les pokemons acquis et les pokemons sauvages (La victoire est donnée lorsque 200 pokemons sont acquis pour compenser le fait que certains pokemons peuvent apparaitre dans les arbres au milieu de la carte).

Nous avons choisi de ne pas prendre en compte la vitesse des pokemons : c'est le pokemon du joueur qui attaque en premier.

Il y a certaines règles lors des combats :
  - Lorsque le pokemon du joueur attaque, le pokemon attaqué réplique
  - Lorsque le joueur change de pokemon, le nouveau pokemon reçoit une attaque du pokemon sauvage
  - Lorsque l'un des pokemons acquis perd tous ses PV, le joueur est obligé de changer de pokemon
  - Lorsque tous les pokemons du joueur n'ont plus de PV, il a perdu le combat

## Détails sur les dégats dans les combats

La formule officielle du calcul des dégâts contenant des données non fournies, l'équipe a choisi de s'en inspirer et de créer les formules suivantes.

### Pour les attaques neutres
La formule utilisée est la suivante :
$$\frac{attaque \times 10}{deffenseennemi}$$

### Pour les attaques spéciales
Chaque type a ses forces et ses faiblasses. Par exemple le type feu est fort face au type glace, mais faible face au type eau. Il existe donc des coefficients multiplicateurs à utiliser.
La formule utilisée est la suivante :
$$\frac{attaquespeciale \times 10}{deffensespecialeennemi} \times CM $$

CM étant le coefficiant multiplicateur correspondant aux types des pokemons en jeu.

### Détails sur la réponse de l'adversaire
L'adversaire attaque "intelligemment" : si son type l'avantage par rapport au type de votre pokemon, il fera une attaque spéciale, s'il est désaventagé il lancera une attaque neutre.
Dans le cas où le pokemon adverse n'est ni avantagé ni désavantagé, le pokemon adverse lancera de manière aléatoire soit une attaque neutre soit une attaque spéciale.

## Détail des différents fichiers

#### Extraction_des_donnees.py
Ce fichier permet d'extraire les données mises à disposition. Il sélectionne 300 pokemons qu'il répartit de manière aléatoire sur la carte.
Il affecte à chaque pokemon sa classe, pour ainsi lui donner ses attributs et méthodes.
L'équipe a fait le choix de ne pas utiliser les coordonnées fournies dans data pour une meilleure répartition sur la carte.

#### GUI_Choix_Pokemon.py
Ce fichier permet la création de la boîte de dialogue pour le changement de pokemon lors d'un combat.
Cette fenêtre montre les pokemons disponibles au joueur et permet une sélection.

#### GUI_Combat.py
Ce fichier permet de créer la fenêtre liée au combat. 

#### GUI_Combat_code.py
Ce fichier permet de coder tout le combat. Il relie notamment les bouttons aux actions et met à jour la fenêtre de combat.

#### Inventory.py
Ce fichier permet la création de la fenêtre Inventory, disponible lorsque vous appuyez sur la touche i.
Cette fenêtre permet au joueur de voir tous les pokemons dont il dispose pour ses prochains comabts.

#### main.py
Ce fichier est le fichier permettant de jouer.

#### MapAndSprite.py
Ce fichier définit la map, les collisions et les déplacements du joueur. 

#### POKEMON.py
Ce fichier définit les différentes classe de Pokemons et la classe joueur.
