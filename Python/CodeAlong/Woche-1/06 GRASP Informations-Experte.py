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
#  <b>GRASP: Informations-Experte</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 GRASP Informations-Experte.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_170_grasp_info_expert.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# - Use Case "Spiel initialisieren"
# - Bisher:
#   - `World` und `Location` Klassen
#   - `World` erzeugt alle `Location` Objekte
# - Nächster Schritt:
#   - Speichern von Information über die Verbindung zwischen den `Location`
#     Objekten
#   - Hilfreich dazu: Finden von Locations anhand ihres Namens
# - Frage:
#   - Wer findet `Location` Objekte anhand ihres Namens?

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
# ## Informations-Experte (engl. "Information Expert", GRASP)
#
# ### Frage
#
# An welche Klasse sollen wir eine Verantwortung delegieren?
#
# ### Antwort
#
# An die Klasse, die die meisten Informationen hat, die für die Erfüllung der
# Verantwortung notwendig sind.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Wer ist der Informationsexperte?

# %% [markdown]
# <div style="float:left;margin:auto;padding:80px 0;width:25%">
# <ul>
# <li> <strike><code>Player</code></strike></li>
# <li> <strike><code>Game</code></strike></li>
# <li> <strike><code>Pawn</code></strike></li>
# <li> <strike><code>Location</code></strike></li>
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
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class Location:
    name: str
    description: str

    @classmethod
    def from_description(cls, description: dict) -> "Location":
        return cls(description["name"], description.get("description", ""))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def _world_from_location_descriptions(location_descriptions):
    locations = {
        data["name"]: Location.from_description(data) for data in location_descriptions
    }
    initial_location_name = location_descriptions[0]["name"]
    return World(locations, initial_location_name)


# %% tags=["start", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    @staticmethod
    def from_location_descriptions(location_descriptions: list[dict]) -> "World":
        return _world_from_location_descriptions(location_descriptions)

# %%

# %%

# %%
