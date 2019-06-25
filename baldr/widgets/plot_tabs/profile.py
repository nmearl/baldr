from glue_jupyter.bqplot.profile import BqplotProfileView
import ipyvuetify as v


class ProfileTab(v.TabItem):
    def __init__(self, figure, **kwargs):
        super().__init__(**kwargs)

        fig_widget = figure.figure_widget
        fig_widget.layout = {'height': '100%', 'width':'100%'}

        self._card = v.Card(style_="height: 100%", children=[figure.figure_widget])

        self.children = self.children + [self._card]
