from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_eq(self): #test __eq__
        node = HTMLNode(tag= "a", value= "link")
        node2 = HTMLNode(tag= "a", value= "link", children= None, props= None)
        self.assertEqual(node, node2)

    def test_notequal(self): #test not __eq__
        node = HTMLNode(children= ["a", "b"])
        node2 = HTMLNode(children= ["aa", "b"])
        self.assertNotEqual(node, node2)

    def test_repr(self): #test __repr__
        node = HTMLNode(tag= "a", 
                         value= "link", 
                         children= ["a"], 
                         props= {
                             "href": "https://www.google.com",
                             "target": "_blank"
                             }
                        )
        self.assertEqual(repr(node),
                        ("HTMLNode(a, link, children: ['a'], {'href': 'https://www.google.com', 'target': '_blank'})"))
        
    def test_to_html_props(self): #test method
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

if __name__ == "__main__":
    unittest.main()