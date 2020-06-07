from hashlib import sha256

def merkleize(sentence: str) -> str:
    merkle_root_str = ""
    blocks = sentence.split(" ")
    blocks_hashed = []
    for block in blocks:    
        blocks_hashed.append((sha256(block.encode('ascii')).hexdigest()))
        
    print(blocks_hashed)
    pass
    
    
from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
  pass # your code here