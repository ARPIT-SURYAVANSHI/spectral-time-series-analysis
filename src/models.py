import numpy as np

def powerlaw(f, A, alpha, C):

    return A*f**(-alpha) + C


def lorentzian(f, norm, f0, width):

    return (
        norm *
        (width/(2*np.pi))
        /
        (
            (f-f0)**2
            +
            (width/2)**2
        )
    )


def powerlaw_plus_lorentzian(
    f,
    A,
    alpha,
    C,
    norm,
    f0,
    width
):

    return (
        powerlaw(f,A,alpha,C)
        +
        lorentzian(f,norm,f0,width)
    )
