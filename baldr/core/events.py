from glue.core.message import Message


class NewProfile1DMessage(Message):
    def __init__(self, figure, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._figure = figure

    @property
    def figure(self):
        return self._figure


class LoadDataMessage(Message):
    def __init__(self, file_path, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._file_path = file_path

    @property
    def file_path(self):
        return self._file_path