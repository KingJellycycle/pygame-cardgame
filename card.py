import pygame
class card:
    cardlist = []
    UniqueCards = []
    cardlocation = [
        [
            [75,105],
            [206,105],
            [337,105],
            [468,105]
        ],
        [
            [75,325],
            [206,325],
            [337,325],
            [468,325]
        ],
        [
            [75,495],
            [206,495],
            [337,495],
            [468,495]
        ]
    ]

    def __init__(self,name,image,title,description=None,attack=1,health=1,cost=0,onplay=None,passive=None,isUnqiue=False):
        self.name = name
        self.image = pygame.image.load("./assets/images/"+image+".png")
        self.imagerect = self.image.get_rect()
        self.title = title
        self.description = description
        self.pos = [[0,0],[75,105]]
        self.scale = 1
        self.size = [121,170]
        self.health = health
        self.attack = attack
        self.cost = cost
        self.onplay = onplay
        self.passive = passive
        self.isRendered = True
        self.isUnqiue = isUnqiue

        if (self.isUnqiue == False):
            card.cardlist.append(self)
        else:
            card.UniqueCards.append(self)
        
    @classmethod
    def draw(cls,surface,draw):
            for item in cls.cardlist:
                if (item.isRendered == True):
                    surface.blit(pygame.transform.scale(item.image, (item.size)), (item.pos[draw]))
        
    def isRendering(self,state):
        self.isRendered = state
    
    def update(cls):
        pass

cards = [
    #name,image,title,description,attack,health,cost,onplay,passive
    ["Azir","Azir","The Emperor of the Sands","On-play: Summons 1 Sand Soldier\n\nSand Soldiers - 3 Attack, 1 Health",2,2,3],
    ["Braum","Braum","The Heart of Freljord","On-play: Becomes a Taunt unit.",2,6,3],
    ["Kindred","Kindred","The Eternal Hunters","On-play: This unit can prevent the death of any unit selected (Last for 1 turn).\n\nPassive: Wolf will mark a random enemy unit if the marked unit is killed Gain 3 Attack.",1,3,4],
    ["MinionC","Minion","Caster","Caster minion!",3,1,2],
    ["MinionM","Minion1","Melee","Melee minion!",1,2,1],
    ["MinionS","Minion2","Seige","Seige minion!",3,3,3]
]

ucards = [
    ["Sand Soldier","Azir","The Emperor's Follower","Summoned By Azir Himself",3,1,0,None,None,True]
]

for thecards in cards:
    card(*thecards)

for thecards in ucards:
    card(*thecards)