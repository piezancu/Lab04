import flet as ft
import controller as ct

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch (.Text(..) serve ad aggiungere del testo alla pagina Page)
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # ROW 1
        def lingua_selezionata(e):
            self._linguaSelez.value = f"La lingua selezionata è:  {self._ddLingua.value}"
            self.page.update()
        self._linguaSelez = ft.Text()
        self._ddLingua = ft.Dropdown(label="Lingua",
                                     options=[
            ft.dropdown.Option("Italiano"),
            ft.dropdown.Option("Inglese"),
            ft.dropdown.Option("Spagnolo")], on_change=lingua_selezionata)
        row1 = ft.Row([self._ddLingua, self._linguaSelez])

        # ROW 2
        def metodo_selezionato(e):
            self._metodoSelez.value = f"Il metodo selezionato è:  {self._ddMetodo.value}"
            self.page.update()
        self._metodoSelez = ft.Text(width=150)
        self._ddMetodo = ft.Dropdown(label="Metodo di ricerca",
                                     options=[
            ft.dropdown.Option("Default"),
            ft.dropdown.Option("Linear"),
            ft.dropdown.Option("Dichotomic")], on_change=metodo_selezionato, width=150)
        self._scriviTesto = ft.TextField(label="inserisci il testo", width=300)
        def handleSpellCheck(e):
            testo = self._scriviTesto.value
            lingua_selez = self._ddLingua.value
            if lingua_selez == "Italiano":
                lingua = "italian"
            elif lingua_selez == "Inglese":
                lingua = "english"
            elif lingua_selez == "Spagnolo":
                lingua = "spanish"
            metodo = self._ddMetodo.value
            valori_validi = True
            if testo == None:
                valori_validi = False
                self._lvOut.controls.append(ft.Text("Nessun testo da tradurre", color="red"))
            if lingua == None:
                valori_validi = False
                self._lvOut.controls.append(ft.Text("Non hai selezionato la lingua", color="red"))
            if metodo == None:
                valori_validi = False
                self._lvOut.controls.append(ft.Text("Non hai selezionato il metodo di controllo ortografico", color="red"))
            if valori_validi:
                self._lvOut.controls.append(ft.Text(f"Frase inserita: {testo}"))
                parole_errate, tempo_impiegato = ct.SpellChecker(self).handleSentence(testo, lingua, metodo)
                self._lvOut.controls.append(ft.Text(f"Parole errate: {parole_errate}\nTempo impiegato: {tempo_impiegato}"))
            self.page.update()
        self._bottoneDiRicerca = ft.ElevatedButton(text="Verifica ortografia", on_click=handleSpellCheck)

        row2 = ft.Row([self._ddMetodo, self._metodoSelez, self._scriviTesto, self._bottoneDiRicerca])

        #ROW 3
        self._lvOut = ft.ListView()
        row3 = ft.Row([self._lvOut])

        # ora aggiungo i controlli che ho definito nelle diverse rige
        # della pagina tramite il comando .add()
        self.page.add(row1, row2, row3)

        # aggiorno la pagina così da visualizzare tutte le righe aggiunte
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
