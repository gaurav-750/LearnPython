# from sales import cal_shipping, cal_tax
# import ecommerce.sales
# from ecommerce.shopping.sales import cal_shipping
# from ecommerce.shopping import sales
# import sys

# print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)
# sales.cal_shipping()
# print(sys.path)

from pathlib import Path
from time import ctime
import shutil

#! Working with files

# path = Path('ecommerce/__init__.py')
# print('path', path)
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.stem)
# print(path.parent)
# print(path.suffix)
# path = path.with_name("file.txt")
# print('path:', path)

# print(path.absolute())


# print('-----------')
# print(Path.cwd())

#! Working with directories:
path = Path('ecommerce')
# print(path.exists())
# path.mkdir()
# path.rmdir()
# path.rename("ecomm")
# print(__file__)
# print(list(path.iterdir()))
for p in path.iterdir():
    # if p.is_dir():
    print(p)

print('-----------')
for py_file in path.rglob("*.py"):
    print(py_file)

print('--------')
path = Path('ecommerce/__init__.py')
print(ctime(path.stat().st_ctime))
print(path.read_text())
# path.write_text("x = 10")

print(Path())

# * Copying from one file to another
target = Path() / "file1.txt"
# target.write_text(path.read_text())

shutil.copy(path, target)
