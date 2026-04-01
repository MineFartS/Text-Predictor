from philh_myftp_biz.array import List
from philh_myftp_biz.file import PKL
from dataclasses import dataclass
from random import choice
from philh_myftp_biz.pc import script_dir

thisd = script_dir()

cache: List[Fragment] = List(PKL(thisd.child('dataset.pkl')))

@dataclass
class Fragment:
    prev: None|str = None
    curr: None|str = None
    next: None|str = None

class _Next:
    
    @property
    def _fragments(self):
        return [f for f in cache if f.next!=None]
    
    def _matches(self, word:str) -> list[Fragment]:
        return [f for f in self._fragments if f.curr==word]

    def random(self, word:str=None) -> None | str:

        if word:
            matches = self._matches(word)
        else:
            matches = self._fragments

        if len(matches) > 0:
            return choice(matches).next

Next = _Next()