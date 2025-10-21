import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r', encoding='windows-1251')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_dict = {}

for node in elements:
    name = None
    value = None
    
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'Name':
                if child.firstChild and child.firstChild.nodeType == 3:
                    name = child.firstChild.data
            if child.tagName == 'Value':
                if child.firstChild and child.firstChild.nodeType == 3:
                    value_str = child.firstChild.data.replace(',', '.')
                    value = float(value_str)
    
    if name and value is not None:
        currency_dict[name] = value

print(currency_dict)

xml_file.close()
