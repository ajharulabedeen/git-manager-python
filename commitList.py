# Python3 code here creating class
class commit:
    def __init__(self, id, message):
        self.id = id
        self.message = message


# creating list
list = []

# appending instances to list
list.append(commit(1, 'Akash'))
list.append(commit(2, 'Deependra'))
list.append(commit(3, 'Reaper'))

for obj in list:
    print(obj.id, obj.message, sep=' ')

# We can also access instances attributes
# as list[0].name, list[0].roll and so on.
