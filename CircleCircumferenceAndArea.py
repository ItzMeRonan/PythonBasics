# Write a new program that displays the area and the circumference of a circle given the radius.

def Circle():
	radius = 2.5
	area = 22/7 * (radius ** 2)
	circumference = (2 * 22/7) * radius

	print("Radius of the circle = " + str(radius))
	print("Area of the circle = " + str(area))
	print("Circumference of the circle = " + str(circumference))

Circle()