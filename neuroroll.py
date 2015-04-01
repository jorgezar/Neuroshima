# -*- coding:utf-8 -*-
from tools import *

class NeuroRoll():
    def __init__(self):
        self.roll = roll_3d20()
        self.attr = 12
        
        self.thresholds = [2, 0, -2, -5, -8, -11, -15]
        self.threshold_marker = 1
        self.dificulty = self.thresholds[self.threshold_marker]
        self.skill = 10
        self.succeses = 0
    
    
    
    def set_threshold(self, argument):
        if argument == 'l':
            self.threshold.marker = 0
        elif argument == 'n':
            self.threshold.marker = 1
        elif argument == 'p':
            self.threshold.marker = 2
        elif argument == 't':
            self.threshold.marker = 3
        elif argument == 'b':
            self.threshold.marker = 4
        elif argument == 'c':
            self.threshold.marker = 5
        elif argument == 'f':
            self.threshold.marker = 6
        else: 
            self.threshold_marker = 1
        print "dificulty set to:", self.dificulty
        #modifiers = [2, 0, -2, -5, -8, -11, -15]
    
    def threshold_check(self):
        for roll in self.roll:
            if roll == 1:
                print u'jedynka! suwak w dół, kolego!'
                self.threshold_marker -=1
            elif roll == 20:
                print u'dwudziestka! trudność rośnie'
                self.threshold_marker +=1 
            else: pass
        if self.skill == 0:
            self.threshold_marker +=1
            print u'brakuje ci skilla, trudność rośnie'
        elif self.skill >= 4:
            print u'suwak!'
            self.threshold_marker -= (self.skill / 4)
        else: pass
        
        
    def skill_check(self):
        if self.threshold_marker < 0:
           print u'automatyczny sukces'
           self.succeses = 3
           
        elif self.threshold_marker > 6:
           print u'automatyczna porażka'
           
        else: pass
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
myroll.threshold_check()
myroll.skill_check()
