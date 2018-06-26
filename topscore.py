def min_sort(l):
    result = []
    while l:
        n = max(l)
        result.append(n)
        l.remove(n)
    l[:] = result
    return(result)

def topscore (puntaje): #LA FUNCION guarda puntaje y nombre para despues mostrar los primeros 10
    
    filepath="topscores.txt"
    puntajeynombre=[]
    listapuntajes=[]
    listanombre=[]
    
    
    f = open('topscores.txt', 'a+')

    try:
        
        nombre=input("ingrese su nombre")
        
        f.write('%r;%r\n' % (puntaje,nombre))
        
    finally:
        f.close()
        
    with open(filepath,'r') as fp:
        
        for line in fp: 
            puntajeynombre.append(line.rstrip().lstrip().split(";"))
        
        
        longitud=len(puntajeynombre)
        
        resultado = {}
        
        for elemento in range (0,longitud):
            puntaje = float(puntajeynombre[elemento][0]) #(porque sino es un string y yo quiero operar con nums) 
            nombre = puntajeynombre[elemento][1]
            
            if puntaje not in resultado:
                resultado[puntaje] = []
            resultado[puntaje].append(nombre)
            
        
        
        listapuntajes=list(resultado.keys())
       
        
        
        
        listapuntajes = min_sort(listapuntajes) #lista ordenada de mayor a menor
        
        print("TOPSCORES")
        for i in range(0,len(listapuntajes)): 
            puntaje = listapuntajes[i]
            nombres = resultado[puntaje]
            for nombre in nombres:
                
                print("{},{}".format(puntaje,nombre))