import sys, numpy as np, pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
df = pd.read_csv(sys.argv[1])
print(df.shape)
n = df.segment.value_counts(); print(n)
print("SRM chi2 p (equal thirds):", stats.chisquare(n.values).pvalue)
print(df.groupby("segment")[["visit","conversion","spend"]].mean())
ctrl = df[df.segment=="No E-Mail"]
for arm in ["Mens E-Mail","Womens E-Mail"]:
    t = df[df.segment==arm]
    for y in ["visit","conversion"]:
        c = np.array([t[y].sum(), ctrl[y].sum()]); nn = np.array([len(t), len(ctrl)])
        z,p = proportions_ztest(c, nn)
        lo,hi = confint_proportions_2indep(c[0],nn[0],c[1],nn[1],method="wald")
        p1,p0 = c/nn
        print(f"{arm} {y}: {p1*100:.2f}% vs {p0*100:.2f}%  diff {100*(p1-p0):.2f}pp CI [{100*lo:.2f},{100*hi:.2f}] rel {100*(p1/p0-1):.1f}% z={z:.2f} p={p:.3g}")
    tt = stats.ttest_ind(t.spend, ctrl.spend, equal_var=False)
    print(f"{arm} spend/customer {t.spend.mean():.3f} vs {ctrl.spend.mean():.3f} diff {t.spend.mean()-ctrl.spend.mean():.3f} welch p={tt.pvalue:.3g}")
# segment: visit lift by mens/womens purchase history
for arm in ["Mens E-Mail","Womens E-Mail"]:
    for col in ["mens","womens"]:
        for v in [1,0]:
            a = df[(df.segment==arm)&(df[col]==v)].visit.mean(); b = df[(df.segment=="No E-Mail")&(df[col]==v)].visit.mean()
            print(f"{arm} | {col}={v}: visit {a*100:.2f}% vs {b*100:.2f}% diff {100*(a-b):.2f}pp")
# only-mens vs only-womens buyers
for lab,m in [("only mens",(df.mens==1)&(df.womens==0)),("only womens",(df.mens==0)&(df.womens==1)),("both",(df.mens==1)&(df.womens==1))]:
    for arm in ["Mens E-Mail","Womens E-Mail"]:
        a = df[m&(df.segment==arm)].visit; b = df[m&(df.segment=="No E-Mail")].visit
        print(f"{lab} {arm}: n={len(a)}/{len(b)} {a.mean()*100:.2f}% vs {b.mean()*100:.2f}% diff {100*(a.mean()-b.mean()):.2f}pp")
