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
#  <b>SOLID: OCP (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 SOLID OCP (Teil 2).py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_340_solid_ocp_part2.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Wiederholung: OCP-Verletzung
#
# <img src="img/movie_v0.svg" alt="MovieV0"
#      style="display:block;margin:auto;width:50%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Lösungsversuch 1: Vererbung
#
# <img src="img/movie_v2.svg" alt="MovieV2"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - OCP ist erfüllt
# - Großer Scope der Vererbung
#   - Preisberechnung ist das wichtigste an Filmen?
# - Nur eindimensionale Klassifikation
# - Keine Möglichkeit, Preisschema zu wechseln

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Lösungsversuch 2: Strategie-Muster
#
# <img src="img/movie_v3.svg" alt="MovieV3"
#      style="display:block;margin:auto;width:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - OCP ist erfüllt
# - Vererbung ist auf die Preisberechnung beschränkt
# - Mehrdimensionale Klassifikation ist einfach
# - Preisschema kann zur Laufzeit gewechselt werden

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Implementierung

# %% tags=["keep"]
from abc import ABC, abstractmethod


# %% tags=["keep"]
class PriceStrategy(ABC):
    @abstractmethod
    def compute_price(self, movie) -> float: ...


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class RegularPriceStrategy(PriceStrategy):
    def compute_price(self, movie) -> float:
        return 4.99


# %% tags=["keep"]
class ChildrenPriceStrategy(PriceStrategy):
    def compute_price(self, movie) -> float:
        return 5.99


