from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (320, 800)


class Alistamento(Screen):
    text_field = ObjectProperty()
    ingreso = ObjectProperty()
    info_partida = ObjectProperty()

    def __init__(self, **kwargs):
        super(Alistamento, self).__init__(**kwargs)

    def mostrar_documento(self, *args):
        documento = f"Eu, {self.text_field.text} comprometo-me a ingressar nesta viagem sobre o commando do capitão Fernão de Maglhães, visando " \
                    "descobrir uma nova rota para as ilhas Molucas."
        self.ingreso.text = documento
        self.info_partida.text = "-> Dia da Partida: 8  de Agosto de 1519.\n -> Horas: 06:00H\n -> Porto de Sivilha"


class HomeScreen(Screen):
    pass


class QuizScreen(Screen):
    pass


class BoxOpcao(MDGridLayout):

    chkref = {}

    def __init__(self, **kwargs):
        super(BoxOpcao, self).__init__(**kwargs)
        self.dialog = None
        self.opcao = [
            "Curioso para saber mais, dirijeste à mesa onde falam da grande viagem e é te proposto que te alistes nesta demanda dirigida por Frenão de Magalhães, um capitão Português",
            "Continuas a beber a tua cerveja e no dia seguinte voltas à tua rotina de marinheiro miserável até ao fim dos teus dias",
        ]
        for i in range(len(self.opcao)):
            self.lbl = MDLabel(text=self.opcao[i], font_size=14, valign="middle", size_hint_x=.9)
            self.chkbox = MDCheckbox(group='opçao', color=[0.1, 1, 0, 4], size_hint=(None, None), size=("48dp", "48dp"),
                                     pos_hint={"y": .4})
            self.chkbox.bind(active=self.on_checkbox_active)

            self.container = MDBoxLayout(size_hint_x=.1)
            self.container.add_widget(self.chkbox)
            self.add_widget(self.container)
            self.add_widget(self.lbl)

            self.chkref[self.chkbox] = self.opcao[i]
            print(self.chkbox.y)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print(f"{checkbox} -> {self.chkref[checkbox]}")


class MainApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")


MainApp().run()
