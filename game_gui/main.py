from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


from kivy.core.window import Window

Window.size = (320, 800)


class HomeScreen(Screen):
    pass


class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
            print(self.ids.lbl_index_1.text)
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')


class MainApp(MDApp):

    def build(self):
        print(self.root.ids.quiz_screen.ids)
        return Builder.load_file("main.kv")


MainApp().run()
