import curses
import random
import traceback

import npyscreen
from omc.service import omc_service

from omcm.service.omcm_service import OmcResourceAction

# disable ok button, https://github.com/npcole/npyscreen/issues/35
from omcm.widget.inputbox import InputBox
from omcm.widget.outputbox import OutputBox


class MainForm(npyscreen.FormBaseNew):

    def __init__(self, name=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT',
                 widget_list=None, cycle_widgets=False, *args, **keywords):
        super().__init__(name=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None,
                         cycle_widgets=False, *args, **keywords)

    def create(self):
        self.hidden = False
        action = OmcResourceAction(omc_service.exec('omc smax cd150 namespace'.split(), True))

        self.cmd = self.add(InputBox, name="Command", rely=1, height=3, hidden=self.hidden, contained_widget_arguments={
            'name': '>',
            'begin_entry_at': 4,
            'handlers': {
                curses.ascii.NL: self.exec_command,
            }

        })

        self.content = self.add(OutputBox, name="", max_height=-1, editable=False, hidden=False)

        self.status = self.add(npyscreen.FixedText, relx=3, value=' '.join(action.get_commands()), editable=False)

    def set_up_handlers(self):
        self.complex_handlers = []
        self.handlers = {
            curses.KEY_F1: self.h_display_help,
            "KEY_F(1)": self.h_display_help,
            "^O": self.h_display_help,
            "^L": self.h_display,
            "^Q": self.exit_func,
            # curses.ascii.ESC: self.toggle_command,
            curses.ascii.alt(curses.KEY_ENTER): self.exec_command,
            # curses.KEY_ENTER: self.exec_command,
            curses.KEY_RESIZE: self._resize,
        }

    def exit_func(self, _input):
        exit(0)

    def exec_command(self, _input):
        try:
            self.content.set_output(self.cmd.value)
        except Exception as e:
            self.content.set_output(traceback.format_exc())

        self.content.update()

    def do_noting(self, _input):
        curses.beep()
