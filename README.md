# Spotify Analysis Dashboard 2024 (Power BI + Python)

<p align="left">
  <a href="https://powerbi.microsoft.com/">
    <img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=000000" />
  </a>
  <a href="https://www.python.org/">
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffffff" />
  </a>
  <a href="https://developer.spotify.com/documentation/web-api">
    <img alt="Spotify Web API" src="https://img.shields.io/badge/Spotify%20Web%20API-1DB954?style=for-the-badge&logo=spotify&logoColor=ffffff" />
  </a>
  <a href="https://pandas.pydata.org/">
    <img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=ffffff" />
  </a>
  <a href="https://numpy.org/">
    <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=ffffff" />
  </a>
  <a href="https://matplotlib.org/">
    <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" />
  </a>
  <a href="https://seaborn.pydata.org/">
    <img alt="Seaborn" src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge" />
  </a>
  <a href="https://www.figma.com/">
    <img alt="Figma" src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=ffffff" />
  </a>
</p>

## 1. Executive Summary

This repository contains a Spotify streaming analytics dashboard built in Power BI and enhanced with Python for API integration and advanced visuals. The dashboard focuses on 2024 listening/streaming patterns, track and artist performance, and audio-feature driven insights.

Key deliverables include:
1. A Power BI report file (`.pbix`) with interactive visuals and filtering.
2. A Python layer for Spotify Web API enrichment (metadata + album cover retrieval).
3. A Python-based heatmap visual (Matplotlib/Seaborn) for temporal usage patterns.

## 2. Objectives

1. Provide a single, interactive dashboard for analyzing Spotify track performance.
2. Combine BI reporting (Power BI) with programmatic enrichment (Python + Spotify Web API).
3. Enable repeatable analysis through documented data and scripts.

## 3. Dashboard Capabilities

### 3.1 Interactivity
1. Artist-level filtering
2. Track-level filtering
3. Time-based slicing (year/month/day-of-week depending on the model)

### 3.2 Analysis Areas
1. Streaming trend analysis
2. Top track / top artist performance
3. Seasonality and weekly listening behavior
4. Audio feature analysis (e.g., valence, danceability, speechiness, energy)

## 4. Visual Inventory (Implemented)

1. Average Streams per Year vs Top Song Average  
2. Energy Level Gauge / Indicator  
3. Streams by Day of the Week  
4. Track Count by Month  
5. Track Usage Heatmap (Python visual)  
6. Streams by Track  
7. Track Details Panel (audio features such as Valence, Danceability, Speechiness, Energy)

## 5. Repository Structure (Recommended)

Use the structure below to make the project production-quality and easy to review:

1. `Spotify_Dashboard.pbix`  
   - Main Power BI dashboard file.

2. `README.md`  
   - Project documentation (this file).

3. `scripts/`  
   - Python scripts for API calls, preprocessing, and any custom visuals.
   - Example:
     - `scripts/spotify_api_enrichment.py`
     - `scripts/heatmap_visual.py`

4. `data/`  
   - Input/output datasets used by Power BI and scripts.
   - Example:
     - `data/raw/spotify-2023.csv`
     - `data/processed/updated_file.csv`

5. `assets/`  
   - Documentation assets such as screenshots and design exports.
   - Example:
     - `assets/dashboard.png`

6. `requirements.txt` (optional but recommended)
   - Python dependencies for reproducibility.

7. `.env.example` + `.gitignore` (recommended if API keys are used)
   - Prevents accidental exposure of secrets.

## 6. Setup and Usage

### 6.1 Open the Dashboard
1. Install Power BI Desktop.
2. Open `Spotify_Dashboard.pbix`.
3. If Power BI prompts for missing data sources:
   - Go to `Transform data` → `Data source settings`
   - Update file paths to the correct CSV locations in `data/`.

### 6.2 Python (Optional)
If you included scripts for API enrichment or visuals:

1. Install Python 3.10+ (recommended).
2. Create and activate a virtual environment.
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Configure Spotify API credentials (see Section 7).
5. Run scripts in `scripts/` as needed to regenerate outputs used by the PBIX.

## 7. Spotify Web API Configuration (Optional)

If your Python workflow uses Spotify Web API credentials:

1. Create an app in the Spotify Developer Dashboard.
2. Store credentials locally (do not commit secrets).

Recommended approach:
1. Create a `.env` file locally (excluded by `.gitignore`)
2. Commit a `.env.example` file for documentation

Example `.env.example`:
```env
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
```

Security requirement:
1. Do not upload tokens, secrets, or personal credentials to GitHub.
2. Rotate credentials immediately if exposed.

## 8. Reproducibility Notes

1. Ensure the dataset(s) referenced by Power BI are included in `data/`, or document where they can be obtained.
2. Keep script outputs deterministic where possible (fixed schema, consistent column naming).
3. If you refresh data periodically, document:
   - Refresh frequency
   - Data source definition
   - Expected schema

## 10. License and Attribution

1. Spotify name and brand assets belong to Spotify.
2. This repository is for educational/portfolio analytics purposes.


## 11. Contact

Author: JIYA1220
