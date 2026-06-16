import numpy as np

def clean_lightcurve(time, flux, flux_err):

    mask = np.isfinite(time) & np.isfinite(flux)

    time = time[mask]
    flux = flux[mask]
    flux_err = flux_err[mask]

    return time, flux, flux_err


def compute_pds(segment_flux, dt):

    Nseg = len(segment_flux)

    flux_mean = np.mean(segment_flux)

    flux_zero_mean = segment_flux - flux_mean

    fft_vals = np.fft.rfft(flux_zero_mean)

    abs_fft2 = np.abs(fft_vals)**2

    df = 1.0 / (Nseg * dt)

    pds = (2.0 * abs_fft2) / (Nseg**2 * flux_mean**2 * df)

    return pds


def average_pds(time, flux, flux_err, seg_len=1024):

    dt = np.median(np.diff(time))

    N = len(flux)

    M = N // seg_len

    flux = flux[:M*seg_len]

    freqs = np.fft.rfftfreq(seg_len, dt)

    pds_all = []

    for i in range(M):

        seg_flux = flux[i*seg_len:(i+1)*seg_len]

        pds_all.append(compute_pds(seg_flux, dt))

    pds_all = np.array(pds_all)

    pds_avg = np.mean(pds_all, axis=0)

    pds_err = np.std(
        pds_all,
        axis=0,
        ddof=1
    ) / np.sqrt(M)

    return freqs, pds_avg, pds_err, dt, M


def log_rebin_with_error(
    freq,
    power,
    power_err,
    bins_per_decade=100
):

    pos = freq > 0

    freq = freq[pos]
    power = power[pos]
    power_err = power_err[pos]

    log_min = np.log10(freq[0])

    log_max = np.log10(freq[-1])

    n_bins = int((log_max-log_min)*bins_per_decade)

    edges = np.logspace(
        log_min,
        log_max,
        n_bins
    )

    freq_rb = []
    power_rb = []
    err_rb = []

    for i in range(len(edges)-1):

        m = (
            (freq >= edges[i])
            &
            (freq < edges[i+1])
        )

        if np.any(m):

            freq_rb.append(
                np.sqrt(edges[i]*edges[i+1])
            )

            power_rb.append(
                np.mean(power[m])
            )

            err_rb.append(
                np.sqrt(
                    np.sum(power_err[m]**2)
                ) / np.sum(m)
            )

    return (
        np.array(freq_rb),
        np.array(power_rb),
        np.array(err_rb)
    )
