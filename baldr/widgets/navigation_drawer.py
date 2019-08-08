import ipyvuetify as v


class NavigationDrawer(v.NavigationDrawer):
    """
    Application navigation drawer containing the lists of data and subsets
    currently in the glue collection.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(mini_variant=False, stateless=False, value=True, *args,
                         **kwargs)

        # Navbar toolbar
        self._navigation_toolbar = v.Toolbar(dense=True, flat=True, children=[
            # v.ToolbarItems(children=[
            #     v.Btn(small=True, flat=True, children=[
            #         v.Icon(children=['chevron_left'])
            #     ]),
            #     v.Btn(small=True, flat=True, children=[
            #         v.Icon(children=['chevron_left'])
            #     ]),
            #     v.Btn(small=True, flat=True, children=[
            #         v.Icon(children=['chevron_left'])
            #     ])
            # ])
            v.List(class_='pa-0', children=[
                v.ListTile(children=[
                    v.ListTileAction(children=[
                        v.Btn(icon=True, children=[
                            v.Icon(children=['folder'])
                        ])
                    ]),
                    v.ListTileAction(children=[
                        v.Btn(icon=True, children=[
                            v.Icon(children=['save'])
                        ])
                    ]),
                    v.Spacer(),
                    v.ListTileAction(children=[
                        v.Btn(icon=True, children=[
                            v.Icon(children=['chevron_left'])
                        ])
                    ])
                ])
            ])
        ])

        # List group containing glue data objects
        self._data_list_group = v.ListGroup(prepend_icon='account_circle',
                                            value=True,
                                            no_action=True,
                                            v_model=True)
        self._data_list_group.on_event(
            'click', lambda *args: self.mini_variant_state(*args, False))

        # Chip displaying count of data objects in glue collection
        self._data_count_chip = v.Chip(small=True, children=[
            "{}".format(len(self._data_list_group.children) - 1)
        ])

        # Add data list title tile with associated chip
        self._data_list_group.children = [
            NavigationListTile("Data", children=[
                self._data_count_chip
            ])
        ]

        # List group containing glue subset objects
        self._subset_list_group = v.ListGroup(prepend_icon='account_circle',
                                              value=True,
                                              no_action=True,
                                              v_model=True)
        self._subset_list_group.on_event(
            'click', lambda *args: self.mini_variant_state(*args, False))

        # Chip displaying count of data objects in glue collection
        self._subset_count_chip = v.Chip(small=True, children=[
            "{}".format(len(self._subset_list_group.children) - 1)
        ])

        # Add subset list title tile with associated chip
        self._subset_list_group.children = [
            NavigationListTile("Subsets", children=[
                self._subset_count_chip
            ])
        ]

        # Create primary list and set as main child of navigation drawer
        self._list = v.List()
        self._list.children = [self._navigation_toolbar,
                               self._data_list_group,
                               self._subset_list_group]

        self.children = [self._list]

        # Testing

        self.add_data("Manga [FLUX]")
        self.add_data("Manga [FLUX]")
        self.add_data("Manga [FLUX]")
        self.add_subset("Subset 1 Managa [FLUX]")

    def mini_variant_state(self, widget, event, data, state):
        self.mini_variant = state
        self._data_list_group.v_model = not self.mini_variant
        self._subset_list_group.v_model = not self.mini_variant

    def add_data(self, name):
        """
        Add a data set to be displayed in the data list.
        """
        children = [x for x in self._data_list_group.children]
        data_list_tile = DataListTile(title=name)

        data_list_tile.on_event('click', lambda: None)

        children.append(data_list_tile)
        self._data_list_group.children = children

        # Update the data list chip count
        self._data_count_chip.children = [
            "{}".format(len(self._data_list_group.children) - 1)]

    def add_subset(self, name):
        """
        Add a subset to be displayed in the subset list.
        """
        children = [x for x in self._subset_list_group.children]
        subset_list_tile = SubsetListTile(title=name)

        subset_list_tile.on_event('click', lambda: None)

        children.append(subset_list_tile)
        self._subset_list_group.children = children

        # Update the data list chip count
        self._subset_count_chip.children = [
            "{}".format(len(self._subset_list_group.children) - 1)]


class NavigationListTile(v.ListTile):
    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, slot='activator', **kwargs)

        self._list_tile_title = v.ListTileTitle(children=[title])

        self.children = [self._list_tile_title] + self.children

    def _toggle_state(self, widget, event, data):
        self.value = not self.value


class DataListTile(v.ListTile):
    def __init__(self, title, content=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._list_tile_content = v.ListTileContent(children=[
            v.ListTileTitle(children=[title])
        ])

        self._submenu_button = v.Btn(flat=True, icon=True, slot='activator',
                                     children=[v.Icon(children=['list'])])

        self._submenu = v.Menu(offset_y=True, children=[
            self._submenu_button,
            v.List(dense=True, color='primary',
                   children=[
                       v.ListTile(children=[
                           v.ListTileTitle(children=['Add'])
                       ]),
                       v.ListTile(children=[
                           v.ListTileTitle(children=['Remove'])
                       ])])
        ])

        self._list_tile_action = v.ListTileAction(children=[self._submenu])

        self.children = [self._list_tile_content, self._list_tile_action]


class SubsetListTile(DataListTile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
