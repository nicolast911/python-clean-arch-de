# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Wie funktioniert Python?</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 02 Wie funktioniert Python.py -->
# <!-- python_courses/slides/module_110_introduction/topic_100_b2_how_does_python_work.py -->

# %% [markdown]
# # Einführung
#
# Wir beantworten die folgenden Fragen:
#
# - Wie funktioniert Python?
# - Wie wird Python Code ausgeführt?
# - Welche Entwicklungsumgebungen gibt es?
# - Wie arbeitet man mit Notebooks?

# %% [markdown]
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown]
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# %% [markdown]
# ## Ausführen von Programmen
#
# <br/>
# <center>
# <video src="img/launching-programs.mp4" controls style="width:75%">
# Videos werden von Ihrem Browser nicht unterstützt.
# </video>
# </center>

# %% [markdown]
# ## Interpreter (Python)
#
# <br/>
# <center>
# <video src="img/python-interpreter.mp4" controls style="width:75%">
# Videos werden von Ihrem Browser nicht unterstützt.
# </video>
# </center>

# %% [markdown]
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %%
def say_hello(name):
    print(f"Hello, {name}!")


# %%
say_hello("World")

# %%
import numpy as np
import matplotlib.pyplot as plt

page_load_time = np.random.normal(3.0, 1.0, 1000)
purchase_amount = np.random.normal(50.0, 1.5, 1000) - page_load_time

plt.figure(figsize=(12, 8))
plt.scatter(page_load_time, purchase_amount)
plt.show()

# %% [markdown]
# ## Entwicklungsumgebungen
#
# - Visual Studio Code
# - PyCharm
# - Vim/Emacs/... + interaktive Shell
