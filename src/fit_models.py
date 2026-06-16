import numpy as np
from scipy.optimize import curve_fit

from models import *

def fit_powerlaw(
    f_fit,
    p_fit,
    err_fit,
    p0
):

    popt, pcov = curve_fit(
        powerlaw,
        f_fit,
        p_fit,
        sigma=err_fit,
        p0=p0,
        maxfev=10000
    )

    return popt, pcov


def fit_qpo(
    f_fit,
    p_fit,
    err_fit,
    p0
):

    popt, pcov = curve_fit(
        powerlaw_plus_lorentzian,
        f_fit,
        p_fit,
        sigma=err_fit,
        p0=p0,
        maxfev=20000
    )

    return popt, pcov
