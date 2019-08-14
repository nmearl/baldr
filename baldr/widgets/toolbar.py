import os

from traitlets import Unicode

from ..core.template_mixin import TemplateMixin

with open(os.path.join(os.path.dirname(__file__), "toolbar.vue")) as f:
    TEMPLATE = f.read()


__all__ = ['Toolbar']


class Toolbar(TemplateMixin):
    template = Unicode(TEMPLATE).tag(sync=True)

