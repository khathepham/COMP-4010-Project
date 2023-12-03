from enum import Enum


class Tier(Enum):
    AboveOU = 0
    OU = 1
    BelowOU = 2


class Type(Enum):
    NoType = 0
    Normal = 1
    Fire = 2
    Water = 3
    Grass = 4
    Electric = 5
    Ice = 6
    Fighting = 7
    Poison = 8
    Ground = 9
    Flying = 10
    Psychic = 11
    Bug = 12
    Rock = 13
    Ghost = 14
    Dragon = 15
    Dark = 16
    Steel = 17
    Fairy = 18


class Category(Enum):
    NoCat = 0
    Physical = 1
    Special = 2
    Status = 3


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.stats = Stats()
        self.moves = {}
        self.abilities = {}
        self.primary_type = Type.NoType
        self.secondary_type = Type.NoType

    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return other.name == self.name
        return NotImplemented

    def __str__(self):
        ostr = f"Name: {self.name}\n"
        ostr += f"Abilities:\n"

        sorted_abilities = sorted(self.abilities.items(), key=lambda x: x[1]["usage"], reverse=True)
        for a, v in sorted_abilities:
            ostr += f"\t{a}: {v['usage']:.2%}\n"

        ostr += f"Moves:\n"

        sorted_moves = sorted(self.moves.items(), key=lambda x: x[1]["usage"], reverse=True)
        for m, v in sorted_moves:
            ostr += f"\t{m}: {v['usage']:.2%}\n"

        return ostr

    def toJSON(self):
        obj = {"name": "name", "stats": self.stats.toDict()}
        moves = {}
        for movename, val in self.moves.items():
            moves[movename] = val["usage"]
        obj["moves"] = moves

        abilities = {}
        for abilityname, val in self.abilities.items():
            abilities[abilityname] = val["usage"]

        obj["primaryType"] = self.primary_type.name

        if self.secondary_type != Type.NoType:
            obj["secondaryType"] = self.primary_type.name

        return obj


class Stats:
    def __init__(self):
        self.attack = 0
        self.defense = 0
        self.spattack = 0
        self.spdefense = 0
        self.speed = 0
        self.hp = 0

    def toDict(self):
        return {
            "attack": self.attack,
            "defense": self.defense,
            "spattack": self.spattack,
            "spdefence": self.spdefense,
            "speed": self.speed,
            "hp": self.hp
        }


class Move:
    ALL_MOVES = []

    def __init__(self, name):
        if self.get_move(name) is None:
            self.name = name
            self.power = 0
            self.effect = ""
            self.type = Type.NoType
            self.category = Category.NoCat
            self.chance = 0

    def __str__(self):
        return self.name

    @classmethod
    def get_move(cls, name):
        for m in cls.ALL_MOVES:
            if m.name == name:
                return m
        return None


class Ability:
    ALL_ABILITIES = []

    def __init__(self, name):
        if self.get_ability(name) is None:
            self.name = name
            self.description = ""
            self.ALL_ABILITIES.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def get_ability(cls, name: str):
        for a in cls.ALL_ABILITIES:
            if a.name == name:
                return a
        return None
