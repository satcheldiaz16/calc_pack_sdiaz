from pathlib import Path

from calc_pack_sdiaz import Calculator
from calc_pack_sdiaz.file_calculator import FileCalculator

print(Calculator().add(1, 2))
FileCalculator().sum_file(Path("~/Desktop/nums.csv").expanduser()) #expanduser fills out abbreviated directory
