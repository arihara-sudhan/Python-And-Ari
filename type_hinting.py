# PARAMETER TYPE HINTING
# greet is expected to get a string data
def greet(name: str):
    return "Hello, " + name
#print(greet(1)) CAUSES ERROR
print(greet("Ari"))



# RETURN TYPE HINTING
# tellsize is expected to return a integer data
def tellsize(name: str) -> int:
    return len(name)



# We can indicate optional parameters using the Optional
# type from the typing module. Additionally, we can
# indicate that a parameter can have multiple acceptable
# types using a union type
from typing import Union, Optional
def hereWeType(a : Union[float,int],b: Optional[int])-> Union[float,int]:
	if b is None:
	    return a*a/2
	return a*b/2




# We can define our own type aliases using the typing module.
# This can make our code more readable, especially when dealing
# with complex types.
from typing import List, Tuple
Coordinates = Tuple[int, int]
PointList = List[Coordinates]
def plot_points(points: PointList) -> None:
	# CODE TO PLOT
    pass



# We can also use type annotations within the function body
# to indicate the types of local variables, although
# this is less common.
def calculate_square(x: int) -> int:
    result: int = x ** 2
    return result
