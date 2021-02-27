# choice = random.choice(['1', '2'])
#
# if choice == '5':
#     self.content.entry_widget.clear()
#     self.content._contained_widget = npyscreen.FixedText
#     self.content.make_contained_widget()
#     self.content.entry_widget.values = '666666\nsfsdf\nsfsdf'
#     self.content.entry_widget.value = '66666\nsdfsdf\snsdfsf'
#
# else:
#     self.content.entry_widget.clear()
#     self.content._contained_widget = npyscreen.SimpleGrid
#     self.content.make_contained_widget(contained_widget_arguments={
#         'col_titles': ['name', 'value', 'height', 'weight'],
#     })
#
#     self.content.entry_widget.values = [['sdfsdfsdfsdfsdfsdfsdf\nsdfsdf'],['sfsdfsdfsd']]


# self.content._contained_widget = npyscreen.FixedText
# self.content.make_contained_widget()
# self.content.entry_widget.values = ['13212312312312']
# self.content.entry_widget.value = ['13212312312312']

# gd = self.add(npyscreen.GridColTitles, ma)
# gd.values = []
# for x in range(36):
#     row = []
#     for y in range(x, x+36):
#         row.append(y)
#     gd.values.append(row)
#
# self.content._contained_widget = npyscreen.GridColTitles
# self.content.make_contained_widget()
# # self.content.
# self.content._contained_widget = None
# self.content.values = ['no content', 'no_content12']