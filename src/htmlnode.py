class HTMLNode:
    def __init__ (self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError("to_html method must be implemented by subclasses")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        
        props_html = []
        for key, value in self.props.items():
            props_html.append(f'{key}="{value}"')
        
        return " " + " ".join(props_html)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__ (self, tag: str = None, value: str = None, props: dict = None):
        super().__init__(tag, value=value, children=None, props=props)
        
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if not self.tag:
            return self.value
        elif self.tag and not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__ (self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    
    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        elif not self.children:
            raise ValueError("ParentNode must have children to convert to HTML")
        else:
            children_html = "".join([child.to_html() for child in self.children])
            if not self.props:
                return f"<{self.tag}>{children_html}</{self.tag}>"
            else:
                return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"