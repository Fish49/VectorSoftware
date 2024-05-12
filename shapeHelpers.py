'''
Helpers for the Vector Manipulation Software
-PaiShoFish49
'''

from pygame import Vector2

class Color():
    COLOR_TYPE = list[int, int, int, int]

    @staticmethod
    def newColor(red : int, green : int, blue : int, alpha : int):
        #snaps channel values to acceptable values. snaps to range 0-255, and ensures that its an integer.
        red = int(max(min(red, 255), 0))
        green = int(max(min(green, 255), 0))
        blue = int(max(min(blue, 255), 0))
        alpha = int(max(min(alpha, 255), 0))

        return [red, green, blue, alpha]

    @staticmethod
    def interpolate(color1 : list[int, int, int, int], color2 : list[int, int, int, int], t : float = 0.5):
        t = float(max(min(t, 1), 0))

        red = int(color1[0] + (t * (color2[0] - color1[0])))
        green = int(color1[0] + (t * (color2[0] - color1[0])))
        blue = int(color1[0] + (t * (color2[0] - color1[0])))
        alpha = int(color1[0] + (t * (color2[0] - color1[0])))

        return [red, green, blue, alpha]

    @staticmethod
    def getChannel(color : list[int, int, int, int], channel : str | int):
        if type(channel) is str:
            channel = channel.lower()

            if channel in 'rgba':
                return color[{'r':0, 'g':1, 'b':2, 'a':3}[channel]]

        else:
            return color[channel]

class Node():
    def __init__(self, position : list[float, float]) -> None:
        self.aligned = False
        self.symmetrical = False
        self.vector = Vector2(position)

class Handle():
    def __init__(self, position : list[float, float]) -> None:
        self.vector : Vector2 = Vector2(position)

class Shape():
    def __init__(
            self, 
            strokeColorRGBA : Color.COLOR_TYPE = Color.newColor(0, 0, 0, 255), 
            strokeWidthUnits : float = 1.0,
            fillColorRGBA : Color.COLOR_TYPE = Color.newColor(255, 255, 255, 255), 
            outlineColorRGBA : Color.COLOR_TYPE = Color.newColor(255, 255, 255, 255),
            outlineWidthUnits : float = 0.0
        ) -> None:
        self.strokeColorRGBA : Color.COLOR_TYPE = strokeColorRGBA
        self.strokeWidthUnits : float = strokeWidthUnits

        self.fillColorRGBA : Color.COLOR_TYPE = fillColorRGBA

        self.outlineColorRGBA : Color.COLOR_TYPE = outlineColorRGBA
        self.outlineWidthUnits : float = outlineWidthUnits

class Circle(Shape):
    def __init__(self, radius : float, position: list[float, float]) -> None:
        super().__init__()
        self.radiusUnits : float = radius
        self.vector : Vector2 = Vector2(radius)

class Rectangle(Shape):
    def __init__(self, TLPoint, isSquare = False) -> None:
        super().__init__()
        self.topLeftCorner: Vector2 = TLPoint
        self.isSquare: bool = isSquare

class Curve(Shape):
    def __init__(self) -> None:
        super().__init__()