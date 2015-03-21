#Francisco Manuel Morales Martin, David Blanco Cañizares

#02 TRABAJANDO CON POKEMON

fichero = open("pokemon.txt", "rt") #Abrimos el fichero pokemon.txt
pokestring = fichero.readlines()
fichero.close() #cerramos el fichero

pokedex = [] #lista original
pokelist = [] #lista para controlar las palabras indexadas
pokemayor = [] #lista para almacenar palabras


for line in pokestring:
	for pokemon in line.split(' '): #recorremos cada elemento inluido los espacios
		if pokemon[-1] == "\n":
			pokemon = pokemon[:-1] #se elimina el carácter fin de línea 
		pokedex.append(pokemon); #añadimos la palabra en la lista

for i in range(len(pokedex)): #recorre la lista
	s = pokedex[i] #almacena la palabra indexada
	for j in range(len(pokedex)-1): #recorre la lista
		if (pokedex[j].startswith(s[-1]) and pokedex[j] not in pokemayor): #comprueba que la ultima letra de cada palabra es la primera letra de la palabra indexada
																		   #comprueba que no se repita para evitar un bucle infinito			
			pokemayor += [pokedex[j]] #si lo es la almacena en pokemayor
			s = pokedex[j] #convertimos la palabra indexada en la de la coincidencia
			j = 0 #vuelve a iniciar el bucle

	if len(pokelist) < len(pokemayor): #si pokelist es mas corta que pokemayor, pokelist se convierte en pokemayor
		pokelist = pokemayor[:] #esa notacion es para mover pokemayor a pokelist sin copiar el objeto

	pokemayor = [] #vaciamos la lista
	
print pokelist #imprimimos pokelist

