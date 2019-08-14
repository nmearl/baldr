from glue.core.message import Message


class NewProfile1DMessage(Message):
    def __init__(self, figure, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._figure = figure

    @property
    def figure(self):
        return self._figure