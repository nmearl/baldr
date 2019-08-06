"""Top-level application container."""
import ipyvuetify as v
from glue_jupyter import jglue
from glue.core import HubListener, Hub
from glue_jupyter import JupyterApplication
from glue.core import DataCollection

from .widgets import Toolbar, ContentArea, DataList, TabArea, ToolPanel
from .core.events import DataLoadedMessage, NewProfile1DMessage
import click
import asyncio

# from ipygoldenlayout import GoldenLayout


class Application(JupyterApplication, HubListener):
    """
    Main class for the JDAViz application.
    """
    def __init__(self):
        dc = DataCollection()
        super().__init__(dc)

        # Create the main toolbar for the entire application
        self._toolbar = Toolbar(app=True, flat=True)

        # Create the navigation drawer instance
        self._nav_drawer = DataList(self.hub, app=True, z_index=1000)

        self._tab_area = TabArea(self.hub)
        self._advanced_panel = ToolPanel()
        self._content = v.Content(children=[self._tab_area])
        self._app = v.App(children=[self._nav_drawer, self._toolbar, self._content, self._advanced_panel])

        # -- Testing
        filename = '/Users/nearl/data/cubeviz/MaNGA/manga-7495-12704-LOGCUBE.fits'
        data = self.load_data(filename, auto_merge=True)

        self.add_viewer('profile1d', data[2])
        # self.add_viewer('profile1d', data[1])

    def register_to_hub(self, hub):
        pass

    def notify(self, message):
        pass

    def load_data(self, *args, **kwargs):
        data_sets = super().load_data(*args, **kwargs)

        return data_sets

    def add_viewer(self, view_type, data):
        if view_type == 'profile1d':
            fig = self.profile1d(data=data, show=False)
            new_profile1d_message = NewProfile1DMessage(fig, sender=self)

            self.hub.broadcast(new_profile1d_message)

    @property
    def hub(self):
        return self.data_collection.hub

    def show(self):
        div = v.Html(tag='div', children=[self._app])

        return self._app

    def add_profile_view(self):
        view = self._glue_model.profile1d()


async def _app_entry():
    kernel = Kernel(shell_port=8888)
    app = Application()
    msg = app._kernel.execute("import baldr; baldr.__version__")
    print(msg)

# @click.command()
# @click.option('--start')
def start():
    loop = asyncio.get_event_loop()

    try:
        asyncio.ensure_future(_app_entry())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing loop")
        loop.close()


