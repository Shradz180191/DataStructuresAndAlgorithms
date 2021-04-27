'''
Use a Player class that provides attributes that store the 
first name, last name, position, at bats, and hits for a player. 
The class constructor should use these five attributes as parameters. 
This class should also provide a method that returns the full name of 
a player and a method that returns the batting average for a player.
'''


class player:
    def __init__(self,firstname,lastname,position,at_bats,hits):
        self.firstName = firstname
        self.lastName = lastname
        self.position = position
        self.at_bats = at_bats
        self.hits = hits
        return self

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPosition(self):
        return self.position

    def getAt_bats(self):
        return self.at_bats

    def getHits(self):
        return self.hits

    def setFirstName(self,firstname):
        self.firstName = firstname

    def setLastName(self,lastname):
        self.lastName = lastname

    def setPosition(self,position):
        self.position = position

    def setAt_bats(self,at_bats):
        self.at_bats = at_bats

    def setHits(self,hits):
        self.hits = hits

    def getFullName(self):
        return self.firstName+" "+self.lastName

    def getBattingAvg(self):
        ab = float(self.at_bats)
        hits = float(self.hits)
        if ab > 0:
            average = hits / ab
        return average


class lineUp:
    def __init__(self,playerList):
        self.lineupList = playerList
        self.max = len(playerList)
        return self

    def displayLineup(self):
        # Print header
        print('   Player  	            	     POS    AB     H     AVG')
        print('-' * 60)
        count = 1
        for player in self.lineupList:
            name = player.getFullName()
            position = player.getPosition()
            AB = player.getAt_bats()
            H = player.getHits()
            ab = float(AB)
            hits = float(H)
            average = 0
            if ab > 0:
                average = hits / ab

            print("{0:3}{1:31}{2:>6}{3:>6}{4:>6}{5:>8}".format(str(count), name, position, AB, H, str(round(average, 3))))
            count = count + 1

    def addPlayer(self, player):
        self.lineupList.append(player)
        print('Player [',player.getFullName, '] has been added successfully!!')


    def removePlayer(self,LineUpNumber):
        if LineUpNumber > len(self.lineUpList)-1:
            print('\n\tInvalid LineUp Number')
            return None
        else:
            self.lineupList.pop(LineUpNumber-1)
            print('\n\tPlayer at LineUp Number ', LineUpNumber,' has been removed from the LineUpList')



    def movePlayer(self,oldLineUpNumber, newLineUpNumber):
        # Player to be moved
        player_to_move = self.LineUpList[int(oldLineUpNumber)-1]
        print('\n\t Player to be moved: \t', player_to_move.getFullName())

        correct = False
        while correct == False:
            try:
                if int(newLineUpNumber) >= 1 and int(newLineUpNumber) <= len(self.LineUpList):
                    correct = True
                else:
                    print('Invalid LineUp number. Enter a valid LineUp number i.e. > = 1 and <=', n)
            except:
                print('Invalid LineUp number. Enter a valid LineUp number i.e. >= 1 and <=', n)

        # Now insert in new position and all players after elem are shifted to the right.
        self.LineupList.insert(newLineUpNumber - 1, player_to_move)
        print(player_to_move.getFullName(), ' has been moved to ',newLineUpNumber)


    def getPlayer(self,LineUpNumber):
        if LineUpNumber>len(self.LineUpList):
            print('\n\t Invalid LineUp number.')
            return None
        else:
            return self.LineUpList[LineUpNumber-1]

    def setPlayer(self,LineUpNumber,player):
        if LineUpNumber>len(self.LineUpList):
            print('\n\t Invalid LineUp number.')
            return None
        else:
            self.LineUpList.insert(LineUpNumber,player)

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            self.n = self.n + 1
            return self.LineUpList[self.n]
        else:
            raise StopIteration
