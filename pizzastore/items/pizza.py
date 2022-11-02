class Pizza:

    def __init__(self, idx, title, price, description):
        self.idx = idx
        self.title = title
        self.price = price
        self.description = description

    def __str__(self):
        return f'{self.idx}. {self.title}, price:{self.price} UAH, {self.description}'
