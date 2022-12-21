class Circle:
    def _init_(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
    def perimeter(self):
        return 2*3.14*self.radius
a = int(input("Enter the radius of the circle: "))
<<<<<<< HEAD
ar = Circle(a)
pr = Circle(a)
=======
ar = circle(a)
pr = circle(a)
>>>>>>> b5211b02bcb62a77801fb316aaa04cb9847e5830
print("Area of circle: ",ar.area())
print("perimeter of circle: ",pr.perimeter())

print()

