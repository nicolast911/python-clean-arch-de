# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung ins Refactoring</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Einführung ins Refactoring.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_110_a3_refactoring_intro.py -->

# %% [markdown]
#
# ## Was ist Refactoring?
#
# - Ändern eines Software-Systems
# - ohne dessen externes Verhalten zu ändern
# - um dessen interne Struktur zu verbessern
#
# *Im Wesentlichen, wenn Sie refaktorisieren, verbessern Sie das Design des Codes,
# nachdem er geschrieben wurde.* (Martin Fowler)

# %% [markdown]
#
# ## Warum Refactoring?
#
# - Code wird verständlicher
# - Code wird einfacher zu warten
# - Code wird einfacher zu erweitern
# - Code wird einfacher zu testen
# - ...

# %% [markdown]
#
# ## Was ist Refactoring nicht?
#
# - Große Änderungen am Code in einem Schritt
# - Hinzufügen von neuen Features
# - Beheben von Bugs

# %% [markdown]
#
# ## Wann Refactoring?
#
# - Wenn Code verstanden werden muss
# - Wenn Code erweitert werden muss
# - Wenn wir schlechten Code finden, den wir ändern müssen

# %% [markdown]
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
