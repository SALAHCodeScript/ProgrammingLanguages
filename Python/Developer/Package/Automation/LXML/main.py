from lxml import etree, html

xml_data = """<root>
    <child name="foo">Hello</child>
    <child name="bar">World</child>
</root>"""

tree = etree.fromstring(xml_data)
print(tree.tag)

html_data = "<html><body><h1>Hello, World!</h1></body></html>"
tree = html.fromstring(html_data)

h1_text = tree.xpath("//h1/text()")  # Extract text from <h1> tag
print(h1_text)  # Output: ['Hello, World!']

for child in tree.xpath("//child"):
    print(child.get("name"), child.text)

root = etree.Element("root")
child = etree.SubElement(root, "child", name="example")
child.text = "This is a test"

xml_str = etree.tostring(root, pretty_print=True).decode()
print(xml_str)
