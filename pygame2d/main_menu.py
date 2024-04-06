import pygame
import pygame_menu
import os
from mstmdn_secret.mastermind_ui import mastermindgame,Button
from mstmdn_secret.config import *
from mstmdn_secret.upload_dialogue_box import UploaFile
from mstmdn_secret.options_window import MainMenu,ConfigMenu

pygame.init()

#RED_PEACE_IMAGE=pygame.image.load(os.path.join('assets',"red_circle.svg"))
WOOD_BKG_IMAGE=pygame.image.load(os.path.join('assets',"wood_floor_worn_diff_4k-modified-modified (1).png"))
WOOD_BOX_IMAGE=pygame.image.load(os.path.join('assets',"trunk-portable-network-graphics-wooden-chest-syndrome-image-treasure-chest-clip-art-39ae1625408d9a36807495016a5e8970.png"))
GAME_ICON_SQUARED=pygame.image.load(os.path.join('assets',"logo_squared.png"))
GAME_ICON_TITLE=pygame.image.load(os.path.join('assets',"mstmnd_log.png"))
FULL_BACKGROUND_I=pygame.image.load(os.path.join('assets',"rustic-wooden-texture-1.jpg"))

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_caption("MSTMND SECRET")
pygame.display.set_caption('MSTMND SECRET')
#pygame.display.set_mode([5,5])
pygame.display.set_icon(GAME_ICON_SQUARED)
########################################################
text_test="Sneak Peek"
def set_config(name,value=None, difficulty=None):
    # Do the job here !
    global S_PEAK_TEXT
    print(value,difficulty,name)
    S_PEAK_TEXT=str(difficulty)



window_state="New Game"
def resume_function(name):
    # Do the job here !
    print("resume_function",name)
    global window_state
    window_state = name
    if name == "New Game":
        window_state=name
        print("name")
    elif name == "Resume":
        print("name")
    elif name == "Config":
        config_menu = ConfigMenu( set_config,resume_function,title="Config")
        config_menu.mainloop(WIN)
        print("name")
    elif name=="Back":
        main_menu = MainMenu(set_config,resume_function)
        main_menu.mainloop(WIN)
    start_the_game()



#def start_the_game():
    # Do the job here !
#    pass




#########################################################################
WOOD_BKG=pygame.transform.scale(WOOD_BKG_IMAGE,([*BOARD_POSITION[2:]]))
WOOD_BOX=pygame.transform.scale(WOOD_BOX_IMAGE,(240,80))
MAIN_ICON=pygame.transform.scale(GAME_ICON_TITLE,(400,80))
FULL_BACKGROUND=pygame.transform.scale(FULL_BACKGROUND_I,(600,1200))
#RED_PEACE=pygame.transform.rotate(pygame.transform.scale(RED_PEACE_IMAGE,(80,80)),90)

def draw_window(board):
    WIN.fill(WHITE)
    #WIN.blit(RED_PEACE,(red.x,red.y))
    pygame.display.update()


def write_text(text,font):
    text_surface=font.render(text,True,BLACK)
    return text_surface,text_surface.get_rect()

