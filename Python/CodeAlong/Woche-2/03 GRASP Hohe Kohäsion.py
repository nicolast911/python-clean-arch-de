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
#  <b>GRASP: Hohe Kohäsion</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 GRASP Hohe Kohäsion.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_315_grasp_high_cohesion.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Problem
#
# - Wie können wir objekte fokussiert, verständlich und wartbar gestalten?
#
# ### Lösung
#
# - Weise Verantwortlichkeiten so zu, dass die Kohäsion hoch bleibt.
# - Evaluiere Designalternativen anhand ihrer Kohäsion.
#
# Dadurch erreichen wir als Nebenprodukt oft auch niedrige Kopplung.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Was ist Kohäsion?
#
# - Maß dafür
#   - wie gut verschiedene Teile eines Artefakts zusammenpassen
#   - wie fokussiert die Funktionalität eines Artefakts ist

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Konsequenzen
#
# - Hohe Kohäsion vereinfacht Entwicklung, Wiederverwendung, Testen, Performance
# - Niedrige Kohäsion macht es schwierig, den Code zu verstehen oder herauszufinden,
#   wo Änderungen vorgenommen werden sollen
# - Der **negative Effekt** niedriger Kohäsion ist **immer groß**
# - Es ist **schwer**, ein System mit niedriger Kohäsion in einen Zustand mit mehr
#   Kohäsion zu überführen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Wie können wir feststellen, ob die Kohäsion hoch ist?
#
# - Relativ geringe Anzahl von Methoden
# - Stark zusammenhängende Funktionalität
# - Übernimmt nicht zu viel Arbeit
# - Arbeitet mit anderen Objekten zusammen, um komplexere Aufgaben zu erledigen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Kohäsion und Kopplung
#
# - Geringe Kohäsion führt dazu, dass die Systemfunktionalität über das gesamte
#   System "verschmiert" wird
# - Dies führt oft zu einer *hohen Kopplung*
# - Das System lässt sich nur schwer in einen gewünschten Zustand versetzen
# - Testen wird schwierig
#   - Unit-Tests werden groß und schwerfällig
#   - Erzwingen die Verwendung vieler Testdoubles
#   - Verringern den Wert von Unit-Tests als Dokumentation

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Was können wir tun?
#
# - Extraktion von Klassen (wie bei SRP)
# - Verwendung von Entwurfsmustern
