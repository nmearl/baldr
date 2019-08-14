import os

from ipygoldenlayout import GoldenLayout
from traitlets import Unicode

from ..core.events import NewProfile1DMessage
from ..core.template_mixin import TemplateMixin

with open(os.path.join(os.path.dirname(__file__), "tab_area.vue")) as f:
        TEMPLATE = f.read()


class TabArea(TemplateMixin):
    template = Unicode(TEMPLATE).tag(sync=True)

    def __init__(self, *args, **kwargs):
        self._golden_layout = GoldenLayout()

        super().__init__(*args, components={'b-golden-layout':
            self._golden_layout, **kwargs})

        self.hub.subscribe(self, NewProfile1DMessage, handler=self.vue_add_child)

    def vue_add_child(self, event):
        self._golden_layout.children = [t]
