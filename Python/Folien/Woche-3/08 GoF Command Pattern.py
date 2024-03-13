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
#  <b>GoF: Command Pattern</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 08 GoF Command Pattern.py -->
# <!-- python_courses/slides/module_210_design_patterns/topic_280_command.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispiel: Textverarbeitung
#
# - `Document`-Klasse mit `modify()` und `append()`-Methoden

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from dataclasses import dataclass


# %% tags=["keep"]
@dataclass
class Document:
    state: str = "<empty>"

    def modify(self, change: str | None):
        print("Document.modify()")
        print("  document state before: ", self.state)
        if change is not None:
            self.state = change
        else:
            self.state = "<empty>"
        print("  document state after:  ", self.state)

    def append(self, text: str, times: int = 1):
        print(f"Document::append({text!r}, {times!r})")
        print("  document state before: ", self.state)
        self.state += text * times
        print("  document state after:  ", self.state)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
doc = Document()
doc.modify("Document Template")
doc.append("-append", 3)
doc.modify(None)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Command-Objekte für `Document`
#
# - Wie können wir die Methoden der `Document`-Klasse aufrufen?
# - Verschiedene Aufrufmöglichkeiten:
#   - Menü-System
#   - Toolbar-Buttons
#   - Tastaturkürzel
# - Methoden haben potenziell unterschiedliche Signaturen
# - Wir wollen sie aber möglichst einheitlich handhaben

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod  # noqa: E402


# %%
class CommandV1(ABC):
    @abstractmethod
    def execute(self, doc: Document): ...


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `ModifyCommandV1`

# %%
@dataclass
class ModifyCommandV1(CommandV1):
    change: str | None

    def execute(self, doc: Document):
        doc.modify(self.change)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `AppendCommandV1`

# %% tags=["keep"]
@dataclass
class AppendCommandV1(CommandV1):
    text: str
    times: int = 1

    def execute(self, doc: Document):
        doc.append(self.text, self.times)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwendung

# %%
template_command = ModifyCommandV1("Document Template")
append_command = AppendCommandV1("-append", 3)
clear_command = ModifyCommandV1(None)

# %%
doc = Document()
template_command.execute(doc)
append_command.execute(doc)
clear_command.execute(doc)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Funktionale Implementierung

# %%
def template_fun(doc):
    doc.modify("Document Template")


# %%
from operator import methodcaller  # noqa: E402

append_fun = methodcaller("append", "-append", 3)

# %%
clear_fun = lambda doc: doc.modify(None)  # noqa: E731

# %%
doc = Document()
template_fun(doc)
append_fun(doc)
clear_fun(doc)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class CommandV2(ABC):
    @abstractmethod
    def execute(self): ...


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
@dataclass
class ModifyCommandV2(CommandV2):
    doc: Document
    change: str | None

    def execute(self):
        self.doc.modify(self.change)


# %% tags=["keep"]
@dataclass
class AppendCommandV2(CommandV2):
    doc: Document
    text: str
    times: int = 1

    def execute(self):
        self.doc.append(self.text, self.times)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwendung

# %%
doc = Document()
template_command = ModifyCommandV2(doc, "Document Template")
append_command = AppendCommandV2(doc, "-append", 3)
clear_command = ModifyCommandV2(doc, None)

# %%
template_command.execute()
append_command.execute()
clear_command.execute()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Kommandos mit Undo-Funktionalität

# %% tags=["alt"]
class CommandV3(ABC):  # noqa: F811
    history = []  # Note this is a class variable!

    @staticmethod
    def undo():
        if not CommandV3.history:
            return
        last = CommandV3.history.pop()
        last.undo_execution()

    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo_execution(self): ...


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `ModifyCommandV3`

# %% tags=["alt"]
@dataclass
class ModifyCommandV3(CommandV3):  # noqa: F811
    doc: Document
    change: str | None
    saved_state: str = ""

    def execute(self):
        self.saved_state = self.doc.state
        CommandV3.history.append(self)
        self.doc.modify(self.change)

    def undo_execution(self):
        self.doc.modify(self.saved_state)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `AppendCommandV3`

# %% tags=["alt"]
@dataclass
class AppendCommandV3(CommandV3):  # noqa: F811
    doc: Document
    text: str
    times: int = 1
    saved_state: str = ""

    def execute(self):
        self.saved_state = self.doc.state
        CommandV3.history.append(self)
        self.doc.append(self.text, self.times)

    def undo_execution(self):
        self.doc.modify(self.saved_state)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Verwendung

