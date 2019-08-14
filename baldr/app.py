import warnings

import ipyvuetify as v
from astropy.utils.exceptions import AstropyWarning
from glue.core import HubListener
from glue_jupyter import JupyterApplication
from traitlets import Unicode

from .core.events import NewProfile1DMessage
from .widgets.content_area import ContentArea
from .widgets.navigation_drawer import NavigationDrawer
from .widgets.toolbar import Toolbar


class Application(v.VuetifyTemplate, HubListener):
    template = Unicode("""
    <v-app>
        <b-navigation-drawer />
        <b-toolbar />
        <b-content-area />
    </v-app>
    """).tag(sync=True)

    def __init__(self, *args, **kwargs):
        self._internal_app = JupyterApplication()

        super().__init__(
            *args, components={
                'b-toolbar': Toolbar(hub=self.hub),
                'b-navigation-drawer': NavigationDrawer(hub=self.hub),
                'b-content-area': ContentArea(hub=self.hub)
                },
            **kwargs)

        filename = '/Users/nearl/data/cubeviz/MaNGA/manga-7495-12704-LOGCUBE.fits'

        with warnings.catch_warnings():
            warnings.simplefilter('ignore', AstropyWarning)
            data = self._internal_app.load_data(filename, auto_merge=False)

        profile = self._internal_app.profile1d(data=data[0], show=False)
        new_profile1d_message = NewProfile1DMessage(profile, sender=self)
        self.hub.broadcast(new_profile1d_message)

    @property
    def hub(self):
        return self._internal_app.data_collection.hub



