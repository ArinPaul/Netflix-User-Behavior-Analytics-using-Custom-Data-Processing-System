__version__ = "1.0.0"
__author__ = "Arin Paul"

from .core.dataframe import DataFrame
from .core.parser import read_csv

__all__ = ["read_csv", "DataFrame"]
