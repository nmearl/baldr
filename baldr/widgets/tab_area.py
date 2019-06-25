import ipyvuetify as v
from glue_jupyter import jglue
from glue.core import HubListener
from ..core.events import NewProfile1DMessage
from .plot_tabs.profile import ProfileTab


class TabArea(v.Html, HubListener):

    def __init__(self, hub, **kwargs):
        super().__init__(tag='div', style_="height: calc(100vh - 96px)", **kwargs)

        self._current_item = None

        hub.subscribe(self, NewProfile1DMessage, handler=self.add_tab)

        self._tabs = v.Tabs(grow=True)

        self.children = self.children + [self._tabs]

    def register_to_hub(self, hub):
        pass

    def notify(self, message):
        pass

    def add_tab(self, message):
        close_button = v.Btn(icon=True, children=[v.Icon(children=['close'])])
        tab = v.Tab(children=["Profile 1D", v.Spacer(), close_button])

        if isinstance(message, NewProfile1DMessage):
            content = ProfileTab(message.figure)

        close_button.on_event('click.stop', lambda: self.remove_tab())

        self._tabs.children = self._tabs.children + [tab, content]
        # self._items.children = self._items.children + [content]

    def remove_tab(self, tab=None):
        print("Removing tab", tab)

        # children = self.children
        # children.remove(tab)

        self.children = []
