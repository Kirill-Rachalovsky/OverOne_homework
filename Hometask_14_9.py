from Hometask_14_7 import HighHouse


class SalonMixin:
    def time(self, open_time, close_time):
        print(f'Рабочее время салона: {open_time} - {close_time}')

    def manicure(self):
        pass

    def pedicure(self):
        pass


class HouseWithSalon(HighHouse, SalonMixin):
    def __init__(self, floors, concierge_name, open_time, close_time):
        super().__init__(floors, concierge_name)
        self.open_time = open_time
        self.close_time = close_time


if __name__ == '__main__':
    Elite = HouseWithSalon(50, 'Ванесса', '9:00', '20:00')
    print(Elite.__dict__)
    Elite.time(Elite.open_time, Elite.close_time)
