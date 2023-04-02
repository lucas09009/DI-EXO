#1)
print("Hello World")


#2)     
x = (99**3)*8
print(x)


#3)

# print(5 < 3)
# print(3 == 3)
# print(3 == "3")
# print("3" > 3)
# print("Hello" == "hello")


#4)
computer_brand = "ThinkPad lenovo"
print("I have a ",computer_brand," computer")

#5)
name = "Doe"
age = 25
shoe_size = 1.79
info = "je me nomme, {} , j'ai {}ans, je chausse du {}.".format(name, age, shoe_size)
print(info)



#6)
a = 7
b = 6
if(a > b):
    print("Hello World")

else:
    print(a, "est plus petit que", b)



#7)
nombre = input("Veuillez entrez un nombre: ")
nombre = int(nombre)
if (nombre  % 2 == 0):
    print("le nombre est pair")

else:
    print("le nombre est impair")
    
#8)
myName = "Doe"
yourName = input("Veuillez entrer votre nom: ")
if(yourName == myName):
    print(" Woahh! Nous avons le même nom")
else:
    print("Hello", yourName)


#9)
taille = input("Veuillez saisir votre taille en inch: ")
taille = int(taille)
if(taille > 145):
    print("Vous êtes assez grand pour rouler")
else:
    print("Vous n'êtes pas encore prêt pour rouler")

    

