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
#  <b>Adventure: Spielfigur (V2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Adventure Spielfigur (V2).py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_324_adventure_pawn_v2.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 3b: Enumeration der Aktionen
#
# - Enumeration `Action` mit allen möglichen Aktionen
# - `Pawn`-Klasse hat nur noch eine `perform_action()`-Methode
# - `perform_action()`-Methode bekommt eine `action` als Parameter

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 3b: Spielfiguren mit Enumeration
#
# <img src="img/adventure-v3b-overview.svg" alt="Adventure Version 3b"
#      style="display:block;margin:auto;height:80%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass
from enum import Enum

# %% tags=["keep"]
from location_v2 import Location

# %%


# %% tags=["start", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class Pawn:
    name: str
    location: Location

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## GRASP und SOLID Prinzipien
#
# - GRASP:
#   - Geschützte Variation (Protected Variation)
#   - Indirektion
#   - Polymorphie
# - SOLID:
#   - Open-Closed Principle
