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
    

    reader=vtkJPEGReader()
    reader.SetFileName("./Lesson_2/images/lena.jpg")

    texture=vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    planeSource = vtkPlaneSource()
    planeSource.SetOrigin(0,0,0)
    planeSource.SetPoint1(1,0,0)
    planeSource.SetPoint2(0,1,0)

    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection( planeSource.GetOutputPort() )
    
  
    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)
    planeActor.SetTexture(texture)
    
    ren = vtkRenderer()
    ren.AddActor( planeActor )
    ren.SetBackground(1.0, 0.55, 0.41)
   
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)

    renWin.SetSize(640, 480)
    renWin.SetWindowName('Cone')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    iren.Initialize()
    iren.Start()


if __name__ == '__main__':
    main()