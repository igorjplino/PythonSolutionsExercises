print("""
Had we implemented the scale function (page 25) as follows, does it work
properly?
      
def scale(data, factor):
    for val in data:
    val = factor
      
Explain why or why not""")
print()
print("""
The implementation dos not work.
val is a local identifier, it's a copy of the element in the list data
and does not change the original""")