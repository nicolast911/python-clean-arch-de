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
#  <b>Aufräumarbeiten mit Finally</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 05 Aufräumarbeiten mit Finally.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_116_a1_finally.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Aufräumarbeiten mit `finally`
#
# - Manchmal ist es nötig, Anweisungen auszuführen, egal ob eine Ausnahme ausgelöst
#   wurde, oder nicht
# - Z.B. wenn Betriebssystem-Ressourcen angefordert wurden, die freigegeben werden
#   müssen

# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
def process_data_from_file(file_name):  # type: ignore
    print(f"Opening file {file_name}")
    try:
        print(f"Processing data from {file_name}...")
        if file_name == "bad.data":
            raise ValueError("Bad data! But recoverable.")
        if file_name == "worse.data":
            raise TypeError("Very bad data! Cannot recover.")
        print("Done.")
    except ValueError as err:
        print(err)
    finally:
        print(f"Closing {file_name}.")


# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
process_data_from_file("good.data")

# %%
# process_data_from_file("bad.data")

# %%
# process_data_from_file("worse.data")

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Freigeben von Ressourcen
#
# Ihr Programm enthält die folgende Klasse, die eine Datenbankverbindung repräsentiert:


# %% tags=["keep"]
class Database:
    def __init__(self):
        self.id = f"db-{id(self) % 100}"
        self.connected = False

    def connect(self):
        print(f"Connecting to database {self.id}.")
        self.connected = True

    def disconnect(self):
        print(f"Disconnecting from database {self.id}.")
        self.connected = False

    def read_data(self):
        if self.connected:
            print(f"Reading data from database {self.id}.")
        else:
            raise RuntimeError("Not connected to database.")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Ihre Anwendung verwendet die Datenbank in einer Funktion `process_data(db: Database)`:

# %% tags=["keep"]
def process_data(db: Database):
    print(f"Processing data with database {db.id}.")
    db.read_data()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Da Datenbankverbindungen viele Ressourcen in der verwendeten Datenbank belegen, muss
# die Verbindung nach ihrer Verwendung wieder mit `disconnect()` freigegeben werden.
#
# Einer Ihrer Kollegen hat versucht das Problem folgendermaßen zu lösen:

# %% tags=["keep"]
def our_great_app():
    db = Database()
    db.connect()
    process_data(db)
    db.disconnect()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Nach einer Änderung der `process_data()` Funktion kommt es immer wieder
# vor, dass Ihr Programm die Datenbankverbindung nicht freigibt.
#
# - Welche Änderung kann zu diesem Verhalten geführt haben?
# - Ändern Sie `process_data()` entsprechend ab, und Testen Sie, dass
#   die Datenbankverbindung wirklich nicht freigegeben wird:


# %% tags=["alt"]
def process_data(db: Database):  # noqa
    print(f"Processing data with database {db.id}.")
    # db.read_data()
    raise ValueError("Error reading Data!")


# %% tags=["keep"]
# our_great_app()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Modifizieren Sie `our_great_app()` so, dass dieser Fehler vermieden wird.
# - Implementieren Sie die Lösung so, dass sie das Problem auch bei zukünftigen
#   Änderungen vermeiden.
# - Testen Sie, dass die Datenbankverbindung jetzt wirklich freigegeben wird.

# %% tags=["alt"]
def our_great_app():  # noqa
    db = Database()
    db.connect()
    try:
        process_data(db)
    finally:
        db.disconnect()


# %%
# our_great_app()
