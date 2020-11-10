from kivymd.app import MDApp
from kivy.lang import Builder
layout = """
MDBoxLayout:
    orientation: 'vertical'
    Label:
        text: 'this on top'
    Label:
        text: 'this right aligned'
        size_hint_x: None
        size: self.texture_size
        pos_hint: {'right': 1}
    Label:
        text: 'this on bottom'
"""


class TestAPP(MDApp):
    def build(self):
        return Builder.load_string(layout)



TestAPP().run()
canvas.before:
        Color:
            rgba: 0, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size