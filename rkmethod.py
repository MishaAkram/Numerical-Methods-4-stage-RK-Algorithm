import matplotlib.pyplot as plt
# Python program to implement Runge Kutta method
def dydx(x, y):
    return (18 * x + 1.33 * y) / (1.33 * x + 18 * y)

def dydx1(x, y):
    return (x *1.33 * y**2)


# Finds value of y for a given x using step size h
# and initial value y0 at x0.

def rungeKutta(x0, y0, x, h, Q1=0.5,Q2=0.5, w1=0.5,w2=0.5, c1=1, c2=2, c3=2, c4=1):
    # Count number of iterations using step size or
    # step height h
    m=[]
    n = (int)((x - x0) / h)
    # Iterate for number of iterations.
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + Q1 * h, y + w1 * k1)
        k3 = h * dydx(x0 + Q2 * h, y + w2 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        # print("i=", i, " k1 ", k1, " k2 ", k2, " k3 ", k3, " k4 ", k4)
        # Update next value of y
        y = y + (1.0 / (c1 + c2 + c3 + c4)) * (c1 * k1 + c2 * k2 + c3 * k3 + c4 * k4)
        # print(y)
        m.append(y)
        # Update next value of x
        x0 = x0 + h
    # print(len(m))
    return m


def rmse(a, b):
    sum=0
    for i,j in zip(a,b): 
       v=(i-j) ** 2
       sum+=v
    mean=(sum/len(a))**(1/2)
    return mean;
       


# Driver method
x0 = 0
y = 18 / 1.33
x = 18
h = 0.5
# a = rungeKutta(x0, y, x, h)
# b = rungeKutta(x0, y, x, h,0.4)
# c=rmse(a,b)

# print("a=" ,a)
# print("b=" ,b)
# print("c=" ,c)
# a = rungeKutta(x0, y, x, 0.0001)
# b = rungeKutta(x0, y, x,h , 0.2, 0.2,1,1,1,3)
# print("The value of y at x is:",a)
# print("The value of y at x is:", b)
# print(rmse(a, b))

#reducing errors by using modifying values of w,q,ci
# n = [h,h/2,h/4,h/8,h/16]
def compare():
    List=[]
    a=rungeKutta(x0, y, x, h)
    for i in range(1,11):
       b=rungeKutta(x0, y, x, h,0.8,0.5,0.8,0.4,2,3,4,0)
       c=rmse(b,a)
    #    print("a = ",a)
    #    print("b = ",b)
    #    print("c = ",c)
       List.append(c)
    print(List)
    e=rungeKutta(x0,y,x,h,0.6,(List.index(min(List))+1)/10)
    print("e = ",e)
    print("minimum error",min(List),List.index(min(List))+1)
    return List
def calc():
    a=rungeKutta(x0, y, x, h)
    b=rungeKutta(x0, y, x, h,0.6,0.9,2,1,1,2)
    c=rmse(b,a)
    print("error" ,c)
# calc()
compare()
# importing the required module
  
# x axis valueszzx
y = compare()
# corresponding y axis values
  
# plotting the points 
plt.plot([h/16,h/8,h/4,h/2,h], y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('Error Analysis Graph!')
  
# function to show the plot
plt.show()