#! /usr/bin/env python3

# $$y = a*x + b$$

class linear_function():
    def __init__(self, a, b):
        '''
        @brief create linear function by slope 'a' and y-intercept 'b'
        @param linear function instance
        @param a slope
        @param b y-intercept
        '''
        self.a = a
        self.b = b

    def calculate(self, coordinates):
        '''
        @brief calculate the EOS of line
        @param self line instance
        @param coordinates real points of data
        @retval the EOS of line and points
        '''
        errors = map(lambda p:(p[1] - (self.a * p[0] + self.b)) ** 2, coordinates)
        error  = sum(errors)/float(len(coordinates))
        return error


if '__main__' == __name__:
    # initialize coefficient
    line = linear_function(1,2)  
    # calculate EOS from give data
    err = line.calculate([(3,6),(6,9),(12,16)])  
    print(err)

