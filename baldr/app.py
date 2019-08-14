import ipyvuetify as v
from glue.core import HubListener
from glue_jupyter import JupyterApplication
from traitlets import Unicode

from .core.events import NewProfile1DMessage, LoadDataMessage
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

        self.hub.subscribe(self, LoadDataMessage, handler=self.add_data)

    @property
    def hub(self):
        return self._internal_app.data_collection.hub

    def add_data(self, msg):
        data = self._internal_app.load_data(msg.file_path, auto_merge=False)

        profile = self._internal_app.profile1d(data=data[0], show=False)
        new_profile1d_message = NewProfile1DMessage(profile, sender=self)
        self.hub.broadcast(new_profile1d_message)

