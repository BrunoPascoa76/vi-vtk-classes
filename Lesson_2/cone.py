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

def main():
    
    coneSource = vtkConeSource()

  
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection( coneSource.GetOutputPort() )

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)

    coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
    coneActor.GetProperty().SetDiffuse(0.7)
    coneActor.GetProperty().SetSpecular(0.4)
    coneActor.GetProperty().SetSpecularPower(20)
    coneActor.GetProperty().SetOpacity(0.5)

    property = vtkProperty()
    property.SetColor(1.0, 0.3882, 0.2784)
    property.SetOpacity(0.5)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)

    coneActor2 = vtkActor()
    coneActor2.SetMapper(coneMapper)
    coneActor2.SetPosition(-2, 0, 0)
    coneActor2.SetProperty(property)
    
    ren = vtkRenderer()
    ren.AddActor( coneActor )
    ren.SetBackground( 0.1, 0.2, 0.4 )
    ren.SetViewport(0,0,0.5,1)

    ren2=vtkRenderer()
    ren2.AddActor(coneActor2)
    ren2.SetViewport(0.5,0,1,1)
    ren2.SetBackground( 0.2, 0.3, 0.4 ) 

    cam2=ren2.GetActiveCamera()
    cam2.Azimuth(90)
   
    
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.AddRenderer(ren2)

    renWin.SetSize(600, 300)
    renWin.SetWindowName('Cone')

    for _ in range(0,360):
        renWin.Render()
        coneActor.RotateY(1)
        coneActor2.RotateY(1)


if __name__ == '__main__':
    main()