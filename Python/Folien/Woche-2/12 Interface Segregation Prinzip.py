# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Interface Segregation Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 12 Interface Segregation Prinzip.py -->
# <!-- python_courses/slides/module_280_solid/topic_150_a3_solid_isp.py -->

# %% [markdown]
#
# # SOLID: Interface Segregation Prinzip
#
# - Kein Client einer Klasse C sollte von Methoden abhängen, die er nicht
#   benutzt.
# - Wenn das nicht der Fall ist
#   - Unterteile die Schnittstelle von C in mehrere unabhängige Schnittstellen.
#   - Ersetze C in jedem Client durch die vom Client tatsächlich verwendeten
#     Schnittstellen.

# %%
class Car:
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %%
class Driver:
    def drive(self, car: Car):
        car.drive()


# %%
class Mechanic:
    def work_on(self, car: Car):
        car.repair()


# %%
d = Driver()
m = Mechanic()
c = Car()

# %%
d.drive(c)

# %%
m.work_on(c)


# %%
from abc import ABC, abstractmethod


# %%
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        ...


# %%
class Repairable(ABC):
    @abstractmethod
    def repair(self):
        ...


# %%
class Car(Drivable, Repairable):
    def drive(self):
        print("Accelerating.")

    def repair(self):
        print("Repairing.")


# %%
class Driver:
    def drive(self, d: Drivable):
        d.drive()


# %%
class Mechanic:
    def work_on(self, r: Repairable):
        r.repair()


# %%
d = Driver()
m = Mechanic()
c = Car()

# %%
d.drive(c)

# %%
m.work_on(c)
