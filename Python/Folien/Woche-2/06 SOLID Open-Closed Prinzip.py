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
#  <b>SOLID: Open-Closed Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 06 SOLID Open-Closed Prinzip.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_330_solid_ocp.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # Open-Closed Prinzip (SOLID)
#
# Klassen sollen
#
# - offen für Erweiterung
# - geschlossen für Modifikation
#
# sein.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from enum import Enum


# %% tags=["keep"]
class MovieKindV0(Enum):
    REGULAR = 1
    CHILDREN = 2


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class MovieV0:
    def __init__(self, title: str, kind=MovieKindV0.REGULAR):
        self.title = title
        self.kind = kind

    def compute_price(self) -> float:
        match self.kind:
            case MovieKindV0.REGULAR:
                return 4.99
            case MovieKindV0.CHILDREN:
                return 5.99
            case _:
                return 0.0

    def print_info(self):
        print(f"{self.title} costs {self.compute_price()}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
m1 = MovieV0("Casablanca")
m2 = MovieV0("Shrek", MovieKindV0.CHILDREN)


# %% tags=["keep"]
m1.print_info()
m2.print_info()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/movie_v0.svg" alt="MovieV0"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Was passiert, wenn wir eine neue Filmart hinzufügen wollen?

# %% tags=["keep"]
from enum import Enum


# %% tags=["alt"]
class MovieKind(Enum):
    REGULAR = 1
    CHILDREN = 2
    NEW_RELEASE = 3


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class MovieV1:
    def __init__(self, title: str, kind=MovieKind.REGULAR):
        self.title = title
        self.kind = kind

    def compute_price(self) -> float:
        match self.kind:
            case MovieKindV0.REGULAR:
                return 4.99
            case MovieKindV0.CHILDREN:
                return 5.99
            case MovieKind.NEW_RELEASE:
                return 6.99
            case _:
                return 0.0

    def print_info(self):
        print(f"{self.title} costs {self.compute_price()}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
m1 = MovieV1("Casablanca")
m2 = MovieV1("Shrek", MovieKind.CHILDREN)
m3 = MovieV1("Brand New", MovieKind.NEW_RELEASE)

# %% tags=["keep"]
m1.print_info()
m2.print_info()
m3.print_info()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/movie_v1.svg" alt="MovieV1"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## OCP-Verletzung
#
# - Neue Filmarten erfordern Änderungen an `MovieV1`
# - `MovieV1` ist nicht geschlossen für Modifikation

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung (Versuch 1: Vererbung)
#
# - Neue Filmarten werden als neue Klassen implementiert
# - `MovieV2` wird abstrakt
# - `MovieV2` ist geschlossen für Modifikation

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


# %% tags=["keep"]
class MovieV2(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def compute_price(self) -> float: ...

    def print_info(self) -> None:
        print(f"{self.title} costs {self.compute_price()}")


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class RegularMovie(MovieV2):
    def compute_price(self) -> float:
        return 4.99


# %% tags=["keep"]
class ChildrenMovie(MovieV2):
    def compute_price(self) -> float:
        return 5.99


# %% tags=["keep"]
class NewReleaseMovie(MovieV2):
    def compute_price(self) -> float:
        return 6.99


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
m1 = RegularMovie("Casablanca")
m2 = ChildrenMovie("Shrek")
m3 = NewReleaseMovie("Brand New")

# %%
m1.print_info()
m2.print_info()
m3.print_info()

# %%
isinstance(m1, MovieV2)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/movie_v2.svg" alt="MovieV0"
#      style="display:block;margin:auto;width:100%"/>


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - `MovieV2` ist offen für Erweiterung
# - Neue Filmarten können hinzugefügt werden, ohne die bestehenden Klassen zu
#   ändern
# - Aber: Die Vererbungshierarchie umfasst die ganze Klasse
#   - Nur eine Art von Variabilität
# - Was ist, wenn wir für andere Zwecke eine andere Klassifikation brauchen?
#   - Z.B. DVD, BluRay, Online?
# - Mehrfachvererbung?
# - Produkt von Klassen?
#   - `ChildrenDVD`, `ChildrenBluRay`, `ChildrenOnline`, ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Bessere Auflösung: Strategy Pattern
#
# - Das Strategy-Pattern erlaubt es uns, die Vererbung auf kleinere Teile der
#   Klasse anzuwenden
# - In fast allen Fällen ist das die bessere Lösung!
# - Vererbung ist ein sehr mächtiges Werkzeug
# - Aber je kleiner und lokaler wir unsere Vererbungshierarchien halten, desto
#   besser


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Zoo-Management-System
#
# In diesem Workshop werden wir mit einem hypothetischen Szenario arbeiten, das
# ein Zoo-Management-System für die Fütterungspläne der Tiere betrifft. Die
# Herausforderung? Das vorhandene System verstößt gegen das OCP, und es liegt
# an uns, das zu korrigieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Szenario
#
# Stellen Sie sich einen Zoo vor. Dieser Zoo hat eine Vielzahl von Tieren:
# Säugetiere, Vögel, Reptilien und Wasserlebewesen. Jede Art von Tier hat ihren
# eigenen einzigartigen Fütterungsplan und ihre eigenen Ernährungsbedürfnisse.
#
# Nun muss das digitale System des Zoos diese Fütterungspläne verfolgen. Das
# Problem mit dem aktuellen System ist seine Verwendung einer Enumeration, um
# den Tier-Typ und basierend darauf seinen Fütterungsplan zu bestimmen. Dieser
# Ansatz ist nicht skalierbar und verstößt gegen das OCP. Was passiert, wenn der
# Zoo eine neue Tierart erwirbt? Oder was ist, wenn sich der Fütterungsplan für
# Reptilien ändert? Die aktuelle Code-Struktur erfordert Änderungen an mehreren
# Stellen.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from enum import Enum, auto


# %% tags=["keep"]
class AnimalType(Enum):
    Mammal = auto()
    Bird = auto()
    Reptile = auto()
    Aquatic = auto()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class AnimalV0:
    def __init__(self, animal_type):
        self._type = animal_type

    @property
    def feeding_schedule(self) -> str:
        if self._type == AnimalType.Mammal:
            return "Feed at 9am and 5pm."
        elif self._type == AnimalType.Bird:
            return "Feed at 8am and 4pm."
        elif self._type == AnimalType.Reptile:
            return "Feed at 12pm."
        elif self._type == AnimalType.Aquatic:
            return "Feed at 11am and 6pm."
        else:
            return f"No feeding schedule for {self._type}!"

    @property
    def diet(self) -> str:
        if self._type == AnimalType.Mammal:
            return "Diet: Grass and fruits."
        elif self._type == AnimalType.Bird:
            return "Diet: Seeds and insects."
        elif self._type == AnimalType.Reptile:
            return "Diet: Insects."
        elif self._type == AnimalType.Aquatic:
            return "Diet: Algae and small fish."
        else:
            return f"No diet for {self._type}!"


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
animals_original = [
    AnimalV0(AnimalType.Mammal),
    AnimalV0(AnimalType.Bird),
    AnimalV0(AnimalType.Reptile),
]


# %% tags=["keep"]
def display_feeding_info(animals):
    for animal in animals:
        print(f"{animal.feeding_schedule} {animal.diet}")


# %% tags=["keep"]
display_feeding_info(animals_original)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Beseitigen Sie das Problem mit der OCP-Verletzung im vorhandenen Code
# - Sie können entweder den vorhandenen Code ändern oder eine neue Lösung von
#   Grund auf erstellen

# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        super().__init__()

    @property
    def feeding_schedule(self) -> str:
        return self.get_feeding_schedule()

    @property
    def diet(self) -> str:
        return self.get_diet()

    @abstractmethod
    def get_feeding_schedule(self) -> str:
        pass

    @abstractmethod
    def get_diet(self) -> str:
        pass


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class Mammal(Animal):
    def get_feeding_schedule(self) -> str:
        return "Feed at 9am and 5pm."

    def get_diet(self) -> str:
        return "Diet: Grass and fruits."


# %% tags=["alt"]
class Bird(Animal):
    def get_feeding_schedule(self) -> str:
        return "Feed at 8am and 4pm."

    def get_diet(self) -> str:
        return "Diet: Seeds and insects."


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class Reptile(Animal):
    def get_feeding_schedule(self) -> str:
        return "Feed at 12pm."

    def get_diet(self) -> str:
        return "Diet: Insects."


# %% tags=["alt"]
class Aquatic(Animal):
    def get_feeding_schedule(self) -> str:
        return "Feed at 11am and 6pm."

    def get_diet(self) -> str:
        return "Diet: Algae and small fish."


# %% tags=["alt"]
animals_refactored = [Mammal(), Bird(), Reptile()]


# %% tags=["alt"]
def display_feeding_info(animals):
    for animal in animals:
        print(f"{animal.feeding_schedule} {animal.diet}")


# %% tags=["alt"]
display_feeding_info(animals_refactored)
