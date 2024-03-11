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
#  <b>Fehlerbehandlung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 03 Fehlerbehandlung.py -->
# <!-- python_courses/slides/module_170_exceptions/topic_112_a1_handling_exceptions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# # Behandeln von Exceptions
#
# Wir haben die folgende Funktion zur Berechnung ganzzahliger Quadratwurzeln
# definiert, die einen `ValueError` auslöst, falls `n` keine Quadratzahl ist:

# %% tags=["keep"]
def int_sqrt(n: int) -> int:
    for m in range(n + 1):
        if m * m == n:
            return m
    raise ValueError(f"{n} is not a square number.")


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wir konnten diese Funktion dann so verwenden:

# %% tags=["keep"]
def print_int_sqrt_v1(n):
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %% tags=["keep"]
print_int_sqrt_v1(9)


# %% tags=["keep"]
# print_int_sqrt_v1(8)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Wie schreiben wir damit eine `print_int_sqrt()`-Funktion, die keinen Fehler auslöst,
# wenn `n` keine Quadratzahl ist?

# %% tags=["start"]
def print_int_sqrt(n):  # type: ignore
    root = int_sqrt(n)
    print(f"The root of {n} is {root}.")


# %% tags=["keep"]
print_int_sqrt(9)


# %% tags=["keep"]
# print_int_sqrt(8)

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Ausnahmebehandlung
#
# - Ausnahmen können mit einem `try`/`except`-Block behandelt werden
# - Alle "passenden" Ausnahmen, die während der Ausführung des `try`-Blocks
#   ausgelöst werden, führen zur Ausführung des `except`-Blocks
# - Wir sagen, die Ausnahme wurde behandelt
# - Nach der Behandlung der Ausnahme wird das Programm nach dem `try`/`except`-Block
#   weiter ausgeführt

# %% tags=["start", "subslide"] slideshow={"slide_type": "subslide"}
def print_int_sqrt(n):  # type: ignore
    try:
        root = int_sqrt(n)
        print(f"The root of {n} is {root}.")
    except ValueError as error:
        print(error)


# %% tags=["keep"]
print_int_sqrt(9)


# %% tags=["keep"]
print_int_sqrt(8)


# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Workshop: Bank Account (Teil 2)
#
# Wir haben eine Klasse `BankAccount` definiert, die in folgenden Fällen einen
# `ValueError` auslöst:
#
# - Wenn ein neuer `BankAccount` mit negativer `balance` angelegt werden soll.
# - Wenn `deposit` mit einem negativen Wert aufgerufen wird.
# - Wenn `withdraw` mit einem negativen Wert aufgerufen wird oder durch das
#   Abheben des Betrags die `balance` des Kontos negativ werden würde.

# %% [markdown] lang="de"
#
# Testen Sie die Funktionalität der Klasse sowohl für erfolgreiche
# Transaktionen, als auch für Transaktionen, die Exceptions auslösen.
# Behandeln Sie dabei die Ausnahmen, die ausgelöst werden und geben Sie
# eine sinnvolle Nachricht aus.

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError(
                f"Cannot create an account with negative balance: {balance}."
            )
        self.balance = balance

    def __repr__(self):
        return f"BankAccount({self.balance:.2f})"

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError(f"Cannot deposit a negative amount: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError(f"Cannot withdraw a negative amount: {amount}")
        if amount > self.balance:
            raise ValueError(
                f"Cannot withdraw {amount} because it exceeds "
                f"the current balance of {self.balance}."
            )
        self.balance -= amount

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%

# %%

# %%

# %%

# %%
