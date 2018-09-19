#! /usr/bin/env python3


class forth_order_function():
        def __init__(self, a, b, c, d, e):
            '''
            @brief class of forth order function $$y = ax^4+bx^3+cx^2+dx+e$$
            @param a
            @param b
            @param c
            @param d
            @param e
            '''
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e

        def result(self,x):
            '''
            @brief calculate result of function apply to x
            @param x the value of function independent variable
            @retval result of function apply to x
            '''
            return self.a * x ** 4 + self.b * x ** 3 + self.c * x ** 2 + self.d * x + self.e

        def difference(self, x1, x2):
            '''
            @brief calculate difference of point(x1,y) point(x2,y)
            @param self
            @param x1 value of coordinate 1
            @param x2 value of coordinate 2
            @retval difference of point(x1,y) and point(x2,y)
            '''
            return (self.result(x1) - self.result(x2))/(x1-x2)
            
#hyper parameters
initial_x = 0.5
learning_rate = 0.01
iterations = 60

if '__main__' == __name__:
    # create a error function
    line = forth_order_function(5,0,6,0,0)
    current_x = initial_x
    previous_x = 0.51
    for _ in range(iterations):
        temp = current_x
        current_x += -learning_rate * line.difference(previous_x, current_x)
        previous_x = temp

    print("The local minimum occurs at {}.".format(current_x))

