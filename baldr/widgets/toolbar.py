import os

from traitlets import Unicode

from ..core.template_mixin import TemplateMixin
from ..core.events import LoadDataMessage

with open(os.path.join(os.path.dirname(__file__), "toolbar.vue")) as f:
    TEMPLATE = f.read()


__all__ = ['Toolbar']


class Toolbar(TemplateMixin):
    template = Unicode(TEMPLATE).tag(sync=True)

    def vue_load_data(self, event):
        new_load_data_message = LoadDataMessage(
            file_path='/Users/nearl/data/cubeviz/MaNGA/manga-7495-12704-LOGCUBE.fits',
            sender=self)
        self.hub.broadcast(new_load_data_message)
