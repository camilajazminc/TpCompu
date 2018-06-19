#El cultivo 0 sin cultivo, 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#Los tipos de estado son: 0 vacío, 1 muerto, 2 creciento, 3 cosecha
#rendimiento va a tener como valores 1 cuando es mínimo, 2 cuando es medio y 3 para el máximo
#En la lista2 tenemos en la posición 0 el tipo de cultivo, 1 el estado del cultivo, 2 la cantidad de lluvia del cultivo, 3 el crecimiento del cultivo, 4 turnos sin crecer

#PANTALLA

#eventype para el mouse.nap devuelve el click

import sys, pygame
from pygame.locals import*
pygame.init()

WIDTH=600
HEIGHT=400
Color=(25, 255, 100)

#posx,posy=pygame.mouse.get_pos()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(Color)
    pygame.display.set_caption("El Gran Granjero")
    pygame.draw.rect(screen, (100,0,0), (100, 100, 300, 300), 0)
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
    
    
    mifuente=pygame.font.sysfont("Arial",10)
    MiTexto1=MiFuente.render("Furtas Finas",0,(200,60,88))
    MiTexto2=MiFuente.render("Aloe Vera",0,(200,60,88))
    MiTexto3=MiFuente.render("Hongos",0,(200,60,88))
    #botones seleccion de cultivos
    
    pygame.draw.rect(screen, (100,100,100), (500, 50, 50, 50), 0)
    sreen.blit(MiTexto1,(500, 50, 50, 50))
    pygame.draw.rect(screen, (100,100,100), (500, 150, 50, 50), 0)
    sreen.blit(MiTexto2,(500, 150, 50, 50))
    pygame.draw.rect(screen, (100,100,100), (500, 250, 50, 50), 0)
    sreen.blit(MiTexto3,(500, 250, 50, 50))
    pygame.display.flip()
    
    
    while True:  
        for eventos in pygame.event.get():   
            if eventos.type == QUIT: 
                sys.exit(0)    



def funciondevuelveclima(turno):
    
    filepath = 'ejemplo.txt'  
    list=[]

    with open(filepath,'r') as fp:
        for line in fp:
        
            list.append(line.rstrip().lstrip().split(','))
        
#print(list[1][0])METER ACA UN FOR U IN RANGE 0,9 IMPRIMIR LOS RANGOS DE CADA COSA
    for u in range (turno,turno+9):
        print("turno",u,"\n rango de temp:",list[u][0],"rango lluv",list[u][1],"rango vient",list[u][2],"rango catn",list[u][3])
    
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

funciondevuelveclima(2)                
                
                
lista1=[] #random con los datos del archivo de clima
lista2=[] #elementos que hay en cada parcela
    

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
                
    lista3=[crece, nocrece, lluvia,muerte]
            
    return (lista3)


def cosecha (lista4):
   
   rendimiento=0
   muere=0
   if lista4[0]==1 : 
        if lista4[4]<=2:
          if lista4[2]>1000 :
            muere=1
          elif lista4[3]==9: #cosecho
               
               if (lista4[2]>=300 and lista4[2]<=600):
                   rendimiento=1
               elif (lista4[2]>600 and lista4[2]<=800):
                   rendimiento=2
               elif (lista4[2]>800 and lista4[2]<=1000):
                   rendimiento=3
          elif lista4[3]<9:
                rendimiento=0
          else:
            muere=1
    
   if lista4[0]==2:
        if lista4[4]<=2:
            if lista4[3]==1: #cosecho
               
               if lista4[2]<=100:
                   rendimiento=1
               elif (lista4[2]>100 and lista4[2]<=300):
                   rendimiento=2
               elif lista4[2]>300 :
                   rendimiento=3
            elif lista4[3]<1:
                rendimiento=0
        else:
            muere=1
   
   if lista4[0]==3 : 
        if lista4[4]<=2:
            if list4[2]>600:
                   muerte=1
            elif lista4[3]==5: #cosecho
               
               if (lista4[2]>=100 and lista4[2]<=400):
                   rendimiento=1
               elif (lista4[2]>400 and lista4[2]<=500):
                   rendimiento=2
               elif (lista4[2]>500 and lista4[2]<=600):
                   rendimiento=3
            elif lista4[3]<5:
                rendimiento=0
        else:
            muere=1
        lista5=[rendimiento, muere]
       
        return(lista5)


