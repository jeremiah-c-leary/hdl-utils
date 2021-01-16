
from hdl_utils import svg


class New():

    def __init__(self):
        self.lStatus = []
        self.y_margin = 10
        self.x_margin = 10
        self.iTitleHeight = 30
        self.sTitle = 'Legend'
  
    def add_status(self, oStatus):
        self.lStatus.append(oStatus)
  
    def num_status(self):
        return len(self.lStatus)
  
    def write_svg(self, iLegendX, iLegendY):
        lReturn = []
        iWidth = self.get_width()
        lReturn.extend(svg.center_text(iLegendX + iWidth/2, iLegendY + self.iTitleHeight/2, self.sTitle, 'legend_title'))

        iLegendX = iLegendX + self.x_margin
        iLegendY = iLegendY + self.iTitleHeight + self.y_margin

        for oStatus in self.lStatus:
            lReturn.extend(oStatus.write_svg(iLegendX, iLegendY))
            iLegendY += oStatus.get_height()
        return lReturn

    def get_height(self):
        iReturn = 0

        iReturn += self.iTitleHeight
        iReturn += self.y_margin

        for oStatus in self.lStatus:
            iReturn += oStatus.get_height() 

        return iReturn

    def get_width(self):
        iReturn = 0
        iReturn += self.x_margin

        iWidth = 0
        for oStatus in self.lStatus:
            iWidth = max(oStatus.get_width(), iWidth)
        iReturn += iWidth

        return iReturn
