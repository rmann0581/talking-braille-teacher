import wx
#define the ascii values for each key used as a Braille dot
dot1=70
dot2=68
dot3=83
dot4=74
dot5=75
dot6=76
backspace=59
space=32
#use a Python dictionary to store all the Braille letters
letters={"a":dot1}
letters.update({"b":(dot1,dot2)})
letters.update({"c":(dot1,dot4)})
letters.update({"d":(dot1,dot4,dot5)})
letters.update({"e":(dot1,dot5)})
letters.update({"f":(dot1,dot2,dot4)})
letters.update({"g":(dot1,dot2,dot4,dot5)})
letters.update({"h":(dot1,dot2,dot5)})
letters.update({"i":(dot2,dot4)})
letters.update({"j":(dot2,dot4,dot5)})
letters.update({"k":(dot1,dot3)})
letters.update({"l":(dot1,dot2,dot3)})
letters.update({"m":(dot1,dot3,dot4)})
letters.update({"n":(dot1,dot3,dot4,dot5)})
letters.update({"o":(dot1,dot3,dot5)})
letters.update({"p":(dot1,dot2,dot3,dot4)})
letters.update({"q":(dot1,dot2,dot3,dot4,dot5)})
letters.update({"r":(dot1,dot2,dot3,dot5)})
letters.update({"s":(dot2,dot3,dot4)})
letters.update({"t":(dot2,dot3,dot4,dot5)})
letters.update({"u":(dot1,dot3,dot6)})
letters.update({"v":(dot1,dot2,dot3,dot6)})
letters.update({"w":(dot2,dot4,dot5,dot6)})
letters.update({"x":(dot1,dot3,dot4,dot6)})
letters.update({"y":(dot1,dot3,dot4,dot5,dot6)})
letters.update({"z":(dot1,dot3,dot5,dot6)})

class Gui(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="test", size=(800, 400))
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
        print( "Key up", evt.GetKeyCode() )
        if not self.handled:
            self.handleChord()
        self.keylist.remove( evt.GetKeyCode() )

    def onTimer( self, evt ):
        print( "Timer" )
        if not self.handled:
            self.handleChord()

    def handleChord( self ):
        self.timer.Stop()
#Now we need to convert our list of keys to a tuple so we can check it against the dictionary of letters.
        self.final_key_list=tuple(self.keylist)
        print "You pressed ",self.final_key_list[0:len(self.final_key_list)],"."
        print test
        self.handled = True


if __name__ == '__main__':
    app = wx.App(redirect=False)
    top = Gui()
    top.Show()
    app.MainLoop()
