
import svg


class New():

    def __init__(self, sName, sColor):
        self.sName = sName
        self.sColor = sColor
        self.iHeight = 25 
        self.iWidth = 100
        self.sTextColor = 'white'
  
    def write_svg(self, iX, iY):
        lReturn = []
        lReturn.extend(svg.rect(iX, iY, self.iWidth, self.iHeight, self.sColor, self.sTextColor))
        iTextX = iX + self.iWidth / 2
        iTextY = iY + self.iHeight / 2 
        lReturn.extend(svg.center_text(iTextX, iTextY, self.sName, 'status_name'))
        return lReturn

    def get_height(self):
        return self.iHeight

    def get_width(self):
        return self.iWidth

    def get_fill_color(self):
        return self.sColor
