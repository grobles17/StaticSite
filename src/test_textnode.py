import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self): #test __eq__
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self): #test Enum type __eq__
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self): #test text __eq__
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self): #test url __eq__
        node = TextNode("This is a text node", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self): #test __repr__
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()