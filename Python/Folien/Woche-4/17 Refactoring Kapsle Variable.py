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
#  <b>Refactoring: Kapsle Variable</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 17 Refactoring Kapsle Variable.py -->
# <!-- python_courses/slides/module_250_refactoring/topic_270_refact_encapsulate_variable.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Kapsle Variable

# %% tags=["keep"]
class ProductV0:
    def __init__(self, name: str):
        self.name = name


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class ProductV1:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Motivation
#
# - Erleichtert zukünftige Refactorings
#   - Forwarding ist bei Funktionen einfacher als bei Daten
#   - Durch Kapselung kann man Techniken zum Refactoring von Funktionen
#     anwenden
# - Verhindert ungewollte Änderungen an Daten
# - Ermöglicht Validierung, Monitoring, ...
# - In Python weniger relevant als in anderen Sprachen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# #### Mechanik
#
# - Implementiere Getter (und nur bei Bedarf Setter)
# - Ersetze Zugriffe auf die Variable durch Getter (und Setter)
# - Teste nach jeder solchen Änderung
# - Schränke die Sichtbarkeit der Variable ein
# - Falls die Variable einen Record-Typ hat, ziehe *Encapsulate Record* in
#   Betracht
