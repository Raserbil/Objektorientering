class car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def get_color(self):
        print(self.color)

    def set_color(self, new_color):
        self.color = new_color

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, new_mileage):
        self.milage = new_mileage

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')
a_car.get_brand()
print("")
'''
3. 
När man gör det här bestämmer man först att ens bil är en Volvo som är blå, och har åkt 1587 mil.
Sedan Skriver man ut bilmärket.
Sen ändrar man märket på bilen.
Programmet skriver ut det nya märket, Renault.
'''

b_car = car('Toyota', 'Lila', 13806)
'''
4.
Bilen jag skapade är en lila toyota som har åkt 13806 mil
'''

a_car.get_brand()
b_car.get_brand()
print("")
'''
5. 
Detta skriver ut märkena som båda bilarna har, som är Renault och Toyota.
'''


'''
6. 
def get_color(self):
    print(self.brand)

def set_color(self, new_color):
    self.color = new_color

----------------------------------------

man kan skriva ut färgen på sin bil med:
    def get_color(self):

Man kan ändra vilken färg bilen har med:
    def set_color(self, new_color):

'''

print(f"{b_car.color}\n")
'''
7. 
Programmet skriver ut vilken färg bilen har
'''


'''
8.
def set_mileage(self, new_mileage):
    self.milage = new_mileage

----------------------------------------

Gör exakt samma sak som uppgift 6, 
bara att det har att göra med miltalet 
istället för färgen på bilen.
'''

the_mileage = a_car.get_mileage()
print(the_mileage)
print("")
'''
9. 
def get_mileage(self):
    return self.mileage

Programmet returnerar miltalet på 
bilen man väljer, och sedan skriver 
man ut miltalet på en av bilarna.
'''

c_car = car('Chevrolet', 'Orange', 8394)
d_car = car('jeep', 'Grön', 374)

my_cars = ['a_car', 'b_car', 'c_car', 'd_car']
print(my_cars)
'''
10. 
c_car och d_car finns nu, och 
en lista med alla bilar finns
'''

i = 0
while i < 4:
    my_cars[i].get_brand()
    i += 1
