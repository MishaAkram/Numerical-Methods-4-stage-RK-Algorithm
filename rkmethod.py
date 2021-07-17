# Python program to implement Runge Kutta method
def dydx(x, y):
    return (18 * x + 1.33 * y) / (1.33 * x + 18 * y)


# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h, Q=0.5, w=0.5, c1=1, c2=2, c3=3, c4=1):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0) / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + Q * h, y + w * k1)
        k3 = h * dydx(x0 + Q * h, y + w * k2)
        k4 = h * dydx(x0 + h, y + k3)
        print("i=", i, " k1 ", k1, " k2 ", k2, " k3 ", k3, " k4 ", k4)
        # Update next value of y
        y = y + (1.0 / (c1 + c2 + c3 + c4)) * (c1 * k1 + c2 * k2 + c3 * k3 + c4 * k4)
        print(y)
        # Update next value of x
        x0 = x0 + h
    return y


def rmse(a, b):
    return (((b - a) ** 2) / 2) ** (1 / 2)


# Driver method
x0 = 0
y = 18 / 1.33
x = 18
h = 0.5
a = rungeKutta(x0, y, x, h)
b = rungeKutta(x0, y, x, h, 0.2, 0.2)
print("The value of y at x is:", a)
print("The value of y at x is:", b)
print(rmse(a, b))


