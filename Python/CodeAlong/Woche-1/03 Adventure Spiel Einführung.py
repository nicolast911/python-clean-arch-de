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
#  <b>Adventure Spiel: Einführung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Adventure Spiel Einführung.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_120_adventure_intro.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Beispiel: Adventure-Game
#
# - Der Spieler kann sich durch eine Welt bewegen, die aus miteinander
#   verbundenen Orten besteht
# - An manchen Orten sind Objekte zu finden, mit denen der Spieler interagieren
#   kann, z.B. Behälter mit Beute, usw.
# - In der Welt gibt es vom Computer kontrolliere Figuren (NPCs)
# - Der Spieler kann mit NPCs interagieren (z.B. reden, kämpfen, handeln)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Siehe Game Pitch für Details (Ordner `Extras`)
# - Design-Modelle als UML-Diagramme
#   - Wichtig: Verständnis für die Domäne
#   - Nicht wichtig: Details der Modellierung, UML vs. ...
#   - Nicht wichtig: Entwicklungsprozess, ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Domänenmodell: Statische Struktur

# %% [markdown]
# <img src="img/adv-domain-00a.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/adv-domain-00.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/adv-domain-01.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/adv-domain-02.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Domänenmodell: Verhalten
#
# - Verständnis von Verhalten ist wichtig
# - Viele Möglichkeiten, Verhalten zu beschreiben
#   - Use Cases
#   - User Stories
#   - Aktivitätsdiagramme
#   - Sequenzdiagramme
#   - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Use Cases
#
# - Wir wollen für unser Spiel die folgenden Use Cases betrachten:
#   - Initialisierung des Spiels
#   - Haupt-Spiel-Schleife (Main Game Loop)
#   - Spieler macht einen Zug
