import math
x1 = input("Enter x for the first point")
y1 = input("Enter y for the first point")
perimeter = 0
while True:

	x2 = raw_input("Enter the value of x")
	if x2 == ' ':
		break;
	y2 = raw_input("Enter the value of y")
	x2 = int(x2)
	y2 = int(y2)
	dx = x2 - x1
	dy = y2 - y1
	d = math.sqrt((dx ** 2) + (dy ** 2))
	perimeter = perimeter + d
	x1 = x2
	y1 = y2
print "The perimeter of the polygon is", perimeter