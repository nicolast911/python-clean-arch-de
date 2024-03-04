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
#  <b>SRP: Lösungsansätze</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 11 SRP Lösungsansätze.py -->
# <!-- python_courses/slides/module_500_solid_grasp/topic_280_srp_resolutions.py -->

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Ein Änderungsgrund?
#
# <img src="img/book_01.svg"
#      style="display:block;margin:auto;width:35%"/>
#

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Verletzung des SRPs
#
# <img src="img/book_02.svg"
#      style="display:block;margin:auto;width:60%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def print(self):
        # Lots of code that handles the printer
        print(f"Printing {self.title} to printer.")

    def save(self):
        # Lots of code that handles the database
        print(f"Saving {self.title} to database.")


# %% tags=["keep"]
book = Book("Clean Code", "Robert C. Martin", 464)
book.print()
book.save()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung der SRP-Verletzung (Version 1a)
#
# Vorschlag von Robert C. Martin in Clean Architecture:
#
# <img src="img/book_resolution_1a_srp.svg"
#      style="display:block;margin:auto;width:40%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookV1a:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookPrinterV1a:
    def __init__(self, book):
        self.book = book

    def print(self):
        # Lots of code that handles the printer
        print(f"Printing {self.book.title} to printer.")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookDatabaseV1a:
    def __init__(self, book):
        self.book = book

    def save(self):
        # Lots of code that handles the database
        print(f"Saving {self.book.title} to database.")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
book_v1a = BookV1a("Clean Code", "Robert C. Martin", 464)

# %% tags=["keep"]
book_printer_v1a = BookPrinterV1a(book_v1a)
book_printer_v1a.print()

# %% tags=["keep"]
book_database_v1a = BookDatabaseV1a(book_v1a)
book_database_v1a.save()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung der SRP-Verletzung (Version 1a mit Fassade)
#
# <img src="img/book_resolution_1a_srp_facade.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookPrinterFacadeV1a:
    def __init__(self, book):
        self.book_printer = BookPrinterV1a(book)
        self.book_database = BookDatabaseV1a(book)

    def print(self):
        self.book_printer.print()

    def save(self):
        self.book_database.save()


# %% tags=["keep"]
book_printer_facade_v1a = BookPrinterFacadeV1a(book_v1a)
book_printer_facade_v1a.print()
book_printer_facade_v1a.save()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung der SRP-Verletzung (Version 1)
#
# <img src="img/book_resolution_1_srp.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookV1:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookPrinterV1:
    @staticmethod
    def print(book):
        # Lots of code that handles the printer
        print(f"Printing {book.title} to printer.")


# %% tags=["keep"]
class BookDatabaseV1:
    @staticmethod
    def save(book):
        # Lots of code that handles the database
        print(f"Saving {book.title} to database.")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
book_v1 = BookV1("Clean Code", "Robert C. Martin", 464)
book_printer_v1 = BookPrinterV1()
book_database_v1 = BookDatabaseV1()


# %% tags=["keep"]
book_printer_v1.print(book_v1)

# %% tags=["keep"]
book_database_v1.save(book_v1)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung der SRP-Verletzung (Version 1 mit Facade)
#
# <img src="img/book_resolution_1_srp_facade.svg"
#      style="display:block;margin:auto;width:50%"/>

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
class BookFacadeV1:
    def __init__(self, book):
        self.book = book
        self.book_printer = BookPrinterV1()
        self.book_database = BookDatabaseV1()

    def print(self):
        self.book_printer.print(self.book)

    def save(self):
        self.book_database.save(self.book)


# %% tags=["keep"]
book_facade_v1 = BookFacadeV1(book_v1)

# %% tags=["keep"]
book_facade_v1.print()

# %% tags=["keep"]
book_facade_v1.save()


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Implementierung als Funktionen

# %% tags=["keep"]
def print_book(book):
    # Lots of code that handles the printer
    print(f"Printing {book.title} to printer.")


# %% tags=["keep"]
def save_book(book):
    # Lots of code that handles the database
    print(f"Saving {book.title} to database.")


# %% tags=["keep"]
print_book(book_v1)

# %% tags=["keep"]
save_book(book_v1)


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auflösung der SRP-Verletzung (Version 2)
#
# <img src="img/book_resolution_2_srp.svg"
#      style="display:block;margin:auto;width:60%"/>

# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookV2:
    def __init__(
        self, title: str, author: str, pages: int, book_printer, book_database
    ):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_printer = book_printer
        self.book_database = book_database

    def print(self):
        # Assuming book_printer has a print method takes a BookV2 instance.
        self.book_printer.print(self)

    def save(self):
        # Assuming book_database has a save method takes a BookV2 instance.
        self.book_database.save(self)


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class BookPrinterV2:
    def print(self, book):
        # Lots of code that handles the printer
        print(f"Printing {book.title} to printer.")


# %% tags=["keep"]
class BookDatabaseV2:
    def save(self, book):
        # Lots of code that handles the database
        print(f"Saving {book.title} to database.")


# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
book_v2 = BookV2(
    "Clean Code", "Robert C. Martin", 464, BookPrinterV2(), BookDatabaseV2()
)

# %% tags=["keep"]
book_v2.print()

# %% tags=["keep"]
book_v2.save()

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Vergleich
#
# <div>
# <img src="img/book_resolution_1_srp.svg"
#      style="float:left;padding:5px;width:40%"/>
# <img src="img/book_resolution_2_srp.svg"
#      style="float:right;padding:5px;width:50%"/>
# </div>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: SRP-Verletzung auflösen
#
# - Implementieren Sie die fehlen Funktionalität in Ihrem Bibliothekssystem,
#   falls Sie das noch nicht gemacht haben
# - Untersuchen Sie die Klassen Ihres Bibliothekssystems, ob Sie darin
#   bereits SRP-Verletzungen finden
# - Falls dies der Fall ist, lösen Sie sie auf
