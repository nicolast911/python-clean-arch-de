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
#  <b>Dependency Inversion Prinzip</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Dependency Inversion Prinzip.py -->
# <!-- python_courses/slides/module_280_solid/topic_160_a3_solid_dip.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Abhängigkeiten
#
# - Wir müssen zwei Arten von Abhängigkeiten unterscheiden:
#   - Daten- und Kontrollfluss
#   - Quellcode-Abhängigkeiten
# - Daten- und Kontrollfluss-Abhängigkeiten sind inhärent in der Logik
# - Quellcode-Abhängigkeiten können wir durch die Architektur kontrollieren

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel
#
# - Modul `my_module.py` schreibt Daten in eine Datenbank
# - Datenfluss: von `my_module.py` zur Datenbank
# - Quellcode-Abhängigkeit: `my_module.py` hängt von der Datenbank (`sqlite3`) ab

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Modul `my_module.py`:

# %% tags=["keep"]
import sqlite3  # Quellcode-Abhängigkeit


# %% tags=["keep"]
class MyDomainClassV1:
    def __init__(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE my_table (data text)")
        conn.commit()
        self.conn = conn

    def perform_work(self, data: str):
        data = "Processed: " + data
        self.conn.execute("INSERT INTO my_table VALUES (?)", (data,))
        self.conn.commit()

    def retrieve_result(self):
        cur = self.conn.execute("SELECT * FROM my_table")
        return cur.fetchall()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Modul `main.py`:

# %% tags=["keep"]
# from my_module import MyDomainClassV1

my_domain_object = MyDomainClassV1()
my_domain_object.perform_work("Hello World")
print(my_domain_object.retrieve_result())

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Die Quellcode-Abhängigkeit geht in die gleiche Richtung wie der Datenfluss:
#
# `my_module.py` ⟹ `sqlite3`
#
# <img src="img/dependency-01.svg"
#      style="display:block;margin:auto;width:75%"/>


# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir würden derartige Abhängigkeiten im Kern unsere Anwendung gerne vermeiden
#
# - Einfacher zu testen
# - Einfacher zu erweitern
# - Einfacher externe Abhängigkeiten zu ersetzen
# - Einfacher den Code zu verstehen
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/dependency-02.svg"
#      style="display:block;margin:auto;width:75%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Modul `my_module.py`:
#   - Keine Abhängigkeit mehr zu `sqlite3`
#   - Kombination aus Adapter und Strategy Pattern

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


# %% tags=["keep"]
class DatabaseAdapter(ABC):
    @abstractmethod
    def save_object(self, data: str):
        ...

    @abstractmethod
    def retrieve_data(self):
        ...


# %% tags=["keep"]
class MyDomainClassV2:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    def perform_work(self, data: str):
        data = "Processed: " + data
        self.db.save_object(data)

    def retrieve_result(self):
        return self.db.retrieve_data()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Modul `sqlite_adapter.py`:
#   - Implementiert `DatabaseAdapter` für `sqlite3`
#   - Hängt von `sqlite3` ab

# %% tags=["keep"]
import sqlite3


# %% tags=["keep"]
class SqliteAdapter(DatabaseAdapter):
    def __init__(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE my_table (data text)")
        conn.commit()
        self.conn = conn

    def save_object(self, data: str):
        self.conn.execute("INSERT INTO my_table VALUES (?)", (data,))
        self.conn.commit()

    def retrieve_data(self):
        cur = self.conn.execute("SELECT * FROM my_table")
        return cur.fetchall()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Modul `main.py`:

# %% tags=["keep"]
# from my_module import MyDomainClassV2
# from sqlite_adapter import SqliteAdapter


# %% tags=["keep"]
my_domain_object = MyDomainClassV2(SqliteAdapter())
my_domain_object.perform_work("Hello World")
print(my_domain_object.retrieve_result())

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # SOLID: Dependency Inversion Prinzip
#
# - Die Kernfunktionalität eines Systems hängt nicht von seiner Umgebung ab
#   - **Konkrete Artefakte hängen von Abstraktionen ab** (nicht umgekehrt)
#   - **Instabile Artefakte hängen von stabilen Artefakten ab** (nicht umgekehrt)
#   - **Äußere Schichten** der Architektur **hängen von inneren Schichten ab**
#     (nicht umgekehrt)
#   - Klassen/Module hängen von Abstraktionen (z. B. Schnittstellen) ab,
#     nicht von anderen Klassen/Modulen
# - Abhängigkeitsinversion (Dependency Inversion) erreicht dies durch die Einführung
#   von Schnittstellen, die "die Abhängigkeiten umkehren"

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Vorher
# <img src="img/dependency-01.svg"
#      style="display:block;margin:auto;width:75%"/>
#
# ### Nachher
# <img src="img/dependency-02.svg"
#      style="display:block;margin:auto;width:75%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/dip-01.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/dip-02.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown] tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/dip-03.svg"
#      style="display:block;margin:auto;width:95%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel

# %% tags=["keep"]
from dataclasses import dataclass
from pprint import pprint

# %% tags=["keep"]
from augurdb import AugurDatabase


# %% tags=["keep"]
@dataclass
class BadEmployee:
    id: int
    name: str
    database: AugurDatabase

    def save(self):
        self.database.start_transaction()
        self.database.store_field(self.id, "name", self.name)
        self.database.commit_transaction()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
db = AugurDatabase()
be = BadEmployee(123, "Joe", db)

# %% tags=["keep"]
be.save()

# %% tags=["keep"]
pprint(db.records)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Einführen eines Interfaces

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Verwenden des Interfaces

# %% tags=["start"]
@dataclass
class BetterEmployee:
    id: int
    name: str
    database: AugurDatabase

    def save(self):
        self.database.start_transaction()
        self.database.store_field(self.id, "name", self.name)
        self.database.commit_transaction()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Konkrete Implementierung des Interfaces

# %% tags=["keep"]
from dataclasses import dataclass, field

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Wetterbericht
#
# In einem Programm wird ein Wetterbericht von einem Server abgerufen. Leider ist
# dabei die Abhängigkeit zum Server hart kodiert.
#
# - Führen Sie eine Abstraktion ein, um die Abhängigkeit umzukehren
# - Schreiben Sie eine konkrete Implementierung der Abstraktion
# - Testen Sie die Implementierung

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass


# %% tags=["keep"]
@dataclass
class WeatherReport:
    temperature: float
    humidity: float


# %% tags=["keep"]
@dataclass
class WeatherServer:
    def get_weather_report(self) -> WeatherReport:
        from random import random

        return WeatherReport(20 + 10 * random(), 0.5 + 0.5 * random())


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class WeatherReporter:
    def __init__(self, server: WeatherServer):
        self.server: WeatherServer = server

    def report(self):
        report = self.server.get_weather_report()
        if report.temperature > 25:
            return "It's hot"
        else:
            return "It's not hot"


# %% tags=["keep"]
reporter = WeatherReporter(WeatherServer())

# %% tags=["keep"]
reporter.report()


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%
