from dataclasses import dataclass

@dataclass
class Fragment:

    prev: None|str = None
    curr: None|str = None
    next: None|str = None
    