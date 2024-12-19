###############################################################################
#       						Cone.py
###############################################################################

# This example creates a polygonal model of a Cone e visualize the results in a
# VTK render window.
# The program creates the cone, rotates it 360º and closes
# The pipeline  source -> mapper -> actor -> renderer  is typical 
# and can be found in most VTK programs

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

class vtkMyCallback(object):
    def __init__(self, renderer,actor):
        self.actor=actor
        self.ren = renderer

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        print(caller.GetClassName(), 'Event Id:', ev)
        # Now print the camera position.
        print("Camera Position: %f, %f, %f" % (self.ren.GetActiveCamera().GetPosition()[0],self.ren.GetActiveCamera().GetPosition()[1],self.ren.GetActiveCamera().GetPosition()[2]))
        self.actor.SetPosition(self.ren.GetActiveCamera().GetPosition())
# Callback for the interaction

def main():

    # We Create an instance of vtkConeSource and set some of its
    # properties. The instance of vtkConeSource "cone" is part of a
    # visualization pipeline (it is a source process object); it produces data
    # (output type is vtkPolyData) which other filters may process.
    
    coneSource = vtkConeSource()
    sphereSource = vtkSphereSource()
    sphereSource.SetRadius(1.0)
    coneSource.SetHeight(0.4)  
    coneSource.SetRadius(0.2)

    pointSource=vtkSphereSource()
    pointSource.SetRadius(0.05)
    pointMapper=vtkPolyDataMapper()
    pointMapper.SetInputConnection(pointSource.GetOutputPort())
    pointActor=vtkActor()
    pointActor.SetMapper(pointMapper)



    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection( sphereSource.GetOutputPort() )
    
    # We create an instance of vtkPolyDataMapper to map the polygonal data
    # into graphics primitives. We connect the output of the cone source 
    # to the input of this mapper.
    glyph = vtkGlyph3D()
    glyph.SetSourceConnection(coneSource.GetOutputPort())
    glyph.SetInputConnection(sphereSource.GetOutputPort())


    glyph.SetVectorModeToUseNormal()
    glyph.SetScaleFactor(1)


    glyphMapper=vtkPolyDataMapper()
    glyphMapper.SetInputConnection(glyph.GetOutputPort())

    # We create an actor to represent the cone. The actor orchestrates rendering
    # of the mapper's graphics primitives. An actor also refers to properties
    # via a vtkProperty instance, and includes an internal transformation
    # matrix. We set this actor's mapper to be coneMapper which we created
    # above.
  
    glyphActor = vtkActor()
    glyphActor.SetMapper(glyphMapper)

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    # Create the Renderer and assign actors to it. A renderer is like a
    # viewport. It is part or all of a window on the screen and it is
    # responsible for drawing the actors it has.  We also set the background
    # color here.
    ren = vtkRenderer()

    ren.AddActor( pointActor )
    ren.SetBackground(1.0, 0.55, 0.41)
    
    # Finally we create the render window which will show up on the screen.
    # We put our renderer into the render window using AddRenderer. We also
    # set the size to be 300 pixels by 300.
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(640, 480)
    renWin.SetWindowName('Glyph')

    
    # Adds a render window interactor to the cone example to
    # enable user interaction (e.g. to rotate the scene)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    myPicker = vtkPointPicker()
    iren.SetPicker(myPicker)
    
    mo1 = vtkMyCallback(ren,pointActor)  # Pass the renderer, not the picker
    myPicker.AddObserver(vtkCommand.EndPickEvent ,mo1)

    
    # Create and set up the picker before starting the interactor
    

    # Create the callback

    # Associate the callback with the interactor, not the picker
    iren.AddObserver(vtkCommand.LeftButtonPressEvent, mo1)

    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()