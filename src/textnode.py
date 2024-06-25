from htmlnode import LeafNode

textTypeText = "text"
textTypeBold = "bold"
textTypeItalic = "italic"
textTypeCode = "code"
textTypeLink = "link"
textTypeImage = "image"

class TextNode:
    def __init__(self, text, textType, url=None):
        self.text = text
        self.textType = textType
        self.url = url
    def __eq__(self,other):
        return (
            self.textType == other.textType
            and self.text == other.text
            and self.url == other.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.textType}, {self.url})"

def text_node_to_html_node(textNode):
    if textNode.text_type == textTypeText:
        return LeafNode(None, textNode.text)
    if textNode.text_type == textTypeBold:
        return LeafNode("b", textNode.text)
    if textNode.text_type == textTypeItalic:
        return LeafNode("i", textNode.text)
    if textNode.text_type == textTypeCode:
        return LeafNode("code", textNode.text)
    if textNode.text_type == textTypeLink:
        return LeafNode("a", textNode.text, {"href": textNode.url})
    if textNode.text_type == textTypeImage:
        return LeafNode("img", "", {"src": textNode.url, "alt": textNode.text})
    raise ValueError(f"Invalid text type: {textNode.text_type}")