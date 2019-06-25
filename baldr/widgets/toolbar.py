import ipyvuetify as v


__all__ = ['Toolbar']


class Toolbar(v.Toolbar):
    def __init__(self, **kwargs):
        super().__init__(color='teal lighten-3', dark=False, **kwargs)

        self._overflow_button = v.OverflowBtn(label='Create viewer...',
                                              class_='pa-0',
                                              hide_details=True)

        self._file_open_button = v.Btn(icon=True,
                                       fab=False,
                                       children=[
                                           v.Icon(children=['folder_open'])],
                                       # style_="min-width: 0; margin-left: 0; padding-left: 10px; padding-right: 10px"
                                       )
        self._file_save_button = v.Btn(icon=True,
                                       children=[v.Icon(children=['save'])],
                                       # style_="min-width: 0; margin-left: 0; padding-left: 10px; padding-right: 10px"
                                       )

        self._file_group = v.ItemGroup(children=[
            self._file_open_button,
            self._file_save_button
        ])

        self._union = v.Btn(flat=True, children=[v.Icon(children=['view_array'])])
        self._subtract = v.Btn(flat=True, children=[v.Icon(children=['view_carousel'])])
        self._intersect = v.Btn(flat=True, children=[v.Icon(children=['view_column'])])
        self._difference = v.Btn(flat=True, children=[v.Icon(children=['view_day'])])

        self._operator_toggle = v.BtnToggle(class_="transparent", children=[self._union, self._subtract, self._intersect, self._difference])

        self._toolbar_items = v.ToolbarItems(children=[
            self._file_open_button,
            self._file_save_button,
            v.Divider(vertical=True, class_='mx-2'),
            self._overflow_button,
            v.Divider(vertical=True, class_='mx-2'),
            self._operator_toggle
        ])

        # self.add_item(self._toolbar_items)

        self.add_item(self._file_open_button)
        self.add_item(self._file_save_button)
        self.add_item(v.Divider(vertical=True, class_='mx-2'))
        self.add_item(self._overflow_button)
        self.add_item(v.Divider(vertical=True, class_='mx-2'))
        self.add_item(self._operator_toggle)

    def add_item(self, widget):
        """
        Append child widget to the tool.

        Parameters
        ----------
        widget : :class:`~ipyvuetify.VuetifyWidget`
            Widget to be appended.
        """
        # item = v.ToolbarItems(children=[
        #     widget
        # ])

        self.children = self.children + [widget]