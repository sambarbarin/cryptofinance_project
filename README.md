cryptofinance_project



## **Selfish mining**
Ce script consiste en une attaque où l'on mine sans dévoiler ses blocks, c'est a dire que l'attaquant va miner des blocs tant qu'il a de l'avance sur la blockchain officiel, il diffuse ses blocs quand il sens qu'il va être rattraper et l'on obtient le graph suivant, pour le rendement des honnêtes mineurs et des mineurs malhonnêtes. 

On obtient un seuil de rentabilité autour des 33% quand on compare la puissance necessaire au minages et le profit des mineurs. 

![selfish_mining](https://user-images.githubusercontent.com/71398780/211200454-40c8cff1-a27a-4ddb-b64f-ab1988bcb942.png)


## **Mining game**
Cette attaque consiste à cacher des blocs et à ne pas les diffuser, afin de créer un fork caché. Puis de le brodaster au moment où le réseau rattrape le mineur égoïste. Le fork caché sera pris en compte car il est plus long. En faisant cela, le mineur égoïste s'assure d'augmenter son rendement.

Avec 33% de la puissance de hachage, nous gagnons pour être malhonnête



## **Attack 1+2**

Lors de cette technique de minage, un attaquant essaie, sur des cycles de 3 blocs, de découvrir le plus de bloc que son adversaire et donc pouvoir ajouter ses blocs découvert à la chaine officielle à l'issue d'un cycle. Comme pour le selfish mining, les seuls paramètres ici sont la puissance de hashage relative alpha de l'attaquant et le nombre de simulation executés n.

