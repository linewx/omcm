import npyscreen
from omc.service import omc_service

from omcm.service.omcm_service import OmcResourceAction


class MainForm(npyscreen.TitleForm):
    def create(self):
        action = OmcResourceAction(omc_service.exec('omc smax cd219 namespace'.split(), True))
        # self.add(npyscreen.TitleText, name="  >", rely=-3)
        # self.cmd = self.add(InputBox, name="Input", rely=-3)
        # self.cmd = self.add(npyscreen.BoxBasic, name = "Basic Box:", max_width=30, relx=2, max_height=3)
        self.cmd = self.add(npyscreen.TitleText, name=">", rely=1, begin_entry_at=5)
        self.content = self.add(npyscreen.Pager, max_width=30)
        self.status = self.add(npyscreen.FixedText, rely=-5, value=' '.join(action.get_commands()))
        result = action.execute()

        self.content.values = [result]
