class Color:

    def __init__(self, rgb: tuple[int, int, int]):
        self._rgb = rgb
        self._alpha = 255

    def add_color(self, value: int):
        ...

    @property
    def rgb(self):
        return self._rgb

    @property
    def rgba(self):
        return self.rgb + (self._alpha,)

    @property
    def r(self):
        return self.rgb[0]

    @property
    def g(self):
        return self.rgb[1]

    @property
    def b(self):
        return self.rgb[2]

    @property
    def alpha(self):
        return self._alpha

    def set_alpha(self, alpha: int):
        self._alpha = alpha

    def __call__(self, *args, **kwargs):
        return self.rgb

    def __str__(self):
        return f'({self.r}, {self.g}, {self.b})'

    def __repr__(self):
        return f'({self.r}, {self.g}, {self.b})'
