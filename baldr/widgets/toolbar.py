import os

from traitlets import Unicode, List, Int

from ..core.template_mixin import TemplateMixin
from ..core.events import LoadDataMessage, DataSelectedMessage

with open(os.path.join(os.path.dirname(__file__), "toolbar.vue")) as f:
    TEMPLATE = f.read()


__all__ = ['Toolbar']


class Toolbar(TemplateMixin):
    template = Unicode(TEMPLATE).tag(sync=True)
    viewers = List(['Profile', 'Image']).tag(sync=True)
    selected_viewer = Int(0).tag(sync=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selected_data = None

        self.hub.subscribe(self, DataSelectedMessage,
                           handler=self._on_data_selected)

    def vue_load_data(self, event):
        new_load_data_message = LoadDataMessage(
            file_path='/Users/nearl/data/cubeviz/MaNGA/manga-7495-12704-LOGCUBE.fits',
            sender=self)
        self.hub.broadcast(new_load_data_message)

    def _on_data_selected(self, msg):
        self._selected_data = msg.data
