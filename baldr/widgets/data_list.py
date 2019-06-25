import ipyvuetify as v

from glue.core import HubListener
from glue.core.message import (DataCollectionAddMessage, )


class DataList(v.NavigationDrawer, HubListener):

    def __init__(self, hub, **kwargs):
        super().__init__(**kwargs)

        hub.subscribe(self, DataCollectionAddMessage, handler=self._data_added)

        self._data_elements = []
        self._subset_elements = []

        data_subheader = v.Subheader(children=["Data"])
        self._data_list = v.List(two_line=True, children=[data_subheader])
        self._data_elements.append(data_subheader)

        subset_subheader = v.Subheader(children=["Subsets"])
        self._subset_list = v.List(two_line=True, children=[subset_subheader])
        self._subset_elements.append(subset_subheader)

        layout = v.Layout(column=True, fill_height=True, children=[self._data_list, self._subset_list])

        self.children = self.children + [layout]

    def register_to_hub(self, hub):
        pass

    def notify(self, message):
        pass

    def _data_added(self, message):
        data = message.data

        divider = v.Divider(inset=False)

        data_list_tile = DataListTile(data)

        self._data_list.children = self._data_list.children + [data_list_tile, divider]


class DataListTile(v.ListTile):
    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)

        self._data = data

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

        self._action = v.ListTileAction(children=[self._submenu])

        self._title = v.ListTileTitle(
            children=[data.label])
        self._subtitle = v.ListTileSubTitle(
            children=["Size: {}".format(data.size)])
        self._content = v.ListTileContent(
            children=[self._title, self._subtitle])

        self.children = self.children + [self._content, self._action]
