class Number():
    def __init__(self, number=0):
        self.value = float(number)

    def __str__(self):
        return "Your number = {}".format(self.value)

    def add(self, number=0):
        self.value += float(number)

    def sub(self, number=0):
        self.value -= float(number)

    def mult(self, number=1):
        self.value *= float(number)

    def div(self, number=1):
        self.value /= float(number)