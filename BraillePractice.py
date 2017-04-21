import wx
#use subprocess to execute the say command
from subprocess import call
#import the file with the Braille dictionaries
from braille_table import * #put the dictionaries in current namespace 
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
        if dot6 in self.keylist and len(self.keylist) >1:
            self.temp_key_list.append(dot6)
        if dot6 in self.keylist and len(self.keylist)==1:
            print "got dot 6"
            call(["say ","-m dot 6"])
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
