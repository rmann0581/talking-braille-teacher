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
