#1)ESSAI D'EXPLICATION
#Nous pouvons appeler python3 en étant en dehors du répertoire exécutable grâce à la variable PATH,
#cette variable PATH, nous permet de stocker des répertoires, une fois ces répertoires stockés nous pouvons des commandes sans 
#toutefois spécifier leur emplacement complet dans le terminal



#2)
#Après avoir lu la documentation sur alias, j'ai compris qu'on parle d'alias lorsque plusieurs variables pointent directement ou 
#indirectement à une seule de stockage



#3)
3 <= 3 < 9
True #car en réalité nous avons deux membres, le premier est 3<=3 ce qui équivaut à (3<3) or (3=3), la réponse est True./
#le second membre est 3<9, ce qui est vrai, en conclusion la réponse finale est True./

3 == 3 == 3
True

bool(0)
False

bool(5 == "5")
False

bool(4 == 4) == bool("4" == "4")
True

bool(bool(None))
False


x = (1 == True)
print("x is", x)
x is True


y = (1 == False)
print("y is", y)
y is False   


a = True + 4
print("a:", a)
a: 5


b = False + 10
print("b:", b)
b: 10



#4)
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
"sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
"Ut enim ad minim veniam, quis nostrud exercitation ullamco "
"laboris nisi ut aliquip ex ea commodo consequat."
"Duis aute irure dolor in reprehenderit in voluptate velit"
"esse cillum dolore eu fugiat nulla pariatur."
"Excepteur sint occaecat cupidatat non proident,"
"sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

#5)
#SAISIE DE LA PREMIERE PHRASE 
phrase = input("Veuillez saisir la phrase la plus longue que vous pouvez sans le caractère « A »: ")
#CONTROLE POUR DETECTER LA PRESENCE DE "A"
while "A" in phrase:
    phrase = input("Veuillez saisir la phrase la plus longue que vous pouvez sans le caractère « A »: ")
    a = len(phrase)
else:
#SAISIE DE LA DEUXIEME PHRASE 
    newPhrase = input("Veuillez saisir à nouveau la phrase la plus longue que vous pouvez sans le caractère « A »: ")
#CONTROLE POUR DETECTER LA PRESENCE DE "A"
    while "A" in newPhrase:
        newPhrase = input("Veuillez saisir à nouveau dla phrase la plus longue que vous pouvez sans le caractère « A »: ")
    else:
        b = len(newPhrase)
    if(b > a):
        print("WOAHH, Vous avez saisi une phrase plus longue que la première")
    elif(b == a):
        print("Désolé, Vous avez saisi une phrase qui a le même nombre de caractères que la première")
    else:
        print("Désolé, Vous avez saisi une phrase moins longue que la première")
         
    
    
    
