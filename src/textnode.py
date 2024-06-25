from htmlnode import LeafNode

textTypeText = "text"
textTypeBold = "bold"
textTypeItalic = "italic"
textTypeCode = "code"
textTypeLink = "link"
textTypeImage = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self,other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == textTypeText:
        return LeafNode(None, text_node.text)
    if text_node.text_type == textTypeBold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == textTypeItalic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == textTypeCode:
        return LeafNode("code", text_node.text)
    if text_node.text_type == textTypeLink:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == textTypeImage:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")

def splitNodesDelimiter(oldNodes, delimiter, textType):
    nodeList = []
    for oldNode in oldNodes:
        if oldNode.textType != textTypeText:
            nodeList.append(oldNode)
        splitNodes = []
        sections = oldNode.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splitNodes.append(TextNode(sections[i], textTypeText))
            else:
                splitNodes.append(TextNode(sections[i], textType))
        nodeList.extend(splitNodes)
    return nodeList