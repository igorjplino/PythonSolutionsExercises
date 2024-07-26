from Vector import Vector

class Vector_SenqInit(Vector):
    def __init__(self, lst):
        """
        In Python, you cannot directly overload methods (including constructors) 
        like in some other programming languages (e.g., C++ or Java) 
        where you can have multiple methods with the same name but different 
        parameter types.
        """
        if isinstance(lst, int):
            super().__init__(lst)
        else:
            self.coords = lst
    