from typing import FrozenSet
from dataclasses import dataclass

from classes.conditional_pattern import ConditionalPattern


@dataclass(frozen=True)
class ConditionalPatternBase:
    """
    A class representing a single conditional pattern base.

    Potentially contains multiple conditional patterns as one item can have multiple prefix paths (conditional patterns) in the FP-tree.
    """

    conditional_patterns: FrozenSet[ConditionalPattern]
