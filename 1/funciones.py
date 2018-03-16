#LISTAS

#lista = ["Aqui puede ir de todo", 1, [1,2,3,4,5], "A", ["A", "B", "C"]]
#print lista
#print lista[2:]
#print lista[3:4]
#print lista[2][3]

#-------------------------------------------------------------------

#FUNCIONES

def square(a):	
	return a**2

def op(a, b=4):
	suma = a + b
	resta = a - b
	return suma, resta

#s, r = op(4, 2);
#print s, r

#Como copiar listas

l1 = [1,2,3,4,5,6,7] 

l2 = list(l1)	#Forma1
l2 = l1[:]		#Forma2

#ITERADORES


l3 = [1,2,3,4,5,6,7]

for x in l3:
	print x

# if 5 in l3:
# 	print "El 5 esta"
# else:
# 	print "El 5 no esta"
	







