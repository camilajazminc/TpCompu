import sys, pygame
from pygame.locals import* 

def funciondevuelveclima(turno):
    
    filepath = 'ejemplo.txt'  
    list=[]
    rangemax=0
    with open(filepath,'r') as fp:
        for line in fp:
        
            list.append(line.rstrip().lstrip().split(','))
        
    # IMPRIMIR LOS RANGOS DE Cada variable para los proximos 3 turnos
    if (turno<21):
        for u in range (turno,turno+3):
            print("turno",u,"\n rango de temp:",list[u-1][0],"rango lluv",list[u-1][1],"rango vient",list[u-1][2],"rango catn",list[u-1][3])
    else:
        rangemax= len(list) - turno
        
        for u in range (turno,turno+rangemax):
            print("turno",u,"\n rango de temp:",list[u-1][0],"rango lluv",list[u-1][1],"rango vient",list[u-1][2],"rango catn",list[u-1][3])
  
    listtemp=[]
    listlluv=[]
    listvien=[]
    listcatn=[]
    i= (turno-1) #tiene que ir a buscar la linea correspondiente al turno
    #le meto los rangos segun el turno
    rangotemp=list[i][0]
    rangolluvia=list[i][1]
    rangoviento=list[i][2]
    rangocatastrofenat=list[i][3]
    #creo listas que el rango lo separan en los dos valores
    listtemp.append(rangotemp.split('-'))
    listlluv.append(rangolluvia.split('-'))
    listvien.append(rangoviento.split('-'))
    listcatn.append(rangocatastrofenat.split('-'))
    #asigno los a y b para despues pedir el random

    mintemp=listtemp[0][0]
    maxtemp=listtemp[0][1]
    minlluv=listlluv[0][0]
    maxlluv=listlluv[0][1]
    minvien=listvien[0][0]
    maxvien=listvien[0][1]
    mincatn=listcatn[0][0]
    maxcatn=listcatn[0][1]


    import random
    for x in range (1):
        #defino todos los limites
        a=int(mintemp)
        b=int(maxtemp)
        c=int(minlluv)
        d=int(maxlluv)
        e=int(minvien)
        f=int(maxvien)
        g=int(mincatn)
        h=int(maxcatn)
        
        temp=(random.randint(a,b))
        lluv=(random.randint(c,d))
        vien=(random.randint(e,f))
        catn1=(random.randint(0,1000))
        #el random de catastrofe natural es distinto
        if (catn1>g) and (catn1<h):
            print("CATASTROFE NATURAL!!!!!!!")
            catn=1
        else:
            catn=0
    
    lista1=[temp,lluv,vien,catn]
    return(lista1)

def clima (lista1,lista2):
    crece=0
    nocrece=0
    lluvia=0
    muerte=0
    if lista1[3]==1:
        muerte=1
    else:
        if lista2[0]==1: 
         if (((lista1[0]>=9)and(lista1[0]<=25)) and ((lista1[1]<=112)and(lista1[1]>=34)) and (lista1[2]<=30)):
            crece=1
            lluvia+=lista1[1]
         else:
            nocrece = 1
            
        elif lista2[0]==2 :
         if (((lista1[0]>=1)and(lista1[0]<=40)) and (lista1[2]<=100)):
            crece=1
            lluvia+=lista1[1]
         else:
            nocrece=1
            
        elif lista2[0]==3:
         if (((lista1[0]>=6)and(lista1[0]<=30)) and ((lista1[1]<=200)and(lista1[1]>=34)) and (lista1[2]<=80)):
            crece=1
            lluvia=lista1[1]
         else:
            nocrece = 1
            
    return [crece, nocrece, lluvia,muerte]

#cultivos
estadoMuerto = 0
estadoCreciendo = 1
sinCultivo = 0
frutasFinas = 1
aloeVera = 2
hongos = 3
#posiciones de las parcelas
tipodecultivo   = 0
crecimientoDelCultivo = 3
cantidadDeLluevia = 2
turnosSinCrecer = 4

turnosMaximosSinCrecer = 2
lluviaMaximaFrutasFinas = 1000
lluviaMaximoHongos = 600
def cosecha (parcela):
   rendimiento=0
   muere = 0
   if parcela[tipodecultivo] == frutasFinas: 
        if parcela[tipodecultivo] <= turnosMaximosSinCrecer:
          if parcela[cantidadDeLluevia] > lluviaMaximaFrutasFinas:
            muere=1
          elif parcela[3]==9: #cosecho
               
               if (parcela[cantidadDeLluevia] >= 300 and parcela[cantidadDeLluevia] <= 600):
                   rendimiento=1
               elif (parcela[cantidadDeLluevia] > 600 and parcela[cantidadDeLluevia] <= 800):
                   rendimiento=2
               elif (parcela[cantidadDeLluevia] > 800 and parcela[cantidadDeLluevia] <= 1000):
                   rendimiento=3
          elif parcela[crecimientoDelCultivo] < 9:
                rendimiento=0
        else:
          muere=1
    
   if parcela[tipodecultivo] == aloeVera:
        if parcela[tipodecultivo] <= turnosMaximosSinCrecer:
            if parcela[3]==1: #cosecho
 
               if parcela[cantidadDeLluevia] <= 100:
                   rendimiento=1
               elif (parcela[cantidadDeLluevia] > 100 and parcela[cantidadDeLluevia] <= 300):
                   rendimiento=2
               elif parcela[cantidadDeLluevia] > 300 :
                   rendimiento=3
            elif parcela[crecimientoDelCultivo] < 1:
                rendimiento=0
        else:
            muere=1
   
   if parcela[tipodecultivo] == hongos : 
        if parcela[tipodecultivo] <= turnosMaximosSinCrecer:
            if parcela[cantidadDeLluevia] > lluviaMaximoHongos:
                   muerte=1
            elif parcela[3]==5: #cosecho
               
               if (parcela[2]>=100 and parcela[2]<=400):
                   rendimiento=1
               elif (parcela[2]>400 and parcela[2]<=500):
                   rendimiento=2
               elif (parcela[2]>500 and parcela[2]<=600):
                   rendimiento=3
            elif parcela[crecimientoDelCultivo] < 5:
                rendimiento=0
        else:
            muere=1
   return [rendimiento, muere]


