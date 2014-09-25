#!/usr/bin/env python

# An Introduction to Interactive Programming in Python
# Quiz 01

import math

print "Question 2"
p = True
q = True
print not (p or not q)

p = True
q = False
print not (p or not q)

p = False
q = True
print not (p or not q)

p = False
q = False
print not (p or not q)

print "\n________________"
print "Question 4"
n = 123
print ((n - n % 10) / 10) % 10
print (n % 100 - n % 10) / 10
print (n - n % 10) / 10

print "_____________"
print "Question 5"
#f(x) = -5 x^5 + 69 x^2 - 47

def my_fun (x):
    return (-5 * (x ** 5) + 69 * (x ** 2) - 47)

print "f(0): ", my_fun(0) 
print "f(1): ", my_fun(1) 
print "f(2): ", my_fun(2) 
print "f(3): ", my_fun(3) 

print "_____________"
print "Question 6"
#FV = PV (1+rate)^periods
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    return present_value * ((1 + rate_per_period) ** periods)

print "$1000 at 2% compounded daily for 3 years yields $", 
future_value(1000, .02, 365, 3)

print "$500 at 4% compounded weekly for 10 years yields $",
future_value(500, .04, 10, 10)
                                                                        
print "\n_____________"
print "Question 7"
#Area of a polygon = ¼ n s^2 / tan(π/n).

def poly_area(sides, length):
    return ( (1.0/4.0) * sides * (length ** 2.0) ) / (math.tan(math.pi/sides))

print "polygon with 5 sides, each of length 7 inches, has area ", 
poly_area(5, 7)    

print "polygon with 7 sides each of length 3 inches, has area ", 
poly_area(7,3)
                                                                        
print "\n________________"
print "Question 8"

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))
print "max of 20, -15 and 55 is: ", max_of_3 (20,-12,55)

print "________________"
print "Question 9"
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = (distance / dist_to_origin)
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)


                                                                        