#Valor del cultivo + (valor del cultivo*rendimiento/100)
def ganancia (lista4, funcioncosecha):
    monedas=0
    if lista4[0]==1 :
        if funcioncosecha[0]==1:
            monedas=10+(10*50/100)
        elif funcioncosecha[0]==2:
            monedas=10+(10*80/100)    
        elif funcioncosecha[0]==3:
            monedas=10+(10*100/100)
    elif lista4[0]==2 :
        if funcioncosecha[0]==1:
            monedas=1+(1*50/100)
        elif funcioncosecha[0]==2:
            monedas=1+(1*80/100)    
        elif funcioncosecha[0]==3:
            monedas=1+(1*100/100)
    elif lista4[0]==3 :
        if funcioncosecha[0]==1:
            monedas=5+(5*50/100)
        elif funcioncosecha[0]==2:
            monedas=5+(5*80/100)    
        elif funcioncosecha[0]==3:
            monedas=5+(5*100/100)
    return(monedas)

#apuesta

def apuesta (monedastotal,listaparcelas):
    for i in range (1,17):
       if listaparcelas[i-1][1]==0:
        print("Quiere plantar en la parcerla " , i, "? responda 1 para plantar o 2 para pasar a la siguiente parcela")
        respuesta=int(input())
        if respuesta ==1:
         listaparcelas[i-1][0]=int(input("Ingrese 1 para ff, 2 para aloe vera y 3 para hngos."))
         if listaparcelas[i-1][0]==1: #falta comprobar si tiene plata para jugar
                monedastotal-=10
         elif listaparcelas[i-1][0]==2:
                monedastotal-=1
         elif listaparcelas[i-1][0]==3:
                monedastotal-=5
                
    return monedastotal,listaparcelas
  
    
#acá empieza el programa principal

#El cultivo 0 sin cultivo, 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#Los tipos de estado son: 0 muerto, vacío o cosechado y 1 creciendo.
#rendimiento va a tener como valores 1 cuando es mínimo, 2 cuando es medio y 3 para el máximo
#En la listab tenemos en la posición 0 el tipo de cultivo, 1 el estado del cultivo, 2 la cantidad de lluvia del cultivo, 3 el crecimiento del cultivo, 4 turnos sin crecer

tipodecultivo=0
estado=0
cantidaddelluvia=0
crecimiento=0
nocrecimiento=0
monedastotal=84
monedast=0

listab=[tipodecultivo, estado, cantidaddelluvia, crecimiento, nocrecimiento] #elementos que hay en cada parcela (lista2)
listaparcelas=[]
for i in range (1,17):
    listaparcelas.append(listab)#lista4
random=funciondevuelveclima(i) #random con los datos del archivo de clima (lista1)
funcionclima=clima(random,listaparcelas)
funcioncosecha=cosecha(listaparcelas) #lista6
#falta plantar (listas de parcelas[j-1]=listab)


for i in range (1,25):

    monedasturno=0
    for j in range (1,17):
        #apuesta
        monedast,listaparcelas=apuesta(monedastotal,listaparcelas)
        #controlparcelas
        funcionclima=clima(random,listaparcelas[j-1])
        funcioncosecha=cosecha(listaparcelas[j-1])
        
        print(listaparcelas)
        
        #reemplazo valores en la lista de cada parcela
        if ((funcioncosecha[1]==1) or (funcioncosecha[0]!=0)):
            listaparcelas[j-1]=listab
        
        else:
            listaparcelas[j-1][1]=1
            listaparcelas[j-1][2]+=funcionclima[2]
            listaparcelas[j-1][3]+=funcionclima[0]
            listaparcelas[j-1][4]+=funcionclima[1]
         
        monedasturno+=ganancia(listaparcelas[j-1],funcioncosecha)
    monedast+=monedasturno
            
            
main()           
            

            
            
