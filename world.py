
class Mapmanager():
    def __init__(self):
        self.model = "block.glb"
        self.texture = "newgrass.png"
        self.color = [(0.2, 0.2, 0.35, 1),
                     (0.7, 0.1, 0.85, 1),
                     (0.7, 0.9, 0.5, 1),
                     (0.2, 0.6, 0.25, 1)
                     ]
        self.startNew()
        self.addBlock((0,10,0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def getColor(self, y):
        if y < len(self.color):
            return self.color[y]
        else:
            return self.color[len(self.color)-1]

    def addBlock(self, position):
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position)
       self.c = self.getColor(int(position[2]))
       self.block.setColor(self.c)
       self.block.reparentTo(self.land)

    def loadMap(self):
        self.land.removeNode()
        self.startNew()
        with open("land.txt") as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for l in line:
                    for z0 in range(int(l)+1):
                        block = self.addBlock((x,y,z0))
                    x +=1
                y += 1
        return x,y