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
#  <b>Concrete Factory</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Concrete Factory.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_270_adventure_factory.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Adventure Game Version 2b
#
# - Zuweisung von Funktionalität zu `World` und `Location` ist sinnvoll
# - `World` ist in Gefahr ist, zu viele "Änderungsgründe" zu haben
#   - Änderungen an der Implementierung der Spiele-Welt
#   - Änderungen an den Initialisierungsdaten (z.B. XML statt JSON)
# - Können wir das vermeiden?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Concrete Factory (Simple Factory)
#
# - Einfachere Version des Abstract Factory Patterns aus dem GoF Buch
#
# ### Frage
#
# - Wer soll ein Objekt erzeugen, wenn es Umstände gibt, die gegen Creator
#   sprechen?
#   - Komplexe Logik zur Erzeugung
#   - SRP/Kohäsion
#   - Viele Parameter zur Erzeugung notwendig
#
# ### Antwort
#
# - Eine Klasse, die nur für die Erzeugung von Objekten zuständig ist
# - Diese Klassen werden oft als *Factory* bezeichnet

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
import json
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint
from typing import Any, Mapping, Sequence

# %% tags=["keep"]
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


# %% tags=["keep"]
@dataclass
class Location:
    name: str
    description: str = ""
    connections: dict[str, "Location"] = field(default_factory=dict)

    @classmethod
    def from_description(cls, data: LocationDescription) -> "Location":
        return cls(data["name"], data.get("description", ""))

    def __getitem__(self, direction: str) -> "Location | None":
        return self.connections.get(direction)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def _build_connections_for_all_locations(
    locations: dict[str, Location], location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    def __getitem__(self, location_name: str):
        return self.locations[location_name]


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Die `WorldFactory`-Klasse

# %%
@dataclass
class WorldFactory:

    @staticmethod
    def create(location_descriptions: LocationDescriptions):
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        _build_connections_for_all_locations(locations, location_descriptions)
        return World(locations, initial_location_name)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwendung der Factory

# %%
factory = WorldFactory()

# %%
world = factory.create(simple_locations)

# %%
pprint(world)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Factories sind Beispiele für das GRASP Pattern "Pure Fabrication"
# - Sie können die Kohäsion von Klassen erhöhen und ihre Komplexität reduzieren
# - Sie erhöhen aber auch die Gesamtkomplexität des Systems

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Factory im Bibliothekssystem
#
# - Sie haben in vorhergehenden Workshops den Beginn eines Bibliothekssystems
#   implementiert
# - Implementieren Sie eine Möglichkeit, die Daten Ihrer Bibliothek aus einer
#   JSON-Datei zu laden. (Legen Sie dazu eine JSON-Datei an, die strukturell
#   zu Ihrer Implementierung passt)
# - Verlagern Sie dann die Erzeugung des Bibliothekssystems in eine Factory-Klasse
