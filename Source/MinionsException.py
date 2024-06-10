class WrongMinionTypeError(Exception):
    def __init__(self):
        super().__init__('minion type must be Melee(0), Caster(1), or Seige(2)')

class PixelNotFound(Exception):
    def __init__(self):
        super().__init__('Pixel Not Found in the image')