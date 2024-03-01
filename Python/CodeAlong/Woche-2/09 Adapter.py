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
#  <b>Adapter</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
# <!-- 09 Adapter.py -->
# <!-- python_courses/slides/module_210_design_patterns/topic_190_adapter.py -->

# %% [markdown] lang="de" tags=["slide"] slideshow={"slide_type": "slide"}
#
# ## Zweck
#
# - Anpassung der Schnittstelle einer Klasse an ein erwartetes Interface
# - Zusammenarbeit von Klassen, die aufgrund inkompatibler Schnittstellen nicht
#   zusammenarbeiten können

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Auch bekannt als
#
# - Wrapper

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Motivation
#
# - Nutzung einer Bibliotheks-Klasse aufgrund inkompatibler Schnittstellen nicht möglich
# - Beispiel: Grafischer Editor
#   - Grafik-Objekte sind relativ einfach zu realisieren
#   - Text ist komplexer, möglicherweise ist der Einsatz einer externen Bibliothek
#     sinnvoll
# - Die Schnittstelle dieser Bibliothek ist nicht kompatibel mit der Schnittstelle,
#   die unser Editor erwartet
# - Mit einem Adapter können wir die Schnittstelle der Bibliothek an die
#   Schnittstelle unseres Editors anpassen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# <img src="img/PlantUML/adapter-example.svg"
#      style="display:block;margin:auto;width:80%"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Anwendbarkeit
#
# - Nutzung einer bestehenden Klasse mit inkompatibler Schnittstelle
# - [...]

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Struktur
#
# - Es werden zwei Varianten definiert: Klassenadapter und Objektadapter
# - Klassenadapter verwenden Mehrfachvererbung und werden seltener eingesetzt
# - Klassendiagramm für Objektadapter:
#
# <img src="img/PlantUML/pat_adapter.svg"
#      style="display: block; margin: auto; width: 80%;"/>

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Teilnehmer
#
# - **Client**
#   - Nutzt das Interface von Target
# - **Target**
#   - Definiert das Interface, das vom Client verwendet wird
# - **Adapter**
#   - Implementiert das Interface von Target und hält eine Referenz auf das Adaptee
# - **Adaptee**
#   - Die Klasse, deren Schnittstelle angepasst werden soll

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Interaktionen
#
# - Der Client ruft eine Target-Methode auf einem Adapter-Objekt auf
# - Der Adapter ruft die entsprechende Methode auf dem Adaptee auf

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Konsequenzen
#
# - Klassenadapter
#   - ...
# - Objektadapter
#   - ein Adapter kann mit mehreren adaptierten Objekten zusammenarbeiten
#   - erschwert das Überschreiben von Adaptee-Methoden

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Weitere Konsequenzen
#
# - Anpassungsaufwand variiert je nachdem, wie unterschiedlich die Schnittstellen sind
# - Klassen mit integrierter Schnittstellenanpassung (pluggable Adapters)
# - 2-Wege-Adapter, wenn verschiedene Clients das gleiche Objekt adaptieren müssen

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Implementierung
#
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Beispielcode

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %% tags=["subslide", "keep"] slideshow={"slide_type": "subslide"}
_legacy_employee_1 = LegacyEmployee("John", "Doe", 1500.0)
_employee_1 = LegacyEmployeeAdapter(_legacy_employee_1)
_employee_1


# %% tags=["keep"]
_legacy_employee_2 = LegacyEmployee("Jane", "Miller", 2000.0)
_employee_2 = LegacyEmployeeAdapter(_legacy_employee_2)
_employee_2

# %% tags=["keep"]
_company = Company([_employee_1, _employee_2])
_company

