
from hdl_utils import xml


def rect(iX, iY, iWidth, iHeight, sFill, sStroke):
    lReturn = []
    lReturn.append(xml.self_closing_tag(f'rect x="{iX}" y="{iY}" width="{iWidth}" height="{iHeight}" fill="{sFill}" stroke="{sStroke}"'))
    return lReturn


def center_text(iX, iY, sText, sClass=None):
    lReturn = []
    if sClass is None:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" dominant-baseline="middle" text-anchor="middle"')
    else:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" dominant-baseline="middle" text-anchor="middle" class="{sClass}"')
    sReturn += sText
    sReturn += xml.close_tag('text')
    lReturn.append(sReturn)
    return lReturn


def left_align_text(iX, iY, sText, sClass=None):
    lReturn = []
    if sClass is None:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" text-anchor="start"')
    else:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" text-anchor="start" class="{sClass}"')
    sReturn += sText
    sReturn += xml.close_tag('text')
    lReturn.append(sReturn)
    return lReturn


def right_align_text(iX, iY, sText, sClass=None):
    lReturn = []
    if sClass is None:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" text-anchor="end"')
    else:
        sReturn = xml.open_tag(f'text x="{iX}" y="{iY}" text-anchor="end" class="{sClass}"')
    sReturn += sText
    sReturn += xml.close_tag('text')
    lReturn.append(sReturn)
    return lReturn


def rect_with_rounded_top_corners(iX, iY, iWidth, iHeight, sFill, sStroke):
    lReturn = []
    iCurve = 10
    sCmd = 'path d="'
    sCmd += f' M{iX},{iY+iCurve}'
    sCmd += f' a{iCurve},{iCurve} 0 0,1 {iCurve},-{iCurve}'
    sCmd += f' h {iWidth - 2*iCurve}'
    sCmd += f' a{iCurve},{iCurve} 0 0,1 {iCurve},{iCurve}'
    sCmd += f' v {iHeight - iCurve}'
    sCmd += f' h -{iWidth}'
    sCmd += f' z'
    sCmd += '"'
    sCmd += f' fill="{sFill}"'
    sCmd += f' stroke="{sStroke}"'
    lReturn.append(xml.self_closing_tag(sCmd))
    return lReturn


def rect_with_rounded_bottom_corners(iX, iY, iWidth, iHeight, sFill, sStroke):
    lReturn = []
    iCurve = 10
    sCmd = 'path d="'
    sCmd += f' M{iX},{iY}'
    sCmd += f' h {iWidth}'
    sCmd += f' v {iHeight - iCurve}'
    sCmd += f' a{iCurve},{iCurve} 0 0,1 -{iCurve},{iCurve}'
    sCmd += f' h -{iWidth - 2*iCurve}'
    sCmd += f' a{iCurve},{iCurve} 0 0,1 -{iCurve},-{iCurve}'
    sCmd += f' z'
    sCmd += '"'
    sCmd += f' fill="{sFill}"'
    sCmd += f' stroke="{sStroke}"'
    lReturn.append(xml.self_closing_tag(sCmd))
    return lReturn

def line(iX1, iY1, iX2, iY2, sStroke="black"):
    lReturn = []
    sCmd = 'line '
    sCmd += f'x1="{iX1}" '
    sCmd += f'y1="{iY1}" '
    sCmd += f'x2="{iX2}" '
    sCmd += f'y2="{iY2}" '
    sCmd += f'stroke="{sStroke}"'
    lReturn.append(xml.self_closing_tag(sCmd))
    return lReturn
