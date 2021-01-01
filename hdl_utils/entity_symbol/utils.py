
from hdl_utils import xml

iTextScalingFactor = 10


def build_html_header():
    lReturn = []
    lReturn.append(xml.open_tag('html'))
    lReturn.extend(build_style())
    lReturn.append(xml.open_tag('body'))
    return lReturn


def build_html_footer():
    lReturn = []
    lReturn.append(xml.close_tag('body'))
    lReturn.append(xml.close_tag('html'))
    return lReturn


def build_style():
    lReturn = []
    lReturn.append(xml.open_tag('style'))

    lReturn.append('svg { display: inline !important;}')

    lReturn.append('.invisible { visibility: hidden;}')

    lReturn.append(xml.close_tag('style'))

    return lReturn


def build_svg_header(iCanvasWidth, iCanvasHeight, sId, sVisibility='visible'):
    lReturn = []
    lReturn.append(xml.open_tag(f'svg id="{sId}" xmlns="http://www.w3.org.2000/svg" width="{iCanvasWidth}" height="{iCanvasHeight}" visibility="{sVisibility}"'))
    return lReturn


def build_svg_footer():
    lReturn = []
    lReturn.append(xml.close_tag('svg'))
    return lReturn
