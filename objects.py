from dataclasses import dataclass

@dataclass
class Adjective:
    name: str
    tagline: str
    description: str
    link: str = None
    info_id: str = None

@dataclass
class Weapon:
    name: str
    tagline: str
    description: str
    image: str
    link: str
    info_id: str = None

@dataclass
class Person:
    key: str
    name: str
    emoji_id: str
    description: str
    link: str
    image: str
    weapon: Weapon = None
    adjective: str = None
    info_id: str = None

@dataclass
class Place:
    name: str
    tagline: str
    description: str
    link: str 
    image: str
    info_id: str = None

@dataclass
class Match:
    fighters: list[str]
    tagline: str
    description: str
    link: str
    rules: str
    adjectives_allowed: str
    locations_allowed: str
    weapons_allowed: str
    type: str
    place: Place = None
    info_id: str = None
