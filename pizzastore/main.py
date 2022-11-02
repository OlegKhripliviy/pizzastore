from pizzastore.items.pizzastore import PizzaStore
import os


def menu_print():
    print('\nWelcome to the pizzeria.\n0 - Exit\n1 - Print all pizzas'
          '\n2 - Random pizza\n3 - Filter by price\n4 - Update check\n5 - Add new pizza')


def main(pizza_store):
    while True:
        menu_print()
        c = input('Your choice: ')
        match c:
            case '0':
                break
            case '1':
                pizza_store.print_all_pizzas()
            case '2':
                pizza_store.random_pizza(pizzas_file)
            case '3':
                clients_money = input('Enter amount limit: ')
                print(pizza_store.budget_pizza(clients_money))
            case '4':
                pizza_store.update_check()
            case '5':
                pizza_store.new_pizza(pizzas_file)
            case _:
                print('Wrong choice! Try again please')
    print('Bye!')


if __name__ == '__main__':
    direct = os.getcwd()
    pizzas_file = f'{direct}/pizzas.csv'
    quotes_file = f'{direct}/quotes.csv'
    ps = PizzaStore(pizzas_file, quotes_file)
    main(ps)
