from typing import Any
from typing import Callable

class PythonFuzz:
    def __init__(self, func: Callable[[bytes], Any]) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
