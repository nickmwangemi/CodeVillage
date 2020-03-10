PI = 3.142
radius = float(input("Please enter the radius: "))


# Calculate area of circle


def area(radius):
    area = PI * radius * radius
    return area

# Get circumference of circle


def circumference(radius):
    circumference = (2*radius)*PI
    return circumference


print("The area is {} and circumference {}".format(
    area(radius), circumference(radius)))
