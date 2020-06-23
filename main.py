import sys, pygame
from setting import Setting
from model import Model
from view_model import ColorPointView


def main():
    pygame.init()
    setting = Setting()
    screen: pygame.Surface = pygame.display.set_mode(setting.SCREEN_SIZE)
    #print(type(screen))
    pygame.display.set_caption('Color Point')
    clock = pygame.time.Clock()
    color_point_view = ColorPointView(setting)


    running = True
    # Цикл игры
    while running:
        # Держим цикл на правильной скорости
        clock.tick(setting.FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        color_point_view.cells.update()

        # Рендеринг
        screen.fill(setting.WHITE)
        color_point_view.cells.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    sys.exit(main())
