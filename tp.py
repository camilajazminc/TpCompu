#El cultivo 1 son las frutas finas, 2 el aloe vera y 3 los hongos
#EL orden de la lista 1 es= temperatura, lluvia, viento, desastre natural
#crece va a tener como valores 0 cuando no crece, 1 cuando crece el mínimo, 2 cuando tiene crecimiento medio y 3 para el crecimiento máximo
#En la lista2 tenemos en la posición 1 el tipo de cultivo, 2 el estado del cultivo, 3 la cantidad de lluvia del cultivo, 4 el crecimiento del cultivo, 5 turnos sin crecer

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
    lluvia=0
    if lista2[1]==1 :
        if (((lista1[1]>=17)and(lista1[1]<=25)) and ((lista1[2]<=112)and(lista1[2]>=34)) and (lista1[3]<=30)):
            crece=3
            lluvia+=lista1[2]
        elif  (((lista1[1]>=12)and(lista1[1]<=16)) and ((lista1[2]<=112)and(lista1[2]>=34)) and (lista1[3]<=30)):
            crece=2
            lluvia+=lista1[2]
        elif  (((lista1[1]>=9)and(lista1[1]<=11)) and ((lista1[2]<=112)and(lista1[2]>=34)) and (lista1[3]<=30)):
            crece=1
            lluvia+=lista1[2]
        else:
            crece = 0
            lluvia+=lista1[2]
    elif lista2[1]==2 :
        if (((lista1[1]>=10)and(lista1[1]<=40)) and (lista1[3]<=100)):
            crece=3
            lluvia+=lista1[2]
        elif (((lista1[1]>=1)and(lista1[1]<=10)) and (lista1[3]<=100)):
            crece=2
            lluvia+=lista1[2]
        elif ((lista1[1]<=1) and (lista1[3]<=100)):
            crece=1
            lluvia+=lista1[2]
        else:
            crece=0
            lluvia+=lista1[2]
    elif lista2[1]==3:
        if (((lista1[1]>=16)and(lista1[1]<=30)) and ((lista1[2]<=200)and(lista1[2]>=34)) and (lista1[3]<=80)):
            crece=3
            lluvia+=lista1[2]
        elif  (((lista1[1]>=12)and(lista1[1]<=15)) and ((lista1[2]<=200)and(lista1[2]>=34)) and (lista1[3]<=80)):
            crece=2
            lluvia+=lista1[2]
        elif  (((lista1[1]>=6)and(lista1[1]<=11)) and ((lista1[2]<=200)and(lista1[2]>=34)) and (lista1[3]<=80)):
            crece=1
            lluvia+=lista1[2]
        else:
            crece = 0
            lluvia+=lista1[2]
    
    lista3=[crece,lluvia]
            
    return (lista3)
            
            
main()           
            
            
            

            
            
