class BuildRequester(BoxLayout):
    chkref = {}

    def on_checkbox_active(self, chkbox, value):
        self.ids.label2.text = 'Selected ' + self.chkref[chkbox]

    def __init__(self, **kwargs):
        super(BuildRequester, self).__init__(**kwargs)
        prods = [' B_0003', ' B_0007', ' B_0008', ' B_0200']

        for i in range(4):
            self.add_widget(Label(text=prods[i], italic=True, bold=True))
            chkbox = CheckBox(group='1', color=[0.1, 1, 0, 4])
            chkbox.bind(active=self.on_checkbox_active)
            self.add_widget(chkbox)
            self.chkref[chkbox] = prods[i]
