import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "hello,world!",
            None,
            {"class": "greetings", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.PROPS_TO_HTML(),
            ' class="greetings" href="https://boot.dev"',
        )
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.TO_HTML(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.TO_HTML(), "Hello, world!")
    
    def test_to_html_no_children(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
    def test_to_html_childs(self):
        node = ParentNode(
         "d",
         [
            LeafNode("x", "Xursed text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "itallic text"),
         ]   
        )
         

if __name__ == "__main__":
    unittest.main()