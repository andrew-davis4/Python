import math
from os import system

def to_radians(deg):
    return (deg*math.pi)/180
def solve_d_x(d_y, v, theta):
    v_x = v*math.cos(theta)
    v_y = v*math.sin(theta)
    discriminant = (v_y**2)-(4*-4.905*-d_y)
   
    t_1 = (-v_y-math.sqrt(discriminant))/-9.81

    return t_1*v_x

def solve_d_y(d_x, v, theta):
    v_x = v*math.cos(theta)
    v_y = v*math.sin(theta)

    d_y = ((((-9.81*d_x)/v_x)+v_y)**2-(v_y**2))/-19.62

    return d_y



#solving for displacement in x

system("cls") #clear terminal



d_y = int(input("Elevation gain(+)/loss(-): "))
v = int(input("Initial Speed: "))
angle = int(input("Angle of launch: "))

system("cls")

print(solve_d_x(d_y, v, to_radians(angle)))




