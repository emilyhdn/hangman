from graphics import*
import random
import string

wordbank = ['interpreter', 'idle', 'python', 'editor', 'output', 'input',
            'float', 'string', 'loop', 'boolean', 'cgi', 'shell', 'module'
            'error', 'concatenation', 'format', 'sequence', 'append',
            'infile', 'outfile', 'graphics', 'animation', 'random', 'elif'
            'range', 'tuple', 'html', 'browser', 'interface', 'computation',
            'assembler', 'logic', 'circuit', 'binary', 'arithmetic', 'hexadecimal',
            'base', 'function', 'pip', 'bit', 'register', 'accumulator', 'xor',
            'transistor', 'gate', 'nand', 'nor', 'database', 'intelligence',
            'network', 'algorithm', 'sql', 'row', 'column']

easy=[]
medium=[]
difficult=[]
for word in wordbank:
    if len(word)<5:
        easy.append(word)
        random.shuffle(easy)
        entry=easy.pop()
    elif len(word)<9:
        medium.append(word)
        random.shuffle(medium)
        entry=medium.pop()
    else:
        difficult.append(word)
        random.shuffle(difficult)
        entry=difficult.pop()

def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

def makeColoredRect(corner, width, height, color, win):
    corner2 = corner.clone()  
    corner2.move(width, -height)
    rect = Rectangle(corner, corner2)
    rect.setFill(color)
    rect.draw(win)
    return rect

def getChoice(choicePairs, default, win):
    point=win.getMouse()
    for (rectangle, choice) in choicePairs:
        if isInside(point, rectangle):
            return choice
    return default

def setting():
    win=GraphWin("Hangman", 600, 600)
    win.yUp()
    win.setBackground('aquamarine1')
    message1=Text(Point(300, 580), 'Test your COMP 150 vocabulary!')
    message1.setTextColor('aquamarine4')
    message1.setSize(18)
    message1.draw(win)
    message2=Text(Point(100, 550), 'Click box to select difficulty')
    message2.draw(win)
    c1=Text(Point(60, 524), 'Easy')
    c1.draw(win)
    c2=Text(Point(70, 494), 'Medium')
    c2.draw(win)
    c3=Text(Point(70, 464), 'Difficult')
    c3.draw(win)
    line1=Line(Point(200, 200), Point(400,200))
    line1.setOutline('green')
    line1.setWidth(3)
    line1.draw(win)
    line2=Line(Point(350, 200), Point(350,400))
    line2.setOutline('green')
    line2.setWidth(3)
    line2.draw(win)
    line3=Line(Point(350, 400), Point(270,400))
    line3.setOutline('green')
    line3.setWidth(3)
    line3.draw(win)
    line4=Line(Point(270, 400), Point(270,370))
    line4.setOutline('green')
    line4.setWidth(3)
    line4.draw(win)
    

    choicePairs=list()
    buttonSetup=[(20, 530, 'aquamarine2'), (20, 500, 'DeepSkyBlue1'), (20, 470, 'DeepSkyBlue4')]
    for (x, y, color) in buttonSetup:
       button = makeColoredRect(Point(x, y), 15, 15, color, win)
       choicePairs.append((button, color))

'''win.promptClose(win.getWidth()/2,20)'''

setting()


def makeLetters():
    alpha = string.ascii_lowercase
    count = 0 #number of letters in alpha
    xtraverse = 20 #location x 
    ytraverse = 530 #location y
    while count != 26:
        
        
        
        

'''        
def getChoice(choicePairs, default, win):
    point=win.getMouse()
    for (rectangle, choice) in choicePairs:
        if isInside(point, rectangle):
            return choice
    return default

'''
    
    
