""" 
Scribble3.py
Brett Huffman
This version adds continuous lines as long as
you hold down the mouse
"""

import pyglet
from pyglet.gl.gl import GL_LINES, glBegin, glEnd, glVertex3f
window = pyglet.window.Window(1400, 720, "Scribble", resizable=False)

# Drawing Vectors
drawing_vec = []
isDrawing = False
startPoint = None

# Handle Mouse Down
@window.event
def on_mouse_press(x, y, button, modifiers):
    global isDrawing, startPoint
    isDrawing = True
    startPoint = (x,y)

# Handle Mouse Drag
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global isDrawing, startPoint, drawing_vec
    if isDrawing == True:
        drawing_vec.append((startPoint[0], startPoint[1], x, y))
        startPoint = (x,y)


@window.event
def on_mouse_release(x, y, button, modifiers):
    global isDrawing, startPoint, drawing_vec
    isDrawing = False
    drawing_vec.append((startPoint[0], startPoint[1], x, y))

# Handle the drawing to the screen
@window.event
def on_draw():
    window.clear()
    # create a line context
    glBegin(GL_LINES)
    # create a line, x,y,z
    global drawing_vec
    if not drawing_vec == None:
        for bstart, bend, estart, eend in drawing_vec:
            glVertex3f(bstart, bend, 0.0)
            glVertex3f(estart, eend, 0.0)
    glEnd()

def update(dt):
    pass

# Main function
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()

