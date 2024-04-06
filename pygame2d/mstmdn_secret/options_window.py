import pygame_menu

class OptionsWindow:
    def __init__(self,title="Welcome",width=400,height=500,theme=pygame_menu.themes.THEME_SOLARIZED,title_font_size=30,widget_font_size=20,alignment=pygame_menu.locals.ALIGN_LEFT):
        self.theme = self.make_custom_theme(theme,title_font_size,widget_font_size,alignment)
        self.menu=pygame_menu.Menu(title, width, height, theme=self.theme)

    def make_custom_theme(self,theme,title_font_size,widget_font_size,alignment):
        theme=theme.copy()
        theme.title_font_size = title_font_size  # Set the font size for the title
        theme.widget_font_size = widget_font_size  # Set the font size for the widgets (buttons, labels, etc.)
        theme.widget_alignment = alignment
        return theme

    def mainloop(self,win):
        self.menu.mainloop(win)

class MainMenu(OptionsWindow):
    def __init__(self,onchange_function,resume_function,*args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.add_selectors(onchange_function,resume_function)

    def add_selectors(self,onchange_function,resume_function):
        self.menu.add.button('New Game', resume_function,"New Game")
        self.menu.add.button('Resume', resume_function,"Resume")
        self.menu.add.button('Config', resume_function,"Config")
        self.menu.add.button('Quit', pygame_menu.events.EXIT)



class ConfigMenu(OptionsWindow):
    def __init__(self,onchange_function,resume_function,*args, **kwargs):
        super(ConfigMenu, self).__init__(*args, **kwargs)
        self.add_selectors(onchange_function,resume_function)

    def add_selectors(self,onchange_function,go_back_function):
        self.menu.add.selector('Players Mode:                   ', [('PvP', 1), ('PvC', 2), ('CvC', 3), ('CvP', 4)],
                               onchange=onchange_function)
        self.menu.add.selector('Suggestion Mode :               ', [('On', 1), ('Off', 2)], onchange=onchange_function,name="Players")
        self.menu.add.selector('Allow Color Repetition:         ', [('Y', 1), ('N', 2)], onchange=onchange_function,name="Players")
        self.menu.add.selector('Show Available Solutions:     ', [('Y', 1), ('N', 2)], onchange=onchange_function,name="Players")
        self.menu.add.button('Back', go_back_function,"Back")

