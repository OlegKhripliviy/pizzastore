from datetime import datetime

from pizzastore.items.check_line import CheckLine


class Check:
    def __init__(self, check_number):
        self.check_number = check_number
        self.lines = []
        self.date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def add_line(self, line: CheckLine):
        self.lines.append(line)

    def print_pizzas(self):
        total_price = 0

        check_text = f'\nCheck № {self.check_number}'
        check_text += f' {self.date:^40}\n'
        check_text += f'{40*"-"}\n'
        if len(self.lines) == 0:
            print("Check has been deleted\n")
        else:
            for item in self.lines:
                check_text += f'{item}\n'
                total_price += item.pizza.price * item.quantity
            check_text += f'{40*"-"}\n'
            check_text += f'Total {len(self.lines)} positions, total price = {total_price} UAH'
            print(check_text)






