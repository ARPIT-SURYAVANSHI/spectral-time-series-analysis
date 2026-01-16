from io_utils import load_lightcurve
from pds import compute_pds, log_rebin
from models import *
from fitting import *

# Load data
time, flux, flux_err = load_lightcurve("../data/test4.lc")

# Compute dt, segments, PDS
# Call fitting
# Call plotting
