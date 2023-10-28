# importing pycairo
import cairo

# Creating function for make arrow shape


def arrow(context, x, y, width, height, a, b):
	context.move_to(x, y + b)
	context.line_to(x, y + height - b)
	context.line_to(x + a, y + height - b)
	context.line_to(x + a, y + height)
	context.line_to(x + width, y + height/2)
	context.line_to(x + a, y)
	context.line_to(x + a, y + b)
	context.close_path()


	# creating a SVG surface
	# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# using Context method
	context = cairo.Context(surface)

	context.set_source_rgb(0, 0, 0.5)
	# Call the function
	arrow(context, 20, 20, 150, 150, 75, 50)
	# Fill the color inside
	context.fill()

	# Call the function
	arrow(context, 220, 20, 150, 150, 50, 30)
	# Fill the color inside
	context.fill()
	# Call the function
	arrow(context, 420, 20, 150, 150, 25, 20)
	# Fill the color inside
	context.fill()
	# Call the function
	arrow(context, 70, 220, 75, 150, 0, 50)
	# Fill the color inside
	context.fill()
# stroke out the color and width property
	# context.stroke()

# printing message when file is saved
print("File Saved")
