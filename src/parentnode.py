from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children=children, props=props, value=None,)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node cannot be None, it must have a tag (str)")
        if (self.children == None) or (len(self.children) < 1) or type(self.children) != list:
            raise ValueError("ParentNode must have a valid children input (list of ParentNode or LeafNode)")
        children = ""
        for child in self.children:
            if not isinstance(child, (ParentNode, LeafNode)):
                raise ValueError("child node not a valid type (ParentNode or LeafNode)")
            children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
    
if __name__ == "__main__":
    node = ParentNode("p",[
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")])

    print(node.to_html())
