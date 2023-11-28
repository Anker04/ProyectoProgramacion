import arcade
import random
import tkinter as tk

# Cargar tiles
tile_size = 32
# Texturas
dirt_texture = arcade.load_texture("tierra.jpg")
grass_texture = arcade.load_texture("pasto.png")
water_texture = arcade.load_texture("agua.jpg")
snow_texture = arcade.load_texture("nieve.png")
sand_texture = arcade.load_texture("arena.png")

# Animales
cebra_texture = arcade.load_texture("vaca.png")
leon_texture = arcade.load_texture("lobo.png")
oveja_texture = arcade.load_texture("oveja.png")

# plantas
tree_texture = arcade.load_texture("arbol.png")
Planta_texture = arcade.load_texture("planta.png")

# Crear la matriz del mapa
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
]


# Definición de clases
class Organismo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.energia = 50
        self.velocidad = 1


class Animal(Organismo):
    def __init__(self, x, y, especie, dieta):
        super().__init__(x, y)
        self.especie = especie
        self.dieta = dieta
        self.ciclos = 0
        self.velocidad = 20  # Ajusta la velocidad según tus preferencias

    def cazar(self, presa):
        if isinstance(presa, Planta):
            if self.dieta == "herbivoro":
                self.energia += presa.energia
                ecosistema.matriz_espacial[presa.x][presa.y] = None
        elif isinstance(presa, Animal):
            # Verifica si el animal es una presa y está cerca
            distancia = abs(self.x - presa.x) + abs(self.y - presa.y)
            if (
                distancia <= 1
                and presa.dieta != self.dieta
                and self.energia > presa.energia
            ):
                if self.dieta == "carnivoro":
                    # El carnívoro se come al herbívoro
                    self.energia += presa.energia
                    ecosistema.matriz_espacial[presa.x][presa.y] = None

    def mover_aleatoriamente(self, ecosistema):
        if self.ciclos % self.velocidad == 0:
            nueva_x = self.x + random.choice([-1, 0, 1])
            nueva_y = self.y + random.choice([-1, 0, 1])

            if (
                0 <= nueva_x < len(ecosistema.matriz_espacial)
                and 0 <= nueva_y < len(ecosistema.matriz_espacial[0])
                and ecosistema.matriz_espacial[nueva_x][nueva_y] != "Agua"
            ):
                organismo_en_nueva_posicion = ecosistema.matriz_espacial[nueva_x][
                    nueva_y
                ]
                if organismo_en_nueva_posicion is None:
                    ecosistema.matriz_espacial[self.x][self.y] = None
                    self.x = nueva_x
                    self.y = nueva_y
                    ecosistema.matriz_espacial[self.x][self.y] = self
                elif isinstance(organismo_en_nueva_posicion, (Planta, Animal)):
                    self.cazar(organismo_en_nueva_posicion)
        self.ciclos += 1

    def reproducir(self, pareja):
        if (
            isinstance(pareja, Animal)
            and self.especie == pareja.especie
            and self.energia > 50
            and pareja.energia > 50
        ):
            nueva_energia = (self.energia + pareja.energia) // 2
            nueva_posicion = self.encontrar_posicion_libre(self.x, self.y)
            if nueva_posicion:
                hijo = Animal(
                    nueva_posicion[0], nueva_posicion[1], self.especie, self.dieta
                )
                hijo.energia = nueva_energia
                self.energia //= 2
                pareja.energia //= 2
                return hijo

    def encontrar_posicion_libre(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_x, nueva_y = x + i, y + j
                if (
                    0 <= nueva_x < len(ecosistema.matriz_espacial)
                    and 0 <= nueva_y < len(ecosistema.matriz_espacial[0])
                    and ecosistema.matriz_espacial[nueva_x][nueva_y] is None
                ):
                    return nueva_x, nueva_y


class Planta(Organismo):
    def __init__(self, x, y, especie="planta"):
        super().__init__(x, y)
        self.especie = especie
        self.edad = 0

    def fotosintesis(self):
        # Lógica de fotosíntesis
        self.energia += 5

    def crecer(self):
        # Lógica de crecimiento
        self.edad += 1
        if self.edad >= 5:
            # La planta alcanza la madurez y puede reproducirse
            self.reproducir()

    def reproducir(self):
        # Lógica de reproducción para las plantas
        nueva_posicion = self.encontrar_posicion_libre(self.x, self.y)
        if nueva_posicion:
            nueva_planta = Planta(nueva_posicion[0], nueva_posicion[1], self.especie)
            # Las plantas jóvenes tienen más energía para empezar
            nueva_planta.energia = self.energia // 2
            self.energia //= 2
            return nueva_planta

    def encontrar_posicion_libre(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                nueva_x, nueva_y = x + i, y + j
                if (
                    0 <= nueva_x < len(ecosistema.matriz_espacial)
                    and 0 <= nueva_y < len(ecosistema.matriz_espacial[0])
                    and ecosistema.matriz_espacial[nueva_x][nueva_y] is None
                ):
                    return nueva_x, nueva_y
        return None


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
                if isinstance(self.matriz_espacial[fila][columna], Animal):
                    tipo_bioma = "Animal"
                elif isinstance(self.matriz_espacial[fila][columna], Planta):
                    tipo_bioma = "Planta"
                self.matriz_espacial[fila][columna] = tipo_bioma

    def encontrar_pareja(self, x, y):
        for i in range(-2, 3):
            for j in range(-2, 3):
                nueva_x, nueva_y = x + i, y + j
                if 0 <= nueva_x < len(
                    ecosistema.matriz_espacial
                ) and 0 <= nueva_y < len(ecosistema.matriz_espacial[0]):
                    organismo = self.matriz_espacial[nueva_x][nueva_y]
                    if isinstance(organismo, Animal) and organismo.especie == "lobo":
                        return organismo

    def iniciar_ecosistema(self):
        animal1 = Animal(5, 5, "lobo", "carnivoro")
        animal2 = Animal(8, 8, "vaca", "herbivoro")
        animal3 = Animal(5, 4, "oveja", "herviboro")
        animal4 = Animal(7, 9, "lobo", "carnivoro")
        animal5 = Animal(1, 9, "vaca", "herbivoro")
        animal6 = Animal(3, 9, "oveja", "herviboro")
        # Agrega más animales según sea necesario
        # ...
        planta1 = Planta(3, 3, "planta")
        planta2 = Planta(12, 12, "arbol")
        planta3 = Planta(5, 7, "planta")
        planta4 = Planta(10, 20, "arbol")

        # logica animales
        self.matriz_espacial[animal1.x][animal1.y] = animal1
        self.matriz_espacial[animal2.x][animal2.y] = animal2
        self.matriz_espacial[animal3.x][animal3.y] = animal3
        self.matriz_espacial[animal4.x][animal4.y] = animal4
        self.matriz_espacial[animal5.x][animal5.y] = animal5
        self.matriz_espacial[animal6.x][animal6.y] = animal6

        # logica plantas
        self.matriz_espacial[planta1.x][planta1.y] = planta1
        self.matriz_espacial[planta2.x][planta2.y] = planta2
        self.matriz_espacial[planta3.x][planta3.y] = planta3
        self.matriz_espacial[planta4.x][planta4.y] = planta4

        self.actualizar_ecosistema

    def ciclo_vida_reproduccion(self):
        for fila in range(len(self.matriz_espacial)):
            for columna in range(len(self.matriz_espacial[0])):
                organismo = self.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    organismo.mover_aleatoriamente(self)

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

    def on_update(self, delta_time):
        self.ecosistema.ciclo_vida_reproduccion()

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
                # Dibujar textura del animal o planta si hay uno en esa posición
                organismo = self.ecosistema.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    if organismo.especie == "lobo":
                        texture_animal = leon_texture
                    elif organismo.especie == "vaca":
                        texture_animal = cebra_texture
                    elif organismo.especie == "oveja":
                        texture_animal = oveja_texture
                    arcade.draw_texture_rectangle(
                        x + tile_size / 2,
                        y + tile_size / 2,
                        tile_size,
                        tile_size,
                        texture_animal,
                        0,
                    )
                elif isinstance(organismo, Planta):
                    if organismo.especie == "arbol":
                        texture = tree_texture
                    else:
                        texture = Planta_texture
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

