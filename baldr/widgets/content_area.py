import ipyvuetify as v

from .tab_area import TabArea


class ContentArea(v.Container):
    def __init__(self, hub, **kwargs):
        super().__init__(class_='grid-list-md', **kwargs)

        self._tab_area = TabArea(hub)
        self._advanced_panel = v.NavigationDrawer(children=['Testing'])

        self._left_flex = v.Flex(class_='xs6', children=[self._tab_area])
        self._right_flex = v.Flex(class_='xs6', children=[self._advanced_panel])

        self._layout = v.Layout(row=True, wrap=True, children=[self._left_flex, self._right_flex])

        self.children = self.children + [self._layout]