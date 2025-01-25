from textnode import TextType, TextNode
import re #regular expression modules 

def find_substring(text: str, substring: str)-> list[int]:
    """Scans a text to return a list of ints with the indexes where a given substring is found.
    If either text or substring are empty, it returns an empty list"""
    indexes:list[int] = []
    if len(text) == 0 or len(substring) == 0:
        return indexes
    idx = text.find(substring)
    while idx != -1:
        indexes.append(idx)
        idx = text.find(substring, idx+len(substring)) 
    return indexes   

def split_nodes_delimiter(nodes: list[TextNode], delimiter: str, text_type: TextType)-> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in nodes:
        indexes: list[int] = find_substring(node.text, delimiter)
        if len(indexes) == 0:
            new_nodes.append(node)
            continue
        if len(indexes) % 2 != 0:
            raise Exception("Opened delimiter in text not closed")
        splits: list[str] = []
        if indexes[0] != 0: #If text does not start with markdown delimiter
            splits.append((node.text[0:indexes[0]], False)) #False to show its just text
        while len(indexes) > 2:
            splits.append((node.text[indexes[0]+len(delimiter):indexes[1]], True)) #From index open + 1 to index close (not included), True to signal type
            splits.append((node.text[indexes[1]+len(delimiter):indexes[2]], False))
            indexes = indexes[2:]
        splits.append((node.text[indexes[0]+len(delimiter):indexes[1]], True))
        if len(node.text[indexes[1]+len(delimiter):]) != 0:
            splits.append((node.text[indexes[1]+len(delimiter):], False))
        for text, type in splits:
            if type:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes
            
def extract_markdown_images(text):
    texts = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) #each () w/o the escape \, is a match group
    return texts

def extract_markdown_links(text):
    texts = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) #(?>!xxx) xxx CANNOT precede the match
    return texts

if __name__ == "__main__":  
    node = TextNode("**bold** and *italic*", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
    print(new_nodes)
        
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    #text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))