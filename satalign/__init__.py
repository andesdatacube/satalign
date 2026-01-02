from __future__ import annotations

from satalign import utils
from satalign.ecc import ECC
from satalign.lgm import LGM
from satalign.pcc import PCC

__all__ = ["ECC", "LGM", "PCC", "utils"]

try:
    from importlib.metadata import version

    __version__ = version("satalign")
except Exception:
    __version__ = "0.0.0-dev"
