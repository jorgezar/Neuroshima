# -*- coding:utf-8 -*-
from tools import *

class NeuroRoll():
    def __init__(self):
        self.attr = 12
        self.dificulty = 0
        self.thresholds = [2, 0, -2, -5, -8, -11, -15]
        self.skill = 10
        self.succeses = 0
    def set_threshold(self, argument):
        if argument == 'l':
            self.dificulty = self.thresholds[0]
        elif argument == 'n':
            self.dificulty = self.thresholds[1]
        elif argument == 'p':
            self.dificulty = self.thresholds[2]
        elif argument == 't':
            self.dificulty = self.thresholds[3]
        elif argument == 'b':
            self.dificulty = self.thresholds[4]
        elif argument == 'c':
            self.dificulty = self.thresholds[5]
        elif argument == 'f':
            self.dificulty = self.thresholds[6]
        else: 
            self.dificulty = 0
        print "dificulty set to:", self.dificulty
        #modifiers = [2, 0, -2, -5, -8, -11, -15]
        
    
    def skill_check(self):
        dice_roll = sorted(roll_3d20())
        print u'twój rzut:', dice_roll
        print 'testowana cecha', (self.attr + self.dificulty)
        succeses = 0
        failure_dice = []
        print u'punkty umiejętności', self.skill
        for roll in dice_roll:
            if roll <= (self.attr + self.dificulty):
                succeses +=1
                print roll, "succes"
            else:
                failure_dice.append(roll)
                print roll, 'failure'
        for failed_roll in sorted(failure_dice):
            failure_margin = failed_roll - (self.attr + self.dificulty)
            
            print u'wyrzuciłem %r, do sukcesu zabrakło %r.' %(failed_roll, failure_margin)
            if failure_margin <= self.skill:
                self.skill -= failure_margin
                failed_roll -= failure_margin
                #return self.skill
                print u"wydaję %r punktów umiejętności, zostalo %r punktow" % (failure_margin, self.skill)
                succeses +=1
                #skill_points -=(failed_roll - (self.attr + self.dificulty)
                #print 'zostalo %d punktow' % skill_points        
            else: 
                print u'sorry,ale rzutem %r już nic się nie da zrobić. mam nadzieję, że jakoś dasz sobie radę' %failed_roll
        if succeses >=2:
            print u'zebrałeś %r sukcesy' %succeses
        else:
            print u"zebrałeś %r sukcesów. porażka!"
                
myroll = NeuroRoll()
myroll.set_threshold('t')
myroll.skill_check()
