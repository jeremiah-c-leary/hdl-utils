
from hdl_utils.deployment_diagram import utils


class New():

    def __init__(self):
        self.lDevices = []
        self.oLegend = None
  
    def add_device(self, oDevice):
        self.lDevices.append(oDevice)
  
    def get_devices(self):
        return self.lDevices
  
    def num_devices(self):
        return len(self.lDevices)
 
    def add_legend(self, oLegend):
        self.oLegend = oLegend
 
    def write_svg(self, sFilename):
        iWidth, iHeight = self.calculate_diagram_area()
        lReturn = utils.build_header(iWidth, iHeight)
        lReturn.extend(utils.build_style())
  
        iDeviceX = 0
        iDeviceY = 0
        for oDevice in self.lDevices:
            lReturn.extend(oDevice.write_svg(iDeviceX, iDeviceY, iHeight))
            iDeviceX += oDevice.get_width()

        lReturn.extend(self.oLegend.write_svg(iDeviceX, iDeviceY))
  
        lReturn.extend(utils.build_footer())
        for sLine in lReturn:
            print(sLine)
  
    def max_number_of_blocks(self):
        iReturn = 0
        for oDevice in self.lDevices:
            iReturn = max(iReturn, oDevice.num_blocks())
        return iReturn
  
    def calculate_diagram_area(self):
        iWidth = 0
        iHeight = 0
        for oDevice in self.lDevices:
            iWidth += oDevice.get_width()
            iHeight = max(iHeight, oDevice.get_height())

        iWidth += self.oLegend.get_width()
        iHeight = max(iHeight, self.oLegend.get_height())

        return iWidth, iHeight
