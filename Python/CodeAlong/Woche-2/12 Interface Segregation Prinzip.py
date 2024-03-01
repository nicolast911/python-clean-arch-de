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
#  <b>Interface Segregation Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 Interface Segregation Prinzip.py -->
# <!-- python_courses/slides/module_280_solid/topic_150_a3_solid_isp.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # SOLID: Interface Segregation Prinzip
#
# - Kein Client einer Klasse C sollte von Methoden abhängen, die er nicht
#   benutzt.
# - Wenn das nicht der Fall ist
#   - Unterteile die Schnittstelle von C in mehrere unabhängige Schnittstellen.
#   - Ersetze C in jedem Client durch die vom Client tatsächlich verwendeten
#     Schnittstellen.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Car:
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Driver:
    def drive(self, car: Car):
        car.drive()


# %% tags=["keep"]
class Mechanic:
    def work_on(self, car: Car):
        car.repair()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
d = Driver()
m = Mechanic()
c = Car()

# %% tags=["keep"]
d.drive(c)

# %% tags=["keep"]
m.work_on(c)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


# %% tags=["keep"]
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        ...


# %% tags=["keep"]
class Repairable(ABC):
    @abstractmethod
    def repair(self):
        ...


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Car(Drivable, Repairable):
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Driver:
    def drive(self, d: Drivable):
        d.drive()


# %% tags=["keep"]
class Mechanic:
    def work_on(self, r: Repairable):
        r.repair()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
d = Driver()
m = Mechanic()
c = Car()

# %% tags=["keep"]
d.drive(c)

# %% tags=["keep"]
m.work_on(c)
