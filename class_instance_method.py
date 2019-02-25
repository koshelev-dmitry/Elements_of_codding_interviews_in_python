import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return (f"Pizza({self.radius!r})"
                f"{self.ingredients!r}")
    
    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
    


print(Pizza.quatre_fromage())