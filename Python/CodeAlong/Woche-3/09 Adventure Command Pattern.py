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
#  <b>Adventure: Command Pattern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Adventure Command Pattern.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_380_adventure_commands.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Letzter Stand: Spielfiguren mit Enumeration
#
# <img src="img/adventure-v3b-overview.svg" alt="Adventure Version 3b"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Probleme
#
# - Signatur von `Pawn.perform()` ist nicht sehr klar
#   - Verschiedene Aktionen benötigen verschiedene Parameter
#   - In Python können wir das mit `*args` und `**kwargs` umgehen
# - Open-Closed Prinzip verletzt
#   - Neue Aktionen benötigen Änderungen an `Pawn` und `Action`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Lösung: Command Pattern
#
# - Aktionen werden in eigene Klassen ausgelagert
# - `Pawn.perform()` nimmt ein `Action`-Objekt
# - Die zur Ausführung der Aktion benötigten Daten werden im `Action`-Objekt
#   gespeichert
# - `Action`-Objekte können zusätzliche Funktion zur Verfügung stellen, z.B.
#    Texte für das UI bereitstellen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 3c: Command Pattern
#
# <img src="img/adventure-v3c-overview.svg" alt="Adventure Version 3c"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Vorteile
#
# - Open-Closed Prinzip wird eingehalten
# - `Pawn.perform()` hat eine klare Signatur
# - `Action`-Klassen können zusätzliche Funktionen bereitstellen

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod
from dataclasses import dataclass

from location_v2 import Location


# %%


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class MoveAction(Action):
    direction: str
    target: Location

    @property
    def description(self) -> str:
        return f"move {self.direction} to {self.target.name}"

    def perform(self, instigator: "Pawn") -> None:
        instigator.location = self.target


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class SkipTurnAction(Action):
    @property
    def description(self) -> str:
        return "wait one turn"

    def perform(self, instigator: "Pawn") -> None:
        # Do nothing...
        pass


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from world_factory_v2 import WorldFactory  # noqa: E402
from simple_locations import simple_locations  # noqa: E402

# %% tags=["keep"]
world = WorldFactory.create(simple_locations)

# %% tags=["keep"]
room_1: Location = world["Room 1"]
room_2: Location = world["Room 2"]

# %% tags=["keep"]
print({d: loc.name for (d, loc) in room_1.connections.items()})

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
pawn = Pawn("Player", room_1)

# %% tags=["keep"]
print(pawn.name, "is in", pawn.location.name)

# %% tags=["keep"]
pawn.perform(MoveAction("north", room_2))

# %% tags=["keep"]
print(pawn.name, "is in", pawn.location.name)
