import npyscreen

from omcm.widget.inputbox import InputBox


class MainForm(npyscreen.FormBaseNew):
    def create(self):
        # self.cmd = self.add(InputBox, name="Input", rely=-7, relx=100)
        self.cmd = self.add(npyscreen.BoxBasic, name = "Basic Box:", max_width=30, relx=2, max_height=3)