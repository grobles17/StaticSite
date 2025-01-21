class HTMLNode():
    def __init__(
            self, 
            tag: str|None = None, 
            value: str|None = None, 
            children: list[str]|None = None,
            props: dict[str, str]|None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return (self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


    def to_html(self):
        raise NotImplementedError("Not implemented to_HTML method")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        return string

node = HTMLNode(tag= "a",
                value= "link",
                children= ["a"], 
                props= {
                        "href": "https://www.google.com",
                        "target": "_blank"
                        })

if __name__ == "__main__":
    print(node)
    print(node.props_to_html())