from Figure import Figure

class King(Figure):

    def __init__(self, position, white):
        Figure.__init__(self,position)
        if( white ):
            self.white = True
        else:
            self.white = False

    def __str__(self):
        return "K"
