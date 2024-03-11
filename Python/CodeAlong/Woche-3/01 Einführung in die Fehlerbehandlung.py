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
#  <b>Einführung in die Fehlerbehandlung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 01 Einführung in die Fehlerbehandlung.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_108_a1_intro_error_handling.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Fehlerbehandlung
#
# Wir wollen eine Funktion `int_sqrt(n: int) -> int` schreiben, die die
# "Ganzzahlige Wurzel" berechnet:
# - Wenn `n` eine Quadratzahl ist, also die Form `m * m` hat, dann soll `m`
#   zurückgegeben werden.
# - Was machen wir, falls `n` keine Quadratzahl ist?
# - Um den Mechanismus, den Python verwendet, zu motivieren, besprechen wir erst
#   zwei andere Möglichkeiten Fehler zu behandeln


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können versuchen, einen "Fehlerwert" zurückzugeben, der kein gültiges
#   Ergebnis ist.
# - Hier z.B. eine negative Zahl

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Diese Version ist einfach zu verwenden, aber fehleranfällig:

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Code zur Fehlerbehandlung ist mit dem "Erfolgsfall" verwoben

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir können auch zwei Werte zurückgeben: Ergebnis und ein Erfolg/Fehler Flag

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Die Probleme bei dieser Lösung sind ähnlich wie bei der vorhergehenden.

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
#  Beide Ansätze haben mehrere Probleme:
#  - Die Fehlerbehandlung ist optional. Wird sie nicht durchgeführt, so wird mit
#    einem falschen Wert weitergerechnet.
#  - Kann der Aufrufer den Fehler nicht selber behandeln, so muss der Fehler über
#    mehrere Ebenen von Funktionsaufrufen "durchgereicht" werden.
#  - Das führt zu
#    unübersichtlichem Code, da der "interessante" Pfad nicht vom Code zur
#    Fehlerbehandlung getrennt ist.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Gewünschte Eigenschaften
#
# - Normale Programmlogik wird nicht beeinträchtigt
# - Behandlung von Fehlern wird erzwungen
# - Entdecken eines Fehlers ist entkoppelt von seiner Behandlung
# - Information über den Fehler kann leicht zum Handler kommuniziert werden
