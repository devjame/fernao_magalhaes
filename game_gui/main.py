from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


from kivy.core.window import Window

Window.size = (320, 800)


class HomeScreen(Screen):
    pass


class QuizScreen(Screen):
    pass


class Manager(ScreenManager):
    pass


class MainApp(MDApp):

    def print_ids(self, *args):
        print(self.root.ids)

    def build(self):
        # add the layout
        self.print_ids()
        home_screen = HomeScreen()
        quiz_screen = QuizScreen()
        manager = Manager(id="screen_manager")
        manager.add_widget(home_screen)
        manager.add_widget(quiz_screen)
        return manager


MainApp().run()
