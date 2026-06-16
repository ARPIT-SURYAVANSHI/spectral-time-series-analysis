# X-ray Timing Analysis and QPO Detection Pipeline

A Python-based pipeline for timing analysis of X-ray light curves, power density spectrum (PDS) generation, and quasi-periodic oscillation (QPO) detection using spectral modeling techniques commonly employed in high-energy astrophysics.

---

## Overview

Variability in X-ray emission from compact objects such as neutron stars and black holes provides valuable insight into accretion physics and disk dynamics. This project analyzes X-ray light curves in the frequency domain by constructing Power Density Spectra (PDS), modeling broadband noise components, and identifying narrow quasi-periodic oscillation (QPO) features.

The pipeline performs:

* FITS light curve ingestion
* Data cleaning and preprocessing
* Averaged PDS estimation using FFT
* Fractional RMS normalization
* Logarithmic frequency rebinning
* Power-law noise fitting
* Lorentzian QPO modeling
* Q-factor estimation
* Goodness-of-fit analysis using χ² statistics

---

## Scientific Motivation

Quasi-Periodic Oscillations (QPOs) appear as narrow peaks in the power spectrum of accreting compact objects and are believed to originate from physical processes occurring in the inner accretion flow.

Detecting and characterizing these features allows investigation of:

* Accretion disk variability
* Inner disk dynamics
* Characteristic variability timescales
* Neutron star and black hole environments

---

## Analysis Workflow

```text
FITS Light Curve
        ↓
Data Cleaning
        ↓
Segmentation
        ↓
FFT
        ↓
Power Density Spectrum
        ↓
Segment Averaging
        ↓
Logarithmic Rebinning
        ↓
Model Fitting
        ↓
QPO Detection & Characterization
```

---

## Models Implemented

### Broadband Noise Model

Power-law model:

P(f) = A f^(-α) + C

where:

* A = normalization
* α = power-law index
* C = white-noise level

---

### QPO Model

Lorentzian profile:

L(f) = (Norm × Width / 2π) / [(f − f₀)² + (Width/2)²]

where:

* f₀ = centroid frequency
* Width = FWHM
* Norm = amplitude

---

### Composite Model

Power-law + Lorentzian

Used to identify statistically significant QPO-like features above the broadband noise continuum.

---

## Features

### Light Curve Processing

* FITS file support
* NaN and invalid-value removal
* Uniform segmentation
* Error propagation

### Power Spectrum Analysis

* FFT-based PDS computation
* Fractional RMS normalization
* Segment averaging
* Logarithmic rebinning

### Spectral Modeling

* Power-law fitting
* Lorentzian fitting
* Power-law + Lorentzian fitting
* Multi-component model support

### Statistical Evaluation

* χ²
* Reduced χ²
* Residual analysis
* Parameter uncertainties

### QPO Characterization

* Centroid frequency
* Width (FWHM)
* Quality Factor (Q)
* Variability timescale estimation

---

## Repository Structure

```text
.
├── data/
│   └── test4.lc
│
├── src/
│   ├── load_data.py
│   ├── pds.py
│   ├── models.py
│   ├── fit_models.py
│   ├── plotting.py
│   └── main.py
│
├── notebooks/
│   └── lc_fft_analysis.ipynb
│
├── results/
│   ├── lightcurve.png
│   ├── pds.png
│   ├── powerlaw_fit.png
│   └── qpo_fit.png
│
├── requirements.txt
└── README.md
```

---

## Example Outputs

* Raw light curve visualization
* Averaged power density spectrum
* Log-rebinned PDS
* Broadband noise fit
* QPO candidate detection
* Residual analysis

---

## Dependencies

* NumPy
* SciPy
* Matplotlib
* Astropy

Install:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* Automatic QPO significance testing
* Bayesian parameter estimation (MCMC)
* Multi-Lorentzian decomposition
* Dynamic power spectrum generation
* NICER/XMM-Newton pipeline integration

---

## Author

Developed as part of an undergraduate research project in X-ray timing analysis and variability studies of compact astrophysical systems.
