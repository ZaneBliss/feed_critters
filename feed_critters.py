from datetime import date

class Donkey: 
    
    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Llama:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()
        self.shift = shift
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Fish:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
    def __str__(self):
        return f"{self.name} is a {self.species}"

jack = Donkey('Jack', 'Irish', 'midday', 'kibles')
tina = Llama('Tina', 'Llama', 'morning', 'bits')
bruce = Snake('Bruce', 'Copperhead')
gigi = Fish('Gigi', 'Clown')
