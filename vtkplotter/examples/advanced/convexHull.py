"""
Create a 3D Delaunay triangulation of input points.
"""
from vtkplotter import *

spid = load(datadir+"spider.ply", c="brown")

ch = convexHull(spid.points()).alpha(0.2)

show(spid, ch, Text2D(__doc__), axes=1)
