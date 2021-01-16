
from hdl_utils import svg


class New():

    def __init__(self, sName, sType=None):
        self.lContainers = []
        self.sName = sName
        self.type = sType
        self.y_margin = 10
        self.x_margin = 10
        self.type_height = 30
        self.iTitleHeight = 30
  
    def add_container(self, oContainer):
        self.lContainers.append(oContainer)
  
    def get_containers(self):
        return self.lContainers
  
    def num_containers(self):
        return len(self.lContainers)
  
    def write_svg(self, iDeviceX, iDeviceY, iHeight):
        lReturn = []
        iWidth = self.get_width()

        lReturn.extend(svg.rect_with_rounded_top_corners(iDeviceX, iDeviceY, iWidth, self.iTitleHeight, 'lightgrey', '#B0B0B0'))
        lReturn.extend(svg.center_text(iDeviceX + iWidth/2, iDeviceY + self.iTitleHeight/2, self.sName, 'device_name'))
        lReturn.extend(svg.rect_with_rounded_bottom_corners(iDeviceX, iDeviceY+self.iTitleHeight, iWidth, iHeight - self.iTitleHeight, 'white', '#B0B0B0'))

        iContainerX = iDeviceX + self.x_margin
        iContainerY = iDeviceY + self.iTitleHeight + self.y_margin
        
        if self.type is not None:
            lReturn.extend(svg.rect(iContainerX, iContainerY, iWidth - (2 * self.x_margin), self.type_height, '#90AADC', '#C8C8C8'))
            lReturn.extend(svg.center_text(iDeviceX + iWidth/2, iContainerY + self.type_height/2, self.type, 'type_name'))
            iContainerY += self.type_height + self.y_margin


        for oContainer in self.lContainers:
            lReturn.extend(oContainer.write_svg(iContainerX, iContainerY))
            iContainerY += oContainer.get_height() + self.y_margin
        return lReturn

    def set_type(self, sType):
        self.type = sType

    def get_type(self):
        return self.type

    def get_height(self):
        iReturn = 0

        iReturn += self.iTitleHeight
        iReturn += self.y_margin

        if self.type is not None:
            iReturn += self.type_height
            iReturn += self.y_margin

        for oContainer in self.lContainers:
            iReturn += oContainer.get_height() 

        iReturn += (self.num_containers() - 1) * self.y_margin

        iReturn += self.y_margin

        return iReturn

    def get_width(self):
        iReturn = 0
        iReturn += self.x_margin * 2

        iWidth = 0
        for oContainer in self.lContainers:
            iWidth = max(oContainer.get_width(), iWidth)
        iReturn += iWidth

        return iReturn
