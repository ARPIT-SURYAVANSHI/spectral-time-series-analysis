import numpy as np
from astropy.io import fits

def load_lightcurve(filename):
    with fits.open(filename) as hdul:
        data = hdul[1].data
        time = data['TIME']
        flux = data['RATE']
        if 'ERROR' in data.columns.names:
            flux_err = data['ERROR']
        else:
            flux_err = np.sqrt(np.abs(flux))

    mask = np.isfinite(time) & np.isfinite(flux)
    return time[mask], flux[mask], flux_err[mask]
