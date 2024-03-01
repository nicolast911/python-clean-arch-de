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
#  <b>Adventure: Spielfigur (V1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Adventure Spielfigur (V1).py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_320_adventure_pawn_v1.py -->

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 3a: Spielfiguren
#
# <img src="img/adventure-v3a-overview.svg" alt="Adventure Version 3a"
#      style="display:block;margin:auto;height:80%"/>

# %% tags=["subslide", "start"] slideshow={"slide_type": "subslide"}
@dataclass
class Pawn:
    name: str
    location: Location
