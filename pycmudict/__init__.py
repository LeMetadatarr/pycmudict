"""pycmudict — CMU Pronouncing Dictionary cross-reference bulk harvester, grouped on harvestkit.

Importing this package imports :mod:`pycmudict.harvest`, which in turn
imports the scraper module so it registers itself with
:mod:`harvestkit.engine` (``@register``).
"""
from pycmudict.version import __version__

import pycmudict.harvest  # noqa: F401  (import for @register side effects)

__all__ = ["__version__"]
