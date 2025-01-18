from textnode import *
#Import classes

def main():
    test = TextNode("Hello world", TextType.BOLD, "https://www.heyho.com") 
    #set the second atribute as Enum class.
    print(test)

if __name__ == "__main__":
    main() #avoids func calls from modules
