\# Interac Enterprise Payment Lakehouse

\## Built on Microsoft Fabric



End-to-end payment analytics and fraud detection platform for Interac — 

Canada's national payment network.



\## Architecture

\- Bronze Layer: Raw ingestion from ADLS Gen2 via OneLake Shortcut

\- Silver Layer: Cleaned, validated, PII-masked Delta tables

\- Gold Layer: Enriched analytical tables for Power BI reporting

\- Real-Time: Eventstream → Eventhouse KQL for live payment monitoring



\## Datasets

\- 194,000 batch records across 7 CSV files

\- 93,000 streaming events across 4 JSON files



\## Tech Stack

\- Microsoft Fabric (Lakehouse, Warehouse, Eventstream, Eventhouse)

\- PySpark (Delta Lake, OPTIMIZE, ZORDER)

\- KQL (Real-time analytics)

\- Power BI (DirectLake semantic model)

\- GitHub Actions (CI/CD)



\## Notebooks

\- notebooks/bronze/ — Bronze ingestion

\- notebooks/silver/ — Silver transformation (7 notebooks)

\- notebooks/gold/ — Gold analytical layer

\- scripts/ — Python event producer

