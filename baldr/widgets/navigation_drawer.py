import os

from glue.core.message import (DataCollectionAddMessage, )
from traitlets import (Unicode, List, Bool, Int)

from ..core.template_mixin import TemplateMixin

with open(os.path.join(os.path.dirname(__file__), "navigation_drawer.vue")) as f:
    TEMPLATE = f.read()


class NavigationDrawer(TemplateMixin):
    """
    Application navigation drawer containing the lists of data and subsets
    currently in the glue collection.
    """
    drawer = Bool(True).tag(sync=True)
    mini = Bool(False).tag(sync=True)
    data_items = List([]).tag(sync=True)
    subset_items = List([]).tag(sync=True)
    selected = Int(0).tag(sync=True)

    template = Unicode(TEMPLATE).tag(sync=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hub.subscribe(self, DataCollectionAddMessage,
                           handler=self._data_added)

    def _data_added(self, message):
        self.data_items = self.data_items + [{'title': "{}".format(message.data.label),
                                    'icon': 'dashboard'}]
