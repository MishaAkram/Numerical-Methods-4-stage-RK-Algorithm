# Python program to implement Runge Kutta method
def dydx(x, y):
    return (18 * x + 1.33 * y) / (1.33 * x + 18 * y)

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0) / h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        print("i=",i," k1 ", k1, " k2 ", k2, " k3 ", k3, " k4 ", k4)
        # Update next value of y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        print (y)
        # Update next value of x
        x0 = x0 + h
    return y

# Driver method
x0 = 0
y = 18 / 1.33
x = 18
h = 2
print("The value of y at x is:", rungeKutta(x0, y, x, h))
