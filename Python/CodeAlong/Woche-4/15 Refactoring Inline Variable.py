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
#  <b>Refactoring: Inline Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 15 Refactoring Inline Variable.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_250_refact_inline_variable.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Inline Variable

# %% tags=["keep"]
from order_line import make_order_lines


# %% tags=["keep"]
def order_line_price(order_line):
    return order_line.quantity * order_line.price


# %% tags=["keep"]
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        price = order_line_price(order_line)
        total += price
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line_price(order_line)  # <-- inline variable
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Motivation
#
# - Manchmal kommuniziert der Name der Variable nicht mehr als der Ausdruck selbst
# - Manchmal verhindert eine Variable das Refactoring von anderem Code

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Mechanik
#
# - Stelle sicher, dass der Initialisierungs-Ausdruck frei von Seiteneffekten ist
# - Falls die Variable nicht schon konstant ist, mache sie konstant und teste
#   das Programm
# - Finde die erste Referenz auf die Variable
# - Ersetze die Variable durch ihren Initialisierungs-Ausdruck
# - Teste das Programm
# - Wiederhole für jede Referenz auf die Variable
