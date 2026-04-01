from philh_myftp_biz.array import List
from philh_myftp_biz.file import PKL
from philh_myftp_biz.pc import Path
from dataclasses import dataclass

@dataclass
class Fragment:
    prev: None|str = None
    curr: None|str = None
    next: None|str = None

cache: List[Fragment] = List(PKL(Path('dataset.pkl')))
