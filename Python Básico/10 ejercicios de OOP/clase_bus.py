"""Used the person class to add passengers to the bus class"""

class Person:
    pass


person_1 = Person()


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.passenger_list = []

    def add_passenger(self, passenger):
        """To get passengers onto the bus"""
        if self.current_passengers < self.max_passengers:
            self.current_passengers = self.current_passengers + 1
            self.passenger_list.append(passenger)

        else:
            print("El bus esta lleno")

    def less_passengers(self, passenger):
        """To let passengers off the bus"""
        self.current_passengers = self.current_passengers - 1
        self.passenger_list.remove(passenger)

    def show_passengers(self):
        """Show the number of passenger on the consol"""
        print(f"La cantidad de pasajeros es {self.current_passengers}")


transtuasa = Bus(10)
transtuasa.add_passenger(person_1)
transtuasa.show_passengers()