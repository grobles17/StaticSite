from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self): #method names typically use lowercase with underscores NOT to_Html
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    
node = LeafNode(tag= "a", value= "link", props= {"href": "https://www.google.com"})

if __name__ == "__main__":
    print(node.to_html())
    print(node.props)