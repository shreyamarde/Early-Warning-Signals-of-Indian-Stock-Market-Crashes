# Early Warning Signals of Indian Stock Market Crashes (2008–2025)

## Project Overview

This project explores whether major Indian stock market drawdowns are preceded by identifiable warning signals. Using historical financial data from NIFTY 50, India VIX, USD/INR, Gold, and Brent Crude Oil, the study analyzes market behavior before significant stress events, including the 2008 Global Financial Crisis, 2011 Eurozone Crisis, 2016 Global Selloff, and 2020 COVID Crash.

## Objectives

* Identify major market drawdowns in the Indian stock market.
* Analyze the behavior of key financial indicators before each drawdown.
* Determine whether common patterns exist across different crisis events.
* Develop a simple risk-scoring framework to evaluate market stress conditions.

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook / VS Code

## Methodology

1. Data Collection and Integration
2. Data Cleaning and Quality Assessment
3. Exploratory Data Analysis (EDA)
4. Drawdown Detection
5. Event Study Analysis (12-Month, 6-Month, and 3-Month Pre-Crash Windows)
6. Pattern Identification
7. Risk Score Development

## Key Findings

* India VIX showed significant increases before major market crashes, particularly during 2008 and 2020.
* USD/INR depreciation was the most consistent indicator across all analyzed market stress events.
* Gold and Brent Crude Oil did not demonstrate reliable pre-crash behavior across all events.
* A prototype risk score combining market volatility and currency weakness showed potential as an early-warning framework.

## Future Improvements

* Incorporate FII/FPI flows, inflation, and RBI Repo Rate data.
* Apply machine learning models for crash prediction.
* Develop an interactive dashboard for real-time risk monitoring.
