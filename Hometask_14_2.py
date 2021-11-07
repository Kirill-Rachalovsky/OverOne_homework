from Hometask_14_1 import Dog as Dog_v1


class Dog(Dog_v1):
    def rename(self, new_name):
        self.name = new_name

if __name__ == '__main__':
    Watson = Dog('Corgi', 15, 'Watson', 2)

    print(Watson.__dict__)
    Watson.rename('Sherlock')
    print(Watson.__dict__)

