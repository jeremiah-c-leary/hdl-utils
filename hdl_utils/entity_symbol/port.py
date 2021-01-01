

class New():

    def __init__(self, sName, sDirection):
        self.sName = sName
        self.sDirection = sDirection
        self.iWidth = len(sName)
  
    def get_name(self):
        return self.sName
  
    def get_direction(self):
        return self.sDirection

    def get_width(self):
        return self.iWidth
