import pygame
import os
import sys
import random

WINDOW_SIZE = 750, 750
WALL_WIDTH, WALL_GAP, X_VEL, GRAVITY, JUMP_HEIGHT = 75, 220, 2, 0.16, 4.6
# WALL_WIDTH, WALL_GAP, X_VEL, GRAVITY, JUMP_HEIGHT = 75, 190, 2, 0.13, 3.65
HOLE_SIZE = 175
MIN_WALL_HEIGHT = 125
# MIN_WALL_HEIGHT = 125
PLAYER_WIDTH = PLAYER_HEIGHT = 50

WIDTH, HEIGHT = WINDOW_SIZE
FPS = 100
WALL_COLOR = 'green'
GROUND_COLOR = 'brown'
MAX_Y_VEL = 8
GROUND_HEIGHT = 50

def run_game():
    def run_life():

        # def load_level(filename):
        #     filename = "data/" + filename
        #     # читаем уровень, убирая символы перевода строки
        #     with open(filename, 'r') as mapFile:
        #         level_map = [line.strip() for line in mapFile]
        #
        #     # и подсчитываем максимальную длину
        #     max_width = max(map(len, level_map))
        #
        #     # дополняем каждую строку пустыми клетками ('.')
        #     return list(map(lambda x: x.ljust(max_width, '.'), level_map))

        class Tile(pygame.sprite.Sprite):
            def __init__(self, tile_type, pos_x, pos_y):
                super().__init__(tiles_group, all_sprites)
                if tile_type == 'wall':
                    wall_group.add(self)
                self.image = tile_images[tile_type]
                self.rect = self.image.get_rect().move(
                    PLAYER_WIDTH * pos_x, PLAYER_HEIGHT * pos_y)
                self.mask = pygame.mask.from_surface(self.image)

        class Wall(pygame.sprite.Sprite):
            def __init__(self, pos_y, length):
                super().__init__(wall_group, all_sprites)
                self.image = pygame.Surface((WALL_WIDTH, length))
                self.image.fill(WALL_COLOR)
                self.rect = self.image.get_rect()
                self.rect.x = WIDTH
                self.rect.y = pos_y
                # вычисляем маску для эффективного сравнения
                self.mask = pygame.mask.from_surface(self.image)

            def update(self):
                if self.rect.right < 0:
                    self.kill()

        def spawn_walls():
            spawn_y = random.randrange(MIN_WALL_HEIGHT, HEIGHT - MIN_WALL_HEIGHT - HOLE_SIZE)
            # spawn_y = random.choice([MIN_WALL_HEIGHT, HEIGHT - MIN_WALL_HEIGHT - HOLE_SIZE])
            Wall(-HEIGHT * 3, spawn_y + HEIGHT * 3)
            Wall(spawn_y + HOLE_SIZE, HEIGHT - spawn_y + HOLE_SIZE)


        class Ground(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(ground_group, static_group, all_sprites)
                self.image = pygame.Surface((WIDTH, GROUND_HEIGHT))
                self.image.fill(GROUND_COLOR)
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = HEIGHT - GROUND_HEIGHT
                # вычисляем маску для эффективного сравнения
                self.mask = pygame.mask.from_surface(self.image)

        class Player(pygame.sprite.Sprite):
            def __init__(self, pos_x, pos_y):
                super().__init__(player_group, all_sprites)
                self.image = player_image
                self.rect = self.image.get_rect().move(
                    pos_x, pos_y)
                self.mask = pygame.mask.from_surface(self.image)
                self.y_vel = 0

            def update(self):
                self.rect.x += X_VEL
                for i in wall_group:
                    if pygame.sprite.collide_mask(self, i):
                        life_status.set_value(False)
                for i in ground_group:
                    if pygame.sprite.collide_mask(self, i):
                        life_status.set_value(False)
                self.y_vel += GRAVITY
                # if self.y_vel > MAX_Y_VEL:
                #     self.y_vel = MAX_Y_VEL
                self.rect.y += self.y_vel

            def jump(self):
                self.y_vel = -JUMP_HEIGHT

        # def generate_level(level):
        #     new_player, x, y = None, None, None
        #     for y in range(len(level)):
        #         for x in range(len(level[y])):
        #             if level[y][x] == '#':
        #                 Tile('wall', x, y)
        #             elif level[y][x] == '@':
        #                 new_player = Player(x, y)
        #     # вернем игрока, а также размер поля в клетках
        #     return new_player, x, y

        class Camera:
            # зададим начальный сдвиг камеры
            def __init__(self):
                self.dx = 0

            # сдвинуть объект obj на смещение камеры
            def apply(self, obj):
                if obj not in static_group:
                    obj.rect.x += self.dx

            # позиционировать камеру на объекте target
            def update(self, target):
                self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 3)

        life_status = Container(True)
        tile_images = {
            'wall': load_image('box.png'),
            'empty': load_image('grass.png')
        }
        player_image = pygame.transform.scale(load_image('hero.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))

        player = None

        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        wall_group = pygame.sprite.Group()
        static_group = pygame.sprite.Group()
        ground_group = pygame.sprite.Group()


        pos = None
        # player, level_x, level_y = generate_level(load_level(map_name))
        player = Player(WIDTH // 3, HEIGHT // 2)
        camera = Camera()
        Ground()
        wall_spawn_counter = 0
        score_counter = (WIDTH * 2) // 3 + WALL_GAP + WALL_WIDTH
        score = 0
        while life_status.get_value():
            # изменяем ракурс камеры
            # внутри игрового цикла ещё один цикл
            # приёма и обработки сообщений
            for event in pygame.event.get():
                # при закрытии окна
                if event.type == pygame.QUIT:
                    run_status.set_value(False)
                    life_status.set_value(False)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player.jump()
                if event.type == pygame.KEYDOWN:
                    player.jump()
            wall_group.update()
            player.update()

            wall_spawn_counter += X_VEL
            if wall_spawn_counter >= WALL_GAP + WALL_WIDTH:
                spawn_walls()
                wall_spawn_counter = 0

            score_counter -= X_VEL
            if score_counter <= 0:
                score_counter = WALL_GAP + WALL_WIDTH
                score += 1

            camera.update(player)
            # обновляем положение всех спрайтов
            for sprite in all_sprites:
                camera.apply(sprite)
            screen.fill((255, 255, 255))
            ground_group.draw(screen)
            wall_group.draw(screen)
            player_group.draw(screen)
            font = pygame.font.Font(None, 50)
            string_rendered = font.render(f'{score}', 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            screen.blit(string_rendered, (WIDTH // 2 - intro_rect.width // 2, 10))
            clock.tick(FPS)
            pygame.display.flip()
        # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        return score

    def terminate():
        pygame.quit()

    def start_screen():
        intro_text = ["ЗАСТАВКА", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_status.set_value(False)
                    return True
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return False

    def end_screen(score):
        try:
            with open('game/high_score_encoded.txt', mode='rb') as f:
                high_score = int(encrypt1(f.read(), b'iSHdbvjhgiucascoafukywedugbqx').decode('utf-8'))
            if score > high_score:
                high_score = score
                with open('game/high_score_encoded.txt', mode='wb') as f:
                    f.write(encrypt1(str(high_score).encode('utf-8'), b'iSHdbvjhgiucascoafukywedugbqx'))
        except BaseException:
            high_score = score
            with open('game/high_score_encoded.txt', mode='wb') as f:
                f.write(encrypt1(str(high_score).encode('utf-8'), b'iSHdbvjhgiucascoafukywedugbqx'))
        intro_text = ["ИГРА ОКОНЧЕНА", "",
                      f"Ваш счёт: {score}",
                      f"Рекорд: {high_score}",
                      ""]

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        while True:
            pygame.display.flip()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    run_status.set_value(False)
                    return True
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return False

    def encrypt1(var, key):
        return bytes(a ^ b for a, b in zip(var, key))

    class Container:
        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return f'Container-{self.value}'

        def get_value(self):
            return self.value

        def copy(self):
            return Container(self.value())

        def set_value(self, value):
            self.value = value

    def load_image(name, colorkey=None):
        fullname = os.path.join('game/data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    run_status = Container(True)
    start_screen()
    while run_status.get_value():
        score = run_life()
        if not run_status.get_value():
            continue
        end_screen(score)
    terminate()


# if __name__ == "__main__":
#     run_game()
