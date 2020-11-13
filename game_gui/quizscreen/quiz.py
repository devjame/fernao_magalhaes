from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import fernao_magalhaes.game_gui.homescreen.home as hs_name


class QuizNavBox(hs_name.NavBox):
    pass


class QuizWindow(MDBoxLayout):
    pass


class QuizApp(MDApp):
    def build(self):
        return QuizWindow()


if __name__ == "__main__":
    QuizApp().run()
