def capiyalize_and_ascii_sum(word: str):
    return sum(ord(x) for x in word.capitalize())

animals =['dog', 'cat' ,'cow']

### normal way
#animal_output = []
#
#for animal in animals:
#    asci_value = capiyalize_and_ascii_sum(animal)
#    animal_output.append(asci_value)        
#
#print(animal_output)


## using map
animal_output = list(map(capiyalize_and_ascii_sum, animals))
print(animal_output)


###  square 

numbers = [1, 2, 3, 4, 5]

square = map(lambda x: x ** 2, numbers)
print(list(square))


