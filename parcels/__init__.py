from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass

from parcels.fieldset import *  # noqa
from parcels.particle import *  # noqa
from parcels.particleset import *  # noqa
from parcels.field import *  # noqa
from parcels.kernel import *  # noqa
import parcels.rng as random  # noqa
from parcels.particlefile import *  # noqa
from parcels.kernels import *  # noqa
from parcels.scripts import *  # noqa
from parcels.gridset import *  # noqa
from parcels.grid import *  # noqa
from parcels.tools import *  # noqa
