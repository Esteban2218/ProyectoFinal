class Ajustes:
    def __init__(self):

        self.fps=30
        self.anchura  =840
        self.altura = 650
        self.fondo = "C:/Users/LENOVO/Documents/SOFTWARE/Algoritmos y estructura de Datos/Proyecto finalTK/TANK-2024-NIVELES-UNIDOS-main/TANK_2024/Menu/suelo.jpg"
        



        #Balas 
        self.velocidadBala = 1
        self.anchuraBala = 3
        self.alturaBala = 14
        self.colorBala = (11,255,255)
        self.balasPermitidas = 10



        #Enemigo 
        self.velocidadEnemigo = 1
        self.velocidadBalaEnemiga =1.5
        self.probabilidadDisparo = 1
        self.probabilidadEnviarEnemigo = 1


        self.enemigosQuePuedenHuir = 10
        self.vidaJugador = 5