import sys

from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

if sys.version_info[:2] >= (3, 10):
  from typing import TypeAlias
else:
  from typing_extensions import TypeAlias
from .strategy.core import StrategyList
from .strategy.dict import DictStrategies
from .strategy.list import ListStrategies
from .strategy.set import SetStrategies

ConfigDictType: TypeAlias = Dict[str, Any]

class Merger:
    PROVIDED_TYPE_STRATEGIES: Dict[type, Union[ListStrategies, DictStrategies, SetStrategies]] = ...

    def __init__(
        self,
        type_strategies: List[Tuple[type, str]],
        fallback_strategies: List[str],
        type_conflict_strategies: List[str],
    ) -> None: ...
    def merge(self, base: ConfigDictType, nxt: ConfigDictType) -> ConfigDictType: ...
    def type_conflict_strategy(self, *args: Any) -> Any: ...
    def value_strategy(self, path: str, base: StrategyList, nxt: StrategyList) -> None: ...
