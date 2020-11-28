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


# canvas.before:
#         Color:
#             rgba: 0, 0, 1, 1
#         Rectangle:
#             pos: self.pos
#             size: self.size
#

###################


###############################
class BuildRequester(BoxLayout):
    chkref = {}

    def on_checkbox_active(self, chkbox, value):
        self.ids.label2.text = 'Selected ' + self.chkref[chkbox]

    def __init__(self, **kwargs):
        super(BuildRequester, self).__init__(**kwargs)
        prods = [' B_0003', ' B_0007', ' B_0008', ' B_0200']

        for i in range(4):
            self.ids.content_grid.add_widget(Label(text=prods[i], italic=True, bold=True id="lbl_indedx_{}".format(i)))
            chkbox = CheckBox(group='1', color=[0.1, 1, 0, 4],id="cb_indedx_{}".format(i))
            chkbox.bind(active=self.on_checkbox_active)
            self.add_widget(chkbox)
            self.chkref[chkbox] = prods[i]

MDCheckbox:
                    id: cb_index_1
                    size_hint: None, None
                    size: "48dp", "48dp"
                    group: "1"
                    on_active: app.root.ids.quiz_screen.on_checkbox_active(*args)

                MDLabel:
                    id: lbl_index_1
                    text: "Mauris et lorem augue. Pellentesque euismod, augue ut tristique tincidunt"
                    font_size: 14

                MDCheckbox:
                    id: cb_index_2
                    size_hint: None, None
                    size: "48dp", "48dp"
                    group: "1"
                    on_active: app.root.ids.quiz_screen.on_checkbox_active(*args)

                MDLabel:
                    id: lbl_index_2
                    text: "Mauris et lorem augue. Pellentesque euismod, augue ut tristique tincidunt"
                    font_size: 14

                MDCheckbox:
                    id: cb_index_3
                    size_hint: None, None
                    size: "48dp", "48dp"
                    group: "1"
                    on_active: app.root.ids.quiz_screen.on_checkbox_active(*args)

                MDLabel:
                    id: lbl_index_3
                    text: "Mauris et lorem augue. Pellentesque euismod, augue ut tristique tincidunt"
                    font_size: 14

                MDCheckbox:
                    id: cb_index_4
                    size_hint: None, None
                    size: "48dp", "48dp"
                    group: "1"
                    on_active: app.root.ids.quiz_screen.on_checkbox_active(*args)

                MDLabel:
                    id: lbl_index_4
                    text: "Mauris et lorem augue. Pellentesque euismod, augue ut tristique tincidunt"
                    font_size: 14