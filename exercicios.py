#EXERCICIO part. 1
#nomes = ["Ana", "Carlos", "Maria", "João", "Pedro"]
#for nome in nomes:
 #   print(nome)

#EXERCICIO 1 part. 2
#numeros = [10, 20, 30, 40, 50]
#numeros[2] = 100  
#print(numeros)

#EXERCICIO 2 part. 1
# #mtz = [
 #   [1, 2, 3],
  #  [4, 5, 6],
   # [7, 8, 9]
#]
#def exibir_matriz(mtz):
 #   for linha in mtz:
  #      print("\t".join(map(str, linha)))
#exibir_matriz(mtz)

#EXERCICIO 2 Part.2 
# print("-----------------")
#mtz[1][1] = 0
#exibir_matriz(mtz)

#Atividade 3-pt1 
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#fatiamento = lista[2:8]
#print("Elementos do terceiro ao oitavo:", fatiamento)

#Atividade 3-pt2
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#inversao = lista[::-1]
#print("Lista invertida:", inversao)

#Exercício 4-pt1

#letras = ['a', 'b', 'c', 'd', 'e']
#print("Elementos da lista de letras:")
#for letra in letras:
 #   print(letra)

#Exercicio 4-pt2
#numeros = [5, 10, 15, 20, 25]
#dobro_numeros = []
#for numero in numeros:
 #   dobro_numeros.append(numero * 2)
#print(dobro_numeros)

#EXERCICIO 5
#inguagens = ['Python', 'Java', 'C++', 'JavaScript']
#valores = [100, 200, 300, 400]

#for indice, linguagem in enumerate(linguagens):
#    print(indice, linguagem)
    
#for indice, valor in enumerate(valores):
#    if indice % 2 == 0: 
#        print(valor)

#EXERCICIO 6
#quadrados = [x**2 for x in range(1, 11)]
#print(quadrados)

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#pares = [x for x in numeros if x % 2 == 0]
#print(pares)

#Atividade 7 - Pt.1                                              
# numeros = [1,2,3,4,5]
#dobros = []
#for i in numeros:
#    dobros.append(i*2)

#print(dobros)

#Atividade 7 Pt.2

#lista = [10, 20, 60,  80, 100]
#fift = []
#for i in lista:
   # if i >= 50:
      #  fift.append(50)

    #else: 
       # fift.append(i)
    
#print(fift)

#Atividade 8 - Pt.1 

#lista = [10, 20, 30]
#lista.append(99)
#print(lista)

#Atividade 8 - Pt.2

#lista = [1, 2, 3, 4, 5]
#lista.clear()
#print(lista)

#Atividade 8 - Pt.3
#lista = [7, 8, 9]
#lista.copy()
#print(lista)

#Atividade 8 - Pt.4
#lista = [1, 3, 3, 7, 3, 9]
#print(lista.count(3))

#Atividade 8 - Pt.5
#lista = [1,2,3]
#lista.extend([4,5,6])
#print(lista)

#Atividade 8 - Pt.6
#lista = [5,10,15,20,25]
#print(lista.index(20))

#Atividade 8 - Pt.7
#lista = [10,20,30]
#print(lista[-1])
#lista.pop()

#Atividade 8 - Pt.8
#lista = [7, 8, 9, 7, 10]
#lista.remove(7)
#print(lista)

#Atividade 8 - Pt.9
#lista = [1, 2, 3, 4, 5]
#lista.reverse()
#print(lista)

#Atividade 8 - Pt.10
#lista = [5, 3, 8, 1, 2]
#lista.sort()
#print(lista)

#Atividade 8 - Pt.11
#lista = [9, 4, 6, 2, 8]
#print(sorted(lista))
#print(lista)