__version__ = "1.0.0"
__author__ = "Arin Paul"

from .core.dataframe import DataFrame
from .core.groupby import GroupBy
from .utils.parser import read_csv

__all__ = ["read_csv", "DataFrame", "GroupBy"]
