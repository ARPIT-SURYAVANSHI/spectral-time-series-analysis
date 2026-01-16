# X-ray Timing Analysis and QPO Detection using Power Spectral Modeling

This project performs a detailed timing analysis of X-ray light curve data to study variability properties and detect quasi-periodic oscillations (QPOs). The analysis is based on power density spectrum (PDS) estimation, logarithmic rebinning, and statistical model fitting using physically motivated spectral components.

---

## Overview

X-ray variability carries crucial information about accretion processes in compact objects such as black holes and neutron stars. In this project, time-domain light curve data are transformed into the frequency domain to characterize broadband noise and identify narrow spectral features associated with QPOs.

The workflow includes:
- Light curve preprocessing
- Power density spectrum computation using FFT
- Averaging over multiple segments to reduce variance
- Logarithmic rebinning with error propagation
- Model fitting using power-law and Lorentzian components
- Statistical evaluation using χ² and residual analysis

---

## Methodology

### 1. Light Curve Processing
- Input X-ray light curves are read from FITS files.
- Invalid or non-finite data points are removed.
- The data are segmented into equal-length intervals to enable averaged PDS estimation.

### 2. Power Density Spectrum (PDS)
- The PDS is computed using the squared modulus of the Fourier transform.
- Fractional rms normalization is applied.
- PDS from multiple segments are averaged to suppress stochastic noise.
- Logarithmic rebinning is performed to improve signal-to-noise at high frequencies.

### 3. Spectral Modeling
The rebinned PDS is modeled using:
- **Power-law**: to represent broadband noise
- **Lorentzian component(s)**: to model quasi-periodic oscillations (QPOs)

Models implemented:
- Power-law only
- Power-law + single Lorentzian
- Power-law + two Lorentzians (optional)

Model parameters are estimated using non-linear least squares fitting with uncertainty propagation.

### 4. Statistical Evaluation
- χ² and reduced χ² are computed for goodness-of-fit assessment
- Residuals are analyzed to validate model adequacy
- QPO centroid frequency, width, and quality factor (Q) are derived

---

## Results

- The averaged PDS shows a clear broadband noise component.
- A statistically significant narrow feature is detected and modeled as a Lorentzian.
- The inclusion of a Lorentzian component significantly improves the fit compared to a pure power-law model.
- Residual analysis confirms the presence of a QPO-like feature at the fitted centroid frequency.

---

## Repository Structure

## Repository Structure

```text
.
├── data/
│   └── test4.lc                  # Input X-ray light curve (FITS)
├── src/
│   ├── io_utils.py               # FITS I/O and preprocessing
│   ├── pds.py                    # Power Density Spectrum computation & rebinning
│   ├── models.py                 # Power-law and Lorentzian models
│   ├── fitting.py                # Model fitting and χ² statistics
│   ├── plotting.py               # Plotting utilities
│   └── main.py                   # End-to-end analysis pipeline
├── plots/
│   ├── lightcurve_raw.png
│   ├── pds_averaged_logrebinned.png
│   └── pds_fit_powerlaw_lorentzian_qpo.png
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
