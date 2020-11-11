from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (320, 800)


class HomeWindow(MDBoxLayout):
    pass


class NavBox(MDBoxLayout):
    pass


class HomeApp(MDApp):
    def build(self):
        return HomeWindow()


HomeApp().run()
