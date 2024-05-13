'''
Helpers for the Vector Manipulation Software
-PaiShoFish49
'''

from pygame import Vector2

class Color():
    COLOR_TYPE = list[int, int, int, int]

    @staticmethod
    def validateColor(color : COLOR_TYPE):
        return [int(max(0, min(i, 255))) for i in color]

    @staticmethod
    def newColor(red : int, green : int, blue : int, alpha : int):
        returnColor = [red, green, blue, alpha]
        returnColor = Color.validateColor(returnColor)

        return returnColor

    @staticmethod
    def interpolate(color1 : COLOR_TYPE, color2 : COLOR_TYPE, t : float = 0.5):
        t = float(max(min(t, 1), 0))

        red = int(color1[0] + (t * (color2[0] - color1[0])))
        green = int(color1[0] + (t * (color2[0] - color1[0])))
        blue = int(color1[0] + (t * (color2[0] - color1[0])))
        alpha = int(color1[0] + (t * (color2[0] - color1[0])))

        return Color.validateColor([red, green, blue, alpha])

    @staticmethod
    def getChannel(color : COLOR_TYPE, channel : str | int):
        if type(channel) is str:
            channel = channel.lower()

            if channel in 'rgba':
                return color[{'r':0, 'g':1, 'b':2, 'a':3}[channel]]

        else:
            return color[channel]

    @staticmethod
    def modifyChannel(color : COLOR_TYPE, channel : str | int, value : int):
        if type(channel) is str:
            channel = channel.lower()
            returnColor = color.copy()

            if channel in 'rgba':
                returnColor[{'r':0, 'g':1, 'b':2, 'a':3}[channel]] = value

        else:
            returnColor[channel] = value

        return Color.validateColor(returnColor)

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