# Python3 code here creating class
class geeks:
    def __init__(self, name, roll):
        self.id = name
        self.roll = roll

# creating list
list = []

# appending instances to list
list.append( geeks('Akash', 2) )
list.append( geeks('Deependra', 40) )
list.append( geeks('Reaper', 44) )

for obj in list:
    print( obj.name, obj.roll, sep =' ' )

# We can also access instances attributes
# as list[0].name, list[0].roll and so on.