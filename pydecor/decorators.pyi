"""
Type hints for the decorators module
"""

from types import FunctionType, MethodType
from typing import Any, Callable, Dict, Optional, Tuple, Union


DecoratorType = Union[FunctionType, MethodType, type]
BeforeFuncReturn = Optional[Tuple[Tuple, Dict]]


def before(
        func: Callable[..., BeforeFuncReturn],
        unpack: bool = True,
        key: str = 'decorator_kwargs',
        **decorator_kwargs) -> DecoratorType: ...