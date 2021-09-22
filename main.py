#solve the quadratic equation ax**2 + bx + c = 0

#import complex math module
import cmath

a = 1
b = 5
c = 6

print("Let's start with an example. ax^2 + bx + c where a = 1, b=5, and c=6.")

# calculate the discriminant

d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt((d))/2*a)

sol2 = (-b+cmath.sqrt((d))/2*a)

print('The solutions are {0} and {1} '.format(sol1,sol2))

a1 = int(input("Now, you enter an integer for a:"))

b1 = int(input("Please pick an integer for b: "))

c1 = int(input("Please pick an integer for c: "))

d1 = (b1**2) - (4*a1*c1)

# find two solutions
sol3 = (-b1-cmath.sqrt((d1))/2*a1)

sol4 = (-b1+cmath.sqrt((d1))/2*a1)

print('The solutions are {0} and {1} '.format(sol3,sol4))


#consider using a loop 


#modified from https://www.programiz.com/python-programming/examples/quadratic-roots