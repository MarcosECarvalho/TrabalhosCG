from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

quadros = 0
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )


def desenha():
    global quadros
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    raio = 1
    base = 100
    theta = (2 * math.pi) / base  
    coordTopo = []
    coordBase = []

    glPushMatrix()

    glRotatef(quadros, 0.0, 1.0, 0.0)
    glColor3fv(cores[0])
    glTranslatef(0, -0.5, -0.5)
    glRotatef(-45, 1.0, 0.0, 0.0)

    glBegin(GL_POLYGON)
    for i in range(0, base):
        x = raio*math.cos(i*theta)
        y = raio*math.sin(i*theta)
        coordBase += [(x, y)]
        glVertex3f(x, y, 2.0)  
    glEnd()

    glBegin(GL_POLYGON)
    for i in range(0, base):
        x = raio*math.cos(i*theta)
        y = raio*math.sin(i*theta)
        coordTopo += [(x, y)]
        glVertex3f(x, y, 0.0)  
    glEnd()

    glBegin(GL_QUAD_STRIP) 
    for i in range(0, base):
        glColor3fv(cores[(i + 1) % len(cores)])
        glVertex3f(coordTopo[i][0], coordTopo[i][1], 0.0) 
        glVertex3f(coordTopo[(i + 1) % base][0], coordTopo[(i + 1) % base][1], 0.0)
        glVertex3f(coordBase[i][0], coordBase[i][1], 2.0)
        glVertex3f(coordBase[(i + 1) % base][0], coordBase[(i + 1) % base][1],2.0)
    glEnd()

    glPopMatrix()
    quadros += 1
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(30,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CILINDRO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-5)
glutTimerFunc(30,timer,1)
glutMainLoop()