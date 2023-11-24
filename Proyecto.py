# -*- coding: utf-8 -*-
import pyglet
import random


class MatrizEspacial:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.celdas = [[None for _ in range(width)] for _ in range(height)]

    def agregar_organismo(self, organismo, x, y):
        self.celdas[y][x] = organismo

    def remover_organismo(self, x, y):
        self.celdas[y][x] = None

    def obtener_organismo(self, x, y):
        return self.celdas[y][x]


class Ambiente:
    def __init__(self):
        # Lógica para la creación del ambiente
        pass

    def generar_evento_climatico(self):
        # Lógica para generar eventos climáticos aleatorios
        pass


class Ecosistema:
    
    def __init__(self, width, height):
        self.organismos = []
        self.ambiente = Ambiente()
        self.matriz_espacial = MatrizEspacial(width, height)
        self.eventos = []
        self.tile_map = TileMap(image_path="pasto.png", tile_width=32, tile_height=32)

    def agregar_organismo(self, organismo, x, y):
        self.organismos.append(organismo)
        self.matriz_espacial.agregar_organismo(organismo, x, y)

    def remover_organismo(self, organismo, x, y):
        self.organismos.remove(organismo)
        self.matriz_espacial.remover_organismo(x, y)

    def simular_ciclo(self, dt):
        for evento in self.eventos:
            evento.aplicar(self)
        for organismo in self.organismos:
            organismo.actualizar(dt)

    def dibujar_tile_map(self):
        self.tile_map.draw()

class TileMap:
    def __init__(self, image_path, tile_width, tile_height, matriz_espacial):
        self.image = pyglet.resource.image(image_path)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.matriz_espacial = matriz_espacial

    def draw(self):
        for row_index, row in enumerate(self.matriz_espacial.biomas):
            for col_index, bioma_id in enumerate(row):
                bioma = obtener_bioma_por_id(bioma_id)
                color = bioma.color if bioma else (255, 255, 255)  # Color predeterminado si no hay bioma definido
                x = col_index * self.tile_width
                y = row_index * self.tile_height
                self.image.get_region(x, y, self.tile_width, self.tile_height).blit(
                    x, y, width=self.tile_width, height=self.tile_height, color=color
                )


class SimuladorWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ecosistema = Ecosistema(
            width=800, height=600
        )  # Ajusta las dimensiones según tus necesidades

    def on_draw(self):
        self.clear()
        self.ecosistema.dibujar_tile_map()
        for organismo in self.ecosistema.organismos:
            organismo.dibujar()


def update(dt):
    window.ecosistema.simular_ciclo(dt)


class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

    def moverse(self):
        # Lógica para el movimiento del organismo
        pass

    def reproducirse(self, otro_organismo):
        # Lógica para la reproducción del organismo
        pass

    def morir(self):
        # Lógica para la muerte del organismo
        pass

    def actualizar(self, dt):
        # Lógica para la actualización del organismo en cada ciclo
        pass

    def dibujar(self):
        # Lógica para dibujar el organismo
        pass


class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta

    def cazar(self, presa):
        # Lógica para la caza del animal
        pass


class Planta(Organismo):
    def __init__(self, posicion, vida, energia, velocidad):
        super().__init__(posicion, vida, energia, velocidad)

    def fotosintesis(self):
        # Lógica para la fotosíntesis de la planta
        pass

    def reproducirse_por_semillas(self):
        # Lógica para la reproducción por semillas de la planta
        pass


if __name__ == "__main__":
    window = SimuladorWindow(width=800, height=600, caption="Simulador Ecológico")
    ecosistema = Ecosistema(
        width=100, height=100
    )  # Ajusta las dimensiones según tus necesidades

    # Agrega algunos organismos al ecosistema
    organismo1 = Animal(
        posicion=(10, 20),
        vida=100,
        energia=50,
        velocidad=5,
        especie="León",
        dieta="Carnívoro",
    )

    organismo2 = Planta(posicion=(50, 40), vida=50, energia=30, velocidad=2)

    ecosistema.agregar_organismo(organismo1, x=10, y=20)
    ecosistema.agregar_organismo(organismo2, x=50, y=40)

    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()
