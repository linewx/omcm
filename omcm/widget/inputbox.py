import curses

import npyscreen


class InputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.TitleText

    def __init__(self, screen, contained_widget_arguments=None, *args, **keywords):
        super(InputBox, self).__init__(screen, contained_widget_arguments=None, *args, **keywords)
        if contained_widget_arguments and 'handlers' in contained_widget_arguments:
            self.entry_widget.add_handlers(contained_widget_arguments['handlers'])



