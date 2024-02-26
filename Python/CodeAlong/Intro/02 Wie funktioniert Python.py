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
#  <b>Wie funktioniert Python?</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Wie funktioniert Python.py -->
# <!-- python_courses/slides/module_110_introduction/topic_100_b2_how_does_python_work.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# # Einführung
#
# Wir beantworten die folgenden Fragen:
#
# - Wie funktioniert Python?
# - Wie wird Python Code ausgeführt?
# - Welche Entwicklungsumgebungen gibt es?
# - Wie arbeitet man mit Notebooks?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Ausführen von Programmen
#
# <br/>
# <center>
# <video src="img/launching-programs.mp4" controls style="width:75%">
# Videos werden von Ihrem Browser nicht unterstützt.
# </video>
# </center>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Interpreter (Python)
#
# <br/>
# <center>
# <video src="img/python-interpreter.mp4" controls style="width:75%">
# Videos werden von Ihrem Browser nicht unterstützt.
# </video>
# </center>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def say_hello(name):
    print(f"Hello, {name}!")


# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)
plt.show()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
# ## Entwicklungsumgebungen
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interaktive Shell
