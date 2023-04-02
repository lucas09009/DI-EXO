#1)
print("Hello World","\n","I love python")


#2)
enterMonth = input("Entrer un mois compris entre 1 à 12, ex: le chiffre 1 correspond à Janvier , 2 correspond à Février, etc: ")
enterMonth = int(enterMonth)
if(enterMonth >=3) and (enterMonth <=5):
    print("la saison qui correspond au mois saisie est:", "Printemps de Mars(3) à Mai(5)")
elif(enterMonth >=6) and (enterMonth <=8):
    print("la saison qui correspond au mois saisie est:", "Eté de Juin(6) à Août(8)")

elif(enterMonth >=9) and (enterMonth <=12):
    print("la saison qui correspond au mois saisie est:", "Automne de Septembre(9) à Novembre(11)")

elif(enterMonth >=1) and (enterMonth <=2):
    print("la saison qui correspond au mois saisie est:", "Hiver de Décembre(12) à Février(2)")
else:
    print("saisie invalide")
