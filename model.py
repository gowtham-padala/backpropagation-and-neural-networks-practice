class Result:
    
    def __init__(self, data, children=(), operation=''):
        self.data = data
        self.prev  = set(children)
        self.operation = operation

    def __repr__(self):
        return f"Result(data={self.data})"

    def __add__(self, var):
        return Result(self.data + var.data, (self, var), '+')

    def __mul__(self, var):
        return Result(self.data * var.data, (self, var), '*')


x = Result(10.0)
y = Result(3.0)

z = x + y

# This should print out x and y values
print(z.prev)