# %% tags=["keep"]
doc = Document()
template_command = ModifyCommandV3(doc, "Document Template")
append_command = AppendCommandV3(doc, "-append", 3)
clear_command = ModifyCommandV3(doc, None)

# %% tags=["keep"]
template_command.execute()
append_command.execute()
clear_command.execute()

# %%
CommandV3.undo()

# %%
CommandV3.undo()

# %%
CommandV3.undo()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# <img src="img/command_example.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Verbesserte Implementierung

# %% tags=["keep"]
class Command(ABC):  # noqa: F811
    history = []  # Note this is a class variable!
    redo_stack = []

    def __init__(self, doc: Document):
        self.doc = doc
        self.saved_state = ""

    @abstractmethod
    def do_execute(self): ...

    def execute(self):
        Command.redo_stack.clear()
        self._execute_keeping_redo_stack()

    def _undo_execution(self):
        self.doc.modify(self.saved_state)

    def _execute_keeping_redo_stack(self):
        self.saved_state = self.doc.state
        Command.history.append(self)
        self.do_execute()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Undo/Redo

# %% tags=["keep"]
def undo():
    if not Command.history:
        return
    last = Command.history.pop()
    Command.redo_stack.append(last)
    last._undo_execution()  # noqa


# %% tags=["keep"]
def redo():
    if not Command.redo_stack:
        return
    last = Command.redo_stack.pop()
    last._execute_keeping_redo_stack()  # noqa


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `ModifyCommand`

# %%
class ModifyCommand(Command):
    def __init__(self, doc: Document, change: str | None):
        super().__init__(doc)
        self.change = change

    def do_execute(self):
        self.doc.modify(self.change)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### `AppendCommand`

# %%
class AppendCommand(Command):  # noqa: F811
    def __init__(self, doc: Document, text: str, times: int = 1):
        super().__init__(doc)
        self.text = text
        self.times = times

    def do_execute(self):
        self.doc.append(self.text, self.times)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Beispiel-Anwendung

# %% tags=["keep"]
def run_text_processing():
    doc = Document()
    while True:
        print("Document state:", doc.state)
        print("Commands: [m]odify, [a]ppend, [u]ndo, [r]edo, [q]uit")
        user_input = input("Enter command: ")
        if not user_input or user_input.lower().startswith("q"):
            break
        elif user_input.lower().startswith("u"):
            undo()
        elif user_input.lower().startswith("r"):
            redo()
        else:
            command = create_command(doc, user_input)
            command.execute()


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
def create_command(doc: Document, user_input: str) -> Command:
    command, *args = user_input.split()
    if command.lower().startswith("m"):
        new_state = " ".join(args) or "<empty>"
        return ModifyCommand(doc, new_state)
    elif command.lower().startswith("a"):
        text = args[0] if args else "!"
        times = int(args[1]) if len(args) > 1 else 1
        return AppendCommand(doc, text, times)
    else:
        raise ValueError(f"Unknown command: {command}")


# %%
# run_text_processing()

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ### Zweck
#
# Kapselung eines Requests als Objekt, um so die Parametrisierung von Clients
# mit verschiedenen Requests, Warteschlangen- oder Logging-Operationen sowie
# das Rückgängigmachen von Operationen zu ermöglichen.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Auch bekannt als
#
# Action, Transaction

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Motivation
#
# Kommandos in grafischen Benutzeroberflächen
#
# - Können auf mehrere Arten aktiviert werden (Menü, Tastatur, Maus)
# - Sollten oft Undo/Redo unterstützen
# - Sollten geloggt werden können
# - Sollten in Warteschlangen abgelegt werden können
# - Sollten für Macros verwendet werden können

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Mögliche Lösung: Implementierung als Objekt
#
# - Jedes Kommando wird als Objekt implementiert
# - Das Kommando-Objekt kapselt die Operation und ihre Parameter
# - Das Kommando-Objekt bietet eine Methode `execute()`, die die Operation
#   ausführt

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Struktur
#
# <img src="img/pat_command.svg"
#      style="display:block;margin:auto;width:40%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Teilnehmer
#
# - `Command`
#   - Deklariert eine Schnittstelle für das Ausführen einer Operation
# - `ConcreteCommand`
#   - Definiert eine Verbindung zwischen einem `Receiver`-Objekt und einer
#     Operation
#   - Implementiert `execute()` durch Aufruf der entsprechenden Operation(en)
#     auf `Receiver`
# - `Client`
#   - Erstellt ein `ConcreteCommand`-Objekt und setzt dessen `Receiver`
# - `Invoker`
#   - Ruft `execute()` auf `ConcreteCommand` auf um die Anfrage auszuführen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Sequenzdiagramm
#
# <img src="img/pat_command_seq.svg"
#      style="display:block;margin:auto;width:70%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Konsequenzen
#
# - Einfache Erweiterung des Systems durch neue `ConcreteCommand`-Klassen
#   (Open/Closed Principle)
# - Einfache Implementierung von Undo/Redo und anderen erweiterten Funktionen
# - Entkoppelt, das Objekt, das eine Operation auslöst von dem Objekt, das sie
#   ausführt
# - Zusammengesetzte Operationen sind möglich (z.B. Makros, siehe Composite Pattern)

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Implementierung
#
# - Für einfache Szenarien kann eine `SimpleCommand`-Klasse, die einen Zeiger
#   auf eine Funktion oder Methode speichert, verwendet werden
# - ...

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
from document_commands import Document, Command, undo, redo  # noqa
from typing import Callable  # noqa: E402


