from pizzastore.items.pizza import Pizza


class CheckLine:
    def __init__(self, pizza: Pizza, quantity: int, indx: int):
        self.pizza = pizza
        self.quantity = quantity
        self.indx = indx

    def __str__(self):
        return f'{self.indx}.{self.pizza.title}: {self.pizza.price} * ' \
               f'{self.quantity} = {self.pizza.price * self.quantity}'

