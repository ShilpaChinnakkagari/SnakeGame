from turtle import Turtle
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake():
    def __init__(self):
        self.segments=[] #Make collection of segments
        self.create_snake() #Create snake from segments list
        self.head = self.segments[0] # 3-segments combine to a snake, out of 3, first segment is our head

    def create_snake(self): #Create snake game
        for position in STARTING_POSITIONS: #Loop through positions to create segments of 3
            new_segment = Turtle(shape='square') #Create snake_segment
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def add_segment(self,position):
        new_segment = Turtle(shape='square')  # Create snake_segment
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        #Add segment to the snake
        #Get previous one position (x,y)
        self.add_segment(self.segments[-1].position()) #Here position is a pair of (x,y) - position - buitlin func to return (x,y)

    def move(self): #segment-3 moves w.r.t segment-2 pos, segment-2 moves w.r.t segment-1 pos
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  #First segment_snake moves as per fixed dist = MOVE_DISTANCE

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
