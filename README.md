# ATM Fleet Financial Modeling, Forecasting & Cash Logistics Toolkit

A Python library and analytical framework for modeling independent ATM deployment, location performance, inventory replenishment (cash float), fleet scaling dynamics, and risk management.

---

> **Disclaimer & Project Purpose**  
> This repository is strictly an independent, personal educational, simulation, and analytical modeling project created for learning and visualization purposes. It formalizes concepts and financial frameworks discussed in educational business media (specifically the YouTube series *Ned Talks Business*). This project is non-commercial, non-monetized, and holds no official affiliation, endorsement, or partnership with the content creators, media channels, or companies referenced herein.

---

## 📌 Primary Media Source & Context

* **Primary Media Source:** *Ned Talks Business* / *Mr. Finance Extra* — [The Economics of Owning ATM Machines](https://youtu.be/qQDaUGjCZeE?si=cZR6sGcd6eEV9OkQ)
* **Industry:** Independent ATM Operations (IAD), Independent Sales Organizations (ISO), Merchant Services, Retail Cash Logistics & Cash-in-Transit (CIT).
* **Industry Framework:** 
  * **Interchange & Convenience Fee Splits:** Surcharge revenue, ISO routing cuts, payment network switch fees, and merchant commission splits.
  * **Cash Working Capital Cycle:** ACH T+1/T+2 settlement float dynamics vs. Vault Cash opportunity/borrowing costs.
  * **Inventory Replenishment Mechanics:** Economic Order Quantity (EOQ) applied to cash-out risk minimization, route density, and emergency replenishment costs.
  * **Fleet Scaling Tipping Points:** Transition thresholds from solo operations (1–5 units) to software-monitored routes (10–25 units) and enterprise Armored Carrier / Vault Cash financing (50+ units).
  * **Operational Risk Modeling:** Quantitative loss expectancy for bank de-risking account freezes, physical ram-raids, cash-trapping, and jackpotting cyber-attacks.

---

## 📁 Repository File Structure

```text
atm-fleet-toolkit/
├── LICENSE                      # MIT Open Source License
├── README.md                    # Project Documentation & Guide
├── requirements.txt             # Dependency specifications
├── dashboard.py                 # Streamlit Interactive Web Application
├── atm_toolkit/
│   ├── __init__.py             # Package initializer
│   ├── unit_economics.py       # Single-machine ROI, NPV, margin & payback models
│   ├── forecasting.py          # Monte Carlo transaction & location yield simulators
│   ├── replenishment.py        # EOQ cash inventory & route replenishment optimization
│   ├── fleet_scaling.py        # Fleet economics, overhead, and CIT logistics scaling
│   └── risk_analysis.py       # De-risking, crime, and chargeback loss modeling
├── data/
│   └── sample_locations.csv    # Benchmark dataset for location archetypes
├── examples/
│   └── quickstart_demo.py      # Executable end-to-end analytical workflow
└── tests/
    └── test_toolkit.py         # Pytest verification test suite
```

---

## ⚙️ Installation

### Prerequisites
* Python 3.9+
* `pip` or `conda`

### Install Dependencies
```bash
git clone https://github.com/sjamal/atm-fleet-toolkit.git
cd atm-fleet-toolkit
pip install -r requirements.txt
```

---

## 🖥️ Interactive Streamlit Dashboard

To launch the interactive web dashboard for real-time scenario analysis and visualization:

```bash
streamlit run dashboard.py
```

---

## 🚀 Quickstart & Usage Examples

Run the bundled demonstration script to verify your setup and run sample simulations:

```bash
python examples/quickstart_demo.py
```

---

## 🧪 Running Tests

Validate module logic, cash flow math, and risk models using `pytest`:

```bash
pytest tests/ -v
```

---

## ❓ Frequently Asked Questions (FAQs)

### 1. Is an ATM business truly "passive income"?
No. While mature fleets operated via Armored Carriers and real-time monitoring software require low ongoing hourly effort (2–4 hours/month per machine), initial location acquisition, merchant negotiation, cash loading, physical maintenance, and transaction dispute resolution require active operational work.

### 2. How does the cash float cycle work?
When a customer withdraws $100, that cash comes out of the operator's physical safe. The cardholder's bank settles the $100 principal plus surcharge through payment clearing networks back to the operator's bank account via ACH within 24–48 hours (T+1 or T+2). The principal is revenue-neutral; profit is derived solely from the surcharge net of processing fees and merchant splits.

### 3. What is "De-risking" and why is it a top risk?
Under Anti-Money Laundering (AML) regulations, commercial banks incur heavy compliance expenses monitoring large physical cash transactions. As a result, banks frequently terminate bank accounts for independent ATM operators ("de-risking") without warning, temporarily halting settlement deposits and operations until alternative commercial banking partners are established.

### 4. What are the key location performance metrics?
Foot traffic volume and cash necessity determine success. High-performing locations (300+ withdrawals/month) typically include cash-preferred bars, nightclubs, festivals, and unbanked retail hubs. Low-performing locations (<50 withdrawals/month) occur where free bank-owned ATMs are nearby or digital payments dominate.
