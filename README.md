# Générateur de mot de passe

Génère des mots de passe aléatoire personnalisé ou non.

Le mot de passe généré est automatiquement copier dans le presse papier.

_________________

Options :

-h, --help AIDE Montrer les options
<br>
<code> python generateur_mdp.py -h </code>

-nb NOMBRE, --nombre NOMBRE Nombre de chiffre
<br>
<code> python generateur_mdp.py -nb </code>

-mi MINUSCULE, --minuscule MINUSCULE Nombre de lettre minuscule
<br>
<code> python generateur_mdp.py -mi </code>

-ma MAJUSCULE, --majuscule MAJUSCULE Nombre de lettre majuscule
<br>
<code> python generateur_mdp.py -ma </code>
  
-cs CARACTERE_SPECIAL, --caractere-special CARACTERE_SPECIAL Nombre de caractère spécial
<br>
<code> python generateur_mdp.py -cs </code>

-lg LONGUEUR, --longueur LONGUEUR La longueur totale du mot de passe. S'il est passé, il ignorera -nb, -mi, -ma et -cs, et générer des mots de passe complètement aléatoires avec la longueur spécifiée
<br>
<code> python generateur_mdp.py -lg </code>

-qte QUENTITE, --quentite QUENTITE Nombre de mot de passe à générer
<br>
<code> python generateur_mdp.py -qte </code>

_________________

Exemples :

<code> python generateur_mdp.py -lg 25 </code>
> GV~t)<T1d6m>MK6MH[;$|q_^g

<code> python generateur_mdp.py -nb 2 -mi 5 -ma 5 -cs 2 -lg 25 -qte 1 </code>
> Q@J;A'Z6EF_S~`mM'^qbdS)w(

<code> python generateur_mdp.py -nb 0 -mi 2 -ma 5 -cs 0 -lg 25 -qte 2 </code>
> dMgoho7="MA~hhV(4+Mi483N/
> 
> ]2m=\aQOfi:E~_2vfOA-QC{ru
