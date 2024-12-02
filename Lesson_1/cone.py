###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical 
# and can be found in most VTK programs

# Imports

# Import all VTK modules
from vtkmodules.all import *

# Import only needed modules
# import vtkmodules.vtkInteractionStyle
# import vtkmodules.vtkRenderingOpenGL2
# from vtkmodules.vtkFiltersSources import vtkConeSource
# from vtkmodules.vtkRenderingCore import (
#     vtkActor,
#     vtkPolyDataMapper,
#     vtkRenderWindow,
#     vtkRenderWindowInteractor,
#     vtkRenderer
# )

def add_light(ren, color, position,sphereSource):
    cam=ren.GetActiveCamera()
    light = vtkLight()
    light.SetColor(color)
    light.SetFocalPoint(cam.GetFocalPoint())
    light.SetPosition(position)
    ren.AddLight(light)

    sphereMapper=vtkPolyDataMapper()
    sphereMapper.SetInputConnection( sphereSource.GetOutputPort() )
    sphereActor=vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetPosition(position)
    sphereActor.GetProperty().SetColor(color)
    sphereActor.GetProperty().LightingOff()
    ren.AddActor(sphereActor)


def main():

    # We Create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource "cone" is part of a
    # visualization pipeline (it is a source process object); it produces data
    # (output type is vtkPolyData) which other filters may process.

    cylinderSource=vtkConeSource(height=3,radius=2,resolution=10)
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(10)
    sphereSource.SetPhiResolution(10)

    cylinderMapper=vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinderSource.GetOutputPort())

    # We create an actor to represent the sphere. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be sphereMapper which we created
    # above.
    
    cylinderActor=vtkActor()
    cylinderActor.SetMapper(cylinderMapper)

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()
    ren.AddActor( cylinderActor )
    
    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300,300)

    cam=ren.GetActiveCamera()
    cam.SetPosition(0,25,0)
    cam.SetFocalPoint(0,0,0)
    cam.SetViewUp(0,0,-1)

    renWin.SetWindowName('sphere')

    add_light(ren, (1,0,0),(-5,0,0),sphereSource)
    add_light(ren, (0,0,1),(0,0,-5),sphereSource)
    add_light(ren, (0,1,0),(5,0,0),sphereSource)
    add_light(ren, (1,1,0),(0,0,5),sphereSource)
    
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()

    print(renWin.GetSize())

if __name__ == '__main__':
    main()