#Creamos un input para que el cliente responda por sí mismo
userReply = input("Do you need to ship a package? (Enter yes or no) ")

#Implantamos el bucle de posible respuesta
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

#Ponemos un nuevo bucle para que peueda elegir y qué imprime según la elección
userReply = input("Would you like to by stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank yoy, please come again")