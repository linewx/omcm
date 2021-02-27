import npyscreen

from omcm.main_form import MainForm


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.MainForm = self.addForm("MAIN", MainForm, framed=False)
