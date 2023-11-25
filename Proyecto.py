import arcade
import random


# Cargar tiles
tile_size = 32
# Texturas
dirt_texture = arcade.load_texture("tierra.jpg")
grass_texture = arcade.load_texture("pasto.png")
water_texture = arcade.load_texture("agua.jpg")
snow_texture = arcade.load_texture("nieve.png")
sand_texture = arcade.load_texture("arena.png")

# Animales
cebra_texture = arcade.load_texture("cebra.png")
leon_texture = arcade.load_texture("leon.png")

# Crear la matriz del mapa
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
]


# Definición de clases
class Organismo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.energia = 50
        self.velocidad = 1

    def mover(self):
        # Lógica de movimiento
        pass

    def reproducir(self, pareja):
        # Lógica de reproducción
        pass


class Animal(Organismo):
    def __init__(self, x, y, especie, dieta):
        super().__init__(x, y)
        self.especie = especie
        self.dieta = dieta

    def cazar(self, presa):
        # Lógica de caza
        pass

    def mover_aleatoriamente(self):
        nueva_x = self.x + random.choice([-1, 0, 1])
        nueva_y = self.y + random.choice([-1, 0, 1])

        # Verifica si la nueva posición está dentro de los límites del mapa
        if 0 <= nueva_x < len(ecosistema.matriz_espacial) and 0 <= nueva_y < len(
            ecosistema.matriz_espacial[0]
        ):
            # Mueve el animal a la nueva posición
            ecosistema.matriz_espacial[self.x][self.y] = None
            self.x = nueva_x
            self.y = nueva_y
            ecosistema.matriz_espacial[self.x][self.y] = self


class Planta(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y)

    def fotosintesis(self):
        # Lógica de fotosíntesis
        pass


class Ambiente:
    def __init__(self):
        # Lógica para inicializar el ambiente
        pass


class Ecosistema:
    def __init__(self, filas, columnas):
        self.matriz_espacial = [[None for _ in range(columnas)] for _ in range(filas)]
        self.iniciar_ecosistema()

    def asignar_biomas(self):
        biomas = {
            0: "Tierra",
            1: "Pasto",
            2: "Agua",
            3: "Nieve",
            4: "Arena"
            # Agrega más tipos de biomas según sea necesario
        }

        for fila in range(len(self.matriz_espacial)):
            for columna in range(len(self.matriz_espacial[0])):
                tipo_bioma = biomas[mapa[fila][columna]]
                self.matriz_espacial[fila][columna] = tipo_bioma

    def iniciar_ecosistema(self):
        # Lógica para inicializar el ecosistema
        animal1 = Animal(5, 5, "leon", "carnivoro")
        animal2 = Animal(8, 8, "Cebra", "Herbívoro")
        self.matriz_espacial[animal1.x][animal1.y] = animal1
        self.matriz_espacial[animal2.x][animal2.y] = animal2

        # Lógica para inicializar el ecosistema

    def ciclo_vida_reproduccion(self):
        for fila in range(len(self.matriz_espacial)):
            for columna in range(len(self.matriz_espacial[0])):
                organismo = self.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    organismo.mover_aleatoriamente()

    def cadena_alimenticia(self):
        # Lógica de la cadena alimenticia
        pass

    def actualizar_ecosistema(self):
        # Lógica para actualizar el estado del ecosistema en cada ciclo
        pass


class EcosistemaVisual(arcade.Window):
    def __init__(self, ecosistema):
        super().__init__(800, 600, "Simulador de Ecosistema")
        self.ecosistema = ecosistema

    def on_draw(self):
        arcade.start_render()
        self.draw_map()

    def draw_map(self):
        for fila in range(len(mapa)):
            for columna in range(len(mapa[0])):
                if mapa[fila][columna] == 0:
                    texture = dirt_texture
                elif mapa[fila][columna] == 1:
                    texture = grass_texture
                elif mapa[fila][columna] == 2:
                    texture = water_texture
                elif mapa[fila][columna] == 3:
                    texture = snow_texture
                elif mapa[fila][columna] == 4:
                    texture = sand_texture

                x = columna * tile_size
                y = fila * tile_size
                arcade.draw_texture_rectangle(
                    x + tile_size / 2,
                    y + tile_size / 2,
                    tile_size,
                    tile_size,
                    texture,
                    0,
                )
                # Dibujar textura del animal si hay uno en esa posición
                organismo = self.ecosistema.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    if organismo.especie == "leon":
                        texture = leon_texture
                    elif organismo.especie == "Cebra":
                        texture = cebra_texture
                    arcade.draw_texture_rectangle(
                        x + tile_size / 2,
                        y + tile_size / 2,
                        tile_size,
                        tile_size,
                        texture,
                        0,
                    )


# Ejecutar el simulador
ecosistema = Ecosistema(20, 25)
app = EcosistemaVisual(ecosistema)
arcade.run()
