import ipyvuetify as v
from glue.core import HubListener


class TemplateMixin(v.VuetifyTemplate, HubListener):
    def __new__(cls, *args, **kwargs):
        """
        Overload object creation so that we can inject a reference to the
        ``Hub`` class before components can be initialized. This makes it so
        hub references on widgets can be passed along to components in the
        call to the initialization method.
        """
        hub = kwargs.pop('hub', None)
        obj = super().__new__(cls, *args, **kwargs)
        setattr(obj, '_hub', hub)

        return obj

    @property
    def hub(self):
        return self._hub


