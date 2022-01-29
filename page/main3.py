from . import demo as PageDemo
from widget import pixel as WidgetPixel
from widget import common as WidgetCommon
from data import theme as DataTheme


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = self.W

        # <Logo> ------------------------------------------------------------------------------------------------------
        WidgetPixel.str_middle(self, s='SNAKE 3', x=0, y=2 * w, width=self.winfo_width(), height=3 * w,
                               w=0.3 * w, color=DataTheme.snake_logo)
        # </Logo> -----------------------------------------------------------------------------------------------------

        # <Single Button> ---------------------------------------------------------------------------------------------
        single_button = WidgetCommon.Button(self, bg='White', active_background='LightGrey', fg=DataTheme.single_theme,
                                            text='SINGLE MODE', w=0.18 * w)
        single_button.place(relx=0.5, x=-5 * w, y=8 * w, width=10 * w, height=2.4 * w)
        # </Single Button> --------------------------------------------------------------------------------------------

        # <Level Button> ----------------------------------------------------------------------------------------------
        level_button = WidgetCommon.Button(self, bg='White', active_background='LightGrey', fg=DataTheme.level_theme,
                                           text='LEVEL MODE', w=0.18 * w)
        level_button.place(relx=0.5, x=-5 * w, y=11 * w, width=10 * w, height=2.4 * w)
        # </Level Button> ---------------------------------------------------------------------------------------------

        # <Setting Button> --------------------------------------------------------------------------------------------
        setting_button = WidgetCommon.Button(self, bg='White', active_background='LightGrey')
        setting_button.place(relx=0.5, x=-5 * w, y=16.5 * w, width=2 * w, height=2 * w)
        # </Setting Button> -------------------------------------------------------------------------------------------

        # <About Button> ----------------------------------------------------------------------------------------------
        about_button = WidgetCommon.Button(self, bg='White', active_background='LightGrey', fg='Purple',
                                           text='ABOUT', w=0.16 * w)
        about_button.place(relx=0.5, x=-2.4 * w, y=16.5 * w, width=7.4 * w, height=2 * w)
        # </About Button> ---------------------------------------------------------------------------------------------


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
