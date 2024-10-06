
key_move_forward = "w"
key_move_back = "s"
key_move_left = "a"
key_move_right = "d"

class Hero:
    def __init__(self,position,land):
        self.land = land
        self.hero = loader.loadModel("block.glb")
        self.hero.setScale(0.1)
        self.hero.setPos(position)
        self.hero.reparentTo(render)
        self.functions()

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    
    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)

    def move_to(self,angle):
        self.move(angle)

    def move(self,angle):
        pos = self.moving(angle)
        self.hero.setPos(pos)

    def moving(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.check_moving(angle)
        new_x = x + dx
        new_y = y + dy
        return new_x,new_y,z
    def check_moving(self,angle):
        if angle >= 0 and angle <= 20:
            return(0,-1)
        elif angle <= 65:
            return(1,-1)
        elif angle <= 110:
            return(1,0)
        elif angle <= 155:
            return(1,1)
        elif angle <= 200:
            return(0,1)
        elif angle <= 245:
            return(-1,1)
        elif angle <= 290:
            return(-1,0)
        elif angle <= 335:
            return(-1,-1)
        else:
            return(0,-1)
        
    def functions(self):
        base.accept(key_move_forward, self.forward)
        base.accept(key_move_forward + "-repeat", self.forward)

        base.accept(key_move_back, self.back)
        base.accept(key_move_back+ "-repeat", self.back)

        base.accept(key_move_left, self.left)
        base.accept(key_move_left + "-repeat", self.left)

        base.accept(key_move_right, self.right)
        base.accept(key_move_right + "-repeat", self.right)