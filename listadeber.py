
class Lista:
    def __init__(self,tamanio):
        self.lista=[]
        self.longitud=0
        self.size= tamanio
        
        
        
        
    def append(self, dato): #agregar datos a la lista
        if self.longitud < self.size:
           self.lista += [dato]
           self.longitud += 1
        else:
            print("Lista esta llena")
            
    def obtener(self,pos): #obtener datos de la lista        
        if pos < 0 or pos >= self.longitud:
            return None
        else: 
            return self.lista[pos]
        
    def mostrar (self,orden="asc"): # muestra la lista ingresada de forma des-asc dependiendo de las condiciones del usuario
        if orden.lower == "asc":
            for pos in range(self.longitud):
                print("[{}]".format(self.lista[pos]))
        else:
            for pos in range(self.longitud-1,-1,-1):
                print("[{}]".format(self.lista[pos]))
        
        
    def buscar(self,dato):  
        """ n= int(input("Ingrese cuantos elementos desea agregar a la lista: ")) 
        
        for i in range (n):
            nume= int(input("Ingrese numero : ".format(i+1))) 
            self.list.append(nume)
        print(self.list) """ 
        
        """ dato= int(input("Ingrese el numero que quiere encontrar en la lista: ")) """  
        for pos in range(len(self.lista)):
            if self.lista[pos] == dato:
              return "El numero {} se encuentra en la posicion {}".format(dato,pos)
        return -1
            
        
    def insertarr(self,dato):
        if self.buscar(dato) == -1:
            self.lista += [dato]
            self.longitud += 1
            print ("El dato que no se encontro se asigno a la lista: {}".format(self.lista))
        else:
            print("El numero que ingreso si se encuentra en la lista")
    
    
    def eliminarr(self, dato):
        
        if self.buscar(dato) !=-1:
            self.list.remove(dato)
            print(self.list)
        else:
            print("El numero a eliminar no existe")

""" posi= Lista()
print(posi.buscar(dato=0))  """

""" insert= Lista(list)
dato = int(input("Ingrese el numero que quiere encontrar en la lista: ")) 
insert.insertar(dato) """
