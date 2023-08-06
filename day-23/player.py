from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
      
            
            

    def reset(self):
        self.goto(STARTING_POSITION)

    def is_top(self):
        return self.ycor() > FINISH_LINE_Y
    


#class Player:
#    def __init__(self):
#        self.player = Turtle()
#        self.player.shape("turtle")
#        self.player.penup()
#        self.player.setheading(90)
#        self.player.goto(STARTING_POSITION)
#
#    def move(self):
#        self.player.forward(MOVE_DISTANCE)
#        if self.is_top():
#            #self.update_score()
#            self.reset()
#
#    def reset(self):
#        self.player.goto(STARTING_POSITION)
#        
#    def is_top(self):
#        return self.player.ycor() > FINISH_LINE_Y
#    