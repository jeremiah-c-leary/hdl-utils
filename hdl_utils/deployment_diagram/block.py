
import svg


class New():

    def __init__(self, sName, oStatus):
        self.sName = sName
        self.oStatus = oStatus 
        self.iHeight = 25 
        self.iWidth = 100
  
    def write_svg(self, iX, iY):
        lReturn = []
        sColor = self.oStatus.get_fill_color()
        lReturn.extend(svg.rect(iX, iY, self.iWidth, self.iHeight, sColor, 'white'))
        iTextX = iX + self.iWidth / 2
        iTextY = iY + self.iHeight / 2 
        lReturn.extend(svg.center_text(iTextX, iTextY, self.sName, 'block_name'))
        return lReturn

    def get_height(self):
        return self.iHeight

    def get_width(self):
        return self.iWidth
