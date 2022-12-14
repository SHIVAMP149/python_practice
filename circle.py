class circle():
    def init(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius)**2
    def perimeter(self):
        return 2*3.14*self.radius
a = int(input("Enter the radius of the circle: "))
ar = circle(a)
pr = circle(a)
print("Area of circle: ",ar.area())
print("perimeter of circle: ",pr.perimeter())

print()
