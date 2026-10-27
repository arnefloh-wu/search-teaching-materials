"""Code shown on the Python slides, run as is. Simulated email test: 3.0 % vs about 3.5 % conversion."""
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import (
    proportions_ztest, confint_proportions_2indep, proportion_effectsize)

# Step 1: data and SRM check
rng = np.random.default_rng(16)
n = 20_000
df = pd.DataFrame({
    "group": np.repeat(["A", "B"], n),
    "country": rng.choice(["AT", "DE", "CH"], 2 * n)})
lift = df.country.map({"AT": .006, "DE": .006, "CH": .001})
p = 0.030 + (df.group == "B") * lift
df["converted"] = rng.binomial(1, p)

counts = df.group.value_counts()
print("SRM p =", round(stats.chisquare(counts).pvalue, 3))
print(df.groupby("group").converted.agg(["sum", "count", "mean"]))

# Step 2: z-test, confidence interval, power
x = df.groupby("group").converted.sum()[["B", "A"]]
m = counts[["B", "A"]]
z, pval = proportions_ztest(x, m)
lo, hi = confint_proportions_2indep(x["B"], m["B"], x["A"], m["A"])
print(f"diff = {100 * (x['B'] / m['B'] - x['A'] / m['A']):.2f} pp, "
      f"z = {z:.2f}, p = {pval:.4f}, CI [{100 * lo:.2f}, {100 * hi:.2f}] pp")
es = proportion_effectsize(0.035, 0.030)
n_arm = NormalIndPower().solve_power(es, alpha=0.05, power=0.8)
print("n per arm for 3.0 -> 3.5 %:", round(n_arm))

# Step 3: effect by country and Bayesian view
df["B"] = (df.group == "B").astype(int)
fit = smf.logit("converted ~ B * C(country)", data=df).fit(disp=0)
print(fit.pvalues.filter(like="B:").round(3))
print((df.groupby(["country", "group"]).converted.mean().unstack() * 100).round(2))
a = rng.beta(1 + x["A"], 1 + m["A"] - x["A"], 100_000)
b = rng.beta(1 + x["B"], 1 + m["B"] - x["B"], 100_000)
print("P(B > A) =", round((b > a).mean(), 3))
