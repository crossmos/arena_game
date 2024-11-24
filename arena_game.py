from random import choice, randrange, randint, uniform
from colorama import init, Fore

init(autoreset=False)

PERSON_NAMES = [
    'Frodo', 'Gandalf', 'Aragorn', 'Legolas', 'Gimli', 'Boromir', 'Samwise',
    'Peregrin', 'Meriadoc', 'Gollum', 'Sauron', 'Saruman', 'Radagast',
    'Elrond', 'Eowyn', 'Eomer', 'Eomund', 'Isildur', 'Tingol', 'Teodon'
]

THINGS_NAMES = [
    'Ring', 'Sword', 'Shield', 'Helmet', 'Armor', 'Bow', 'Crossbow', 'Dagger'
]

MAX_RANDOM_STAT = 10
HEALTH = 100
ATTACK_DAMAGE = 15
DEFENCE = 0.1


class Things():
    """Класс вещей для персонажа."""

    def __init__(self, name, health, attack_damage, defence):
        """Характеристики вещи."""
        self.name = name
        self.defence = defence
        self.health = health
        self.attack_damage = attack_damage

    def __str__(self):
        """Название вещи."""
        return f'{self.name}'


class Person():
    """Родительский класс персонажа."""

    def __init__(self, name=None):
        """Характеристики персонажа."""
        self.name = name
        self.health = HEALTH
        self.attack_damage = ATTACK_DAMAGE
        self.defence = DEFENCE
        self.things = []

    def set_things(self, things):
        """Предметы персонажа."""
        for thing in things:
            self.things.append(things)
            self.health += thing.health
            self.attack_damage += thing.attack_damage
            self.defence += thing.defence

    def damage(self, attacker):
        """Расчёт урона по персонажу персонажа."""
        attack_damage = attacker.attack_damage
        damage = round(attack_damage - attack_damage * self.defence, 2)
        self.health -= damage
        return damage

    def __str__(self):
        """Имя и характеристики персонажа."""
        return f'''{self.name},
                   {self.health},
                   {self.attack_damage},
                   {self.defence}'''


class Paladin(Person):
    """Дочерний класс персонажа (Паладин)."""

    def __init__(self, name=None):
        """Характеристики персонажа (Паладин)."""
        super().__init__(name)
        self.health *= 2
        self.defence *= 2

    def __str__(self):
        """Имя и класс персонажа."""
        return f'Паладин {self.name}'


class Warrior(Person):
    """Дочерний класс персонажа (Воин)."""

    def __init__(self, name=None):
        """Характеристики персонажа (Воин)."""
        super().__init__(name)
        self.attack_damage *= 2

    def __str__(self):
        """Имя и класс персонажа."""
        return f'Воин {self.name}'


def generate_things():
    """Создание вещей для персонажей."""
    things = [
        Things(
            name=choice(THINGS_NAMES),
            health=randrange(0, MAX_RANDOM_STAT),
            attack_damage=randrange(0, MAX_RANDOM_STAT),
            defence=round(uniform(0.01, 0.1), 2))
        for _ in range(randint(30, 60))
    ]
    return things


def generate_persons():
    """Создание персонажей."""
    persons = []
    things = generate_things()
    for _ in range(10):
        person = choice([
            Warrior(choice(PERSON_NAMES)),
            Paladin(choice(PERSON_NAMES))
        ])
        person_things = []
        for _ in range(randint(1, 4)):
            person_things.append(things.pop())
        person.set_things(person_things)
        persons.append(person)
    return persons


def main():
    """Основная логика игры."""
    persons = generate_persons()

    # Бой
    while True:
        attacker = persons.pop(randint(0, len(persons)-1))
        defender = persons.pop(randint(0, len(persons)-1))
        print(Fore.YELLOW + f'<Битва {attacker} и {defender}>', end='\n')
        while True:
            damage = defender.damage(attacker)
            print(Fore.BLUE + f'{attacker}, нанёс {damage} урона {defender}')
            if defender.health <= 0:
                persons.append(attacker)
                print(Fore.RED + f'Защитник {defender} погиб')
                print(Fore.GREEN + f'Победитель {attacker}\n')
                break
            attacker, defender = defender, attacker
        if len(persons) == 1:
            break
    print(Fore.YELLOW + f'!--------Победитель арены {attacker}--------!')


if __name__ == '__main__':
    main()
