from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager


class BaseScreen(MDScreen):
    pass


class HomeScreen(MDScreen):
    pass


class QuizScreen(MDScreen):
    pass


class MyScreenManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        return MyScreenManager()


MainApp().run()
