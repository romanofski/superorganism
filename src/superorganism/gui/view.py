class BaseView(object):

    widget = None

    def __init__(self, context, screen):
        self.context = context
        self.screen = screen
        self.update_widgets()

    def __call__(self):
        self.render()

    def render(self):
        size = self.screen.get_cols_rows()
        canvas = self.widget.render(size, focus=True)
        self.screen.draw_screen(size, canvas)
