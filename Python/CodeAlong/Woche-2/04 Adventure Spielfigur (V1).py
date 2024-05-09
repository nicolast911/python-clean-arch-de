# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Adventure: Spielfigur (V1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 04 Adventure Spielfigur (V1).py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_320_adventure_pawn_v1.py -->

# %% [markdown]
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %%
from dataclasses import dataclass

# %%


# %% [markdown]
#
# ## Version 3a: Spielfiguren
#
# <img src="img/adventure-v3a-overview.svg" alt="Adventure Version 3a"
#      style="display:block;margin:auto;height:80%"/>

# %%
@dataclass
class Pawn:
    name: str
    location: Location
