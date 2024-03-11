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
#  <b>Benutzerdefinierte Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 Benutzerdefinierte Exceptions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_130_a3_user_defined_exceptions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Benutzerdefinierte Exceptionklassen
#
# - Es ist möglich, eigenen Exceptionklassen zu definieren.
# - Dazu genügt es, von `Exception` oder einer Unterklasse von `Exception` zu
#   erben.

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Benutzerdefinierte Exceptions können wie alle anderen Exceptions erzeugt und
#   behandelt werden.

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Exceptions können mit beliebig vielen Argumenten initialisiert werden.
# - Die Werte der Argumente können mit `args` abgefragt werden.

# %%

# %%

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Benutzerdefinierte Exceptions können genau wie alle anderen Exceptions
#   ausgelöst und behandelt werden.

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Behandeln von Unterklassen einer Exception
#
# - Eine `except`-Klausel für eine Klasse `A` behandelt auch alle Unterklassen von `A`
# - Das gilt auch für benutzerdefinierte Exceptions

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Wann eigene Exceptions definieren?
#
# Betrachte das Problem aus der Sicht des Benutzers:
#
# - Ist es sinnvoll spezifisch auf das Problem zu reagieren?
# - Ist eine bessere Fehlermeldung möglich?
# - Beispiele:
#   - `FileNotFoundError` statt `OSError`
#   - `DimensionMismatchError` statt `ValueError` für physikalische Berechnungen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Benutzerdefinierte Exceptions
#
# - Schreiben Sie eine Funktion `read_email_from_user()`, die eine E-Mail-Adresse
#   vom Benutzer einliest.
# - Die Funktion soll eine benutzerdefinierte Exception `InvalidEmailError`
#   auslösen, wenn die E-Mail-Adresse nicht in der Liste `valid_mail_addresses`
#   enthalten ist.

# %% tags=["keep"]
valid_mail_addresses = [
    "joe@example.com",
    "jane@example.com",
    "jill@example.com",
]

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%


# %%
