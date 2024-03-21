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
#  <b>Refactoring: Inline Function</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 13 Refactoring Inline Function.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_230_refact_inline_function.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Inline Function
#
# - Invers zu *Extrahiere Funktion*

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from order_line import OrderLine, make_order_lines


# %% tags=["keep"]
def order_line_price(order_line: OrderLine):
    return order_line.price


# %% tags=["keep"]
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line_price(order_line)
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def compute_total(order_lines):
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price  # <-- inline function
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines()))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Motivation
#
# - Manchmal ist eine Funktion nicht leichter zu verstehen als ihr Codeblock
# - Manchmal sind die von einer Funktion verwendeten Hilfsfunktionen nicht gut
#   strukturiert
# - Generell: Potenziell anwendbar, wenn man aufgrund zu vieler Indirektionen den
#   Überblick verliert

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Mechanik
#
# - Stelle sicher, dass die Funktion keiner objektorientierten Polymorphie
#   unterliegt, wie dies bei virtuellen Funktionen in C++ der Fall ist.
#   - In Python gibt es keine expliziten virtuellen Funktionen, aber die Funktion
#     sollte nicht in einer Weise überschrieben werden, die die Semantik des
#     Programms bei einer Entfernung ändern würde.
# - Finde alle Aufrufe der Funktion.
# - Ersetze jeden Aufruf durch den Codeblock der Funktion.
# - Teste nach jedem Schritt!
# - Entferne die Funktionsdefinition.
# - Brich ab, falls Schwierigkeiten wegen Rekursion, mehreren `return`-Anweisungen,
#   etc. auftreten.
