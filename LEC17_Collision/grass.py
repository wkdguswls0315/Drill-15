from pico2d import *
from pathlib import Path

GROUND_Y = 40


class Grass:
    def __init__(self):
        folder = Path(__file__).resolve().parent
        self.image = load_image(str(folder / 'grass.png'))
        self.ruler_image = load_image(str(folder / 'ruler.png'))

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        self.ruler_image.draw(800, 350)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, get_canvas_width(), GROUND_Y
