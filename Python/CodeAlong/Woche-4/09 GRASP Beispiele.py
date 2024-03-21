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
#  <b>GRASP: Beispiele</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 GRASP Beispiele.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_504_grasp_abstraction_examples.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Adapter-Pattern
#
# Wie können wir das Adapter-Pattern mit den abstrakten GRASP-Patterns
# analysieren?
#
# <img src="img/pat_adapter.svg"
#      style="display: block; margin: auto; width: 80%;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Strategie-Pattern
#
# Bei der Auswahl der nächsten Aktion durch den Spieler in unserem Adventure-Spiel
# hatten wir das Strategie-Pattern angewendet:
#
# <img src="img/pat_strategy.svg"
#      style="display:block;margin:auto;width:80%"/>
#
# Wie können wir diese Anwendung des Strategie-Patterns mit den abstrakten
# GRASP-Patterns analysieren?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Template-Methoden-Pattern
#
# Analysieren Sie, wie sich die Anwendung der abstrakten GRASP-Patterns
# auf das Template-Methoden-Pattern von der Anwendung auf das Strategie-Pattern
# unterscheidet.
#
# <img src="img/pat_template_method.svg"
#      style="display:block;margin:auto;width:40%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: GRASP-Abstraktionen
#
# Analysieren Sie die folgenden Beispiele auf ähnliche Art und Weise:

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Beispiel: Command-Pattern
#
# Wir haben das Command-Pattern verwendet, um die Aktionen des Spielers
# zu realisieren. Wie können wir das mit den abstrakten GRASP-Patterns
# analysieren?
#
# <img src="img/pat_command.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Beispiel: Push Observer
#
# Um Benachrichtigungen über Änderungen im Spielzustand zu erhalten, haben
# wir eine Variante des Observer-Patterns verwendet, bei der der Observer
# mehrere `notify...()`-Methoden hat, die von den Subjects aufgerufen werden.
#
# Analysieren Sie diese Anwendung des Observer-Patterns mit den abstrakten
# GRASP-Patterns.
#
# <img src="img/pat_observer_push.svg"
#      style="display:block;margin:auto;width:100%"/>
