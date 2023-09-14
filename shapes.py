def tri_area(x,y,z):
    s=(x+y+z)/2
    A = (s*(s-x)*(s-y)*(s-z))**0.5
    return A
def right_tri_area(x,y):
    return 0.5*x*y
def sq_area(x):
    return x*x
def rec_area(x,y):
    return x*y
def cube_vol(x):
    return x*x*x
def cuboid_vol(x,y,z):
    return x*y*z
def cuboid_area(x,y,z):
    return  2 *(x*y + x*z + z*y)
def cube_area(x):
    return 6*(x**2)
def sphere_vol(r):
    return (4/3)*3.14159265*r*r*r
def sphere_area(r):
    return 4*3.14159265*r*r
def circle_area(r):
    return 3.14159265*r*r
def circumfrence(r):
    return 2*3.14159265*r
