import itertools
import random

import pygame.draw
from sympy.utilities.iterables import multiset_permutations
from collections import Counter
from .config import *
# Define a list of numbers
#my_list = ['1', '2', '3', '4', '5', '6', '7', '8']

# Generate all possible two-element combinations
# Convert the resulting iterator to a list
#combinations = list(itertools.combinations_with_replacement(my_list, 5))

#new_dict={}
#for aa in combinations:

    #new_dict["".join(aa)]=["".join(ii) for ii in multiset_permutations(aa)]


#print(len(new_dict))
#print(new_dict)

def evaluate_match(comb1,comb2):
    equalC=[]
    for ii in range(len(comb1)):
        if comb1[ii]==comb2[ii]:
            equalC.append("b")
    c = list((Counter(comb1) & Counter(comb2)).elements())
    cw=[]
    if len(equalC)>0:
        c=c[:-len(equalC)]
    for ci in c:
        cw.append("w")

    cw.extend(equalC)
    return cw





class Piece:
    def __init__(self,row,col,color=BLACK):
        self.row=row
        self.col=col
        self.color=color
        self.color_index=0
        self.piece_type=None
        self.x=0
        self.y=0
        self.get_pos()
        self.get_piece_type()

    def get_pos(self):
        if self.col < 5:
            self.x=LEFT_SPAN + 2 * SECRET_CIRCLE_RADIUS + self.col * (SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN) * 3
        else:
            self.x = LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ 5*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3+(self.col-5)*EVAL_CIRCLE_RADIUS*3
        self.y=TOP_SPAN + 2 * SECRET_CIRCLE_RADIUS + self.row * (SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN) * 4

    def get_piece_type(self):
        if self.col<5:
            self.piece_type="secret"
        else:
            self.piece_type="eval"
        #return
    def draw(self,win):
        if self.piece_type == "secret":
            pygame.draw.circle(win,self.color,(self.x,self.y),SECRET_CIRCLE_RADIUS)
        else:
            pygame.draw.circle(win, self.color, (self.x, self.y), EVAL_CIRCLE_RADIUS)
    def change(self):
        self.color_index+=1
        if self.piece_type=="secret":
            self.color_index=self.color_index % 9
            self.color = SECRET_COLORS_LIST[self.color_index]
        else:
            self.color_index = self.color_index % 3
            self.color = EVAL_COLORS_LIST[self.color_index]

    def __repr__(self):
        return f"{type} - {self.color}"

class Button:
    def __init__(self,position,title="",font="freesansbold.ttf",font_size=20,color=BLACK):
        self.position=position
        self.x,self.y,self.width,self.height=position
        self.font=font
        self.font_size=font_size
        self.title=title
        self.color=color
        self.rect=None
    def create_button(self,win):
        self.rect=pygame.draw.rect(win, self.color, self.position)
        if self.title:
            Text = pygame.font.Font(self.font, self.font_size)
            textSurf, textRect = self.write_text(self.title, Text)
            textRect.center = (
            (self.x + (self.width / 2)), (self.y + (self.height / 2)))
            win.blit(textSurf, textRect)
    def check_point_collide(self,point):
        return self.rect.collidepoint(point)

    def write_text(self,text,font=None):
        text_surface=font.render(text,True,BLACK)
        return text_surface,text_surface.get_rect()

