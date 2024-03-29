# needs testing major
# seems functonal

class map:

    def _loadMap_(self):
        reader = open("mapConfig.txt", "r")

        info = []

        for row in reader:
            info.append(row[:-1].split(","))

        return info

    def _nodeSetup_(self):
        #NEEDS OPTIMIZATION
        info = self._loadMap_()

        a = mapNode(info[0][0], None)
        b = mapNode(info[1][0], None)
        c = mapNode(info[2][0], None)
        d = mapNode(info[3][0], None)
        e = mapNode(info[4][0], None)
        f = mapNode(info[5][0], None)
        g = mapNode(info[6][0], None)
        h = mapNode(info[7][0], None)
        i = mapNode(info[8][0], None)
        j = mapNode(info[9][0], None)
        k = mapNode(info[10][0], None)
        l = mapNode(info[11][0], None)
        m = mapNode(info[12][0], None)
        n = mapNode(info[13][0], None)
        o = mapNode(info[14][0], None)
        p = mapNode(info[15][0], None)

        a.addConn([b, c, d])
        b.addConn([a, e])
        c.addConn([a, e])
        d.addConn([a, f])
        e.addConn([b, c, g])
        f.addConn([d, h, i])
        g.addConn([e, h, k, l])
        h.addConn([f, g, k, j])
        i.addConn([f])
        j.addConn([h])
        k.addConn([g, h, l, o])
        l.addConn([m, n, g, k, o])
        m.addConn([l])
        n.addConn([l])
        o.addConn([l, k, p])
        p.addConn([o])

        self.currNode = a

    def move(self, target):
        assert target in self.currNode.rtnConn()

        self.currNode = self.currNode.moveNode(target)

        print(self.currNode)

    def __init__(self):
        self.currNode = None
        self._nodeSetup_()

    def __str__(self):
       return self.currNode.__str__()


class mapNode:
    def __init__(self, currLocation, nextNodes = None):
        self.currLocation = currLocation
        self.nextNodes = nextNodes

    def addConn(self, connList):
        self.nextNodes = connList

    def rtnConn(self):
        str = ""

        for i in range(len(self.nextNodes)):
            str += self.nextNodes[i].currLocation + " "

        return str

    def moveNode(self, target):
        for i in range(len(self.nextNodes)):
            if self.nextNodes[i].currLocation == target:
                return self.nextNodes[i]
        return "Error"

    def __str__(self):
        strForm = str(self.currLocation) + ":"

        for i in range(len(self.nextNodes)):
            strForm += " " + self.nextNodes[i].currLocation

        return strForm

    def __len__(self):
        #returns number of connecting nodes
        return len(self.nextNodes)