# %% tags=["keep"]
class NewReleasePriceStrategy(PriceStrategy):
    def compute_price(self, movie) -> float:
        return 6.99


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Movie:
    def __init__(self, title: str, price_strategy):
        self.title = title
        self.price_strategy = price_strategy

    def compute_price(self) -> float:
        return self.price_strategy.compute_price(self)

    def print_info(self):
        print(f"{self.title} costs {self.compute_price()}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
movies = [
    Movie("Casablanca", RegularPriceStrategy()),
    Movie("Shrek", ChildrenPriceStrategy()),
    Movie("Brand New", NewReleasePriceStrategy()),
]

# %% tags=["keep"]
for m in movies:
    m.print_info()

# %%
movies[2].price_strategy = RegularPriceStrategy()

# %%
movies[2].print_info()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Berechnung von ÖPNV-Fahrpreisen
#
# In einer modernen Stadt stehen verschiedene öffentliche Verkehrsmittel zur
# Verfügung – Busse, U-Bahnen, Züge, Boote, etc. Jedes dieser Verkehrsmittel
# hat seine eigene Methode zur Fahrpreisberechnung. Zum Beispiel können
# Bustarife auf Pauschalpreisen basieren, U-Bahnen können auf
# Entfernungstarifen basieren und Boote können Premiumtarife für
# landschaftlich reizvolle Strecken haben.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Sie haben ein rudimentäres Fahrpreisberechnungssystem, das den Fahrpreis
# basierend auf dem Verkehrsmittel bestimmt. Leider verstößt dieses System
# gegen das OCP, da es ohne Modifikation nicht für die Erweiterung geöffnet
# ist. Jedes Mal, wenn ein neues Verkehrsmittel hinzugefügt werden muss, muss
# das Kernsystem geändert werden.
#
# Ihre Aufgabe ist es, das System so zu refaktorisieren, dass es dem OCP
# entspricht. Genauer gesagt, werden Sie die `if`-Anweisung aus der
# Fahrpreisberechnungslogik entfernen. Das Ziel ist es, das System leicht
# erweiterbar zu machen, so dass neue Verkehrsmittel hinzugefügt werden können,
# ohne den vorhandenen Code zu ändern und die Verkehrsmittel für Verbindungen
# zur Laufzeit gewechselt werden können.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from enum import Enum


# %% tags=["keep"]
class TransportType(Enum):
    BUS = 1
    SUBWAY = 2
    TRAIN = 3
    BOAT = 4


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Connection:
    def __init__(self, transport_type):
        self._type = transport_type

    def calculate_fare(self, distance):
        if self._type == TransportType.BUS:
            return 2.5  # flat rate
        elif self._type == TransportType.SUBWAY:
            return 1.5 + (distance * 0.2)  # base rate + per km
        elif self._type == TransportType.TRAIN:
            return 5.0 + (distance * 0.15)  # base rate + per km
        elif self._type == TransportType.BOAT:
            return 10.0  # premium rate
        else:
            return 0.0


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
bus = Connection(TransportType.BUS)
print(f"Bus fare: ${bus.calculate_fare(10)}")

# %% tags=["keep"]
subway = Connection(TransportType.SUBWAY)
print(f"Subway fare: ${subway.calculate_fare(10)}")

# %% tags=["keep"]
train = Connection(TransportType.TRAIN)
print(f"Train fare: ${train.calculate_fare(10)}")

# %% tags=["keep"]
boat = Connection(TransportType.BOAT)
print(f"Boat fare: ${boat.calculate_fare(10)}")

# %%
from abc import ABC, abstractmethod


# %% tags=["alt"]
class FareCalculationStrategy(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_fare(self, distance: float) -> float:
        pass


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class BusFare(FareCalculationStrategy):
    def calculate_fare(self, distance: float) -> float:
        return 2.50  # flat rate


# %% tags=["alt"]
class SubwayFare(FareCalculationStrategy):
    def calculate_fare(self, distance: float) -> float:
        return 1.50 + (distance * 0.20)  # base rate + per km


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class TrainFare(FareCalculationStrategy):
    def calculate_fare(self, distance: float) -> float:
        return 5.00 + (distance * 0.15)  # base rate + per km


# %% tags=["alt"]
class BoatFare(FareCalculationStrategy):
    def calculate_fare(self, distance: float) -> float:
        return 10.00  # premium rate


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class Connection:
    def __init__(self, fare_strategy):
        self._fare_strategy = fare_strategy

    def compute_fare(self, distance: float) -> float:
        return self._fare_strategy.calculate_fare(distance)


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
bus = Connection(BusFare())
print(f"Bus fare: ${bus.compute_fare(10)}")

# %% tags=["alt"]
subway = Connection(SubwayFare())
print(f"Subway fare: ${subway.compute_fare(10)}")

# %% tags=["alt"]
train = Connection(TrainFare())
print("Train fare: $", train.compute_fare(10))

# %% tags=["alt"]
boat = Connection(BoatFare())
print(f"Boat fare: ${boat.compute_fare(10)}")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Extra-Workshop: Zoo-Management System mit Strategy
#
# In einem früheren Workshop haben wir ein Zoo-Management System
# implementiert.
#
# Lösen Sie das OCP-Problem für dieses System mit dem Strategy-Muster.

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class AnimalFeedingSchedule(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_feeding_schedule(self) -> str:
        pass

    @abstractmethod
    def get_diet(self) -> str:
        pass


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class MammalFeedingSchedule(AnimalFeedingSchedule):
    def get_feeding_schedule(self) -> str:
        return "Feed at 9am and 5pm."

    def get_diet(self) -> str:
        return "Diet: Grass and fruits."


# %% tags=["alt"]
class BirdFeedingSchedule(AnimalFeedingSchedule):
    def get_feeding_schedule(self) -> str:
        return "Feed at 8am and 4pm."

    def get_diet(self) -> str:
        return "Diet: Seeds and insects."


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class ReptileFeedingSchedule(AnimalFeedingSchedule):
    def get_feeding_schedule(self) -> str:
        return "Feed at 12pm."

    def get_diet(self) -> str:
        return "Diet: Insects."


# %% tags=["alt"]
class AquaticFeedingSchedule(AnimalFeedingSchedule):
    def get_feeding_schedule(self) -> str:
        return "Feed at 11am and 6pm."

    def get_diet(self) -> str:
        return "Diet: Algae and small fish."


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class Animal:
    def __init__(self, name: str, feeding_schedule):
        self.name = name
        self.feeding_schedule = feeding_schedule

    @property
    def diet(self) -> str:
        return self.feeding_schedule.get_diet()


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
animals = [
    Animal("Elephant", MammalFeedingSchedule()),
    Animal("Penguin", BirdFeedingSchedule()),
    Animal("Snake", ReptileFeedingSchedule()),
    Animal("Shark", AquaticFeedingSchedule()),
]

# %% tags=["alt"]
for animal in animals:
    print(animal.name)
    print(animal.feeding_schedule)
    print(animal.diet)
    print()
