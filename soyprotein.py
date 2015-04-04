#!/usr/bin/python
import soy as s
from time import sleep

cnt = s.Client()
cnt.window.background = s.atoms.Color('black')
cnt.window.title = 'Clickable'

room = s.scenes.Scene()
room['light'] = s.bodies.Light(s.atoms.Position((0, -10, 0)))

room['cam'] = s.bodies.Camera(s.atoms.Position((0, 0, 10)))
cnt.window.append(s.widgets.Projector(room['cam']))

def clicked_body(cam, mpos, bodies):
    """return the first body that intersects with a mouse click
treats every object like a sphere: Only works with Box, Sphere, and Cylinder
cam = projected camera
mpos = mouse position at click
bodies = list of all bodies in the current scene"""
    active = []
    click_ray = cam.rotation(cam.position + s.atoms.Vector((mpos.x,mpos.y)))
    for i in bodies:
        if i.__class__.__name__ == 'Sphere':
            pass
        elif i.__class__.__name__ == 'Cylinder':
            pass
        elif i.__class__.__name__ == 'Box':
            pass
        else:
            continue

    return active[0][1]

room['spher'] = s.bodies.Sphere()
room['spher'].material = s.materials.Material()
room['spher'].position = s.atoms.Position((0,0,0))

if __name__ == '__main__' :
    while cnt.window :
        sleep(.1)
