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
#  <b>Adventure: Strategie</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Adventure Strategie.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_400_adventure_strategy.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4a: `Player`-Klasse
#
# <img src="img/adventure-v4a.svg" alt="Adventure Version 4a"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `Player`-Klasse ist für die Strategie zuständig
# - Im Moment nur eine fest verdrahtete Strategie:
#   - Spieler nimmt immer zufälligen Eintrag in der Liste der Aktionen
# - Wir wollen mehrere Strategien unterstützen
# - Mit einer "interaktiven" Strategie wollen wir den menschlichen Spieler
#   einbinden
# - Versuchen wir eine Enumeration aller möglichen Strategien

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4b: Mehrere Strategien
#
# <img src="img/adventure-v4b.svg" alt="Adventure Version 4b"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Das Klassendiagramm sieht nicht so schlecht aus
# - Implementierung ist unübersichtlich
# - Open-Closed Prinzip ist verletzt
# - Besser: Strategie Pattern

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4c: Strategy Pattern
#
# <img src="img/adventure-v4c.svg" alt="Adventure Version 4c"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4d: Vereinfachung mit First-Class-Funktionen
#
# <img src="img/adventure-v4d.svg" alt="Adventure Version 4d"
#      style="display:block;margin:auto;height:60%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass
from random import choice
from typing import Callable

# %% tags=["keep"]
from action_v4 import Action, SkipTurnAction
from location_v4 import Location
from pawn_v4 import Pawn
from simple_locations import simple_locations
from world_factory_v4 import WorldFactory


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %% tags=["start", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class Player:
    name: str
    pawn: Pawn

    @staticmethod
    def select_action(actions: list[Action]) -> Action:
        if not actions:
            raise ValueError("No actions available")
        return choice(actions)

    def perform(self, action: Action):
        action.perform(self)

    @property
    def location(self) -> Location:
        return self.pawn.location

    @location.setter
    def location(self, value: Location):
        self.pawn.location = value

    @property
    def description(self) -> str:
        return f"{self.name} at {self.location.name}"

    def take_turn(self):
        action = self.select_action(self.actions)
        print(f"{self.description} performs: {action.description}")
        self.perform(action)

    @property
    def actions(self) -> list[Action]:
        return [*self.pawn.actions, SkipTurnAction()]


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
world_factory = WorldFactory()
world = world_factory.create(simple_locations)

# %% tags=["keep"]
pawn = Pawn("Alice", world.locations["Room 1"])
print(pawn)

# %% tags=["keep"]
player = Player("Alice", pawn)
print(player)

# %% tags=["keep"]
player.take_turn()
print(player)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
for _ in range(10):
    player.take_turn()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def interactive_action_strategy(player: "Player"):
    print(f"Available actions for {player.description}:")
    for i, action in enumerate(player.actions, 1):
        print(f"{i}: {action.description}")
    while True:
        try:
            choice = int(input("Your choice: "))
            if 0 < choice <= len(player.actions):
                return player.actions[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(player.actions)}!")
        except ValueError:
            print("Please enter a valid number!")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
player = Player("Iris", pawn, interactive_action_strategy)

# %% tags=["keep"]
for _ in range(5):
    player.take_turn()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Nächste Schritte
#
# - Verbesserung der Strategien
# - Kommunikation des Spiel-Fortschritts
