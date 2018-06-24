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
    
    #defino un cuadradito que siga al cursor
    #class Cursor(pygame.Rect):
     #       def __init__(self):
      #          pygame.Rect.__init__(self,0,0,1,1)
       #     def update(self):
        #        self.left,self.top=pygame.mouse.get_pos()
    
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
    tipodecultivo = 0
    frutasFinas = 1
    aloeVera = 2
    hongos = 3
    nparcela = -1
    pasardeturno = 0
    while salir!=True:  
        for event in pygame.event.get():
           
           #if event.type==pygame.MOUSEBUTTONDOWN:
            #    if Cursor1.colliderect(bcultivo1.rect):
             #       tipodecultivo=1
              #  elif Cursor1.colliderect(bcultivo2.rect):
               #     tipodecultivo=2
                #elif Cursor1.colliderect(bcultivo3.rect):
                 #  tipodecultivo=3
                 
           if event.type == MOUSEBUTTONDOWN:
               mousex, mousey = pygame.mouse.get_pos()
               click=(mousex,mousey)
               acumulador.append(click)
            #if ((mousex>=500) and (mousex<=550) and (mousey>=50) and (mousey<=100)):
             #   tipodecultivo=1
            #elif ((mousex>=500) and (mousex<=550) and (mousey>=150) and (mousey<=200)):
             #   tipodecultivo=2
            #elif ((mousex>=500) and (mousex<=550) and (mousey>=250) and (mousey<=300)):
             #   tipodecultivo=3
            
           if event.type == QUIT: 
                salir=True
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
       
       #Uso del mouse
        #posx,posy=pygame.mouse.get_pos()
       # Cursor1.update()
        #pygame.draw.rect(screen, (100,0,0), (100, 100, 300, 300), 0)
        
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
        fuente1=pygame.font.Font(None,15)
        fuente2=pygame.font.Font(None,30)
        Plata=fuente2.render("Plata",0,(0,0,0))
        screen.blit(Plata,(515,330))
        
        
        if (len(acumulador)>=2):
            clickAnterior = acumulador[len(acumulador)-2]
            ultimoClick = acumulador[len(acumulador)-1]  
            
            #guardo el tipo de cultivo
            if ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 100) and (clickAnterior[1] >= 50)):
                tipodecultivo = frutasFinas
                                           
            elif ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 200) and (clickAnterior[1] >= 150)):
                tipodecultivo = aloeVera    
                    
            elif  ((clickAnterior[0] >= 500) and (clickAnterior[0] <= 550) and (clickAnterior[1] <= 300) and (clickAnterior[1] >= 250)):
                tipodecultivo = hongos
                
                 
            #guardo la parcela  
            if ((ultimoClick[0] >= 100) and (ultimoClick[0] <= 400) and (ultimoClick[1] <= 400) and (ultimoClick[1] >= 100)):
                    nparcela = unirparcelaxy(ultimoClick[0],ultimoClick[1])
                    print("parcela número", nparcela)
                    ubicacion = unirxyparcela(nparcela)
                    print(ubicacion)
            
            #combino tipo de cultivo y parcela
            if (nparcela != -1 and tipodecultivo != 0):
                if tipodecultivo == frutasFinas:
                    screen.blit(parcelaff,ubicacion)
                elif tipodecultivo == aloeVera:
                    screen.blit(parcelaa,ubicacion)
                elif tipodecultivo == hongos:
                    screen.blit(parcelah,ubicacion)
                
                print ("tipo de cultivo", tipodecultivo)
                nparcela = -1
                tipodecultivo = 0
            
            #pasar de turno
            if ((ultimoClick[0] >= 175) and (ultimoClick[0] <= 225) and (ultimoClick[1] <= 20) and (ultimoClick[1] >= 70)):
                pasardeturno = 1
                print ("pasar de turno", pasardeturno)
                screen.blit(bavanzarseleccion,(175,20))
        
        pygame.display.flip()

    pygame.quit()
main()
