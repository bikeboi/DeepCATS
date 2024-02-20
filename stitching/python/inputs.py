"""Get user inputs from the terminal"""

from typing import TypedDict
from pathlib import Path
from prompt_toolkit import print_formatted_text, HTML, PromptSession
from prompt_toolkit.validation import Validator
from prompt_toolkit.completion import PathCompleter


class UserParams(TypedDict):
    tc_path: Path
    output_path: Path
    channel: int
    start_sec: int
    end_sec: int
    x_overlap: float
    y_overlap: float
    downsize: bool
    downsize_factor: float
    avg_corr: bool


class MosaicFileParams(TypedDict):
    n_sections: int
    scan_id: str
    n_rows: int
    n_cols: int
    n_layers: int


# Wrapper for validation functions that's useful
class Validation:
    def __init__(self) -> None:
        self.funcs = []

    def construct_func(self):
        fn_0 = lambda x: True

# Input Validators
def make_validator(f, **kwargs):
    return Validator.from_callable(f, move_cursor_to_end=True, **kwargs)

def make_type_validatotr(typ, **kwargs):
    def f(x):
        try:
            x_ = typ(x)
            return isinstance(x_, typ)
        except ValueError:
            return False
    return make_validator(f, **kwargs)
    


PATH_EXISTS = make_validator(
    lambda s: Path(s).exists(follow_symlinks=True) and Path(s).is_dir(),
    error_message='Directory does not exist',
)
IS_INT = make_type_validator(
    int,
    error_message='Please enter an integer'
)
IS_FLOAT = make_validator(
    float,
    error_message='Please enter a number'
)
IS_PERCENTAGE = make_validator(
    lambda x: isinstance(x, float) and (0 <= x <= 1),
    error_message='Must be a number between 0% and 100%'
)

def get_user_input():
    print_formatted_text(
        HTML('<b>Enter Parameters\n</b>'),
        "---"
    )
    
    s = PromptSession(message='>', validate_while_typing=False)
    tc_path = Path(s.prompt('TC Data Directory:',
                            validator=PATH_EXISTS,
                            completer=PathCompleter(only_directories=True)))
    start_sec = s.prompt('Start Section:', validator=IS_INT)
    end_sec = s.prompt('End Section:', validator=IS_INT)
    x_overlap = s.prompt('X Overlap %:', validator=IS_PERCENTAGE)


get_user_input()