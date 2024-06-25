'''
Helpers for the Vector Manipulation Software
-PaiShoFish49
'''

from pygame import Vector2

class Color():
    COLOR_TYPE = list[int, int, int, int]

    @staticmethod
    def validateColor(color: COLOR_TYPE) -> COLOR_TYPE:
        return [int(max(0, min(i, 255))) for i in color]

    @staticmethod
    def newColor(red: int, green: int, blue: int, alpha: int) -> COLOR_TYPE:
        returnColor = [red, green, blue, alpha]
        returnColor = Color.validateColor(returnColor)

        return returnColor

    @staticmethod
    def interpolate(color1: COLOR_TYPE, color2: COLOR_TYPE, t: float = 0.5) -> COLOR_TYPE:
        t = float(max(min(t, 1), 0))

        red = int(color1[0] + (t * (color2[0] - color1[0])))
        green = int(color1[0] + (t * (color2[0] - color1[0])))
        blue = int(color1[0] + (t * (color2[0] - color1[0])))
        alpha = int(color1[0] + (t * (color2[0] - color1[0])))

        return Color.validateColor([red, green, blue, alpha])

    @staticmethod
    def getChannel(color: COLOR_TYPE, channel : str | int) -> int:
        if type(channel) is str:
            channel = channel.lower()

            if channel in 'rgba':
                return color[{'r':0, 'g':1, 'b':2, 'a':3}[channel]]

        else:
            return color[channel]

    @staticmethod
    def modifyChannel(color: COLOR_TYPE, channel: str | int, value: int) -> COLOR_TYPE:
        if type(channel) is str:
            channel = channel.lower()
            returnColor = color.copy()

            if channel in 'rgba':
                returnColor[{'r':0, 'g':1, 'b':2, 'a':3}[channel]] = value

        else:
            returnColor[channel] = value

        return Color.validateColor(returnColor)

class Node():
    def __init__(self, position: list[float, float]) -> None:
        self.aligned = False
        self.symmetrical = False
        self.vector = Vector2(position)

class Handle():
    def __init__(self, position: list[float, float]) -> None:
        self.vector: Vector2 = Vector2(position)

class Path():
    def __init__(self, nodeStart: Node, nodeEnd: Node, handles: list[Handle]) -> None:
        self.nodeStart = nodeStart
        self.nodeEnd = nodeEnd
        self.handles = handles

    def addHandle(self, handle: Handle, index: int = None) -> None:
        if index == None:
            self.handles.append(handle)

        else:
            self.handles.insert(index, handle)

    def getNodeAndHandlePoints(self) -> list[Vector2]:
        return [self.nodeStart.vector, *[i.vector for i in self.handles], self.nodeEnd.vector]

    def getPoints(self, resolution: int, includeEnd: bool = False) -> list[Vector2]:
        if self.handles != []:
            points: list[Vector2] = [self.nodeStart.vector]

            for i in range(resolution):
                t: float = (i + 1)/(resolution + 1)
                lerpList: list[Vector2] = [self.nodeStart.vector, *[j.vector for j in self.handles], self.nodeEnd.vector]

                while len(lerpList) > 1:
                    newLerpList = []
                    for k in range(len(lerpList) - 1):
                        newLerpList.append(lerpList[k].lerp(lerpList[k+1], t))
                    lerpList = newLerpList

                points.append(lerpList[0])

            if includeEnd: points.append(self.nodeEnd.vector)
            return points

        else:
            return [self.nodeStart.vector, self.nodeEnd.vector]

    def getLines(self, resolution: int) -> list[tuple[Vector2, Vector2]]:
        points: list[Vector2] = self.getPoints(resolution, True)
        lines: list[tuple[Vector2, Vector2]] = []

        for i in range(len(points) - 1):
            lines.append((points[i], points[i+1]))

        return lines

class Curve():
    def __init__(self, paths: list[Path]) -> None:
        self.paths: list[Path] = paths

class Shape():
    def __init__(
            self,
            strokeColorRGBA: Color.COLOR_TYPE = Color.newColor(0, 0, 0, 255),
            strokeWidthUnits: float = 1.0,
            fillColorRGBA: Color.COLOR_TYPE = Color.newColor(255, 255, 255, 255),
            outlineColorRGBA: Color.COLOR_TYPE = Color.newColor(255, 255, 255, 255),
            outlineWidthUnits: float = 0.0
        ) -> None:

        self.strokeColorRGBA: Color.COLOR_TYPE = strokeColorRGBA
        self.strokeWidthUnits: float = strokeWidthUnits

        self.fillColorRGBA: Color.COLOR_TYPE = fillColorRGBA

        self.outlineColorRGBA: Color.COLOR_TYPE = outlineColorRGBA
        self.outlineWidthUnits: float = outlineWidthUnits

class Circle(Shape):
    def __init__(self, radius: float, position: list[float, float]) -> None:
        super().__init__()
        self.radiusUnits: float = radius
        self.vector: Vector2 = Vector2(radius)

class Rectangle(Shape):
    def __init__(self, TLPoint, isSquare = False) -> None:
        super().__init__()
        self.topLeftCorner: Vector2 = TLPoint
        self.isSquare: bool = isSquare

class Drawing(Shape):
    def __init__(self, curves: list[Curve]) -> None:
        super().__init__()
        self.curves: list[Curve] = curves