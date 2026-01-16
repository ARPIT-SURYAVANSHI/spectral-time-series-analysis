import numpy as np

def compute_pds(segment_flux, dt):
    N = len(segment_flux)
    mean_flux = np.mean(segment_flux)
    fft_vals = np.fft.rfft(segment_flux - mean_flux)
    power = np.abs(fft_vals)**2
    df = 1.0 / (N * dt)
    return (2.0 * power) / (N**2 * mean_flux**2 * df)

def log_rebin(freq, power, error, bins_per_decade=100):
    pos = freq > 0
    freq, power, error = freq[pos], power[pos], error[pos]

    log_min, log_max = np.log10(freq[0]), np.log10(freq[-1])
    bins = np.logspace(log_min, log_max,
                       int((log_max - log_min) * bins_per_decade))

    f_rb, p_rb, e_rb = [], [], []
    for i in range(len(bins) - 1):
        mask = (freq >= bins[i]) & (freq < bins[i+1])
        if mask.any():
            f_rb.append(np.sqrt(bins[i] * bins[i+1]))
            p_rb.append(np.mean(power[mask]))
            e_rb.append(np.sqrt(np.sum(error[mask]**2)) / np.sum(mask))

    return np.array(f_rb), np.array(p_rb), np.array(e_rb)
