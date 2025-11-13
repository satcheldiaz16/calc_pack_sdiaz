from pathlib import Path  # built in imports at the top

# section for pip install
from tqdm import tqdm

# section for our package
# from ..calculator import Calculator this is relative path
from calc_pack_sdiaz.calculator import Calculator  # this is absolute path


class FileCalculator(Calculator):
    def sum_file(self, path=None) -> int:
        if path is None:
            path = (
                Path(__file__).parent / "nums.csv"
            )  # critical that when we have a package, all file paths are relative to the package itself, generally pathlib is the way we want to work with paths in Python
        with tqdm(total=100_000_00, desc="summing file") as pbar:
            total = 0
            with path.open() as f:
                for line in f:
                    total += int(line)
                    pbar.update()
            return total
