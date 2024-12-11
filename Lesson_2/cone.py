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
    def __init__(self, renderer):
        self.ren = renderer

    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        print(caller.GetClassName(), 'Event Id:', ev)
        # Now print the camera position.
        print("Camera Position: %f, %f, %f" % (self.ren.GetActiveCamera().GetPosition()[0],self.ren.GetActiveCamera().GetPosition()[1],self.ren.GetActiveCamera().GetPosition()[2]))
# Callback for the interaction

def main():
    
    sphereSource = vtkSphereSource()
    sphereSource.SetThetaResolution(10)
    sphereSource.SetPhiResolution(10)

  
    sphereMapper = vtkPolyDataMapper()
    sphereMapper.SetInputConnection( sphereSource.GetOutputPort() )
    
    sphereMapper2 = vtkPolyDataMapper()
    sphereMapper2.SetInputConnection( sphereSource.GetOutputPort() )

    sphereActor = vtkActor()
    sphereActor.SetMapper(sphereMapper)

    
    sphereActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    sphereActor.GetProperty().SetDiffuse(0.7)
    sphereActor.GetProperty().SetSpecular(0.4)
    sphereActor.GetProperty().SetSpecularPower(20)
    #sphereActor.GetProperty().SetOpacity(0.5)
    sphereActor.GetProperty().SetInterpolationToGouraud()


    property = vtkProperty()
    property.SetColor(1.0, 0.3882, 0.2784)
    #property.SetOpacity(0.5)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)
    property.SetInterpolationToPhong()

    sphereActor2 = vtkActor()
    sphereActor2.SetMapper(sphereMapper2)
    sphereActor2.SetPosition(-2, 0, 0)
    sphereActor2.SetProperty(property)
    
    ren = vtkRenderer()
    ren.AddActor( sphereActor )
    ren.SetBackground( 0.1, 0.2, 0.4 )
    ren.SetViewport(0,0,0.5,1)

    ren2=vtkRenderer()
    ren2.AddActor(sphereActor2)
    ren2.SetViewport(0.5,0,1,1)
    ren2.SetBackground( 0.2, 0.3, 0.4 ) 

    cam2=ren2.GetActiveCamera()
    cam2.Azimuth(90)
   
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.AddRenderer(ren2)

    renWin.SetSize(600, 300)
    renWin.SetWindowName('Cone')

    mo1 = vtkMyCallback(ren)
    ren.AddObserver(vtkCommand.AnyEvent,mo1)

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()