# %% tags=["keep"]
class SimpleCommand(Command):
    def __init__(self, doc: Document, action: Callable, *args, **kwargs):
        super().__init__(doc)
        self.action = action
        self.args = args
        self.kwargs = kwargs

    def do_execute(self):
        self.action(self.doc, *self.args, **self.kwargs)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
doc = Document()
template_command = SimpleCommand(doc, Document.modify, "Document Template")
append_command = SimpleCommand(doc, Document.append, "-123", 2)
modify_command = SimpleCommand(doc, Document.modify, None)

# %% tags=["keep"]
template_command.execute()
append_command.execute()
modify_command.execute()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
undo()

# %% tags=["keep"]
undo()

# %% tags=["keep"]
redo()

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
SimpleCommand(
    doc, lambda doc, text: doc.modify(f"{text}? {text}!"), "That's new"
).execute()

# %% tags=["keep"]
redo()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Command Pattern
#
# ### Szenario
#
# Banken bieten verschiedene Funktionalitäten an Geldautomaten an, wie
# Kontostand abfragen, Geld abheben, Geld einzahlen und Geld überweisen. In
# unserer Simulation konzentrieren wir uns auf die Einzahlungs- und
# Auszahlungsfunktionen. Wir wollen eine ATM-Software entwerfen, die nicht nur
# diese Transaktionen verarbeitet, sondern auch die letzte Transaktion
# rückgängig machen kann.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Ziel
#
# Ihre Aufgabe ist es, die ATM-Operationen mit dem Command Pattern zu
# implementieren, so dass die Funktionalität des Systems in der Zukunft leicht
# zu erweitern ist, und eine Undo-Funktion für die letzte Transaktion
# bereitzustellen.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
# ### Starter Code

# %% tags=["keep"]
class Account:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.balance}")
        else:
            print(f"Insufficient funds. Current Balance: ${self.balance}")

    def get_balance(self):
        return self.balance


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
from abc import ABC, abstractmethod  # noqa: E402


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
class DepositCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)

    def undo(self):
        print(f"Returning deposit of ${self.amount} to client.")
        self.account.withdraw(self.amount)  # Undo deposit by withdrawing


# %% tags=["alt", "subslide"] slideshow={"slide_type": "subslide"}
class WithdrawCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)

    def undo(self):
        print(f"Asking client to return ${self.amount}.")
        self.account.deposit(self.amount)  # Undo withdrawal by depositing


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
class ATM:
    def __init__(self, initial_balance):
        self.account = Account(initial_balance)
        self.last_command = None

    def deposit(self, amount):
        self.last_command = DepositCommand(self.account, amount)
        self.last_command.execute()

    def withdraw(self, amount):
        self.last_command = WithdrawCommand(self.account, amount)
        self.last_command.execute()

    def undo_last_transaction(self):
        if self.last_command:
            self.last_command.undo()
            self.last_command = (
                None  # Ensure undo can only be called once for the last transaction
            )
        else:
            print("No transaction to undo.")


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
def run_atm():
    atm = ATM(1000)
    atm.deposit(100)
    atm.withdraw(200)
    atm.undo_last_transaction()
    atm.undo_last_transaction()


# %% tags=["subslide", "alt"] slideshow={"slide_type": "subslide"}
run_atm()
