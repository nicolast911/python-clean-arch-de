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
#  <b>Einführung ins Refactoring</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Einführung ins Refactoring.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_110_a3_refactoring_intro.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Was ist Refactoring?
#
# - Ändern eines Software-Systems
# - ohne dessen externes Verhalten zu ändern
# - um dessen interne Struktur zu verbessern
#
# *Im Wesentlichen, wenn Sie refaktorisieren, verbessern Sie das Design des Codes,
# nachdem er geschrieben wurde.* (Martin Fowler)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Warum Refactoring?
#
# - Code wird verständlicher
# - Code wird einfacher zu warten
# - Code wird einfacher zu erweitern
# - Code wird einfacher zu testen
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Was ist Refactoring nicht?
#
# - Große Änderungen am Code in einem Schritt
# - Hinzufügen von neuen Features
# - Beheben von Bugs

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Wann Refactoring?
#
# - Wenn Code verstanden werden muss
# - Wenn Code erweitert werden muss
# - Wenn wir schlechten Code finden, den wir ändern müssen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Sollen wir extra Zeit für Refactoring einplanen?
#
# - Normalerweise nicht
# - Refactoring ist Teil der Entwicklung und sollte permanent stattfinden
# - Möglicherweise:
#   - Zeit zum Refaktorisieren einplanen, wenn wir an Code arbeiten, der schlecht ist
#
# *Refaktorisierung ist keine Aktivität, die vom Programmieren getrennt ist - genauso
# wenig, wie Sie Zeit zum Schreiben von if-Anweisungen einplanen.* (Martin Fowler)
