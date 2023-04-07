from OpenGL.GL import *  # car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

########################################################################
# Global variables
########################################################################


########################################################################

########################################################################
# Functions
########################################################################

def init():
    pass

def display():
    pass

def keyboard(key, x, y):
    global

    key = key.decode('utf-8')

    if key == 'z':
        pass
    elif key == 's':
        pass
    elif key == 'q':
        pass
    elif key == 'd':
        pass
    elif key == 'a':
        pass
    elif key == 'e':
        pass

########################################################################

########################################################################
# Main
########################################################################

if __name__ == "__main__":

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

    glutCreateWindow('Wolfenstein basique')
    glutReshapeWindow(320, 200)

    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_key)

    init()

    glutMainLoop()

########################################################################