class mastermindgame:
    def __init__(self, peaces=['1', '2', '3', '4', '5', '6', '7', '8'],manual_secret=True,check_eval=True,display_possibilities_count=True):
        self.peaces = peaces
        self.board=[]
        self.combinations = []
        self.secret = None
        self.is_secret_set=False
        self.count_attempts=None
        self.attempts=None #take len of attemps array instead
        self.count_possible_combs=0
        self.manual_secret=manual_secret
        self.check_eval=check_eval
        self.display_possibilities_count=display_possibilities_count
        self.create_board()
        self.current_play=11
        self.player="Set Secret"

    def change_piece(self,row,col):
        if row == self.current_play :
            if (col < 5 and self.player == "Detective") or (col>= 5 and self.player == "Secret Master"):
                piece=self.board[row][col]
                piece.change()
    def change_player(self):
        print(self.secret)
        if self.player == "Set Secret":
            self.player ="Detective"
            self.current_play = 0
            return "Submit Attempt"
        elif self.player == "Detective":
            self.player="Secret Master"

            return "Submit Attempt"
        elif self.player == "Secret Master":
            self.player="Detective"
            self.current_play += 1
            return "Validate Attempt"

    def get_row_colors(self,row_number):
        color_list=[]
        for i in self.board[row_number]:
            color_list.append(i.color)
        return color_list

    def get_current_row_colors(self):
        return self.get_row_colors(self.current_play)

    #def check_current_row_full(self):
        #if
    #def show_secret(self,win,secret_box):


    def draw_board(self,win,bkg_image,rect_bkg,wood_box,rect_box,full_bkg_image):
        #win.fill(GREY)
        win.blit(full_bkg_image, (0, 0))
        pygame.draw.rect(win, DARK_BROWN, [rect_bkg.x-10, rect_bkg.y-10, rect_bkg.width+20, rect_bkg.height+20],30,45)
        win.blit(bkg_image,(rect_bkg.x,rect_bkg.y))

        pygame.draw.rect(win, BLACK, [rect_bkg.x-1, rect_bkg.y-1, rect_bkg.width+2, rect_bkg.height+2],2,45)
        pygame.draw.rect(win, BLACK, [rect_bkg.x-10, rect_bkg.y-10, rect_bkg.width+20, rect_bkg.height+20],2,45)



        for row in range(10):
            for col in range(10):
                if col < 5:
                    pygame.draw.circle(win,BLACK,(LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ col*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3,
                                                  TOP_SPAN+2*SECRET_CIRCLE_RADIUS+row*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN)*4),
                                                SECRET_CIRCLE_RADIUS)
                else:
                    pygame.draw.circle(win,BLACK,(LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ 5*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3+(col-5)*EVAL_CIRCLE_RADIUS*3,
                                                  TOP_SPAN+2*SECRET_CIRCLE_RADIUS+row*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN)*4),
                                       EVAL_CIRCLE_RADIUS)
        #DRAW SECRET
        for col in range(5):
                pygame.draw.circle(win, BLACK, (
                LEFT_SPAN + 2 * SECRET_CIRCLE_RADIUS + col * (SECRET_CIRCLE_RADIUS + EXTRA_INBETWEEN_VER_SPAN) * 3,
                TOP_SPAN + 2 * SECRET_CIRCLE_RADIUS + 11 * (SECRET_CIRCLE_RADIUS + EXTRA_INBETWEEN_HOR_SPAN) * 4),
                                   SECRET_CIRCLE_RADIUS)

        #draw lines
        pygame.draw.rect(win, BLACK, (LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ 4*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3 + SECRET_CIRCLE_RADIUS*3/2,
                                                  TOP_SPAN+SECRET_CIRCLE_RADIUS,
                                                3,800-2*SECRET_CIRCLE_RADIUS))

        if self.player == "Secret Master":
            pygame.draw.rect(win, BLUE, (LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ 5*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3-10,
                                          TOP_SPAN+2*SECRET_CIRCLE_RADIUS+self.current_play*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN)*4-SECRET_CIRCLE_RADIUS-8,
                                          140,3))

            pygame.draw.rect(win, BLUE, (LEFT_SPAN+2*SECRET_CIRCLE_RADIUS+ 5*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_VER_SPAN)*3-10,
                                      TOP_SPAN+2*SECRET_CIRCLE_RADIUS+self.current_play*(SECRET_CIRCLE_RADIUS+EXTRA_INBETWEEN_HOR_SPAN)*4+SECRET_CIRCLE_RADIUS+3,
                                      140,3))
        else:

            pygame.draw.rect(win, BLUE, (LEFT_SPAN + 5,
                                         TOP_SPAN + 2 * SECRET_CIRCLE_RADIUS + self.current_play * (
                                                     SECRET_CIRCLE_RADIUS + EXTRA_INBETWEEN_HOR_SPAN) * 4 - SECRET_CIRCLE_RADIUS - 8,
                                         208, 3))

            pygame.draw.rect(win, BLUE, (LEFT_SPAN + 5,
                                         TOP_SPAN + 2 * SECRET_CIRCLE_RADIUS + self.current_play * (
                                                     SECRET_CIRCLE_RADIUS + EXTRA_INBETWEEN_HOR_SPAN) * 4 + SECRET_CIRCLE_RADIUS + 3,
                                         208, 3))

    def get_piece(self,row,col):

        return self.board[row][col]

    def create_board(self):
        for row in range(12):
            self.board.append([])
            for col in range(10):
                self.board[row].append(Piece(row,col))

    def draw(self,win,bkg_image,rect_bkg,wood_box,rect_box,full_bkg_image):
        self.draw_board(win,bkg_image,rect_bkg,wood_box,rect_box,full_bkg_image)
        for row in range(10):
            for col in range(10):
                piece = self.board[row][col]
                piece.draw(win)
        for col in range(5):
            piece = self.board[11][col]
            piece.draw(win)


    def start_game(self):
        self.count_attempts=0
        self.attempts=[]
        self.combinations = []
        self.secret_combination = []
        combs=list(itertools.combinations_with_replacement(self.peaces, 5))
        for cc in combs:
            nco=comb(cc)
            self.combinations.append(nco)
            self.count_possible_combs+=len(nco.get_combs())
        print(self.combinations)



    def set_secret(self,secret_comb):
        self.set_manual_secret(False)
        self.secret=secret_comb

    def set_manual_secret(self,bool_v):
        if not isinstance(bool_v, bool):
            raise("value not bool")
        self.manual_secret=bool_v

    def set_check_eval(self,bool_v):
        if not isinstance(bool_v, bool):
            raise("value not bool")
        self.check_eval=bool_v

    def set_display_possibilities_count(self,bool_v):
        if not isinstance(bool_v, bool):
            raise("value not bool")
        self.display_possibilities_count=bool_v

    def get_possible_comb_count(self):
        print(self.count_possible_combs)
        return self.count_possible_combs

    @staticmethod
    def evaluate_match(comb1,comb2):
        equalC = []
        for ii in range(len(comb1)):
            if comb1[ii] == comb2[ii]:
                equalC.append("b")
        c = list((Counter(comb1) & Counter(comb2)).elements())
        cw = []
        if len(equalC) > 0:
            c = c[:-len(equalC)]
        for _ in c:
            cw.append("w")

        cw.extend(equalC)
        return cw
        #return evaluate_match(comb1, comb2)


    def play(self,version=None):
        if not version:
            while True:
                version = input("Choose game version:\n- auto\n- 1p\n- 2p\nVersion=")
                if version in ["auto","1p","2p"]:
                    break
                print("Error: invalid option")


        if self.manual_secret or version=="2p":
            while True:
                tts = input("what is the secret? ")
                if len(tts.strip()) != 5:
                    print("Error: Secret code must have only 5 peaces")
                    continue
                if not (set(tts) <= set(self.peaces)):
                    print("Error: Invalid peaces")
                    continue
                break
            self.secret = tts

        elif not self.secret:
            pick_r = random.randint(0, len(self.combinations) - 1)
            print(pick_r)

            pick_r2 = random.randint(0, len(self.combinations[pick_r].all_comb) - 1)
            print("Setting random secret - *****")
            self.secret = self.combinations[pick_r].all_comb[pick_r2]

        while True:
            self.count_attempts+=1
            if version in ("auto"):
                print("Attempt number "+str(self.count_attempts))
                pick_r=random.randint(0,len(self.combinations)-1)
                #print(pick_r)

                pick_r2 = random.randint(0, len(self.combinations[pick_r].all_comb) - 1)
                tt = self.combinations[pick_r].all_comb[pick_r2]
            else:
                while True:
                    tt = input("what is your " +str(self.count_attempts)+" try? ")
                    if len(tt.strip()) != 5:
                        print("Error: Code must have 5 peaces")
                        continue
                    if not (set(tt) <= set(self.peaces)):
                        print("Error: Invalid peaces")
                        continue
                    break
            #if version in ["auto","1p"]:
            ev=self.evaluate_match(tt,self.secret)
            if version in ["2p"]:
                while True:
                    tt2 = "".join(sorted(input("what is the eval? "),reverse=True))
                    #ev = evaluate_match(tt, self.secret)
                    if len(tt2.strip()) >5:
                        print("Error: Evaluation should have 5 or less peaces")
                        continue
                    if not (set(tt2)<=set("bw")):
                        print("Error: Invalid peaces")
                        continue
                    if self.check_eval and list(ev)!=list(tt2):
                        print("Error: wrong evaluation")
                        continue
                    break
            new_comb=[]
            for aa in self.combinations:
                prev_count=len(aa.all_comb)
                hh=aa.filter_combs(tt,ev)
                new_count = len(aa.all_comb)

                if hh:
                    new_comb.append(aa)
                    self.count_possible_combs = self.count_possible_combs + new_count - prev_count
                else:
                    self.count_possible_combs = self.count_possible_combs - prev_count
            self.combinations=new_comb
            #print(self.combinations)
            self.attempts.append((tt,"".join(ev),self.count_possible_combs))

            for atemp in self.attempts:
                print(atemp)
            if ev==["b","b","b","b","b"]:
                print("Well Done")
                break




