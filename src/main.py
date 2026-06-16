from load_data import *
from pds import *
from models import *
from fit_models import *
from plotting import *

time, flux, err = load_lightcurve(
    "pulsar.lc"
)

time, flux, err = clean_lightcurve(
    time,
    flux,
    err
)

freqs, pds_avg, pds_err, dt, M = average_pds(
    time,
    flux,
    err
)

freq_rb, pds_rb, pds_err_rb = log_rebin_with_error(
    freqs[1:],
    pds_avg[1:],
    pds_err[1:]
)

plot_pds(
    freq_rb,
    pds_rb,
    pds_err_rb
)
