
class Lista:
    def __init__(self,list):
        self.list=list
        """ self.list=[] """
        self.longitud=0
        
        
    def buscar(self,dato):  
        """ n= int(input("Ingrese cuantos elementos desea agregar a la lista: ")) 
        
        for i in range (n):
            nume= int(input("Ingrese numero {}: ".format(i+1))) 
            self.list.append(nume)
        print(self.list) """ 
        
        """ dato= int(input("Ingrese el numero que quiere encontrar en la lista: ")) """ 
        for pos in range(len(self.list)):
            if self.list[pos] == dato:
                return "El numero {} se encontro en la posicion {} ".format(dato,pos)
            
        return -1        
        
    def insertar(self,dato):
        if self.buscar(dato) == -1:
            self.list += [dato]
            self.longitud += 1
            print ("El dato que no se encontro se asigno a la lista: {}".format(self.list))
        else:
            print("El numero que ingreso si se encuentra en la lista")
    
    
    def eliminar(self, dato):
        
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
