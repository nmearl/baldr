import ipyvuetify as v


class ToolPanel(v.NavigationDrawer):
    def __init__(self, **kwargs):
        self._mini = True

        super().__init__(app=True, right=True, clipped=True, mini_variant=True,
                         v_model=self._mini,
                         stateless=True, **kwargs)

        self._mini_toggle_action = v.ListTileAction(children=[v.Btn(icon=True, children=[
            v.Icon(children=['chevron_left'])])])

        self._mini_toggle_action.on_event('click.stop', self.toggle_mini_state)

        self._title_list_tile = v.ListTile(avatar=True, children=[
            v.ListTileAvatar(children=[v.Img(src="https://randomuser.me/api/portraits/men/85.jpg")]),
            v.ListTileContent(children=['Advanced Panel']),
            self._mini_toggle_action
        ])

        self._title_list = v.List(class_='pa0', children=[
            self._title_list_tile
        ])
        self._toolbar = v.Toolbar(flat=True, class_='transparent', children=[
            self._title_list])

        self._info_tile = v.ListTile(children=[
            v.ListTileAction(children=[v.Icon(children=['dashboard'])]),
            v.ListTileContent(children=[v.ListTileTitle(children=['Information'])])
        ])

        self._info_tile.on_event("click", self.toggle_mini_state)

        self._tool_list = v.List(class_='pt-0', dense=True, children=[v.Divider(), self._info_tile])

        self.children = self.children + [self._toolbar, self._tool_list]

    def toggle_mini_state(self):
        print("CLICKING")
        self.mini_variant = not self.mini_variant