#Valor del cultivo + (valor del cultivo*rendimiento/100)
def ganancia (parcela, funcioncosecha):
    monedas=0
    if parcela[0]==1 :
        if funcioncosecha[0]==1:
            monedas=10+(10*50/100)
        elif funcioncosecha[0]==2:
            monedas=10+(10*80/100)    
        elif funcioncosecha[0]==3:
            monedas=10+(10*100/100)
    elif parcela[0]==2 :
        if funcioncosecha[0]==1:
            monedas=1+(1*50/100)
        elif funcioncosecha[0]==2:
            monedas=1+(1*80/100)    
        elif funcioncosecha[0]==3:
            monedas=1+(1*100/100)
    elif parcela[0]==3 :
        if funcioncosecha[0]==1:
            monedas=5+(5*50/100)
        elif funcioncosecha[0]==2:
            monedas=5+(5*80/100)    
        elif funcioncosecha[0]==3:
            monedas=5+(5*100/100)
    return(monedas)

#apuesta

def apuesta (monedastotal,parcela):
    
    if (monedastotal>0):   
       if parcela[1]==0:
           print("Despues del if",parcela)
           print("Quiere plantar en la parcerla " , i, "? responda 1 para plantar o 2 para pasar a la siguiente parcela")
           respuesta=int(input())
           if (respuesta ==1):
            if (monedastotal>=10):
                
              parcela[0]=int(input("Ingrese 1 para ff, 2 para aloe vera y 3 para hngos."))
          
              if parcela[0]==1: #falta comprobar si tiene plata para jugar
                monedastotal-=10
                parcela[1]=1
              elif parcela[0]==2:
                monedastotal-=1
                parcela[1]=1
              elif parcela[0]==3:
                monedastotal-=5
                parcela[1]=1
            elif (monedastotal>=5):
                parcela[0]=int(input("Ingrese 2 para aloe vera o 3 para hngos."))
                if parcela[0]==2:
                  monedastotal-=1
                  parcela[1]=1
                elif parcela[0]==3:
                  monedastotal-=5
                  parcela[1]=1
            else:      
               parcela[0]=int(input("Ingrese 2 para aloe vera."))
               parcela[0]==2
               monedastotal-=1
               parcela[1]=1
    else:
        print ("encontre vacia")
    lista1=[monedastotal,parcela]
    return (lista1)
  

#El cultivo 0 sin cultivo, 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#Los tipos de estado son: 0 muerto, vacio o cosechado y 1 creciendo.
#rendimiento va a tener como valores 1 cuando es minimo, 2 cuando es medio y 3 para el maximo
#En la listab tenemos en la posicion 0 el tipo de cultivo, 1 el estado del cultivo, 2 la cantidad de lluvia del cultivo, 3 el crecimiento del cultivo, 4 turnos sin crecer

tipodecultivo=0
estado=0
cantidadDeLluviaInicial = 0
crecimiento=0
nocrecimiento=0
monedastotal=84
#Deberia ser 16, 2 es para las pruebas
cantidaddeParcelas = 2
cantidaddeturnos = 25

elementosdecadaparcela=[tipodecultivo, estado, cantidadDeLluviaInicial, crecimiento, nocrecimiento] #elementos que hay en cada parcela (lista2)
listaparcelas=[]

for i in range (cantidaddeParcelas):
    listaparcelas.append(elementosdecadaparcela[:])#parcela

#falta plantar (listas de parcelas[j]=listab)

for i in range (cantidaddeturnos):
    random = funciondevuelveclima(i) #random con los datos del archivo de clima (lista1)
    monedasturno = 0
    for j in range (cantidaddeParcelas):
        #apuesta
        print(listaparcelas)
        listadeapuesta = apuesta(monedastotal,listaparcelas[j])
       # print(listadeapuesta)
        print(listaparcelas[j])
        print(listaparcelas[j])
        monedastotal = listadeapuesta[0]
        listaparcelas[j] = listadeapuesta[1]
        #controlparcelas
        funcionclima = clima(random,listaparcelas[j])
        listaparcelas[j][2] = funcionclima[2]
        listaparcelas[j][3] = funcionclima[0]
        listaparcelas[j][4] = funcionclima[1]
        funcioncosecha = cosecha(listaparcelas[j])
        #reemplazo valores en la lista de cada parcela
        rendimientoCosecha = funcioncosecha[0]
        muereCosecha = funcioncosecha[1]
        if (muereCosecha == 1 or rendimientoCosecha != 0):
            listaparcelas[j] = elementosdecadaparcela[:]
        
        else:
            listaparcelas[j][1] = 1
            listaparcelas[j][2] += funcionclima[2]
            listaparcelas[j][3] += funcionclima[0]
            listaparcelas[j][4] += funcionclima[1]
         
        monedasturno += ganancia(listaparcelas[j],funcioncosecha)
    monedastotal += monedasturno
    
    
    #PARA DESPUES ACOPLAR CON PANTALLA
    #monedasparaimprimir=fuente1.render(monedastotales,0,(0,0,0))
   # screen.blit(monedasparaimprimir,(500,320))
    

               
                 
            
            
