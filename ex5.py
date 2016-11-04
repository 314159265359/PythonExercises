# 1 inch = 2.54 centimeters
# 1 kg = 2.2 lbs

name = 'Da Boss'
age = 25.0 #maybe?
height = 1000.0 #inches
weight = 108.0 #lbs
eyes = 'Midnight'
teeth = 'Sharp'
hair = 'Curly'

height_meters = height * 2.54 / 100.0
weight_kilos = weight / 2.2

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "That's %d meters." % height_meters
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She weighs %d kilos." %weight_kilos 
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the atmosphere." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
