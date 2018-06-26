import sys, pygame
from pygame.locals import* 

WIDTH=600
HEIGHT=400
Color=(25, 255, 100)

#funcion que pasa las coordenadas a un n de parcela
def unirparcelaxy (x,y):
    columna=0
    fila=0
    nparcela=-1

    if ((x<400) and (x>100) and (y<400) and (y>100)):
        columna=int((x-100)/75)
        fila=int((y-100)/75)
        nparcela=((fila*4)+columna)
    return (nparcela)


#funcion que pasa el n de parcela a posicion en la pantalla
def unirxyparcela (nparcela):
    columna=0
    fila=0
    x=0
    y=0
    coordenadas=0
    
    fila, columna = (int(nparcela/4), int(nparcela%4))
    
    if ((nparcela<=15) and (nparcela>=0)):
        
        x=((columna*75)+100)
        y=((fila*75)+100)
        coordenadas=(x,y) 
    return(coordenadas)




def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("El Gran Granjero")
    
    #fotosparalosbotones
    bcultivo1=pygame.image.load("frutasfinas.png")
    b1seleccion=pygame.image.load("frutasfinasseleccion.png")
    bcultivo2=pygame.image.load("aloevera.png")
    b2seleccion=pygame.image.load("aloeveraseleccion.png")
    bcultivo3=pygame.image.load("hongos.png")
    b3seleccion=pygame.image.load("hongosseleccion.png")
    bavanzar=pygame.image.load("avanzar.png")
    bavanzarseleccion=pygame.image.load("avanzarseleccion.png")
    parcela=pygame.image.load("parcela.png")
    parcelaff=pygame.image.load("parcelaff.png")
    parcelah=pygame.image.load("parcelah.png")
    parcelaa=pygame.image.load("parcelaa.png")
  
    #Iniciovariables x e y
    posx=0
    posy=0

    #Cursor1=Cursor()
    salir=False
    acumulador=[]
    pasardeturno = 0
    
    #CONSTANTES PARA NO METER NUMEROS MAGICOS
    #cultivos
    estadoMuerto = 0
    estadoCreciendo = 1
    sinCultivo = 0
    frutasFinas = 1
    aloeVera = 2
    hongos = 3
    #posiciones de las parcelas
    tipodecultivo = 0
    estado=1
    crecimientoDelCultivo = 3
    cantidadDeLluvia = 2
    turnosSinCrecer = 4
    turnosMaximosSinCrecer = 2
    lluviaMaximaFrutasFinas = 1000
    lluviaMaximoHongos = 600
    
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
                    print("catástrofe natural!")
                    #catastrofenatural=fuente2.render("CATÁSTROFE NATURAL",1,(0,0,0))
                    #screen.blit(catastrofenatural,(350,10))
                    catn=1
                else:
                    catn=0
    
            lista1=[temp,lluv,vien,catn]
            #print("el clima es", lista1)
            return(lista1)
        
    def apuesta (monedastotal,parcela,nparcela,ubicacion,cultivo): 
             if (monedastotal>0):   
                if parcela[estado]==0:
                    if (len(acumulador)>=2):
                        clickAnterior = acumulador[len(acumulador)-2]
                        ultimoClick = acumulador[len(acumulador)-1]
                        
                        if ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 100) and (clickAnterior[1] >= 50)):
                            cultivo = frutasFinas                    
                        elif ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 200) and (clickAnterior[1] >= 150)):
                            cultivo = aloeVera     
                        elif  ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 300) and (clickAnterior[1] >= 250)):
                            cultivo = hongos
                    #combino tipo de cultivo y parcela
                        
                        if (nparcela != -1 and cultivo != 0):
                            if ((monedastotal>=10) and (cultivo==frutasFinas)):
                                    parcela[tipodecultivo] = frutasFinas
                                    screen.blit(parcelaff,ubicacion)
                                    monedastotal-=10
                                    parcela[estado]=1 
                            elif ((monedastotal>=5)  and (cultivo == hongos)):
                                    parcela[tipodecultivo] = hongos
                                    screen.blit(parcelah,ubicacion)
                                    monedastotal-=5
                                    parcela[estado]=1
                            elif cultivo == aloeVera:
                                    parcela[tipodecultivo] = aloeVera
                                    screen.blit(parcelaa,ubicacion)
                                    monedastotal-=1
                                    parcela[estado]=1
                            cultivo=0
                            #print ("tipo de cultivo", parcela[tipodecultivo])

                            
                lista1=[monedastotal,parcela]
                #print("monedas desde apuesta", monedastotal)
                return monedastotal,parcela
    
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
        print("la cantidad de lluvia es",parcela[cantidadDeLluvia])
        return ([parcela,muerte])

        
    def cosecha (parcela): 
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
    
            elif parcela[tipodecultivo] == aloeVera:
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
   
            elif parcela[tipodecultivo] == hongos : 
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
    cultivo=0
    cantidaddeParcelas = 16

    cantidaddeturnos = 25
    elementosdecadaparcela=[tipodecultivo, Estado, cantidadDeLluviaInicial, crecimiento, nocrecimiento] #elementos que hay en cada parcela (lista2)
    listaparcelas=[]

    for i in range (cantidaddeParcelas):
        listanueva=[]
        listaparcelas.append(listanueva)#parcela
        for x in elementosdecadaparcela:
            listanueva.append(x)
    
    #PARA DESPUES ACOPLAR CON PANTALLA
    
    screen.fill(Color)#color de fondo de la pantalla
    screen.blit(bcultivo1,(500,50))#imprimimos en pantalla las fotos de los botones
    screen.blit(bcultivo2,(500,150))
    screen.blit(bcultivo3,(500,250))
    screen.blit(bavanzar,(175,20))
    screen.blit(parcela,(100,100))
    screen.blit(parcela,(175,100))
    screen.blit(parcela,(250,100))
    screen.blit(parcela,(325,100))
    screen.blit(parcela,(100,175))
    screen.blit(parcela,(175,175))
    screen.blit(parcela,(250,175))
    screen.blit(parcela,(325,175))
    screen.blit(parcela,(100,250))
    screen.blit(parcela,(175,250))
    screen.blit(parcela,(250,250))
    screen.blit(parcela,(325,250))
    screen.blit(parcela,(100,325))
    screen.blit(parcela,(175,325))
    screen.blit(parcela,(250,325))
    screen.blit(parcela,(325,325))

        
        #horizontales
    pygame.draw.line(screen, (0,0,0),(100,100),(400,100),5)
    pygame.draw.line(screen, (0,0,0),(100,175),(400,175),5)
    pygame.draw.line(screen, (0,0,0),(100,250),(400,250),5)
    pygame.draw.line(screen, (0,0,0),(100,325),(400,325),5)
    pygame.draw.line(screen, (0,0,0),(100,400),(400,400),5)

        #verticales
    pygame.draw.line(screen, (0,0,0),(100,100),(100,400),5)
    pygame.draw.line(screen, (0,0,0),(175,100),(175,400),5)
    pygame.draw.line(screen, (0,0,0),(250,100),(250,400),5)
    pygame.draw.line(screen, (0,0,0),(325,100),(325,400),5)
    pygame.draw.line(screen, (0,0,0),(400,100),(400,400),5)
        
        #botóndeplata
    pygame.draw.rect(screen, (100,100,100), (490, 320, 100, 50), 0)
        
        #texto sobre botones
    fuente=pygame.font.Font(None,50)
    fuente1=pygame.font.Font(None,20)
    fuente2=pygame.font.Font(None,30)
    Plata=fuente2.render("Plata",0,(0,0,0))
    screen.blit(Plata,(515,330))
    turno=0
    monedasturno = 0
    nparcela = -1
    #parcela[tipodecultivo] = 0
    while salir!=True:  
        for event in pygame.event.get():
         if (event.type == MOUSEBUTTONDOWN or event.type == QUIT):        
           if event.type == MOUSEBUTTONDOWN:
               mousex, mousey = pygame.mouse.get_pos()
               click=(mousex,mousey)
               acumulador.append(click)
               #print("los clicks", acumulador)
            
           if event.type == QUIT: 
                salir=True
                
           pasardeturno=pygame.image.load("pasardeturno.png")
           normalverde=pygame.image.load("normalverde.png")
               

           if(turno==0):
                #turno=1
                random = funciondevuelveclima(turno)
           if turno < 24:        
               if (len(acumulador)>=1):                
                    clickAnterior = acumulador[len(acumulador)-2]
                    ultimoClick = acumulador[len(acumulador)-1]
                       #print(clickAnterior,"  ", ultimoClick)
                           #PASAR DE TURNO
                    if ((ultimoClick[0] >= 175) and (ultimoClick[0] <= 225) and (ultimoClick[1] <= 70) and (ultimoClick[1] >= 20)):
                        turno+=1
                        print ("pasar de turno")
                        screen.blit(pasardeturno,(110,70))
                        screen.blit(bavanzarseleccion,(175,20))
                        random = funciondevuelveclima(turno) #random con los datos del archivo de clima (lista1)
                        monedasturno = 0
                        print("\n turno",turno)
                        ultimoClick=[0,0]
                        clickAnterior=[0,0]
                           #print(clickAnterior,"  ", ultimoClick)
                        for nparcela in range(cantidaddeParcelas):
                                #print("parcela",nparcela)
                            #apuesta
        ##                        monedastotal, listaparcelas[nparcela]=apuesta(monedastotal,listaparcelas[nparcela],nparcela,ubicacion,cultivo)
                    
        ##                        monedastotal = listadeapuesta[0]
               
                            funcionclima=clima(random,listaparcelas[nparcela])
                            print("lo que devuelve clima. parcela y muerte", funcionclima)
                            print("estado parcela",listaparcelas[0])
                            funcioncosecha=cosecha(listaparcelas[nparcela]) #LE DOY LA PARCELA
                            print("lo que devuelve cosecha. rendimiento y muere", funcioncosecha)
                            #reemplazo valores en la lista de cada parcela
                            rendimientoCosecha = funcioncosecha[0] #si es cero todavia no cosecho
                            muereCosecha = funcioncosecha[1] #si es 1 se murio, sino es cero
                            cultivoxparcela=listaparcelas[nparcela][tipodecultivo] #voy a necesitar que cultivo hay
                
                            muerteporcatastrofenatural=funcionclima[1]
                
                            if (muereCosecha == 1) or (muerteporcatastrofenatural==1) or (rendimientoCosecha != 0):
                                listaparcelas[nparcela]=[0,0,0,0,0]
                                #nparcela = unirparcelaxy(ultimoClick[0],ultimoClick[1])
                                #print("parcela número", nparcela)
                                ubicacion = unirxyparcela(nparcela)
                                screen.blit(parcela, ubicacion)
                  
                            monedasturno+=ganancia(cultivoxparcela,rendimientoCosecha) #le doy la parcela y si cosecho o murio
                            #print("MONEDAS TURNO \n",monedasturno)
                        monedastotal+=monedasturno
                    else:
                        monedasturno = 0
                        screen.blit(normalverde,(110,70))
                                            
                #guardo la parcela
               if (len(acumulador)>=2):
                        
                    if ((ultimoClick[0] >= 100) and (ultimoClick[0] <= 400) and (ultimoClick[1] <= 400) and (ultimoClick[1] >= 100)):
                        screen.blit(normalverde,(110,70))
                        screen.blit(bavanzar,(175,20))
                        nparcela = unirparcelaxy(ultimoClick[0],ultimoClick[1])
                            #print("parcela número", nparcela)
                        ubicacion = unirxyparcela(nparcela)
                            #print(ubicacion)
                            #print("i", i)
                        monedastotal, listaparcelas[nparcela]=apuesta(monedastotal,listaparcelas[nparcela],nparcela,ubicacion,cultivo)
                        #listaparcelas[nparcela]=parcelita
                        print("lo que deberia dar apuesta. monedas total, parcela",monedastotal, listaparcelas[nparcela])
                            #print(listaparcelas[nparcela])
            
                        
               monedasparaimprimir=fuente1.render(str(monedastotal),1,(0,0,0)) 
               screen.blit(monedasparaimprimir,(540,350))
                #print("MONEDAS TOTAL \n",monedastotal)
           else:
               findeljuego=fuente2.render("FIN DEL JUEGO",1,(0,0,0))
               screen.blit(findeljuego,(350,10))
               from topscore import topscore
               topscore(monedastotal)
            
        pygame.display.flip()

    pygame.quit()
main()
