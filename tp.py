import sys, pygame
from pygame.locals import* 

#CONSTANTES PARA NO METER NUMEROS MAGICOS

#cultivos
estadoMuerto = 0
estadoCreciendo = 1
sinCultivo = 0
frutasFinas = 1
aloeVera = 2
hongos = 3
#posiciones de las parcelas
tipodecultivo   = 0
estado=1
crecimientoDelCultivo = 3
cantidadDeLluvia = 2
turnosSinCrecer = 4

turnosMaximosSinCrecer = 2
lluviaMaximaFrutasFinas = 1000
lluviaMaximoHongos = 600

def funciondevuelveclima(turno):
    
    filepath = 'Climas.csv'  
    list=[]
    rangemax=0
    with open(filepath,'r') as fp:
        for line in fp:
        
            list.append(line.rstrip().lstrip().split(';'))
        
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

def clima (random,parcela):
       
    muerte=0
    if random[3]==1: #CATASTROFE NATURAL
        muerte=1
    else:
        if parcela[tipodecultivo] == frutasFinas: 
            if (((random[0]>=9)and(random[0]<=25)) and ((random[1]<=112)and(random[1]>=34)) and (random[2]<=30)):
                parcela[crecimientoDelCultivo]+=1
                parcela[cantidadDeLluvia]+=random[1]
            else:
                parcela[turnosSinCrecer]+= 1
            
        elif parcela[tipodecultivo] == aloeVera:
            if (((random[0]>=1)and(random[0]<=40)) and (random[2]<=100)):
                parcela[crecimientoDelCultivo]+=1
                parcela[cantidadDeLluvia]+=random[1]
            else:
                parcela[turnosSinCrecer]+=1
            
        elif parcela[tipodecultivo] == hongos:
            if (((random[0]>=6)and(random[0]<=30)) and ((random[1]<=200)and(random[1]>=34)) and (random[2]<=80)):
                parcela[crecimientoDelCultivo]+=1
                parcela[cantidadDeLluvia]+=random[1]
            else:
                parcela[turnosSinCrecer]+= 1
    
    return ([parcela,muerte])


def cosecha (parcela): #PORQUE EVALUAMOS SI MUERE EN LA FUNCION COSECHA Y EN LA FUNCION CLIMA FIJARSE QUE ONDA
    rendimiento=0
    muere = 0
    if parcela[tipodecultivo] == frutasFinas: 
        if parcela[turnosSinCrecer] <= turnosMaximosSinCrecer:
            if parcela[cantidadDeLluvia] > lluviaMaximaFrutasFinas:
                muere=1
            elif parcela[crecimientoDelCultivo]==9: #cosecho
               
                if (parcela[cantidadDeLluvia] >= 300 and parcela[cantidadDeLluvia] <= 600): #CALCULOS DE RENDIMIENTO SEGUN LA LLUVIA PARA FRUTA FINA
                    rendimiento=1
                elif (parcela[cantidadDeLluvia] > 600 and parcela[cantidadDeLluvia] <= 800):
                    rendimiento=2
                elif (parcela[cantidadDeLluvia] > 800 and parcela[cantidadDeLluvia] <= 1000):
                    rendimiento=3
            elif parcela[crecimientoDelCultivo] < 9: #NO COSECHO TODAVIA
                rendimiento=0
        else:
            muere=1
    
    if parcela[tipodecultivo] == aloeVera:
        if parcela[turnosSinCrecer] <= turnosMaximosSinCrecer:
            if parcela[crecimientoDelCultivo]==1: #cosecho
 
                if parcela[cantidadDeLluvia] <= 100:
                    rendimiento=1
                elif (parcela[cantidadDeLluvia] > 100 and parcela[cantidadDeLluvia] <= 300):
                    rendimiento=2
                elif parcela[cantidadDeLluvia] > 300 :
                    rendimiento=3
            elif parcela[crecimientoDelCultivo] < 1:
                rendimiento=0
        else:
            muere=1
   
    if parcela[tipodecultivo] == hongos : 
        if parcela[turnosSinCrecer] <= turnosMaximosSinCrecer:
            if parcela[cantidadDeLluvia] > lluviaMaximoHongos:
                muerte=1
            elif parcela[crecimientoDelCultivo]==5: #cosecho
               
                if (parcela[cantidadDeLluvia]>=100 and parcela[cantidadDeLluvia]<=400):
                    rendimiento=1
                elif (parcela[cantidadDeLluvia]>400 and parcela[cantidadDeLluvia]<=500):
                    rendimiento=2
                elif (parcela[cantidadDeLluvia]>500 and parcela[cantidadDeLluvia]<=600):
                    rendimiento=3
            elif parcela[crecimientoDelCultivo] <5:
                rendimiento=0
        else:
            muere=1
   
    return([rendimiento, muere])


