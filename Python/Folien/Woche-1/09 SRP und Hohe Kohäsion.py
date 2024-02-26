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
#  <b>SRP und Hohe Kohäsion</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 SRP und Hohe Kohäsion.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_260_srp_and_high_cohesion_intro.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Aktuelle Implementierung des Adventure-Spiels
#

# %% tags=["keep"]
import json
from dataclasses import dataclass, field
from pathlib import Path
from pprint import pprint
from typing import Any, Mapping, Sequence
from typing import Any, Mapping, Sequence, TypeAlias

# %% tags=["keep"]
json_file = list(Path().glob("**/simple-locations.json"))[0]
with open(json_file) as file:
    simple_locations = json.load(file)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
LocationDescription = Mapping[str, Any]
LocationDescriptions = Sequence[LocationDescription]


# %% tags=["keep"]
@dataclass
class Location:
    name: str
    description: str = ""
    connections: dict[str, "Location"] = field(default_factory=dict)

    @classmethod
    def from_description(cls, data: LocationDescription) -> "Location":
        return cls(data["name"], data.get("description", ""))

    def __getitem__(self, direction: str) -> "Location | None":
        return self.connections.get(direction)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class World:
    locations: dict[str, Location]
    initial_location_name: str

    def __getitem__(self, location_name: str):
        return self.locations[location_name]

    @classmethod
    def from_location_descriptions(cls, location_descriptions: LocationDescriptions):
        locations = {
            data["name"]: Location.from_description(data)
            for data in location_descriptions
        }
        initial_location_name = location_descriptions[0]["name"]
        _build_connections_for_all_locations(locations, location_descriptions)
        return cls(locations, initial_location_name)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def _build_connections_for_all_locations(
    locations: dict[str, Location], location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: locations[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        locations[location_description["name"]].connections = connections


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wie ist diese Implementierung zu bewerten?
#   - Was ist gut?
#   - Was sollten wir noch verbessern?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Generell ist die Struktur gut
# - Ein potenzielles Problem ist, dass wir sehr viel Arbeit in die
#   `World`-Klasse verlagern
# - Das ist typisch, wenn wir "Information Expert" anwenden
# - Wir brauchen einen "Gegenspieler" für dieses Pattern

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Problem: Zu viel Funktionalität in einer Klasse
# - Sowohl SOLID als auch GRASP haben jeweils ein Pattern dafür/dagegen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Single Responsibility Principle (SRP, SOLID)
#
# - Ein Modul sollte nur einen einzigen Grund haben, sich zu ändern
# - Alternative Formulierung: Ein Modul sollte nur gegenüber einem einzigen
#   Aktor verantwortlich sein
# - Der Name kann leicht falsch verstanden werden:
#   - Responsibility-Driven Design (RDD) ist ein etabliertes Vorgehen in der
#     Softwareentwicklung
#   - SRP besagt nicht, dass jede Klasse nur eine einzige Verantwortung (im RDD-Sinne)
#     haben darf

# %% tags=["keep"]
def compute_save_and_print_results(a: int, b: int, results: list) -> int:
    # complex computation...
    new_result = a + b
    # save result to persistent storage...
    results.append(new_result)
    # print report...
    for r in results:
        print(f"Result: {r}")
    # provide information about the new result...
    return new_result


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
my_results = []

# %%
compute_save_and_print_results(1, 2, my_results)

# %%
my_results


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Was sind die Gründe, dass sich diese Funktion ändert?
#
# - Die komplexe Berechnung
# - Das Speichern der Ergebnisse
# - Die Art, in der der Report ausgedruckt wird
# - Die Information, die im Report enthalten ist
# - Die Teile oder Reihenfolge der Berechnung

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def compute_result(a: int, b: int) -> int:
    return a + b


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def save_result(result: int, results: list):
    results.append(result)


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def print_report(results):
    for r in results:
        print(f"Result: {r}")


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
def process_new_sensor_data(a: int, b: int, results: list) -> int:
    new_result = compute_result(a, b)
    save_result(new_result, results)
    print_report(results)
    return new_result


# %%
my_sensor_data = []
process_new_sensor_data(1, 2, my_sensor_data)

# %%
my_sensor_data

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Wir haben die Menge an Code verdoppelt
# - Haben wir wirklich eine Verbesserung erreicht?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Was sind die Gründe, dass sich die neue Funktion ändert?
#
# - <del>Die komplexe Berechnung</del> $\rightarrow$ `compute_result()`
# - <del>Das Speichern der Ergebnisse</del> $\rightarrow$ `save_result()`
# - <del>Die Art, in der der Report ausgedruckt wird</del>
#   $\rightarrow$ `print_report()`
# - <del>Die Information, die im Report enthalten ist</del>
#   $\rightarrow$ `print_report()`
# - Die Teile oder Reihenfolge der Berechnung

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Die neue Funktion hat aber immer noch mehr als eine Verantwortung!
# - Das rührt daher, dass Sie das Command-Query-Separation-Prinzip (CQS)
#   verletzt
#   - Sie hat Seiteneffekte (Speichern und Drucken)
#   - Sie gibt einen Wert zurück (das neue Ergebnis)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Command-Query Separation (CQS)
#
# - Eine Funktion sollte entweder eine Abfrage (Query) oder eine Anweisung
#   (Command) sein, aber nicht beides
# - Eine Abfrage ist eine Funktion, die einen Wert zurückgibt, aber keine
#   beobachtbaren Seiteneffekte hat
# - Eine Anweisung ist eine Funktion, die keine Werte zurückgibt, aber
#   beobachtbare Seiteneffekte hat
# - Eine Funktion, die CQS nicht erfüllt verletzt immer das SRP

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# # GRASP: High Cohesion (Hohe Kohärenz)
#
# - Beschreibt, wie gut verschiedene Teile eines Artefakts zusammenpassen
# - Hohe Kohäsion vereinfacht Entwicklung, Wiederverwendung, Testen, Leistung
# - Niedrige Kohäsion macht es schwierig, den Code zu verstehen oder herauszufinden,
#   wo Änderungen vorgenommen werden sollen
# - Der **negative Effekt** niedriger Kohäsion ist immer **groß**
# - Es ist **schwer**, ein System mit niedriger Kohäsion in einen Zustand mit mehr
#   Kohäsion zu überführen
# - Code Smells: Schrotflinten-Operation (shotgun surgery), divergente Änderungen
#   (divergent change)
# - Verwandt: Schichten, SRP, Command/Query Separation, Aspekte (Separation of
#   Concerns)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Hohe Kohäsion und Tests
#
# - Geringe Kohäsion führt dazu, dass die Systemfunktionalität über das gesamte
#   System "verschmiert" wird
# - Dies führt oft zu einer hohen Kopplung und großen Klassen
# - Diese Klassen lassen sich nur schwer in einen gewünschten Zustand versetzen
# - "Verschmierte Funktionalität"
#   - Erschweren Unit-Tests
#   - Erzwingen die Verwendung vieler Testdoubles
#   - Verringern den Wert von Unit-Tests als Dokumentation
