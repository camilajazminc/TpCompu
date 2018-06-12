#El cultivo 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#rendimiento va a tener como valores 1 cuando es mínimo, 2 cuando es medio y 3 para el máximo
#En la lista2 tenemos en la posición 0 el tipo de cultivo, 1 el estado del cultivo, 2 la cantidad de lluvia del cultivo, 3 el crecimiento del cultivo, 4 turnos sin crecer

#PANTALLA

#eventype para el mouse.nap devuelve el click

import sys, pygame
from pygame.locals import* 

WIDTH=600
HEIGHT=400
Color=(25, 255, 100)

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
    
    #botones seleccion de cultivos
    
    pygame.draw.rect(screen, (100,100,100), (500, 50, 50, 50), 0)
    pygame.draw.rect(screen, (100,100,100), (500, 150, 50, 50), 0)
    pygame.draw.rect(screen, (100,100,100), (500, 250, 50, 50), 0)
    
    pygame.display.flip()
    
    
    while True:  
        for eventos in pygame.event.get():   
            if eventos.type == QUIT: 
                sys.exit(0)    

lista1=[] #random con los datos del archivo de clima
lista2=[] #elementos que hay en cada parcela

def clima (lista1,lista2):
    crece=0
    nocrece=0
    lluvia=0
  if ((lista1[3]>=a)and (lista1[3]<=b)): #CATASTROFENATURAL
    crece=0
  else:
    if lista2[0]==1 : 
        if (((lista1[0]>=9)and(lista1[0]<=25)) and ((lista1[1]<=112)and(lista1[1]>=34)) and (lista1[2]<=30)):
            crece+=1
            lluvia+=lista1[1]
        else:
            nocrece += 1
            
    elif lista2[0]==2 :
        if (((lista1[0]>=1)and(lista1[0]<=40)) and (lista1[2]<=100)):
            crece+=1
            lluvia+=lista1[1]
        else:
            nocrece+=1
            
    elif lista2[0]==3:
        if (((lista1[0]>=6)and(lista1[0]<=30)) and ((lista1[1]<=200)and(lista1[1]>=34)) and (lista1[2]<=80)):
            crece+=1
            lluvia+=lista1[1]
        else:
            nocrece += 1
                
    lista3=[crece, nocrece, lluvia]
            
    return (lista3)

lista4=clima(lista1,lista2)

def cosecha (lista2,lista4):
   cosechar=0
   rendimiento=0
   muere=0
   if lista2[0]==1 : 
        if lista4[1]<=2:
            if lista4[0]==9: #cosecho
               cosechar=1
               if (lista4[2]>=300 and lista4[2]<=600):
                   rendimiento=1
               elif (lista4[2]>600 and lista4[2]<=800):
                   rendimiento=2
               elif (lista4[2]>800 and lista4[2]<=1000):
                   rendimiento=3
            elif lista4[0]<9:
                rendimiento=0
        else:
            muere=1
    
    if lista2[0]==2 : 
        if lista4[1]<=2:
            if lista4[0]==1: #cosecho
               cosechar=1
               if lista4[2]<=100:
                   rendimiento=1
               elif (lista4[2]>100 and lista4[2]<=300):
                   rendimiento=2
               elif lista4[2]>300 :
                   rendimiento=3
            elif lista4[0]<1:
                rendimiento=0
        else:
            muere=1
   
   if lista2[0]==3 : 
        if lista4[1]<=2:
            if lista4[0]==5: #cosecho
               cosechar=1
               if (lista4[2]>=100 and lista4[2]<=400):
                   rendimiento=1
               elif (lista4[2]>400 and lista4[2]<=500):
                   rendimiento=2
               elif (lista4[2]>500 and lista4[2]<=600):
                   rendimiento=3
            elif lista4[0]<5:
                rendimiento=0
        else:
            muere=1
    lista5=[rendimiento, muere]
    return(lista5)
            
            
main()           
            
            
            

            
            
