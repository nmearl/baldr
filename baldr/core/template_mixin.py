import ipyvuetify as v
from glue.core import HubListener


class TemplateMixin(v.VuetifyTemplate, HubListener):
    def __init__(self, *args, components=None, **kwargs):
        print("In Template mixin init")
        print(args, kwargs)
        super().__init__(*args, **kwargs)

        # self._hub = hub

    def __new__(cls, *args, **kwargs):
        print("IN NEW")
        print(args, kwargs)
        hub = kwargs.pop('hub')
        print(kwargs)
        obj = super().__new__(cls, *args, **kwargs)
        setattr(obj, '_hub', hub)
        return obj

    @property
    def hub(self):
        return self._hub


