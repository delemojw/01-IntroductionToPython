"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jabari-Aman Delemore.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
# ----------------------------------------------------------------------
# Red Turtle
# ----------------------------------------------------------------------
shuri = rg.SimpleTurtle('turtle')
shuri.pen = rg.Pen('yellow', 30)
shuri.speed = 40

shuri.forward(200)
shuri.right(250)
shuri.forward(90)
shuri.left(50)
shuri.backward(200)

flash = rg.SimpleTurtle('turtle')
flash.pen = rg.Pen('black', 50)
flash.speed = 40

flash.right(90)
flash.forward(100)
flash.left(90)
flash.forward(400)
flash.left(90)
flash.forward(250)
flash.left(90)
flash.forward(400)
flash.left(90)
flash.forward(150)
print('fastest man alive')
###############################################################################
# Done: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
window.close_on_mouse_click()