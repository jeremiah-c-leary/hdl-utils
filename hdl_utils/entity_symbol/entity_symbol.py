

from hdl_utils.entity_symbol import utils
from hdl_utils import xml
from hdl_utils import svg


class New():

    def __init__(self, sName):
        self.sName = sName
        self.lInterfaces= []
        self.iWidth = None
        self.iBlockWidth = None
        self.iBlockHeight = 50
  
    def add_interface(self, oInterface):
        self.lInterfaces.append(oInterface)
  
    def get_interfaces(self):
        return self.lInterfaces
  
    def num_interfaces(self):
        return len(self.lInterfaces)
 
    def write_svg(self, sFilename):
        self.iWidth, self.iBlockWidth = self.calculate_diagram_width()
        lReturn = utils.build_html_header()
        lReturn.append(xml.open_tag('br')) 
        lReturn.extend(utils.build_svg_header(self.iWidth, self.iBlockHeight, 'header'))
        lReturn.extend(self.build_title_block())
        lReturn.extend(utils.build_svg_footer())

        for oInterface in self.lInterfaces:
            lReturn.append(xml.open_tag('br')) 
            lReturn.extend(oInterface.write_svg(self.iWidth, self.iBlockHeight, self.iBlockWidth))

        lReturn.append(xml.open_tag('script'))
        for oInterface in self.lInterfaces:
            lReturn.extend(oInterface.build_script())
        lReturn.append(xml.close_tag('script'))

        lReturn.extend(utils.build_html_footer())
        for sLine in lReturn:
            print(sLine)

    def calculate_diagram_width(self):
        iWidth = len(self.sName) * utils.iTextScalingFactor
        for oInterface in self.lInterfaces:
            iWidth = max(iWidth, oInterface.get_width())
        return iWidth + 200, iWidth

    def build_title_block(self):
        lReturn = []
        iX = (self.iWidth / 2) - (self.iBlockWidth / 2)
        lReturn.extend(svg.rect(iX, 0, self.iBlockWidth, self.iBlockHeight, "grey", "grey"))
        iX = self.iWidth / 2
        iY = self.iBlockHeight / 2
        lReturn.extend(svg.center_text(iX, iY, self.sName))
        return lReturn
