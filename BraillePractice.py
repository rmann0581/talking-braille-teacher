import wx
#use subprocess to execute the say command
from subprocess import call
#define the ascii values for each key used as a Braille dot
#F,D,S will be dots 1,2, and 3 and J,K, and l will be dots 4,5 and 6.
dot1=70
dot2=68
dot3=83
dot4=74
dot5=75
dot6=76
backspace=59
space=32
#use a Python dictionary to store all the Braille letters
letters={"a":(dot1,),
"b":(dot1,dot2),
"c":(dot1,dot4),
"d":(dot1,dot4,dot5),
"e":(dot1,dot5),
"f":(dot1,dot2,dot4),
"g":(dot1,dot2,dot4,dot5),
"h":(dot1,dot2,dot5),
"i":(dot2,dot4),
"j":(dot2,dot4,dot5),
"k":(dot1,dot3),
"l":(dot1,dot2,dot3),
"m":(dot1,dot3,dot4),
"n":(dot1,dot3,dot4,dot5),
"o":(dot1,dot3,dot5),
"p":(dot1,dot2,dot3,dot4),
"q":(dot1,dot2,dot3,dot4,dot5),
"r":(dot1,dot2,dot3,dot5),
"s":(dot2,dot3,dot4),
"t":(dot2,dot3,dot4,dot5),
"u":(dot1,dot3,dot6),
"v":(dot1,dot2,dot3,dot6),
"w":(dot2,dot4,dot5,dot6),
"x":(dot1,dot3,dot4,dot6),
"y":(dot1,dot3,dot4,dot5,dot6),
"z":(dot1,dot3,dot5,dot6)}

class Gui(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Braille Practice", size=(800, 400))
        self.txt = wx.TextCtrl( self, -1, "", style=wx.TE_MULTILINE )
        self.txt.Bind( wx.EVT_KEY_DOWN, self.onKeyDown )
        self.txt.Bind( wx.EVT_KEY_UP, self.onKeyUp )
        self.keylist =[] 
        self.timer = wx.Timer(self)
        self.Bind( wx.EVT_TIMER, self.onTimer, self.timer )
        self.handled = False

    def onKeyDown( self, evt ):
#        print( "Key down", evt.GetKeyCode() )
        if not self.keylist:
            self.handled = False
            self.timer.Start( 200 )
        if evt.GetKeyCode() != 307:
            self.keylist.append( evt.GetKeyCode() )
    def onKeyUp( self, evt ):
        if not self.handled:
            self.handleChord()
        self.keylist.remove( evt.GetKeyCode() )

    def onTimer( self, evt ):
        print( "Timer" )
        if not self.handled:
            self.handleChord()

    def handleChord( self ):
        self.timer.Stop()
        print self.keylist
#put the keys in order
        self.temp_key_list=[]
        if dot1 in self.keylist:
            self.temp_key_list.append(dot1)
        if dot2 in self.keylist:
            self.temp_key_list.append(dot2)
        if dot3 in self.keylist:
            self.temp_key_list.append(dot3)
        if dot4 in self.keylist:
            self.temp_key_list.append(dot4)
        if dot5 in self.keylist:
            self.temp_key_list.append(dot5)
        if dot6 in self.keylist:
            self.temp_key_list.append(dot6)
        self.final_key_list=tuple(self.temp_key_list)
        for key in letters:
            if letters[key]==self.final_key_list:
                print "You pressed the letter ",key,"."
                call(["say", "-m "+key])
        self.handled = True


if __name__ == '__main__':
    app = wx.App(redirect=False)
    top = Gui()
    top.Show()
    app.MainLoop()
