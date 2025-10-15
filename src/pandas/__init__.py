__version__ = "1.0.0"
__author__ = "Arin Paul"

__all__ = ["parser", "projection", "filter"]

def read_csv(file_path, delimiter=','):
    from .parser import custom_read_csv as parser_read_csv
    return parser_read_csv(file_path, delimiter)