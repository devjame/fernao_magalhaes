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


###################
MDBoxLayout:
            MDLabel:
                canvas.before:
                    Color:
                        rgba: 1, 0, 0, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y: None
                height: 60
                text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
                bold: True
                font_size: 20
                halign: "center"

            MDGridLayout:
                spacing: 10
                cols: 1 if Window.size[0] <= 460 else 2
                size_hint_y: None
                height:
                MDLabel:
                    text: "Donec mollis viverra lacinia. Sed in purus ligula. Praesent et imperdiet felis, a ornare eros. Proin sapien ipsum, fringilla nec ornare non, gravida non purus. Sed consequat orci a risus suscipit convallis"
                    font_size: 16
                    size_hint_y: None
                    height: 150

                MDLabel:
                    canvas.before:
                        Color:
                            rgba: 1, 0, 0, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    text: str(Window.size)
                    bold: True
                    font_size: 20
                    halign: "center"
                    size_hint_y: None
                    height:
                    size_hint_x: 1 if Window.size[0] <= 460 else .2

                MDLabel:
                    canvas.before:
                        Color:
                            rgba: 0, 0, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    size_hint_y: None
                    height: 200
                    text: "Mauris et lorem augue. Pellentesque euismod, augue ut tristique tincidunt, sem velit porta nibh, eget condimentum ipsum risus eu felis. Morbi non justo blandit, tempor nisi eu, vehicula massa. Ut aliquet nunc viverra, egestas nisl id, pharetra purus. Vestibulum imperdiet sem varius, ornare tellus eu, aliquam massa."
                MDLabel:
                    canvas.before:
                        Color:
                            rgba: 0, 1, 0, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    size_hint_y: None
                    height: 200
                    text: "Cras tristique dapibus enim at faucibus. Nam facilisis mi id mi bibendum, nec eleifend ligula lacinia." *5

###############################
class BuildRequester(BoxLayout):
    chkref = {}
    def on_checkbox_active(self,chkbox,value):
        self.ids.label2.text = 'Selected ' + self.chkref[chkbox]
    def __init__(self, **kwargs):
        super(BuildRequester,self).__init__(**kwargs)
        prods = [' B_0003',' B_0007',' B_0008', ' B_0200']

        for i in range(4):
            self.add_widget(Label(text=prods[i],italic=True,bold=True))
            chkbox = CheckBox(group='1',color=[0.1,1,0,4])
            chkbox.bind(active=self.on_checkbox_active)
            self.add_widget( chkbox)
            self.chkref[chkbox]= prods[i]