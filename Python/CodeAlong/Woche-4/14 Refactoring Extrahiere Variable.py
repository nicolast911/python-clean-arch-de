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
#  <b>Refactoring: Extrahiere Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 14 Refactoring Extrahiere Variable.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_240_refact_extract_variable.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Extrahiere Variable

# %% tags=["keep"]
from order_line import make_order_lines


# %% tags=["keep"]
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        order_line_price = order_line.quantity * order_line.price  # new variable
        total += order_line_price
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Motivation
#
# - Hilft dabei, komplexe Ausdrücke zu verstehen
#   - Erklärende Variablen/Konstanten
# - Debugging oft einfacher

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Mechanik
#
# - Stelle sicher, dass der Ausdruck frei von Seiteneffekten ist
# - Erzeuge eine neue Variable
# - Initialisiere sie mit dem Ausdruck
# - Ersetze den Ausdruck durch die Variable
# - Teste das Programm
