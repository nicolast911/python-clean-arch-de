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
#  <b>Strategie</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 Strategie.py -->
# <!-- python_courses/slides/module_210_design_patterns/topic_200_strategy.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Zweck
#
# - Austauschbare Algorithmen / austauschbares Verhalten
# - Algorithmen unabhängig von Klassen, die sie verwenden


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Auch bekannt als
#
# Policy

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Motivation
#
# - Wir wollen einen Text in einem Feld mit begrenzter Breite darstellen
# - Dafür gibt es verschiedene Möglichkeiten:
#   - Abschneiden nach einer bestimmten Anzahl von Zeichen (mit/ohne Ellipse)
#   - Umbruch nach einer bestimmten Anzahl von Zeichen
#     - Umbruch mitten im Wort
#     - Umbruch bei Leerzeichen (greedy/dynamische Programmierung)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Struktur
#
# <img src="img/pat_strategy.svg"
#      style="display:block;margin:auto;width:80%"/>


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Teilnehmer
# - `Strategy`
#   - gemeinsames Interface für alle unterstützten Algorithmen
# - `ConcreteStrategy`
#   - implementiert den Algorithmus
# - `Context`
#   - wird mit einem `ConcreteStrategy`-Objekt konfiguriert
#   - kennt sein `Strategy`-Objekt
#   - optional: Interface, das der Strategie Zugriff die Kontext-Daten ermöglicht


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class Context:
    def __init__(self, strategy: "Strategy"):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface(self)

    def get_data_for_algorithm(self):
        return ...


# %% tags=["keep"]
from abc import ABC, abstractmethod


# %% tags=["keep"]
class Strategy(ABC):
    @abstractmethod
    def algorithm_interface(self, context: Context): ...


# %% tags=["keep"]
class ConcreteStrategy(Strategy):
    def algorithm_interface(self, context: Context):
        data = context.get_data_for_algorithm()
        ...


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Interaktionen
#
# - Strategie und Kontext interagieren, um den gewählten Algorithmus zu implementieren.
#   - Kontext kann Daten an Strategie übergeben
#   - Kontext kann sich selber an Strategie übergeben
# - Ein Kontext leitet Anfragen seiner Clients an seine Strategie weiter. [...]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Implementierung
#
# - `ConcreteStrategy` benötigt effizienten Zugriff auf alle benötigten Daten
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispielcode: Textumbruch

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod


# %% tags=["keep"]
class TextWrapStrategy(ABC):
    @abstractmethod
    def wrap(self, text: str, width: int) -> list[str]: ...


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class TruncationStrategy(TextWrapStrategy):
    def wrap(self, text: str, width: int) -> list[str]:
        if len(text) <= width:
            return [text]
        return [text[: width - 3] + "..."]


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class BreakAnywhereStrategy(TextWrapStrategy):
    def wrap(self, text: str, width: int) -> list[str]:
        lines = []
        while len(text) > width:
            lines.append(text[:width])
            text = text[width:]
        lines.append(text)
        return lines


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BreakOnSpaceStrategy(TextWrapStrategy):
    def wrap(self, text: str, width: int) -> list[str]:
        import textwrap

        return textwrap.wrap(text, width)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BlogPost:
    def __init__(self, author: str, title: str, text: str):
        self.author = author
        self.title = title
        self.text = text


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Blog:  # type: ignore
    def __init__(self, strategy: TextWrapStrategy):
        self.posts = []
        self.strategy = strategy

    def print(self, width: int) -> None:
        for post in self.posts:
            print(f"{'-' * width}")
            print(f"Title: {post.title}")
            print(f"Author: {post.author}")
            for line in self.strategy.wrap(post.text, width):
                print(line)
            print(f"{'-' * width}")

    def add_post(self, author: str, title: str, text: str) -> None:
        self.posts.append(BlogPost(author, title, text))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
blog = Blog(TruncationStrategy())

# %% tags=["keep"]
blog.add_post("John Doe", "My first post", "This is my first post. " * 8)
blog.add_post("Jane Doe", "My second post", "This is my second post. " * 12)

