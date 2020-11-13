from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.app import MDApp

Window.size = (320, 800)


class HomeWindow(MDBoxLayout):
    pass


class NavBox(MDGridLayout):
    pass


class ContentArea(MDBoxLayout):
    pass


class HomeApp(MDApp):
    def build(self):
        return HomeWindow()


if __name__ == "__main__":
    HomeApp().run()
