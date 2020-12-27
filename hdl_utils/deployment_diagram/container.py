
import math
import svg


class New():

    def __init__(self, sName):
        self.lBlocks = []
        self.sName = sName
        self.y_margin = 10
        self.x_margin = 10
        self.iTitleHeight = 30 
        self.iColumns = 1
  
    def add_block(self, oBlock):
        self.lBlocks.append(oBlock)
  
    def get_blocks(self):
        return self.lBlocks
  
    def num_blocks(self):
        return len(self.lBlocks)
 
    def set_columns(self, iColumns):
        self.iColumns = iColumns
 
    def write_svg(self, iX, iY):
        lReturn = []
        iWidth = self.get_width()
        iHeight = self.get_height()
        lReturn.extend(svg.rect(iX, iY, iWidth, self.iTitleHeight, '#8AB8E1', '#2D71AE'))
        lReturn.extend(svg.center_text(iX + iWidth/2, iY + self.iTitleHeight/2, self.sName, 'container_name'))
        lReturn.extend(svg.rect(iX, iY + self.iTitleHeight, iWidth, iHeight - self.iTitleHeight, 'white', '#2D71AE'))
        iBlockX = iX + self.x_margin
        iBlockY = iY + self.y_margin + self.iTitleHeight

        iBlock = 0
        while iBlock < self.num_blocks():
            for iColumn in range(self.iColumns):
                try:
                    oBlock = self.lBlocks[iBlock]
                    lReturn.extend(oBlock.write_svg(iBlockX + (iColumn * oBlock.get_width()), iBlockY))
                    iBlock += 1
                except:
                    iBlock = self.num_blocks()
            iBlockY += oBlock.get_height()
        return lReturn

    def get_height(self):
        iReturn = 0
        iReturn += self.iTitleHeight
        iReturn += self.y_margin

        iNumRows = math.ceil(self.num_blocks()/self.iColumns)
        iReturn += self.lBlocks[0].get_height() * iNumRows

        iReturn += self.y_margin

        return iReturn

    def get_width(self):
        iReturn = 0
        iReturn += self.x_margin * 2

        iWidth = self.iColumns * self.lBlocks[0].get_width()

        iReturn += iWidth

        return iReturn
