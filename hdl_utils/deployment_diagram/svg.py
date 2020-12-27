
import xml


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
