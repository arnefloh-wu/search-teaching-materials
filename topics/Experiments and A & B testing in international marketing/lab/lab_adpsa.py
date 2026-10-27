import sys, numpy as np, pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
df = pd.read_csv(sys.argv[1])
n = df["test_group"].value_counts(); print(n, n/n.sum())
print("SRM vs 96/4 plan p:", stats.chisquare(n[["ad","psa"]].values, f_exp=n.sum()*np.array([.96,.04])).pvalue)
t = df[df["test_group"]=="ad"].converted; c = df[df["test_group"]=="psa"].converted
cnt = np.array([t.sum(), c.sum()]); nn = np.array([len(t), len(c)])
z,p = proportions_ztest(cnt, nn); lo,hi = confint_proportions_2indep(cnt[0],nn[0],cnt[1],nn[1],method="wald"); p1,p0=cnt/nn
print(f"ad {100*p1:.3f}% vs psa {100*p0:.3f}% diff {100*(p1-p0):.3f}pp CI [{100*lo:.3f},{100*hi:.3f}] rel {100*(p1/p0-1):.1f}% z={z:.2f} p={p:.3g}")
df["dose"] = pd.cut(df["total_ads"], [0,10,25,50,100,1e9], labels=["1-10","11-25","26-50","51-100",">100"])
tab = df.groupby(["dose","test_group"], observed=True).converted.agg(["mean","size"]).unstack()
print((tab["mean"]*100).round(2)); print(tab["size"])
