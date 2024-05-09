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
#  <b>Assertions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 07 Assertions.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_120_a3_assertions.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Assertions
#
# Das Assert-Statement ist nur eine kompakte Schreibweise, um eine bestimmte Art von
# Fehler (einen `AssertionError`) auszulösen, wenn eine Bedingung falsch ist:

# %% tags=["keep"]
my_var = 1

# %%
assert my_var == 1

# %%
if my_var != 1:
    raise AssertionError()

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# assert my_var == 2

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Assert mit optionalem Fehler-Text:

# %%
assert my_var == 1, "my_var should be 1"

# %%
if my_var != 1:
    raise AssertionError("my_var should be 1")

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
# assert my_var == 2, "my_var should be 2"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Assertions können mit dem `-O`-Flag deaktiviert werden.

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
# %pycat test_assert.py

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
# !python test_assert.py

# %% tags=["keep"]
# !python -O test_assert.py


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Assertions sind nützlich, um Annahmen über den Programmzustand zu dokumentieren.
# - Sie sind aber nicht dazu gedacht, Fehler in Eingaben abzufangen.

# %% tags=["keep"]
def bad_user_input():
    number = input("Please enter a number: ")
    assert number.isdigit(), "Input must be a number!"
    return int(number)


# %% tags=["keep"]
def better_user_input():
    number = input("Please enter a number: ")
    if not number.isdigit():
        raise ValueError("Input must be a number!")
    return int(number)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Assertions
#
# Das Programm `valid_mail.py` fragt den Benutzer nach einer E-Mail-Adresse und
# gibt diese wieder aus, wenn sie in der Liste `valid_mail_addresses` enthalten
# ist.
#
# Bei ungültigen Eingaben wird eine Exception ausgelöst.
#
# - Führen Sie das Programm mit verschiedenen Eingaben aus und beobachten Sie das
#   Verhalten.
# - Wie können Sie das Programm dazu bringen, auch ungültige Eingaben zu akzeptieren?
# - Schreiben Sie das Programm so um, das dies nicht mehr möglich ist.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
# # !python valid_mail.py

# %%
# # !python -O valid_mail.py
