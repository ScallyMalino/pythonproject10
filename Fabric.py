class Circle:
    def draw(self):
        return "circle"


class Rectangle:
    def draw(self):
        return "Rectangle"


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Errortype")


shape1 = ShapeFactory.create_shape("circle")
shape2 = ShapeFactory.create_shape("rectangle")

print(shape1.draw())
print(shape2.draw())
