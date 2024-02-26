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
#  <b>GRASP: Creator</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 GRASP Creator.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_160_grasp_creator.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Use Case "Spiel initialisieren"
# - Bisher:
#   - `World`- und `Location`-Klassen
#   - Attribute und Getter
# - Frage:
#   - Wer erzeugt die `Location`-Instanzen?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Kandidaten

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <code>Player</code></li>
# <li> <code>Game</code></li>
# <li> <code>Pawn</code></li>
# <li> <code>Location</code></li>
# <li> <code>World</code></li>
# </ul>
# </div>
# <img src="img/adv-domain-03-small.svg"
#      style="float:right;margin:auto;width:70%"/>

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Das Creator Pattern (GRASP)
#
# ### Frage
#
# - Wer ist verantwortlich für die Erzeugung eines Objekts?
#
# ### Antwort
#
# Klasse `A` bekommt die Verantwortung, ein Objekt der Klasse `B` zu erzeugen,
# wenn eine oder mehrere der folgenden Bedingungen zutreffen:
#
# - `A` enthält `B` (oder ist Eigentümer von `B`)
# - `A` verwaltet `B` (registriert, zeichnet auf)
# - `A` verwendet `B` intensiv
# - `A` hat die initialisierenden Daten, die `B` benötigt


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Bemerkung
#
# - Factory ist oft eine Alternative zu Creator

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Creator

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <strike><code>Player</code></strike></li>
# <li> <strike><code>Game</code></strike></li>
# <li> <code>Pawn</code></li>
# <li> <code>Location</code></li>
# <li> <b><code>World</code></b></li>
# </ul>
# </div>
# <img src="img/adv-domain-03-small.svg"
#      style="float:right;margin:auto;width:70%"/>


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass
import json
from pathlib import Path


# %% tags=["keep"]
@dataclass
class Location:
    name: str
    description: str

    @classmethod
    def from_description(cls, description: dict) -> "Location":
        return cls(description["name"], description.get("description", ""))


# %% tags=["keep"]
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    @classmethod
    def from_location_descriptions(cls, location_descriptions: list[dict]) -> "World":
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        return cls(locations, initial_location_name)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können die die `World`-Klasse jetzt verwenden.

# %%
world = World.from_location_descriptions(simple_locations)

# %%
world