# %%

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Praxisbeispiele
#
# - ET++ Draw
# - InterViews 2.6
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Verwandte Muster
#
# - Bridge: ähnliche Struktur, aber andere Absicht (Trennung von Schnittstelle und
#   Implementierung)
# - Decorator: erweitert anderes Objekt, ohne die Schnittstelle zu ändern
# - Proxy: Stellvertreter für ein Objekt, das die gleiche Schnittstelle hat

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Python-Implementierung
#
# - Python bietet Sprachfeatures, die die Implementierung von Adaptern in manchen Fällen
#   vereinfachen können
# - Monkey Patching
#   - Methoden können nach der Definition zu einem Objekt hinzugefügt werden
# - ...

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ### Monkey Patching
#
# - Methoden können nach der Definition zu einem Objekt hinzugefügt werden

# %%

# %%

# %%

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}

# %%

# %%

# %%


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# ## Workshop: Einheitliche Schnittstelle für einen Chat-Client
#
# In diesem Workshop soll eine einheitliche Schnittstelle für einen Chat-Client
# implementiert werden. Der Chat-Client soll mit verschiedenen Messaging-Diensten wie
# SMS, E-Mail und einem In-App-Chat-System kommunizieren können. Die Herausforderung
# besteht darin, dass jeder dieser Dienste seine eigene Art hat, Nachrichten zu senden
# und zu empfangen.
#
# Ihre Aufgabe ist es, den Adapter-Entwurf zu verwenden, um eine gemeinsame
# Kommunikationsschnittstelle für all diese Dienste zu erstellen. Auf diese Weise kann
# die Hauptanwendungslogik Nachrichten einheitlich senden und empfangen, unabhängig vom
# zugrundeliegenden Dienst, der verwendet wird.


# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Im Folgenden finden Sie den Startercode mit separaten Klassen für jeden
# Messaging-Dienst.
#
# Ihre Aufgabe ist es, Adapter für diese Klassen zu erstellen, damit sie von der
# Chat-Anwendung auf einheitliche Weise verwendet werden können.
#
# Bitte stellen Sie sicher, dass Ihre Lösung diese Richtlinien befolgt:
#
# - Es sollte das Adapter-Muster verwenden, um eine gemeinsame Schnittstelle für alle
#   Messaging-Dienste zu erstellen.
# - Die Schnittstelle sollte Methoden zum Senden und Empfangen von Nachrichten
#   bereitstellen.
# - Die Chat-Anwendung sollte nicht über die spezifischen Details jedes
#   Messaging-Dienstes Bescheid wissen. Stattdessen sollte sie mit allen Diensten über
#   die gemeinsame Schnittstelle interagieren.

# %% [markdown] lang="de" tags=["subslide"] slideshow={"slide_type": "subslide"}
#
# Nachdem Sie die Adapter erstellt haben, demonstrieren Sie deren Verwendung, indem Sie
# eine Chat-Anwendung erstellen, die Nachrichten über alle verfügbaren Dienste sendet
# und empfängt. Die Anwendung sollte dies unter Verwendung der gemeinsamen Schnittstelle
# tun, ohne direkt Methoden aufzurufen, die spezifisch für jeden Dienst sind.
#
# Viel Erfolg!

# %% tags=["keep"]
class SMS:
    def __init__(self):
        self.service_name = "SMS"

    def send_text(self, number, message):
        print(f"Sending text to {number} via {self.service_name}: {message}")

    def receive_text(self, number):
        print(f"Receiving a text from {number} via {self.service_name}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class Email:
    def __init__(self):
        self.service_name = "Email"

    def send_email(self, email_address, subject, message):
        print(
            f"Sending email to {email_address} with subject {subject!r} "
            f"via {self.service_name}: {message}"
        )

    def receive_email(self, email_address):
        print(f"Receiving an email from {email_address} via {self.service_name}")


# %% tags=["keep", "subslide"] slideshow={"slide_type": "subslide"}
class InAppChat:
    def __init__(self):
        self.service_name = "In-App Chat"

    def send_message(self, username, message):
        print(f"Sending message to {username} via {self.service_name}: {message}")

    def receive_message(self, username):
        print(f"Receiving a message from {username} via {self.service_name}")

# %% tags=["subslide"] slideshow={"slide_type": "subslide"}
