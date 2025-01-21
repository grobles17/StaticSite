import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_tohtml_emptytag(self):
        emptytagnode = LeafNode(tag= None, value= "test", props= {"href": "hahah"})
        self.assertEqual(emptytagnode.to_html(), "test")
    
    def test_tohtml_emptyvalue(self):
        emptyvaluenode = LeafNode(tag= "a", value= None, props= {"href": "hahah"})
        with self.assertRaises(ValueError):
            emptyvaluenode.to_html() #equivalent to self.assertRaises(ValueError, emptyvaluenode.to_html)
    
    def test_equal(self):
        node = LeafNode("a", "test", props= None)
        node1 = LeafNode("a", "test", props= None)
        self.assertEqual(node, node1)
    
    def test_notequal(self):
        node = LeafNode("a", "test", props= None)
        node1 = LeafNode("a", "testa", props= None)
        self.assertNotEqual(node, node1)
    

if __name__ == "__main__":
    unittest.main()