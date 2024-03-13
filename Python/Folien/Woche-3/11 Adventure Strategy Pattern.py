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
#  <b>Adventure: Strategy Pattern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 Adventure Strategy Pattern.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_390_adventure_strategy.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 3c: Command Pattern
#
# <img src="img/adventure-v3c-overview.svg" alt="Adventure Version 3c"
#      style="display:block;margin:auto;height:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sowohl menschliche als auch computergesteuerte Spieler
# - Dazu notwendig:
#   - Generieren aller möglichen Aktionen (situationsabhängig)
#   - Auswählen einer Aktion
#   - Ausführen der Aktion
# - Wer soll diese Verantwortlichkeiten übernehmen?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Informationsexperte:
#   - Im Moment kennt niemand alle Aktionen, die möglich sind
#   - `Pawn` weiß, wo er sich befindet
#   - Für weitere Aktionen:
#     - `Pawn` enthält wahrscheinlich die meisten benötigten Informationen
# - Sollen wir die Verantwortung an `Pawn` übergeben?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Gegenargumente
#
# - Damit bekommt `Pawn` potenziell zu viele Verantwortlichkeiten
#   - Bewegung auf dem Spielfeld
#   - Darstellung der Grafik
#   - Strategie für computergesteuerte Spieler
#   - Interaktion mit menschlichem Benutzer
# - Niedrige Repräsentationslücke?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Sehen wir im Domänenmodell nach:

# %% [markdown]
# <img src="img/adv-domain-03.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `Player` ist für die Strategie zuständig
# - Wir sollten eine `Player`-Klasse einführen und ihr die Verantwortung
#   für die neuen Aufgaben übergeben

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4a: `Player`-Klasse
#
# <img src="img/adventure-v4a.svg" alt="Adventure Version 4a"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `Player`-Klasse ist für die Strategie zuständig
# - Im Moment nur eine fest verdrahtete Strategie:
#   - Spieler nimmt immer letzten Eintrag in der Liste der Aktionen
# - Wir wollen mehrere Strategien unterstützen
# - Mit einer "interaktiven" Strategie wollen wir den menschlichen Spieler
#   einbinden
# - Versuchen wir eine Enumeration aller möglichen Strategien

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4b: Mehrere Strategien
#
# <img src="img/adventure-v4b.svg" alt="Adventure Version 4b"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Das Klassendiagramm sieht nicht so schlecht aus
# - Implementierung ist unübersichtlich
# - Open-Closed Prinzip ist verletzt
# - Besser: Strategie Pattern

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Version 4c: Mehrere Strategien
#
# <img src="img/adventure-v4c.svg" alt="Adventure Version 4b"
#      style="display:block;margin:auto;height:60%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Nächster Schritt: Verbesserung der interaktiven Strategie
