class Dog:
    def __init__(self, breed, weight, name, age):
        self.breed = breed
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return f'{self.breed} {self.name} is jumping!'

    def run(self):
        return f'{self.breed} {self.name} is running!'

    def bark(self):
        return f'{self.breed} {self.name} is barking!'


if __name__ == '__main__':
    Watson = Dog('Corgi', 15, 'Watson', 2)

    print(Watson.__dict__)
    print(Watson.jump())
    print(Watson.run())
    print(Watson.bark())
