class Farm:
    price_sheep = 500
    price_cow = 1000
    price_chicken = 50
    price_square = 700

    def __str__(self):
        return f'Farm "{self.name}", sq: {self.square} ha, value: ${self.get_value()}'

    # This is currently incomplete:
    def __init__(self, name, square, sheep, cows, chickens):
        self.name = name
        self.square = square
        self.sheep = sheep
        self.cows = cows
        self.chickens = chickens

    def get_value(self):
        "Return money value of the farm"
        value = (
            self.sheep * Farm.price_sheep
            + self.cows * Farm.price_cow
            + self.chickens * Farm.price_chicken
            + self.square * Farm.price_square
        )
        return value

    def __eq__(self, other):
        "Return True/False if value of SELF is equal to the value of OTHER"
        return self.get_value() == other.get_value()

    def __gt__(self, other):
        "Return True/False if value of SEL is greater than the value of OTHER"
        return self.get_value() > other.get_value()


# Simple Test
farm1 = Farm("My First Farm", 400, 10, 10, 10)
farm2 = Farm("My Second Farm", 300, 40, 30, 20)

print(farm1)
print(farm2)
print(farm1 > farm2)
print(farm1 == farm2)
