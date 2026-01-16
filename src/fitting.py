import numpy as np
from scipy.optimize import curve_fit

def fit_model(model, f, p, err, p0, bounds):
    popt, pcov = curve_fit(model, f, p, sigma=err,
                           p0=p0, bounds=bounds, maxfev=50000)
    perr = np.sqrt(np.diag(pcov))
    chi2 = np.sum(((p - model(f, *popt)) / err)**2)
    red_chi2 = chi2 / (len(f) - len(popt))
    return popt, perr, chi2, red_chi2
