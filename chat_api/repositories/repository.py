from abc import ABC
from typing import Tuple, TypeVar, Union

__all__ = ("Repository", "MaybeResult", "MaybeError")

_T = TypeVar("_T")
MaybeError = Union[str, None]
MaybeResult = Tuple[Union[_T, None], MaybeError]


class Repository(ABC):
    pass
