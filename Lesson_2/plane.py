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

def make_plane(source,renderer,translation,rotation,texture_location):
    transform=vtkTransform()
    transform.Translate(translation)

    transform.RotateX(rotation[0])
    transform.RotateY(rotation[1])
    transform.RotateZ(rotation[2])

    transformFilter=vtkTransformPolyDataFilter()
    transformFilter.SetInputConnection(source.GetOutputPort())
    transformFilter.SetTransform(transform)
    
    planeMapper = vtkPolyDataMapper()
    planeMapper.SetInputConnection( transformFilter.GetOutputPort() )
    planeActor = vtkActor()
    planeActor.SetMapper(planeMapper)

    reader=vtkJPEGReader()
    reader.SetFileName(texture_location)

    texture=vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())
    planeActor.SetTexture(texture)

    renderer.AddActor( planeActor )

def main():
    planeSource = vtkPlaneSource()

    ren=vtkRenderer()
    ren.SetBackground(1.0, 0.55, 0.41)

    make_plane(planeSource,ren,(0,0,0),(0,0,0),"./Lesson_2/images/Im1.jpg")
    make_plane(planeSource,ren,(0,0,1),(0,0,90),"./Lesson_2/images/Im2.jpg")
    make_plane(planeSource,ren,(0.5,0,0.5),(0,90,0),"./Lesson_2/images/Im3.jpg")
    make_plane(planeSource,ren,(-0.5,0,0.5),(0,90,0),"./Lesson_2/images/Im4.jpg")
    make_plane(planeSource,ren,(0,0.5,0.5),(90,0,0),"./Lesson_2/images/Im5.jpg")
    make_plane(planeSource,ren,(0,-0.5,0.5),(90,0,0),"./Lesson_2/images/Im6.jpg")

   
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