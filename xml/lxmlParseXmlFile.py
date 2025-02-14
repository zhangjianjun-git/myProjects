from lxml import etree

# 假设我们有以下 XML 内容
xml_content = '''<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''

# 解析 XML
root = etree.fromstring(xml_content)
# 使用 XPath 查询
for country in root.xpath('//country'):
    name = country.get('name')
    rank = country.xpath('rank/text()')[0]
    year = country.xpath('year/text()')[0]
    gdppc = country.xpath('gdppc/text()')[0]
    neighbors = [neighbor.get('name') for neighbor in country.xpath('neighbor')]

    print(f"Country: {name}")
    print(f"Rank: {rank}")
    print(f"Year: {year}")
    print(f"GDP per Capita: {gdppc}")
    print(f"Neighbors: {neighbors}")
    print()
