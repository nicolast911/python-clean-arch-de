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
#  <b>Refactoring: Code Smells</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Refactoring Code Smells.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_150_a3_code_smells.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Was sind Code Smells?
#
# Code Smells sind Hinweise darauf, dass wir schlechten Code haben und refactoren
# sollten.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Code Smells
#
# - Mysterious Name
# - Duplicated Code
# - Long Function
# - Long Parameter List
# - Global Data
# - Mutable Data

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Divergent Change
# - Shotgun Surgery
# - Feature Envy
# - Data Clumps
# - Primitive Obsession
# - Repeated Switches
# - Loops
# - Lazy Element

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Speculative Generality
# - Temporary Field
# - Message Chains
# - Middle Man


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Insider Trading
# - Large Class
# - Alternative Classes with Different Interfaces
# - Data Class
# - Refused Bequest
# - Comments
