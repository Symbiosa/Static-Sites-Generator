import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a text node", "bold", "www.hyvinvointvarkkaja.fi")
        node2 = HTMLNode("Node is text", "italic", url=None)
        node3 = HTMLNode("String", "Kissa", url = False)
        node4 = HTMLNode(self,self,url = self)
        self.assertEqual(node, node2)
        self.assertEqual(node,node3)
        self.assertEqual(node,node4)

if __name__ == "__main__":
    unittest.main()