import sys
from pathlib import Path

# Add the root directory to sys.path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from calculate.cal import add, sub, divide, multiply

# To demonstrate in import and export file fuction

print(f"Addition {add(2,3)}")
print(f"subStraction {sub(3,2)}")
print(f"Division {divide(10,5)}")
print(f"Multiplication {12, 2}")

