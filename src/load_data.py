import numpy as np
from astropy.io import fits

def load_lightcurve(filename):

    with fits.open(filename) as hdul:
        data = hdul[1].data

        time = data["TIME"]
        flux = data["RATE1"]

        if "ERROR1" in data.columns.names:
            flux_err = data["ERROR1"]
        else:
            flux_err = np.sqrt(np.abs(flux))

    return time, flux, flux_err
