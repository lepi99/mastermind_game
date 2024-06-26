
FPS=60

ROWS=10


TOP_SPAN=140
LEFT_SPAN=60

WIDTH, HEIGHT = 500,850+TOP_SPAN

BOARD_POSITION=(LEFT_SPAN,TOP_SPAN,WIDTH-2*LEFT_SPAN,HEIGHT-(TOP_SPAN+60))
BOARDER=5

#GAME_BOARD_POSITION=(50, 50, 400, 800)
HIDE_BOX_POSITION = (50, 675+TOP_SPAN, 240, 80)
TITLE_BOX = (20, 20, 500, 80)



#Colors
BROWN=(156,111,62)
BLACK=(0,0,0)
YELLOW=(249,237,16)
GREEN=(11,210,17)
LIGHT_BLUE=(9,239,236)
RED=(234,22,25)
BLUE=(9,55,219)
PURPLE=(144,1,250)
PINK=(255,0,255)
WHITE=(255,255,255)
GREY=(57,57,57)
DARK_BROWN=(80,45,22)



##Pieces
SECRET_CIRCLE_RADIUS=15
EVAL_CIRCLE_RADIUS=10
EXTRA_INBETWEEN_HOR_SPAN=1
EXTRA_INBETWEEN_VER_SPAN=-1
SECRET_COLORS_LIST=[BLACK,YELLOW,GREEN,LIGHT_BLUE,RED,BLUE,PURPLE,PINK,WHITE]
EVAL_COLORS_LIST=[BLACK,WHITE,GREY]

BUTTON_POSITION=(150,810+TOP_SPAN,200,30)
BUTTON_COLOR=GREEN
BUTTON_COLOR_HIGH=BLUE
BUTTON_COLOR_INV=GREY
BUTTON_TEXT="Set Secret"


S_PEAK_POSITION=(290, 695+TOP_SPAN, 80, 30)
S_PEAK_COLOR=GREEN
S_PEAK_COLOR_HIGH=BLUE
S_PEAK_COLOR_INV=GREY
S_PEAK_TEXT="Sneak Peek"

OPTIONS_POSITION=(400, 10, 80, 30)
OPTIONS_COLOR=GREEN
OPTIONS_COLOR_HIGH=BLUE
OPTIONS_COLOR_INV=GREY
OPTIONS_TEXT="Options"