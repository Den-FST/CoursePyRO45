
class Person:
    def __init__(self, nume:str, varsta:int, inaltime:float, greutate:float):
        self.nume = nume
        self.varsta = varsta
        self.inaltime = inaltime
        self.greutate = greutate

    def get_name(self):
        return self.nume

    def get_age(self):
        return self.varsta

    def get_height(self):
        return self.inaltime

    def get_weight(self):
        return self.greutate

    def set_name(self, nume):
        self.nume = nume

    def set_age(self, varsta):
        self.varsta = varsta

    def set_height(self, inaltime):
        self.inaltime = inaltime

    def set_weight(self, greutate):
        self.greutate = greutate

    def bmi(self):
        greutate_m = self.greutate / 100
        inaltime_kg = self.inaltime
        print(f'{greutate_m} {inaltime_kg}')
        # x = (greutate_m / (inaltime_kg ** 2))
        x = round(greutate_m / (inaltime_kg ** 2), 10)
        return x
        # return "{:.2f}".format(x)


person = Person("Ioana", 30, 165, 65)
print(f'{person.get_name()} -- Bmi: {person.bmi()} Greutatea:  {person.get_weight()} Inaltimea:  {person.get_height()}')

