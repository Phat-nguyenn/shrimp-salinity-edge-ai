# 🦐 Trusted Edge AI for Mekong Delta Salinity Forecasting

> **RMIT Hack-A-Venture 2026 - Round 1 Submission**  
> *Pillar 4: Climate Risk | Pillar 5: Trust Architecture*

## 📖 Executive Overview
Mekong Delta shrimp farmers face escalating salinity-intrusion risks but remain largely excluded from formal insurance and credit. Financial institutions lack trusted pond-level data, face high claim-assessment costs, and struggle with moral hazard. 

This repository contains the **Edge AI & Data Trust** module of our "Resilience-linked Finance" solution. It provides a localized, offline-capable TinyML forecasting model, combined with hardware-level cryptographic signatures to ensure data integrity for automated financial triggers.

## 🎯 The Root Causes We Solve
Our module addresses two critical root causes of the financial inclusion gap:
1. **Lack of Trusted Pond-Level Data:** Macro-level weather/satellite indices miss micro-level salinity variations (basis risk).
2. **Moral Hazard & Fraud:** Insurers cannot verify if farmers actually took preventive actions (e.g., closing sluice gates) to claim early payouts.

## 🏗️ Architecture & Core Technologies
This module is built on three technical pillars:
*   **Localized Edge Forecasting (TinyML):** A quantized time-series model (INT8) deployed on MCU-based nodes (e.g., ESP32-S3). By incorporating tidal data features, it achieves high "Hit Rate" for salinity intrusion while minimizing false alarms.
*   **Hardware-Level Data Integrity:** Each edge node is equipped with a Secure Element (e.g., ATECC608A). Every sensor reading and actuator log is hashed and digitally signed by the hardware's private key before transmission, creating an immutable **Audit Trail**.
*   **Trusted Data Pipeline:** Open API integration (Thông tư 64 compliance) to send verified triggers to insurers and banks, enabling automated payouts via VietQR.

## 📊 Baseline Benchmark (Feasibility Evidence)
We trained a baseline XGBoost model using historical salinity data from the **An Hiệp station** (Hàm Luông river system, Bến Tre). Using only lagged salinity and seasonal features, the baseline achieved an **RMSE of 0.2372 ppt**. 

*(Note: Actual on-device TinyML metrics will be updated during the MVP phase.)*

| Metric | Baseline (Cloud XGBoost) | Proposed (TinyML on ESP32-S3) | Notes |
| :--- | :--- | :--- | :--- |
| **Model Size** | ~ 5 - 20 MB | **< 500 KB** | Via pruning & distillation |
| **RAM Usage** | N/A (Server) | **< 250 KB** | Fits MCU SRAM |
| **Inference Latency** | 100 - 500 ms | **< 50 ms** | Offline execution |
| **RMSE (Salinity)** | **0.2372 ppt** | *[To be updated]* | Estimated slight increase due to INT8 quantization |
| **Hit Rate (Forecast)** | *[To be updated]* | *[To be updated]* | Target: > 85% |

## 📂 Repository Structure
```text
├── data/                   # Open-source datasets (Salinity & Stations CSV)
├── src/                    # Source code
│   └── baseline_model.py   # Training script for the XGBoost baseline
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
