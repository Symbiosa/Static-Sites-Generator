import unittest

from htmlnode import HTMLNode


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
            ' class="greeting" href="https://boot.dev"',
        )


if __name__ == "__main__":
    unittest.main()