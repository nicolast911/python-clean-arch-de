# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Version 1</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Adventure Version 1.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_150_adventure_v1.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wie fangen wir an?

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Niedrige Repräsentationslücke (Low Representational Gap)
#
# - Idee: Konzepte aus der Domäne in Code übertragen
# - Implementieren Sie ein Szenario aus einem Use Case
# - Nehmen Sie die Domänen-Konzepte als Kandidaten für die ersten Klassen her

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Use Case: "Spiel initialisieren"
# - Haupterfolgsszenario ohne Laden eines Spiels

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Domänenmodell
#
# Hier ist noch einmal der relevante Teil des Domänenmodells:

# %% [markdown]
# <img src="img/adv-domain-03-small.svg"
#      style="display:block;margin:auto;width:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Statisches Designmodell

# %% [markdown]
# <img src="img/adv-world-cd-01.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Implementierung
#
# - Ordner: `examples/GraspAdventure/src/grasp_adventure/v1`

# %% tags=["keep"]
from dataclasses import dataclass


# %%
@dataclass
class Location:
    name: str
    description: str


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Kurzer Exkurs zu Properties

# %%
class LocationWithProperties:
    def __init__(self, name: str, description: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
my_location = LocationWithProperties("My Location", "A place to be")

# %%
my_location.name

# %%
# my_location.name = "Your Location"


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Konstruktion von Location Instanzen
#
# - [Einfache Orte](./simple-locations.json)
# - [Dungeon](./dungeon-locations.json)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Es kann sein, dass der Pfad unseres Python Interpreters
#   auf ein Elternverzeichnis des gesuchten Verzeichnisses zeigt
# - Deshalb suchen wir in allen Unterverzeichnissen nach der JSON-Datei:

# %% tags=["keep"]
from pathlib import Path

json_files = Path().glob("**/simple-locations.json")
json_file = list(json_files)[0]

# %% tags=["keep"]
print(json_file.absolute())

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
import json
from pprint import pprint

# %%
with open(json_file) as file:
    simple_locations = json.load(file)

# %%
print(type(simple_locations))

# %%
pprint(simple_locations)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Erzeugen von Location Instanzen aus JSON Daten
#
# - Wir können eine statische Methode in der `Location` Klasse implementieren,
#   die eine `Location` Instanz aus einem Dictionary erzeugt
# - Eine solche Methode nennt man eine Factory-Methode
# - In Python verwenden einige wichtige Bibliotheken dafür die Namenskonvention
#   `from_...`
# - Falls es Unterklassen von `Location` geben kann, ist es besser statt einer
#   statischen Methode eine Klassenmethode zu verwenden
# - Damit können wir auch Instanzen von Unterklassen erzeugen

# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class Location:
    name: str
    description: str

    @classmethod
    def from_description(cls, description: dict) -> "Location":
        return cls(description["name"], description.get("description", ""))


# %%
Location.from_description(simple_locations[0])

# %%
[Location.from_description(description) for description in simple_locations]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Factories und Unterklassen
#
# - Klassenmethoden bekommen die Klasse, auf der sie aufgerufen werden als
#   ersten Parameter
# - Da wir in Python die Klasse verwenden, um Instanzen zu erzeugen, können wir
#   damit auch Instanzen von Unterklassen erzeugen

# %%
@dataclass
class MySpecialLocation(Location):
    pass


# %%
MySpecialLocation.from_description(simple_locations[0])


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Implementierung der World Klasse
#
# - Beliebige Anzahl von `Location`-Instanzen
# - Zugriff auf `Location`-Instanzen über Namen
# - Speicherung des initialen Ortsnamens

# %%
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

