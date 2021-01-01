

from hdl_utils.entity_symbol import utils
from hdl_utils import xml
from hdl_utils import svg


class New():

    def __init__(self, sName):
        self.sName = sName
        self.lInputPorts= []
        self.lOutputPorts = []
        self.iBlockWidth = 10
        self.iBlockHeight = 50
        self.iPortHeight = 25
        self.sId = sName.replace(' ', '_')
        self.sSummaryBlockId = self.sId + '-summary'
        self.sPortBlockId = self.sId + '-port'
  
    def add_port(self, oPort):
        if oPort.get_direction() == 'in':
            self.lInputPorts.append(oPort)
        else:
            self.lOutputPorts.append(oPort)
  
    def get_input_ports(self):
        return self.lInputPorts
  
    def get_output_ports(self):
        return self.lOutputPorts
  
    def num_input_ports(self):
        return len(self.lInputPorts)
 
    def num_output_ports(self):
        return len(self.lOutputPorts)

    def get_height(self):
        iHeight = self.iBlockHeight
        iMaxPorts = max(len(self.lInputPorts), len(self.lOutputPorts))
        iHeight += iMaxPorts * self.iPortHeight
        self.iHeight = iHeight
        return iHeight

    def get_width(self):
        iInputWidth = 0
        for oPort in self.lInputPorts:
            iInputWidth = max(iInputWidth, oPort.get_width())
        
        iOutputWidth = 0
        for oPort in self.lOutputPorts:
            iOutputWidth = max(iOutputWidth, oPort.get_width())
        
        iWidth = iOutputWidth + iInputWidth
        iWidth *= utils.iTextScalingFactor
        return iWidth

    def write_svg(self, iCanvasWidth, iCanvasHeight, iBlockWidth):
        lReturn = []
        lReturn.extend(utils.build_svg_header(iCanvasWidth, iCanvasHeight, self.sName.replace(' ', '_')))
        lReturn.extend(self.build_summary_block(iCanvasWidth, iCanvasHeight, iBlockWidth))
        lReturn.extend(self.build_port_block(iCanvasWidth, iBlockWidth))
        lReturn.extend(utils.build_svg_footer())
    
        return lReturn

    def build_summary_block(self, iCanvasWidth, iCanvasHeight, iBlockWidth):
        lReturn = []
        lReturn.extend(utils.build_svg_header(iCanvasWidth, iCanvasHeight, self.sSummaryBlockId))
        iX = (iCanvasWidth / 2) - (iBlockWidth / 2)
        lReturn.extend(svg.rect(iX, 0, iBlockWidth, iCanvasHeight, "white", "grey"))
        iX = iCanvasWidth / 2
        iY = iCanvasHeight / 2
        lReturn.extend(svg.center_text(iX, iY, self.sName))
        if self.num_input_ports() > 0:
            lReturn.extend(svg.line(0, iCanvasHeight / 2, (iCanvasWidth / 2) - (iBlockWidth / 2), iCanvasHeight / 2))
        if self.num_output_ports() > 0:
            lReturn.extend(svg.line((iCanvasWidth/2) + (iBlockWidth/2), iCanvasHeight / 2, iCanvasWidth, iCanvasHeight / 2))
        lReturn.extend(utils.build_svg_footer())
        return lReturn

    def build_port_block(self, iCanvasWidth, iBlockWidth):
        lReturn = []
        iCanvasHeight = self.get_height()
        lReturn.extend(utils.build_svg_header(iCanvasWidth, iCanvasHeight, self.sPortBlockId, 'hidden'))
        iX = (iCanvasWidth / 2) - (iBlockWidth / 2)
        lReturn.extend(svg.rect(iX, 0, iBlockWidth, iCanvasHeight, "white", "grey"))
        iX = iCanvasWidth / 2
        iY = self.iBlockHeight / 2
        lReturn.extend(svg.center_text(iX, iY, self.sName))
        for iPort, oPort in enumerate(self.lInputPorts):
            iPortY = self.iBlockHeight + (self.iPortHeight * (iPort))
            iPortX = (iCanvasWidth / 2) - (iBlockWidth / 2)
            lReturn.extend(svg.line(0, iPortY, iPortX, iPortY))
            lReturn.extend(svg.left_align_text(iPortX + 5, iPortY + 5, oPort.get_name()))
        for iPort, oPort in enumerate(self.lOutputPorts):
            iPortY = self.iBlockHeight + (self.iPortHeight * (iPort))
            iPortX = (iCanvasWidth / 2) + (iBlockWidth / 2)
            lReturn.extend(svg.line(iPortX, iPortY, iCanvasWidth, iPortY))
            lReturn.extend(svg.right_align_text(iPortX - 5, iPortY + 5, oPort.get_name()))
        lReturn.extend(utils.build_svg_footer())
        return lReturn

    def build_script(self):
        lReturn = []
        lReturn.append(f'document.querySelector("#{self.sSummaryBlockId}").addEventListener("click", function (evt) ' + '{')
        lReturn.append(f'document.querySelector("#{self.sPortBlockId}").setAttribute("visibility", "visible");')
        lReturn.append(f'document.querySelector("#{self.sId}").setAttribute("height", {self.iHeight});')
        lReturn.append(f'document.querySelector("#{self.sSummaryBlockId}").setAttribute("visibility", "hidden");')
        lReturn.append('});')
        lReturn.append('')
        lReturn.append(f'document.querySelector("#{self.sPortBlockId}").addEventListener("click", function (evt) ' + '{')
        lReturn.append(f'document.querySelector("#{self.sSummaryBlockId}").setAttribute("visibility", "visible");')
        lReturn.append(f'document.querySelector("#{self.sId}").setAttribute("height", {self.iBlockHeight});')
        lReturn.append(f'document.querySelector("#{self.sPortBlockId}").setAttribute("visibility", "hidden");')
        lReturn.append('});')
        return lReturn
