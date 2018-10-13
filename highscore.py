import datetime

class HSsystem:

    name = "HSsystem"
    scores = []
    Slocation = "./scores/scores.txt"
    
    def __init__(self):
        self.scores = []
        try: 
            scoreFile = open(self.Slocation,"r")
            # Read score file As python code, Because it is really just an array
            self.scores = eval(scoreFile.read())
            print(scoreFile.read())
            scoreFile.close()
            print(self.name + " - Scores found!")
        except IOError:
            print(self.name + " - No highscore found! (Not able to access IO?) - Directory: ("+str(self.Slocation)+")")
        except ValueError:
            print(self.name + " - Oh no... lets create a new highscore anyway.")
    
    def addScore(self,name,amount):
        date = datetime.datetime.now()

        new = False
        itemIndex = -1
        for i in range(0,len(self.scores)):
            if self.scores[i][0] == name:
                itemIndex = i
        
        if itemIndex >= 0:
            self.scores[itemIndex][1] += amount
        else:
            self.scores.append([name,amount,str(date.strftime("%Y-%m-%d %H:%M"))])

    def saveScores(self):
        # open a file for writing.
        try:
            print(self.name + " - Saving... ("+str(self.scores)+")")
            scoreFile = open(self.Slocation,"w")
            scoreFile.write(str(self.scores))
            scoreFile.close()
        except IOError:
            print(self.name + " - Huh, Can not create highscore file ("+self.Slocation+")")

    def getScores(self,amount):
        scoreList = []

        for i in range(0, len(self.scores)-1):
            self.bubbleSort(self.scores)

        for item in range(0,amount):
            try:
                scoreList.append(self.scores[item])
            except IndexError: 
                scoreList.append(["None",0,0])

        return scoreList

    def bubbleSort(self,selectedlist):
        for num in range(0,len(selectedlist),1):
            for i in range(num):
                if selectedlist[i][1] < selectedlist[i+1][1]:
                    temp = selectedlist[i]
                    selectedlist[i] = selectedlist[i+1]
                    selectedlist[i+1] = temp
                    