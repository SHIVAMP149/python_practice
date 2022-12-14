class circle():
    def init(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius)**2
    def perimeter(self):
        return 2*3.14*self.radius
a = int(input("Enter the radius of the circle: "))
obj = circle(a)
print("Area of circle: ",obj.area())
print("perimeter of circle: ",obj.perimeter())

print()
