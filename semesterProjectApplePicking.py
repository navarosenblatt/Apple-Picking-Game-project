#APPLE PICKING GAME!

#"I hereby certify that this program is solely the result of my own work and is\
#in compliance with the Academic Integrity policy of the course syllabus.”
# -Nava Rosenblatt

import random
import math
import Draw

#making some colors
skyBlue= Draw.color(55, 213, 255)
grassGreen= Draw.color(68, 211, 33)
leaves= Draw.color(13, 168, 21)
appleRed= Draw.color(255, 27, 10)
sunYellow= Draw.color(255, 236, 18)

#this function creates a 2D list of apples. In each sub-list, the first \
#component is the x value and the second component is the y value, \
#so that each sub-list represents the coordinates of one apple:
def appleList():
    #create an empty list
    apples=[]
    #sets how many apples will be on the tree
    numApples= 25
    #turn the list into an empty 2D list
    for row in range(numApples):
        apples.append([0]* 2)
    #fill the list with randomly selected polar coordinates
    #the coordinates should be within the cirlce Draw.filledOval(135, 5, 190, 190) 
    for row in range(len(apples)):
        angle= random.randint(0, int(2*math.pi))
        apples[row][0]= int(random.randint(1,95)*math.cos(angle)+230)
        apples[row][1]= int(random.randint(1,95)*math.sin(angle)+100)
    return apples 

#this function chooses an apple (a set of coordinates) from the list of apples, \
#returns it, and removes that apple from the list
def removeRandomApple(apples):
    if len(apples)>0:
        #appleIndex represents the random apple that was chosen:
        appleIndex=  random.randint(0, len(apples)-1)  
        #this assigns apples sub appleIndex to current apple
        currentApple= apples[appleIndex]
        #now delete that apple from the list:
        del apples[appleIndex]
        #return the apple that was chosen:
        return currentApple
    else:
        return None

#because I draw grass in multiple frames, I made it into a function:
def drawGrass():
    Draw.setColor(grassGreen)
    Draw.filledRect(0, 300, 500, 200)
    
#this function draws the leaves/branches of the tree
def branches(x,y):
    Draw.setColor(leaves)
    Draw.filledOval(x, y, 100, 80) 

#this function draws a cloud at (x,y) location
def cloud(x, y):
    Draw.setColor(Draw.WHITE)
    coords= [x+10,y+30, x+20,y+50, x+45,y+60, x+70,y+55, x+85,y+35, x+70,y+20, \
             x+40,y+15, x+35,y+40]
    for i in range(0, len(coords), 2):
        a= int(coords[i])
        b= int(coords[i+1])
        Draw.filledOval(a, b, 50, 40)
 
#this function loops through two lists of coordinates to draw the clouds \
#at the coordinates, and takes in two variables, cloudMove1 and cloudMove2,\
#which move the clouds across the screen as the game is played
def cloudLocation(cloudMove1, cloudMove2):
    coords= [90,-30, -20,20, 40,120]
    for i in range(0, len(coords), 2):
        x= coords[i]+ cloudMove1
        y=coords[i+1]
        cloud(x,y)
    coords= [0,30, 100,90] 
    for i in range(0, len(coords), 2):
        x= coords[i]+ cloudMove2
        y=coords[i+1]
        cloud(x,y)   

#this is a function to draw an apple at (x,y) location
def appleLocation(x,y):
    #draws the actual red apple cirle
    Draw.setColor(appleRed)
    Draw.filledOval(x, y, 30, 30)
    #draws a white highlight on the apple
    Draw.setColor(Draw.WHITE)
    Draw.filledOval(x+18, y+5, 5, 5)   
    Draw.setColor(Draw.BLACK)
    #draws the stem
    Draw.line(x+15, y, x+15, y-10)
    #outlines the apple
    Draw.oval(x, y, 30, 30)

#this function redraws the board    
def reDrawBoard(apples, appleFalling, basketX, basketY, score, cloudMove1,\
                cloudMove2):
    Draw.clear()
    
    #drawing the sun
    Draw.setColor(sunYellow)
    Draw.filledOval(400, 10, 90, 90)
    
    #drawing the clouds:   
    cloudLocation(cloudMove1, cloudMove2)
    
    #drawing the grass
    drawGrass()
    
    #drawing the tree trunk
    brown= Draw.color(117, 78, 9)
    Draw.setColor(brown)
    Draw.filledRect(230, 150, 40, 180)
    
    #drawing the leaves of the tree
    branches(120, 70)
    branches(140, 30)
    branches(200, 10)
    branches(200, 130)
    branches(150, 120)
    branches(200, 70)
    branches(250, 40)
    branches(270, 80)
    branches(250, 110)
    
   
    #drawing the handle of the basket:
    #drawing the outer circle light brown:
    lightBrown= Draw.color(170, 114, 13)
    Draw.setColor(lightBrown)
    Draw.filledOval(basketX, basketY-35, 70, 70)
    Draw.setColor(Draw.BLACK)
    Draw.oval(basketX, basketY-35, 70, 70)
    #drawing the inner circle the same color as the grass:
    Draw.setColor(grassGreen)
    Draw.filledOval(basketX+5, basketY-30, 60, 60)
    Draw.setColor(Draw.BLACK)
    Draw.oval(basketX+5, basketY-30, 60, 60)    
    
    #drawing the apples:
    #this loops through the list apples to draw an apple at each sub-list's \
    #location 
    #the first component of the sub-list represents the x value \
    #and the second component of the sub-list represents the y value 
    for row in range(len(apples)):
        x= apples[row][0]
        y= apples[row][1]
        appleLocation(x,y)
    #this redraws the current falling apple's new location:
    appleLocation(appleFalling[0], appleFalling[1])
    
    #drawing the actual basket:
    Draw.setColor(lightBrown)
    coords=[basketX,basketY , basketX+70,basketY , \
            basketX+65,basketY+50 , basketX+5,basketY+50]
    Draw.filledPolygon(coords)
    #outline in black
    Draw.setColor(Draw.BLACK)
    Draw.polygon(coords)    
    
    #drawing the score
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily('Courier')
    Draw.setFontSize(25)
    Draw.setFontBold(True)
    Draw.string("score = " + str(score), 320, 450)
  
    Draw.show()

