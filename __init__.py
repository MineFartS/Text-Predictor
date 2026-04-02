from philh_myftp_biz.pc import script_dir
from philh_myftp_biz.array import List
from philh_myftp_biz.file import PKL
from dataclasses import dataclass

#=======================================================

_cachef = script_dir().child('cache.pkl')

cache: List[Word] = List(PKL(_cachef))

#=======================================================

@dataclass
class Word:
    
    rline: list[str]
    index: int
    
    @property
    def word(self) -> str:
        return self.rline[self.index].strip(' ().,?\\/\n-:')
    
    @property
    def line(self) -> list[Word]:
        return cache.filtered(lambda w: w.rline==self.rline).read()

    @property
    def prev(self) -> list[Word]:
        return [w for w in self.line if w.index<self.index]
    
    @property
    def next(self) -> list[Word]:
        return [w for w in self.line if w.index>self.index]

    def __repr__(self) -> str:
        return f'Word({self.word})'

    @property
    def instances(self) -> list[Word]:
        return [f for f in cache if f.word==self.word]

#=======================================================