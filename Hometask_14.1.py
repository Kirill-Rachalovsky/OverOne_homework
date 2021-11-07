class Dog:
    def __init__(self, breed, weight, name, age):
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f'{self.breed} {self.name} is jumping!')

    def run(self):
        print(f'{self.breed} {self.name} is running!')

    def bark(self):
        print(f'{self.breed} {self.name} is barking!')


Watson = Dog('Corgi', 15, 'Watson', 2)

print(Watson.__dict__)
Watson.jump()
Watson.run()
Watson.bark()