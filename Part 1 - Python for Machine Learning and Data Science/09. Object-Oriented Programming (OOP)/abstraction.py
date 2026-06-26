class Abstraction:
    # This is constructor.
    
    def __init__(self):
        self.__y = 3

m = Abstraction()
# show error
# print(m.y)

# no error
print(m._Abstraction__y) # display private variable y



