class HighHouse:
    def __init__(self, floors, concierge_name):
        self.floors = floors
        self.concierge = concierge_name

    def change_concierge(self, new_concierge):
        self.concierge = new_concierge


if __name__ == '__main__':
    Mayak = HighHouse(50, 'Зинаида')
    print(Mayak.__dict__)
    Mayak.change_concierge('Августин')
    print(Mayak.__dict__)
