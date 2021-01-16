
from hdl_utils import xml


def build_header(iWidth, iHeight):
    lReturn = []
    lReturn.append(xml.open_tag('?xml version="1.0"?'))
    lReturn.append(xml.open_tag(f'svg xmls="http://www.w3.org/2000/svg" width="{iWidth}" height="{iHeight}"'))
    return lReturn


def build_footer():
    lReturn = []
    lReturn.append(xml.close_tag('svg'))
    return lReturn


def build_style():
    lReturn = []
    lReturn.append(xml.open_tag('style'))

    lReturn.append('.device_name { font: 16px Calibri}')
    lReturn.append('.block_name { font: 13px Calibri; fill: white;}')
    lReturn.append('.type_name { font: 13px Calibri; fill: white;}')
    lReturn.append('.container_name { font: 16px Calibri}')

    lReturn.append('.legend_title { font: 16px Calibri}')
    lReturn.append('.status_name { font: 13px Calibri; fill: white;}')

    lReturn.append(xml.close_tag('style'))

    return lReturn
