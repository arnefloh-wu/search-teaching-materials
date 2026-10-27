# A/B-testing labs (Python)

Scripts used in the lecture deck "Experiments Across Markets" (Part 7). All ran on 27 Oct 2026 with Python 3.13, pandas, scipy 1.16 and statsmodels 0.15.

| Script | Data | What it does |
|---|---|---|
| `ab_slides_demo.py` | simulated (seed 16) | The code shown on the slides "Step 1-3": SRM check, z-test, CI, power, logit by country, Bayesian P(B > A) |
| `lab_hillstrom.py` | Hillstrom MineThatData e-mail test (64,000 customers, 3 randomised arms) | Visit, conversion and spend per arm vs. no e-mail, SRM check, segments |
| `lab_upworthy.py` | Upworthy Research Archive, exploratory packages file (CC BY 4.0) | Two-variant headline tests: CTR gaps, share significant, A/A pairs, SRM, worked example |
| `lab_adpsa.py` | Kaggle "Marketing A/B Testing" (ad vs. PSA, 588,101 users) | Ad incrementality vs. a placebo ad |

Run with the data file as argument, e.g. `python lab_hillstrom.py hillstrom_email.csv`.

Data sources (not redistributed here):
- Hillstrom: http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv (blog: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)
- Upworthy Research Archive: https://osf.io/jd64p/ (Matias, Munger, Le Quere & Ebersole 2021, Scientific Data)
- Marketing A/B Testing: https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing (Kaggle login)
