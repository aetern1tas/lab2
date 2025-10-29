import xml.dom.minidom as minidom

with open('currency.xml', 'r', encoding='windows-1251') as xml_file:
    xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
currency_dict = {}

for valute in dom.getElementsByTagName('Valute'):
    name = valute.getElementsByTagName('Name')[0].firstChild.data
    value = valute.getElementsByTagName('Value')[0].firstChild.data
    currency_dict[name] = float(value.replace(',', '.'))

print(currency_dict)