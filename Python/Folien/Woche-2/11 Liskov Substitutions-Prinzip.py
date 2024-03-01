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
#  <b>Liskov Substitutions-Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Liskov Substitutions-Prinzip.py -->
# <!-- python_courses/slides/module_280_solid/topic_140_a3_solid_lsp.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # SOLID: Liskov Substitutions-Prinzip
#
# Ein Objekt einer Unterklasse soll immer für ein Objekt der Oberklasse
# eingesetzt werden können.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## LSP Verletzung

# %% tags=["keep"]
from dataclasses import dataclass


# %% tags=["keep"]
@dataclass
class Rectangle:
    length: float
    width: float

    def area(self):
        return self.length * self.width


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, length)

    @property
    def length(self):
        return self.__dict__["length"]

    @length.setter
    def length(self, new_value):
        self.__dict__["length"] = new_value
        self.__dict__["width"] = new_value

    @property
    def width(self):
        return self.__dict__["length"]

    @width.setter
    def width(self, new_value):
        self.__dict__["length"] = new_value
        self.__dict__["width"] = new_value


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
my_rect = Rectangle(3, 4)
print(f"Area is {my_rect.area()}")
my_rect.length = 10
my_rect.width = 12
print(f"After setting values: {my_rect}")
print(f"Area is now {my_rect.area()}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
my_square = Square(3, 4)
print(f"Area is {my_square.area()}")
my_square.length = 10
my_square.width = 12
print(f"After setting values: {my_square}")
print(f"Area is now {my_square.area()}")

# %%
