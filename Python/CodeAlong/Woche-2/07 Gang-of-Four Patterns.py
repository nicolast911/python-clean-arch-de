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
#  <b>Gang-of-Four Patterns</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Gang-of-Four Patterns.py -->
# <!-- python_courses/slides/module_210_design_patterns/topic_130_gof_patterns_short.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Gang-of-Four Patterns
#
# - Patterns aus dem Buch
#   "Design Patterns: Elements of Reusable Object-Oriented Software"
# - Die 4 Autoren wurden scherzhaft "Gang of Four" genannt
# - Die bekannteste Sammlung von Patterns
# - 1994 veröffentlicht
# - 23 Patterns

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Eigenschaften
#
# - Domänenunabhängig
# - Objektorientiert
# - Implementierungsnah
# - Sprachunabhängig

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Beispiele:
#
# - **Builder:** Komplexe Objekte Schritt für Schritt aufbauen
# - **Factory Method:** Objekte erzeugen, ohne die konkrete Klasse zu kennen
# - **Adapter:** Schnittstelle einer Klasse an eine andere Schnittstelle anpassen
# - **Observer:** Änderungen an einem Objekt an andere Objekte weitergeben
# - **Strategy:** Algorithmen austauschbar machen
# - **Template Method:** Grundgerüst einer Operation festlegen, Details in Unterklassen