#this function makes a screen that thanks the user for playing!! :)     
def thanks():
    Draw.clear()
    
    drawGrass()
    Draw.setColor(Draw.WHITE)
    Draw.setFontSize(40)
    Draw.setFontFamily('Courier')
    Draw.setFontBold(True)
    Draw.string("Thanks for playing!", 25, 175)
    Draw.string("Hope you enjoyed!" , 50, 225)
    
    Draw.show()
    
#this function checks for user input if the user wants to play again   
def replay():
    while True:
        #check for user input
        if Draw.hasNextKeyTyped():
            newKey= Draw.nextKeyTyped()
        
            #if the user has typed the "Enter" key, replay game
            if newKey== "Return":
                playGame() 
            
            #if the user has typed the "Esc" key, end game and display "thanks"\
            #screen
            if newKey == "Escape":
                #this invokes the thanks screen function
                thanks()
                return
                
            
#this function draws the end of game screen 
def endGame(score):
    Draw.clear()
    
    #redraws the grass:
    drawGrass()
    
    Draw.setColor(Draw.RED)
    Draw.setFontFamily('Courier')
    Draw.setFontSize(60)
    Draw.setFontBold(True)
    Draw.string("GAME OVER", 85, 80)
    
    Draw.setFontSize(30)
    Draw.setFontBold(False)
    Draw.setFontFamily('Helvetica')
    Draw.setColor(Draw.WHITE)
    Draw.string("Congratulations!", 140, 185)
    Draw.string("You picked " + str(score)+ " apples", 105, 235)
    Draw.string("To play again, press 'Enter'", 70, 325)
    Draw.string("To quit, press 'Esc'", 125, 375)    
    Draw.show() 
    
    #invokes the function which checks if the user wants to replay
    replay()
  

def playGame():
    #initialize variables:
    apples= appleList() 
    basketX= 215
    basketY= 370 
    appleRadius= 15
    appleFalling= removeRandomApple(apples) #this assigns an initial apple to \
    #appleFalling
    score= 0
    appleSpeed= 1
    cloudMove1=0 
    cloudMove2=320
   
    #while there are still apples left or an apple is still falling:
    while len(apples)>0 or appleFalling:
        #move the clouds to the right until they exit the screen, the make them\
        #reappear at the left edge of the screen
        if cloudMove1<=500:
            cloudMove1+=.4
        else:
            cloudMove1=-250
    
        if cloudMove2<=500:
            cloudMove2+=.4
        else:
            cloudMove2= -250
                
        #check if the user has typed a key
        if Draw.hasNextKeyTyped():
            newKey= Draw.nextKeyTyped()
            #if user typed left arrow, decrease the x value of the basket 
            if newKey== "Left" and basketX>=15:
                basketX -=20
            #if user typed right arrow, increase the x value of the basket 
            if newKey == "Right" and basketX<= 415:
                basketX +=20  
            
        #if there is an apple falling,     
        if appleFalling:
            #increase the y value of appleFalling by apple speed to make the \
            #apple fall
            appleFalling[1]+= appleSpeed
            #if the apple has reached the ground level (the y value of the \
            #apple is at least basketY):
            if appleFalling[1]>= basketY:
                #if the apple is within the basket (the x value of the apple is\
                #between the two sides of the basket), increase the score
                if appleFalling[0] >= basketX-appleRadius and \
                   appleFalling[0] <= basketX-appleRadius+70:
                    score+=1
                #once the current apple has reached the ground, put another \
                #apple into play, and increase appleSpeed
                appleFalling= removeRandomApple(apples)
                appleSpeed+=.4
                
        #redraw the board with the updated variables     
        if appleFalling:    
            reDrawBoard(apples, appleFalling, basketX, basketY, score, \
                        cloudMove1, cloudMove2)
            
    #when it exits the while loop (there are no more apples and no apple is \
    #falling), display end of game screen
    endGame(score)

def main():  
    #create the canvas
    Draw.setCanvasSize(500, 500)
    
    Draw.setBackground(skyBlue)
    Draw.show()    
    
    playGame()
    
main()