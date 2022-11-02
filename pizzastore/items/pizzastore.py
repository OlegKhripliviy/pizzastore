import csv
from random import choice, sample, randint

from pizzastore.items.check import Check
from pizzastore.items.check_line import CheckLine
from pizzastore.exeption import MyException
from pizzastore.items.pizza import Pizza


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PizzaStore(metaclass=SingletonMeta):
    def __init__(self, filename_pizza, filename_quotes):
        self.pizzas = self.read_pizzas(filename_pizza)
        self.quotes = self.read_quotes(filename_quotes)
        self.n_check = 0
        self.checks = []
        self.check_num = None

    @staticmethod
    def read_pizzas(filename_pizza):
        pizza_li = []
        with open(filename_pizza, newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                pizza_li.append(Pizza(int(row[0]), row[1], int(row[2]), row[3]))
        return pizza_li

    @staticmethod
    def read_quotes(filename_quotes):
        quotes_li = []
        with open(filename_quotes, newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                quotes_li.append(row[0])
        return quotes_li

    def new_pizza(self, filename_pizza):
        last_idx = self.read_pizzas(filename_pizza)[-1]
        idx = last_idx.idx + 1
        title = input("Enter title: ")
        price = input("Enter price: ")
        description = input("Enter description: ")
        new_pizza_list = [idx, title, price, description]
        with open(filename_pizza, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_pizza_list)

    def add_check(self, check: Check):
        self.checks.append(check)

    def print_quotes(self):
        print(f'***{choice(self.quotes)}***')

    def random_pizza(self):
        check = Check(len(self.checks) + 1)
        rand_num_pizzas = randint(1, 5)
        what_kind_pizzas = sample(self.pizzas, rand_num_pizzas)
        count = 0
        for item in what_kind_pizzas:
            count += 1
            check.add_line(CheckLine(item, randint(1, 3), count))
        self.add_check(check)
        check.print_pizzas()
        self.print_quotes()

    def print_all_pizzas(self):
        for pizza in self.pizzas:
            print(pizza)

    def budget_pizza(self, client_money):
        x = [f'{pizza.title}: {pizza.price} UAH' for pizza in self.pizzas if pizza.price <= int(client_money)]
        try:
            if len(x) == 0:
                raise MyException('Empty list of pizzas')
            return x
        except MyException as ex:
            return f'Exception: {ex}'

    def update_check(self):
        self.check_num = int(input("Enter number check: "))
        try:
            check = self.checks[self.check_num - 1]
            Check.print_pizzas(check)
            old_pizza_num = input("\nThis is the check you want to change\nEnter pizza number to change: ")
            if int(old_pizza_num) > len(check.lines):
                print("\nNo find this pizza")
            else:
                print("Select an action: \n1 - Change pizza \n2 - Change quantity \nAny key - Back to menu\n")
                answ = input('You choice: ')

                match answ:
                    case "1":
                        pizza = self.update_pizza(check, old_pizza_num)
                        self.update_print(check, pizza, old_pizza_num)
                    case "2":
                        pizza = self.update_quantity(check, old_pizza_num)
                        self.update_print(check, pizza, old_pizza_num)
                    case _:
                        print("_" * 40)
        except IndexError as ex:
            pass
            print(f'Exception: {ex}')
        except TypeError as ex:
            print(f'Exception: {ex}')

    def update_pizza(self, check, old_pizza_num):
        new_pizza_num = int(input("Enter idx pizza from pizza list: "))
        check.lines.pop(int(old_pizza_num) - 1)
        pizza = self.pizzas[new_pizza_num - 1]
        return pizza

    def update_quantity(self, check, old_pizza_num):
        deleted_pizza = check.lines.pop(int(old_pizza_num) - 1)
        pizza = self.pizzas[deleted_pizza .pizza.idx - 1]
        return pizza

    def update_print(self, check, pizza, old_pizza_num):
        try:
            quantity = int(input("Enter quantity pizzas: "))
            if quantity <= 0:
                Check.print_pizzas(check)
            else:
                line = CheckLine(pizza, quantity, int(old_pizza_num))
                check.lines.insert(int(old_pizza_num) - 1, line)
                Check(self.check_num).add_line(line)
                check.print_pizzas()
        except ValueError as ex:
            print('Exception', ex)
