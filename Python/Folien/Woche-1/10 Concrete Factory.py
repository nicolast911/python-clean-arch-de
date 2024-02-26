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
#  <b>Concrete Factory</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 10 Concrete Factory.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_270_adventure_factory.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Adventure Game Version 3b
#
# - Zuweisung von Funktionalität zu `World` und `Location` ist sinnvoll
# - Wir sehen, dass `World` in Gefahr ist, zu viele "Änderungsgründe" zu haben
#   - Änderungen an der Implementierung der Spiele-Welt
#   - Änderungen an den Initialisierungsdaten (z.B. XML statt JSON)
# - Können wir das vermeiden?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Concrete Factory (Simple Factory)
#
# - Einfachere Version des Abstract Factory Patterns aus dem GoF Buch
#
# ### Frage
#
# - Wer soll ein Objekt erzeugen, wenn es Umstände gibt, die gegen Creator
#   sprechen?
#   - komplexe Logik zur Erzeugung
#   - Kohäsion
#   - Viele Parameter zur Erzeugung notwendig
#
# ### Antwort
#
# - Eine Klasse, die nur für die Erzeugung von Objekten zuständig ist
# - Diese Klassen werden oft als *Factory* bezeichnet

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# - Factories sind Beispiele für das GRASP Pattern "Pure Fabrication"
# - Sie können die Kohäsion von Klassen erhöhen und ihre Komplexität reduzieren
# - Sie erhöhen aber auch die Gesamtkomplexität des Systems

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel
#
# - In Version 3b ist der Konstruktor von `World` relativ komplex
# - Wir können die Erzeugung in eine Factory auslagern
# - Siehe `code/adventure/v3c`

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Python: Benannte Parameter Idiom
#
# Das Python-Idiom "Benannte Parameter" (engl. "Named Parameters") ist eine
# Variante des Factory Patterns.
#
# - Python unterstützt keine benannten Parameter
# - Manchmal ist es schwer, Funktionen mit vielen Parametern zu vermeiden
#   - Insbesondere bei der Konstruktion von Objekten
# - Selbst wenn wir Default-Werte verwenden, müssen wir viele der Parameter angeben
#   - Alle Parameter vor demjenigen, den wir ändern wollen
# - Es ist schwer, den Überblick zu behalten, welche Parameter was bedeuten
#   - Moderne IDEs vereinfachen das
# - Wie können wir Funktionen mit vielen Parametern übersichtlich gestalten?

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Benannte Parameter / Builder Pattern
#
# ### Frage
#
# - Wie können wir Funktionen mit vielen Parametern so gestalten, dass sie
#   leicht zu benutzen und verständlich bleiben?
# - Wie können wir Objekte konstruieren, die viel Information zu ihrer Konstruktion benötigen?
#
# ### Antwort
#
# - Wir schreiben eine Hilfsklasse, die die Parameter speichert
# - Diese Klasse hat Methoden, die einzelne Parameter setzen
#   - Jede dieser Methoden gibt `*this` als Referenz zurück
# - Eine Methode konstruiert die gewünschte Klasse oder führt die gewünschte Operation aus

# %% tags=["keep"]
class Window:
    def __init__(
        self,
        width: int,
        height: int,
        x: int,
        y: int,
        visible: bool,
        active: bool,
        resizable: bool,
        fullscreen: bool,
    ):
        print(
            f"Building window with width={width}, height={height}, x={x}, y={y}, visible={visible}, active={active}, resizable={resizable}, fullscreen={fullscreen}"
        )


# %% tags=["keep"]
window = Window(800, 600, 0, 0, True, True, True, False)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Window:
    def __init__(self, width, height, x, y, visible, active, resizable, fullscreen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.visible = visible
        self.active = active
        self.resizable = resizable
        self.fullscreen = fullscreen


class WindowBuilder:
    def __init__(self):
        self._width = 800
        self._height = 600
        self._x = 0
        self._y = 0
        self._visible = True
        self._active = True
        self._resizable = True
        self._fullscreen = False

    def build(self):
        return Window(
            self._width,
            self._height,
            self._x,
            self._y,
            self._visible,
            self._active,
            self._resizable,
            self._fullscreen,
        )

    def width(self, width):
        self._width = width
        return self

    def height(self, height):
        self._height = height
        return self

    def x(self, x):
        self._x = x
        return self

    def y(self, y):
        self._y = y
        return self

    def visible(self, visible):
        self._visible = visible
        return self

    def active(self, active):
        self._active = active
        return self

    def resizable(self, resizable):
        self._resizable = resizable
        return self

    def fullscreen(self, fullscreen):
        self._fullscreen = fullscreen
        return self


# %%
default_window = WindowBuilder().build()

# %%
my_window = WindowBuilder().height(200).resizable(False).build()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Mini-Workshop: Factory im Bibliothekssystem
#
# - Sie haben in vorhergehenden Workshops den Beginn eines Bibliothekssystems
#   implementiert
# - Bei der Erzeugung werden die Daten von Büchern aus einer Datei gelesen (wir
#   simulieren das, durch die `library_data_sk` Python-Bibliothek)
# - Verwenden Sie das Factory Pattern, um die Erzeugung der Bücher von dem Rest
#   des Bibliothekssystems zu trennen
#
# *Hinweis:* Sie können das Factory Pattern entweder für die Erzeugung einer
# Sammlung von Büchern oder für die Erzeugung der Bibliothek verwenden. Gibt es
# erhebliche Vor- oder Nachteile von einer der Varianten oder sind sie im
# Wesentlichen äquivalent?