class comb:
    def __init__(self, main=None):
        self.main = "".join(main)
        self.all_comb = ["".join(ii) for ii in multiset_permutations(main)]

    def __repr__(self):
        return "main- "+str(self.main)+" - "+str(self.all_comb)

    def __str__(self):
        return "main: "+str(self.main)+" - "+str(self.all_comb)

    def get_combs(self):
        #print(self.all_comb)
        return self.all_comb

    def filter_combs(self,comb_attempt, match_result):
        new_list=[]
        mr=self.evaluate_match(comb_attempt)
        if len(mr)!=len(match_result):
            return False
        for rcl in self.all_comb:
            if self.evaluate_match(rcl, comb_attempt)==match_result:
                new_list.append(rcl)
        if new_list == []:
            return False
        self.all_comb=new_list
        return True

    def evaluate_match(self,comb1,comb2=None):
        if not comb2:
            comb2=self.main
        equalC = []
        for ii in range(len(comb1)):
            if comb1[ii] == comb2[ii]:
                equalC.append("b")
        c = list((Counter(comb1) & Counter(comb2)).elements())
        cw = []
        if len(equalC) > 0:
            c = c[:-len(equalC)]
        for ci in c:
            cw.append("w")

        cw.extend(equalC)
        return cw
        #return evaluate_match(comb1, comb2)


if __name__ == "__main__":

    ng=mastermindgame()
    ng.start_game()
    ng.get_possible_comb_count()
    #ng.set_secret("87665")
    ng.set_manual_secret(False)
    #ng.play()
    ng.play()


    #new_o=comb("12345")
    #ev=new_o.evaluate_match("13456")
    #print(ev)