#Valor del cultivo + (valor del cultivo*rendimiento/100)
def ganancia (cultivo, rendimiento):
    monedas=0
    if (cultivo==frutasFinas): #si el cultivo en la parcela es fruta fina
        if rendimiento==1: #y el rendimiento fue de 1 2 o 3
            monedas=10+(10*50/100)
        elif rendimiento==2:
            monedas=10+(10*80/100)    
        elif rendimiento==3:
            monedas=10+(10*100/100)
    elif (cultivo==aloeVera): #si el cultivo en la parcela es aloe vera
        if rendimiento==1:#y el rendimiento fue de 1 2 o 3
            monedas=1+(1*50/100)
        elif rendimiento==2:
            monedas=1+(1*80/100)    
        elif rendimiento==3:
            monedas=1+(1*100/100)
    elif (cultivo==hongos): #si el cultivo en la parcela es hongos
        if rendimiento==1:#y el rendimiento fue de 1 2 o 3
            monedas=5+(5*50/100)
        elif rendimiento==2:
            monedas=5+(5*80/100)    
        elif rendimiento==3:
            monedas=5+(5*100/100)
   
    return(monedas)

#apuesta

def apuesta (monedastotal,parcela):
    
    if (monedastotal>0):   
        if parcela[estado]==0:
           
            print("Quiere plantar en la parcerla? responda 1 para plantar o 2 para pasar a la siguiente parcela")
            respuesta=int(input())
            if (respuesta ==1):
                if (monedastotal>=10):
                    parcela[tipodecultivo]=int(input("Ingrese 1 para ff, 2 para aloe vera y 3 para hngos."))
          
                    if parcela[tipodecultivo]==1: 
                        monedastotal-=10
                        parcela[estado]=1
                    elif parcela[tipodecultivo]==2:
                        monedastotal-=1
                        parcela[estado]=1
                    elif parcela[tipodecultivo]==3:
                        monedastotal-=5
                        parcela[estado]=1
                elif (monedastotal>=5):
                    parcela[tipodecultivo]=int(input("Ingrese 2 para aloe vera o 3 para hngos."))
                    if parcela[tipodecultivo]==2:
                        monedastotal-=1
                        parcela[estado]=1
                    elif parcela[tipodecultivo]==3:
                        monedastotal-=5
                        parcela[estado]=1
                else:      
                    parcela[tipodecultivo]=int(input("Ingrese 2 para aloe vera."))
                    parcela[tipodecultivo]==2
                    monedastotal-=1
                    parcela[estado]=1
        
    lista1=[monedastotal,parcela]
    
    return (lista1)
  
    
#acá empieza el programa principal

#El cultivo 0 sin cultivo, 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#Los tipos de estado son: 0 muerto, vacío o cosechado y 1 creciendo.
#rendimiento va a tener como valores 1 cuando es mínimo, 2 cuando es medio y 3 para el máximo
#En la listab tenemos en la posición 0 el tipo de cultivo, 1 el estado del cultivo, 2 la cantidad de lluvia del cultivo, 3 el crecimiento del cultivo, 4 turnos sin crecer

tipodecultivo=0
Estado=0
cantidadDeLluviaInicial = 0
crecimiento=0
nocrecimiento=0
monedastotal=84

cantidaddeParcelas = 2
#Deberia ser 16, 2 es para las pruebas
cantidaddeturnos = 25

elementosdecadaparcela=[tipodecultivo, Estado, cantidadDeLluviaInicial, crecimiento, nocrecimiento] #elementos que hay en cada parcela (lista2)
listaparcelas=[]

for i in range (cantidaddeParcelas):
    listanueva=[]
    listaparcelas.append(listanueva)#parcela
    for x in elementosdecadaparcela:
        listanueva.append(x)
        
for i in range (1,cantidaddeturnos):
    random = funciondevuelveclima(i) #random con los datos del archivo de clima (lista1)
    monedasturno = 0
    print("\n turno",i)
    
    for j in range (cantidaddeParcelas):
        print("parcela",j)
        #apuesta
        
        listadeapuesta=apuesta(monedastotal,listaparcelas[j])
      
        monedastotal = listadeapuesta[0]
       
        
        funcionclima=clima(random,listaparcelas[j])
      
        funcioncosecha=cosecha(listaparcelas[j]) #LE DOY LA PARCELA
        

        
        
        #reemplazo valores en la lista de cada parcela
        rendimientoCosecha = funcioncosecha[0] #si es cero todavia no cosecho
        muereCosecha = funcioncosecha[1] #si es 1 se murio, sino es cero
        cultivoxparcela=listaparcelas[j][0] #voy a necesitar que cultivo hay
        
        
        muerteporcatastrofenatural=funcionclima[1]
        
        if (muereCosecha == 1) or (muerteporcatastrofenatural==1) or (rendimientoCosecha != 0):
            listaparcelas[j]=[0,0,0,0,0]
          
        monedasturno+=ganancia(cultivoxparcela,rendimientoCosecha) #le doy la parcela y si cosecho o murio
        print("MONEDAS TURNO \n",monedasturno)
    monedastotal+=monedasturno
    print("MONEDAS TOTAL \n",monedastotal)
    
    
    #PARA DESPUES ACOPLAR CON PANTALLA
    #monedasparaimprimir=fuente1.render(monedastotales,0,(0,0,0))
   # screen.blit(monedasparaimprimir,(500,320))
    

               
                 
            
            
