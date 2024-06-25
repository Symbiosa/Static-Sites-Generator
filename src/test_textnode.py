import unittest

from textnode import TextNode
from textnode import (
    TextNode,
    textTypeText,
    textTypeBold,
    textTypeItalic,
    textTypeCode,
    textTypeImage,
    textTypeLink,
    splitNodesDelimiter
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", textTypeText)
        node2 = TextNode("This is a text node", textTypeText)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", textTypeText)
        node2 = TextNode("This is a text node", textTypeBold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", textTypeText)
        node2 = TextNode("This is a text node2", textTypeText)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", textTypeItalic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", textTypeItalic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", textTypeText, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
if __name__ == "__main__":
    unittest.main()