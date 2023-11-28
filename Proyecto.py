import arcade
import random
import tkinter as tk

# Cargar tiles
tile_size = 30
# Texturas
dirt_texture = arcade.load_texture("tierra.jpg")
grass_texture = arcade.load_texture("pasto.png")
water_texture = arcade.load_texture("agua.jpg")
snow_texture = arcade.load_texture("nieve.png")
sand_texture = arcade.load_texture("arena.png")
ice_texture = arcade.load_texture("hielo.png")

# Animales
cebra_texture = arcade.load_texture("vaca.png")
leon_texture = arcade.load_texture("lobo.png")
oveja_texture = arcade.load_texture("oveja.png")

# plantas
tree_texture = arcade.load_texture("arbol.png")
Planta_texture = arcade.load_texture("planta.png")
cactus_texture = arcade.load_texture("cactus.png")

# Crear la matriz del mapa
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 0, 1, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 1, 1, 1, 0, 1, 1, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 0, 1, 1, 1, 1, 0, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 3, 2, 3, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 5, 3, 5, 5, 3, 3, 3, 3, 5, 3, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 5, 5, 3, 5, 3, 3, 3, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 5, 3, 3, 5, 3, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 3, 5, 5, 3, 3, 3, 5, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 5, 3, 3, 3, 5, 3, 3, 3, 3, 3, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [5, 5, 5, 3, 3, 3, 5, 3, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# Definición de clases
class Organismo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 100
        self.energia = 50
        self.velocidad = 1


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


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
                    print(f"El {self.especie} se mueve a ({nueva_x}, {nueva_y}).")
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
                print(
                    f"El {self.especie} se reproduce y crea una cría en ({nueva_posicion[0]}, {nueva_posicion[1]})."
                )
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

    def envejecer(self):
        # Lógica para envejecimiento de los animales
        self.vida -= 1
        if self.vida <= 0:
            ecosistema.matriz_espacial[self.x][self.y] = None
            print(f"El {self.especie} muere en ({self.x}, {self.y}).")


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


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

    def fotosintesis_diaria(self):
        # Lógica para fotosíntesis diaria de las plantas
        if self.energia < 100:
            self.fotosintesis()

    def crecimiento_diario(self):
        # Lógica para crecimiento diario de las plantas
        if self.edad < 10:
            self.crecer()

    def actualizar_estado(self):
        # Lógica para actualizar el estado de la planta en cada ciclo
        self.fotosintesis_diaria()
        self.crecimiento_diario()


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


class Ambiente:
    def __init__(self):
        # Lógica para inicializar el ambiente
        pass


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


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
            4: "Arena",
            5: "hielo"
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
        animal2 = Animal(9, 10, "vaca", "herbivoro")
        animal3 = Animal(5, 19, "oveja", "herviboro")
        animal4 = Animal(7, 17, "lobo", "carnivoro")
        animal5 = Animal(1, 9, "vaca", "herbivoro")
        animal6 = Animal(3, 9, "oveja", "herviboro")
        animal7 = Animal(9, 8, "lobo", "carnivoro")
        animal8 = Animal(2, 3, "vaca", "herbivoro")
        animal9 = Animal(4, 7, "oveja", "herviboro")
        animal10 = Animal(1, 4, "lobo", "carnivoro")
        animal11 = Animal(1, 6, "vaca", "herbivoro")
        animal12 = Animal(1, 0, "oveja", "herviboro")
        # Agrega más animales según sea necesario
        # ...
        planta1 = Planta(3, 3, "planta")
        planta2 = Planta(10, 22, "arbol")
        planta3 = Planta(5, 7, "planta")
        planta4 = Planta(11, 20, "arbol")
        planta5 = Planta(5, 2, "planta")
        planta6 = Planta(5, 11, "arbol")
        planta7 = Planta(2, 7, "planta")
        planta8 = Planta(17, 19, "arbol")
        planta9 = Planta(4, 19, "cactus")
        planta10 = Planta(5, 19, "cactus")

        # logica animales
        self.matriz_espacial[animal1.x][animal1.y] = animal1
        self.matriz_espacial[animal2.x][animal2.y] = animal2
        self.matriz_espacial[animal3.x][animal3.y] = animal3
        self.matriz_espacial[animal4.x][animal4.y] = animal4
        self.matriz_espacial[animal5.x][animal5.y] = animal5
        self.matriz_espacial[animal6.x][animal6.y] = animal6
        self.matriz_espacial[animal7.x][animal7.y] = animal7
        self.matriz_espacial[animal8.x][animal8.y] = animal8
        self.matriz_espacial[animal9.x][animal9.y] = animal9
        self.matriz_espacial[animal10.x][animal10.y] = animal10
        self.matriz_espacial[animal11.x][animal11.y] = animal11
        self.matriz_espacial[animal12.x][animal12.y] = animal12

        # logica plantas
        self.matriz_espacial[planta1.x][planta1.y] = planta1
        self.matriz_espacial[planta2.x][planta2.y] = planta2
        self.matriz_espacial[planta3.x][planta3.y] = planta3
        self.matriz_espacial[planta4.x][planta4.y] = planta4
        self.matriz_espacial[planta5.x][planta5.y] = planta5
        self.matriz_espacial[planta6.x][planta6.y] = planta6
        self.matriz_espacial[planta7.x][planta7.y] = planta7
        self.matriz_espacial[planta8.x][planta8.y] = planta8
        self.matriz_espacial[planta9.x][planta9.y] = planta9
        self.matriz_espacial[planta10.x][planta10.y] = planta10

        self.actualizar_ecosistema

    def ciclo_vida_reproduccion(self):
        for fila in range(len(self.matriz_espacial)):
            for columna in range(len(self.matriz_espacial[0])):
                organismo = self.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    organismo.mover_aleatoriamente(self)
                    pareja = self.encontrar_pareja(organismo.x, organismo.y)
                    if pareja:
                        nuevo_organismo = organismo.reproducir(pareja)
                        if nuevo_organismo:
                            self.matriz_espacial[nuevo_organismo.x][
                                nuevo_organismo.y
                            ] = nuevo_organismo

    def cadena_alimenticia(self):
        for fila in range(len(self.matriz_espacial)):
            for columna in range(len(self.matriz_espacial[0])):
                organismo = self.matriz_espacial[fila][columna]
                if isinstance(organismo, Animal):
                    presa = self.encontrar_presa(organismo.x, organismo.y)
                    if presa:
                        organismo.cazar(presa)

    def encontrar_presa(self, x, y):
        for i in range(-2, 3):
            for j in range(-2, 3):
                nueva_x, nueva_y = x + i, y + j
                if (
                    0 <= nueva_x < len(self.matriz_espacial)
                    and 0 <= nueva_y < len(self.matriz_espacial[0])
                    and isinstance(
                        self.matriz_espacial[nueva_x][nueva_y], (Planta, Animal)
                    )
                    and (nueva_x, nueva_y) != (x, y)
                ):
                    return self.matriz_espacial[nueva_x][nueva_y]
        return None

    def actualizar_ecosistema(self):
        # Lógica para actualizar el estado del ecosistema en cada ciclo
        self.cadena_alimenticia()
        self.ciclo_vida_reproduccion()


# ---------------------------------------------------------------------------------------------------------------------------------------------------#


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
                elif mapa[fila][columna] == 5:
                    texture = ice_texture

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
                    elif organismo.especie == "cactus":
                        texture = cactus_texture
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
ecosistema = Ecosistema(20, 27)
app = EcosistemaVisual(ecosistema)
arcade.run()

