from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from home import NavBox


class QuizNavBox(NavBox):
    pass


class QuizWindow(MDBoxLayout):
    pass


class QuizApp(MDApp):
    def build(self):
        return QuizWindow()


if __name__ == "__main__":
    QuizApp().run()
