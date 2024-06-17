import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "21", "many", "any")
        node2 = HTMLNode("Node is text", "italic", None, "catcat")
        node3 = HTMLNode("String", "Kissa", False, "Gotgot")
        node4 = HTMLNode(self,self,self, "cat")
        self.assertEqual(node, node2)
        self.assertEqual(node,node3)
        self.assertEqual(node,node4)

if __name__ == "__main__":
    unittest.main()