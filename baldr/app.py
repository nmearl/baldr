from glue.core import HubListener, Hub
from glue_jupyter import JupyterApplication
from glue.core import DataCollection
import ipyvuetify as v


class Application(v.App, HubListener):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Instantiate the main glue-jupyter application object
        self._glupyter = JupyterApplication()

        # Setup the main toolbar
        self._toolbar = v.Toolbar(app=True, clipped_left=True)

        # Create the navigation drawers
        self._navigation_drawer = v.NavigationDrawer(clipped=True, app=True)

        self.children = [self._toolbar, self._navigation_drawer]

    @property
    def hub(self):
        return self._glupyter.data_collection.hub



