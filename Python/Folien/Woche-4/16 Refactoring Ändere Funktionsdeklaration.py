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
#  <b>Refactoring: Ändere Funktionsdeklaration</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 16 Refactoring Ändere Funktionsdeklaration.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_260_refact_change_function_decl.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Ändere Funktionsdeklaration
#
# Auch bekannt als:
# - Benenne Funktion um
# - Ändere Signatur
# - Benenne Methode um
# - Füge Parameter hinzu
# - Entferne Parameter

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from order_line import make_order_lines


# %% tags=["keep"]
def ttl(discount: bool, order_lines: list) -> float:
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    if discount:
        total *= 0.9
    return total


# %% tags=["keep"]
print(ttl(False, make_order_lines()))
print(ttl(True, make_order_lines()))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def compute_total(order_lines: list, discount: bool = False) -> float:
    total = 0.0
    for order_line in order_lines:
        total += order_line.quantity * order_line.price
    if discount:
        total *= 0.9
    return total


# %% tags=["keep"]
print(compute_total(make_order_lines(), False))
print(compute_total(make_order_lines(), True))

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Motivation
#
# - Der Name der Funktion spiegelt nicht mehr ihre Intention wieder
# - Die Signatur der Funktion ist nicht mehr passend
#   - inkonsistente Parameterreihenfolge zwischen ähnlichen Funktionen
#   - zu viele Parameter
#   - "falsche" Parametertypen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Einfache Mechanik
#
# - Beim Entfernen von Parametern: Stelle sicher, dass der Parameter nicht
#   im Rumpf verwendet wird
# - Ändere die Deklaration/Definition der Funktion
# - Ändere alle Aufrufe der Funktion
# - Teste das Programm

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Migrations-Mechanik
#
# - If necessary, refactor the body of the function to facilitate the following steps
# - Use *Extract Function* to extract the body of the function into a new function
# - If the extracted function requires additional parameters, use the simple
#   mechanics to add them
# - Test the program
# - Use *Inline Function* for the old function
# - Test the program
# - If the new function has a temporary name, use *Change Function Declaration*
#   to change its name
# - Test the program

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# - Mit der Migrations-Mechanik können wir auch ein veröffentlichtes Interface
#   ändern
# - Dazu entfernen wir das alte Interface nach dem Inlining nicht, sondern
#   markieren es als veraltet
# - In einem späteren Schritt können wir das alte Interface entfernen
