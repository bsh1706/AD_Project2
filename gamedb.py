import pickle



class GameDB():

    def __init__(self):
        self.dbfilename = 'gamedb.dat'
        self.readGameDB()

    def readGameDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []
        scdb = []

        try:
            scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return scdb

    def writeGameDB(self, gamedb):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(gamedb, fH)
        fH.close()


if __name__ == '__main__':
    game = GameDB()