# %% tags=["keep"]
blog.print(40)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
blog.strategy = BreakAnywhereStrategy()

# %% tags=["keep"]
blog.print(40)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
blog.strategy = BreakOnSpaceStrategy()

# %% tags=["keep"]
blog.print(40)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Anwendbarkeit
#
# - Konfiguration von Objekten mit einer von mehreren Verhaltensweisen
# - Verschiedene Varianten eines Algorithmus
# - Kapseln von Daten mit Algorithmus (Client muss Daten nicht kennen)
# - Vermeidung von bedingten Anweisungen zur Auswahl eines Algorithmus

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class ContentManagementSystemWithConditional:
    def __init__(self, content_kind: str):
        self.content_kind = content_kind

    def publish(self, content: str) -> None:
        if self.content_kind == "summary":
            self.publish_summary(content)
        elif self.content_kind == "full":
            self.publish_full(content)
        else:
            raise ValueError("Unknown content kind")

    def publish_summary(self, content: str) -> None: ...

    def publish_full(self, content: str) -> None: ...


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class PublishingStrategy(ABC):
    @abstractmethod
    def publish(self, content: str) -> None: ...


# %% tags=["keep"]
class SummaryPublishingStrategy(PublishingStrategy):
    def publish(self, content: str) -> None: ...


# %% tags=["keep"]
class FullPublishingStrategy(PublishingStrategy):
    def publish(self, content: str) -> None: ...


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class ContentManagementSystemWithStrategy:
    def __init__(self, strategy: PublishingStrategy):
        self.strategy = strategy

    def publish(self, content: str) -> None:
        self.strategy.publish(content)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konsequenzen
#
# - Familien wiederverwendbarer, verwandter Algorithmen
# - Alternative zu Vererbung
# - Auswahl einer Strategie ohne bedingte Anweisungen
# - Context/Clients muss die möglichen Strategien kennen
# - Kommunikations-Overhead zwischen Strategie und Kontext
# - Erhöhte Anzahl von Objekten

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Python Implementierung
#
# In Python kann das Strategy Pattern oft einfach durch ein Funktions-Attribut
# implementiert werden:

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from typing import Callable
import textwrap


# %% tags=["start"]
class Blog:  # type: ignore
    def __init__(self, strategy: TextWrapStrategy):
        self.posts = []
        self.strategy = strategy

    def print(self, width: int) -> None:
        for post in self.posts:
            print(f"{'-' * width}")
            print(f"Title: {post.title}")
            print(f"Author: {post.author}")
            for line in self.strategy.wrap(post.text, width):
                print(line)
            print(f"{'-' * width}")

    def add_post(self, author: str, title: str, text: str) -> None:
        self.posts.append(BlogPost(author, title, text))


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def truncate_lines(text: str, width: int) -> list[str]:
    if len(text) <= width:
        return [text]
    return [text[: width - 3] + "..."]


# %% tags=["keep"]
blog = Blog(truncate_lines)

# %% tags=["keep"]
blog.add_post("John Doe", "My first post", "This is my first post. " * 8)
blog.add_post("Jane Doe", "My second post", "This is my second post. " * 12)

# %% tags=["keep"]
blog.print(40)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
blog.strategy = lambda text, width: (
    [text[: width - 3] + "..."] if len(text) > width else [text]
)

# %% tags=["keep"]
blog.print(40)

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
blog.strategy = textwrap.wrap

# %% tags=["keep"]
blog.print(40)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Mini-Workshop: Vorhersagen
#
# Sie wollen ein System schreiben, das Vorhersagen für Aktienkurse treffen kann.
#
# Schreiben Sie dazu eine Klasse `Predictor` mit einer Methode
#
# ```python
# predict(self, values: list[float]) -> float
# ```
#
# Verwenden Sie das Strategy Pattern, um mindestens zwei verschiedene
# Vorhersage-Varianten zu ermöglichen:
#
# - Die Vorhersage ist der Mittelwert aller Werte aus `values`
# - Die Vorhersage ist der letzte Wert in `values` (oder 0, wenn `values` leer ist)

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