def get_row_col_from_mouse(pos):
    x,y=pos
    row=round((y-TOP_SPAN-2*SECRET_CIRCLE_RADIUS)/((SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN)*4))
    col=round((x-50-2*SECRET_CIRCLE_RADIUS)/((SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3))
    if col> 4:
        col = round((x - LEFT_SPAN - 2 * SECRET_CIRCLE_RADIUS-5*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3) / (EVAL_CIRCLE_RADIUS * 3))+5
    return row,col


def start_the_game(new_game=True):
    #if new_game:

    rect_bk = pygame.Rect([*BOARD_POSITION])
    hide_box = pygame.Rect([*HIDE_BOX_POSITION])
    title_box = pygame.Rect([*TITLE_BOX])

    board=mastermindgame()

    clock = pygame.time.Clock()

    b_text = BUTTON_TEXT
    bottom_but = pygame.Rect(BUTTON_POSITION)
    sneak_but = pygame.Rect(S_PEAK_POSITION)
    options_but = pygame.Rect(OPTIONS_POSITION)

    pygame.key.set_repeat(True)
    box_velocity = 0
    run = True
    while run:

        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False


            if event.type== pygame.MOUSEBUTTONDOWN:

                if bottom_but.collidepoint(pos):
                    b_text=board.change_player()


                row,col=get_row_col_from_mouse(pos)
                board.change_piece(row,col)


            #print(board.player)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pos)
            if board.player=="Set Secret":
                    hide_box.y = HIDE_BOX_POSITION[1]-40
            elif event.type == pygame.MOUSEBUTTONDOWN and sneak_but.collidepoint(pos):
                box_velocity = 0

                if hide_box.y-10 > HIDE_BOX_POSITION[1]-15:
                    box_velocity= -10
            if event.type == pygame.MOUSEBUTTONDOWN and options_but.collidepoint(pos):
                main_menu = MainMenu(set_config, resume_function)
                main_menu.mainloop(WIN)



           #up_file=UploaFile()
            #up_file.main()
            #print(up_file.file_path)

            else:
                box_velocity = 0
                hide_box.y =HIDE_BOX_POSITION[1]

        if hide_box.y >HIDE_BOX_POSITION[1]-15:
            hide_box.y+= box_velocity


        board.draw(WIN, WOOD_BKG, rect_bk, WOOD_BOX, hide_box,FULL_BACKGROUND)
        WIN.blit(WOOD_BOX,(hide_box.x,hide_box.y))
        WIN.blit(MAIN_ICON,(title_box.x,title_box.y))




        bottom_button_color = GREY
        if bottom_but.collidepoint(pos):
            bottom_button_color=GREEN

        bottom_button = Button(BUTTON_POSITION, title=b_text, font="freesansbold.ttf", font_size=20, color=bottom_button_color)
        bottom_button.create_button(WIN)

        sneak_button_color = GREEN
        if sneak_but.collidepoint(pos):
            sneak_button_color=RED
            main_menu = MainMenu(set_config, resume_function)
            main_menu.mainloop(WIN)
            # menu = pygame_menu.Menu('Welcome', 400, 300,
            #                         theme=pygame_menu.themes.THEME_SOLARIZED)
            #
            # menu.add.text_input('Name :', default='John Doe')
            # menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_config)
            # menu.add.button('Play', start_the_game)
            # menu.add.button('Quit', pygame_menu.events.EXIT)
            #
            # menu.mainloop(WIN)
        bottom_sneak = Button(S_PEAK_POSITION, title=S_PEAK_TEXT, font="freesansbold.ttf", font_size=12, color=sneak_button_color)
        bottom_sneak.create_button(WIN)
        bottom_options = Button(OPTIONS_POSITION, title=OPTIONS_TEXT, font="freesansbold.ttf", font_size=12, color=OPTIONS_COLOR)
        bottom_options.create_button(WIN)


        pygame.display.update()

        #draw_window(red)
    pygame.quit()



main_menu=MainMenu(set_config,resume_function)
main_menu.mainloop(WIN)
print("---------------------")
print(window_state)
# my_theme = pygame_menu.themes.THEME_SOLARIZED.copy()
# my_theme.title_font_size = 30  # Set the font size for the title
# my_theme.widget_font_size = 20  # Set the font size for the widgets (buttons, labels, etc.)
# my_theme.widget_alignment=pygame_menu.locals.ALIGN_LEFT
# menu = pygame_menu.Menu('Welcome', 400, 500,
#                        theme=my_theme)
#
#
# menu.add.selector('Players Mode:                   ', [('PvP', 1), ('PvC', 2), ('CvC', 3), ('CvP', 4)], onchange=set_difficulty)
# menu.add.selector('Suggestion Mode :               ', [('On', 1), ('Off', 2)], onchange=set_difficulty)
# menu.add.selector('Allow Color Repetition:         ', [('Y', 1), ('N', 2)], onchange=set_difficulty)
# menu.add.selector('Show Available Solutions:     ', [('Y', 1), ('N', 2)], onchange=set_difficulty)
# menu.add.button('New Game', start_the_game)
# menu.add.button('Resume', start_the_game)
# menu.add.button('Config', start_the_game)
# menu.add.button('Quit', pygame_menu.events.EXIT)
#
# menu.mainloop(WIN)

if __name__ == "__main__":
    start_the_game()
