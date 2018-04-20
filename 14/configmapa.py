import ConfigParser


interprete = ConfigParser.ConfigParser()
interprete.read('protomap.map')

#GET
print interprete.get('seccion','a')
print interprete.get('seccion','b')
print interprete.get('seccion2','a')
print interprete.get('seccion2','b')

#SECTIONS Lista de secciones
print interprete.sections()
#ITEMS
print interprete.items('seccion2')


