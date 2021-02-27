import curses
import json

import npyscreen


class OutputBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.SimpleGrid

    def __init__(self, screen, contained_widget_arguments=None, *args, **keywords):
        super(OutputBox, self).__init__(screen, contained_widget_arguments=None, *args, **keywords)
        if contained_widget_arguments and 'handlers' in contained_widget_arguments:
            self.entry_widget.add_handlers(contained_widget_arguments['handlers'])

    def set_output(self, output):
        if isinstance(output, list):
            super(OutputBox, self).set_values(output)
        elif isinstance(output, str):
            super(OutputBox, self).set_values(self._format_string(output))
        else:
            output_string = self._format_string(json.dumps(output, indent=2))
            super(OutputBox, self).set_values(self._format_string(output_string))

    def _format_string(self, value):
        if value:
            return [[one] for one in value.splitlines()]
