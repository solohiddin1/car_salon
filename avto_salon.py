import json
import os

class Salon:
    def __init__(self, name, location, phone_number):
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.balance = 0

    def salon_info(self):
        return f"Salon Name: {self.name}\nLocation: {self.location}\nPhone Number: {self.phone_number}"

    def salon_balance(self, borrowed_cars=[]):
        self.balance = sum(float(car['cost']) for car in borrowed_cars)
        return self.balance

class Car:
    def __init__(self, name, year, model, manufacturer, color, cost):
        self.name = name
        self.year = year
        self.model = model
        self.manufacturer = manufacturer
        self.color = color
        self.cost = cost

    def car_info(self):
        return {
            "name": self.name,
            "year": self.year,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "color": self.color,
            "cost": self.cost
        }

class Customer:
    def __init__(self, name, phone_number, balance=0):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance

    def customer_info(self):
        return {
            "name": self.name,
            "phone_number": self.phone_number,
            "balance": self.balance
        }

    def purchase(self, car_name):
        car_exists = False
        for car in car_info_from_json:
            if car_name == car['name']:
                car_exists = True
                price = float(car['cost'])
                if self.balance >= price:
                    self.balance -= price
                    print(f'Congratulations! You have purchased the {car["name"]} car for {car["cost"]}$.'
                          f'\nYour remaining balance is {self.balance}$.')
                    return True
                else:
                    print('Insufficient balance.')
                    return False
        if not car_exists:
            print('This car is not available!')
        return False

    def remove_car(self, car_name, car_list):
        self.car_name = car_name
        self.car_list = car_list

        new_list = [car for car in self.car_list if car['name'] != self.car_name]
        
        if len(new_list) < len(self.car_list):
            with open('car_info.json', 'w') as js:
                json.dump(new_list, js, ensure_ascii=False, indent=4)
            print('Car sold.')
        else:
            print(f"{self.car_name} not found.")
        return new_list

salon = Salon("Auto Salon", "Tashkent", "+998932543733")

def read_json(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as json_file:
            return json.load(json_file)
    return []

car_info_from_json = read_json('car_info.json')

while True:
    choice = input('Press 1 if you are an Admin --> \n'
                   'Press 2 if you are a Customer -->\n'
                   'Press 3 to Exit --> \n')
    
    if choice == '1':
        while True:
            admin_choice = input('1: View Car Information 1 -> \n'
                                 '2: View Salon Information 2 -> \n'
                                 '3: Add New Car 3 -> \n'
                                 '4: Exit -> 4: -> ')
            if admin_choice == '1':
                print("\nCar Information:\n")
                for car in car_info_from_json:
                    print(f"Car Name: {car['name']}\nYear: {car['year']}\nModel: {car['model']}\nManufacturer: {car['manufacturer']}\nColor: {car['color']}\nPrice: {car['cost']}\n")
            elif admin_choice == '2':
                print(salon.salon_info())
                print('Salon Balance = ', salon.salon_balance(car_info_from_json), '$')
            elif admin_choice == '3':
                name = input('Enter new car name: ')
                year = input('Year = ')
                model = input('Model: ')
                manufacturer = input('Manufacturer: ')
                color = input('Color: ')
                while True:
                    cost = input('Price = ')
                    try:
                        cost = int(cost)
                        break
                    except ValueError:
                        print('Please enter a number for the price!')
                new_car = Car(name, year, model, manufacturer, color, cost)
                car_info_from_json.append(new_car.car_info())
                print(f"{name} car added.")
            elif admin_choice == '4':
                break
            else:
                print('Invalid command!')
    elif choice == '2':
        while True:
            customer_choice = input('Press 1 to View Cars -> \n' \
                                    'Press 2 to Purchase a Car -> \n' \
                                    'Press 3 to Exit -> ')
            if customer_choice == '1':
                print("\nAvailable Car Information:\n")
                for car in car_info_from_json:
                    print(f"Car Name: {car['name']}\nYear: {car['year']}\nModel: {car['model']}\nManufacturer: {car['manufacturer']}\nColor: {car['color']}\nPrice: {car['cost']}\n")
            elif customer_choice == '2':
                name = input('Enter your name -> ')
                phone = input('Enter your phone number -> ')
                while True:
                    balance = input('Enter your balance -> ')
                    try:
                        balance = float(balance)
                        break
                    except ValueError:
                        print('Please enter a number for the balance!')
                car_name = input('Enter the car name -> ')
                customer = Customer(name, phone, balance)
                purchase_success = customer.purchase(car_name)
                if purchase_success:
                    car_info_from_json = customer.remove_car(car_name, car_info_from_json)
                    print('Thank you for your purchase!')
                else:
                    print('Please try again!')
            elif customer_choice == '3':
                break
            else:
                print('Invalid command!')
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid selection! Please try again.")

with open('car_info.json', 'w') as json_file:
    json.dump(car_info_from_json, json_file, ensure_ascii=False, indent=4)

print("Car information has been written to 'car_info.json'.")