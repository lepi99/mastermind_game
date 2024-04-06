import itertools
import random
from sympy.utilities.iterables import multiset_permutations
from collections import Counter

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
        self.current_play=11
        self.player="Set Secret"

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