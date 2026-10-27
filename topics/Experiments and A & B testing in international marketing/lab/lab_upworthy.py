import sys, numpy as np, pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
df = pd.read_csv(sys.argv[1], index_col=0)
print(df.shape, df.clickability_test_id.nunique(), df.impressions.sum())
k = df.groupby("clickability_test_id").size()
print(k.value_counts().sort_index().head(10))
two = df[df.clickability_test_id.isin(k[k==2].index)].copy()
two["ctr"] = two.clicks/two.impressions
g = two.groupby("clickability_test_id")
best = g.ctr.max(); worst = g.ctr.min()
ok = worst>0
rel = (best[ok]/worst[ok]-1)*100
print("2-pkg tests:", len(best), "with worst>0:", ok.sum(), "impressions:", two.impressions.sum(), "clicks:", two.clicks.sum())
print("overall CTR % :", 100*two.clicks.sum()/two.impressions.sum())
print("median CTR per variant %:", 100*two.ctr.median())
print("rel diff quantiles %:", rel.quantile([.1,.25,.5,.75,.9]).round(1).to_dict(), "mean", rel.mean().round(1))
absd = (best-worst)*100
print("abs diff pp quantiles:", absd.quantile([.25,.5,.75]).round(3).to_dict())
# z-test each 2-pkg test
ps=[]
for tid, s in g:
    c = s.clicks.values; n = s.impressions.values
    if c.sum()==0: continue
    ps.append(proportions_ztest(c,n)[1])
ps=np.array(ps); print("tests z-tested:", len(ps), "share p<0.05:", (ps<0.05).mean().round(3))
# SRM within 2-pkg tests (50/50 split)
srm = g.impressions.apply(lambda x: stats.chisquare(x.values).pvalue)
print("SRM: share tests p<0.001:", (srm<0.001).mean().round(3), "median imp per test:", g.impressions.sum().median())
# worked example: largest-traffic 2-pkg test
tid = g.impressions.sum().idxmax()
s = two[two.clickability_test_id==tid].sort_values("ctr", ascending=False)
print(s[["created_at","headline","impressions","clicks","ctr"]].to_string())
c = s.clicks.values; n = s.impressions.values
z,p = proportions_ztest(c,n); lo,hi = confint_proportions_2indep(c[0],n[0],c[1],n[1],method="wald")
p1,p0=c/n
print(f"example {tid}: {100*p1:.3f}% vs {100*p0:.3f}% diff {100*(p1-p0):.3f}pp CI [{100*lo:.3f},{100*hi:.3f}] rel {100*(p1/p0-1):.1f}% z={z:.2f} p={p:.3g}")
print("SRM example p:", stats.chisquare(n).pvalue)
# median-traffic example too
med = g.impressions.sum(); tid2 = (med-med.median()).abs().idxmin()
s2 = two[two.clickability_test_id==tid2]; c=s2.clicks.values;n=s2.impressions.values
print("median test", tid2, n, c, proportions_ztest(c,n)[1])
# identical-headline tests (variants differ in image/excerpt only)
same = g.headline.nunique()==1
print("2-pkg tests with identical headline:", same.sum())
# worked example: highest-traffic 2-pkg test with DIFFERENT headlines and same image
diff = g.headline.nunique().eq(2) & g.eyecatcher_id.nunique().eq(1)
cand = g.impressions.sum()[diff].sort_values(ascending=False)
print("headline-only tests:", len(cand))
for tid in cand.index[:6]:
    s = two[two.clickability_test_id==tid].sort_values("ctr", ascending=False)
    c=s.clicks.values;n=s.impressions.values;z,p=proportions_ztest(c,n)
    lo,hi=confint_proportions_2indep(c[0],n[0],c[1],n[1],method="wald");p1,p0=c/n
    print("\n",tid, s.created_at.iloc[0][:10]); 
    for h,ni,ci in zip(s.headline,n,c): print("  ",ni,ci,f"{100*ci/ni:.2f}%",h)
    print(f"  diff {100*(p1-p0):.3f}pp CI [{100*lo:.3f},{100*hi:.3f}] rel {100*(p1/p0-1):.1f}% z={z:.2f} p={p:.3g} SRM p={stats.chisquare(n).pvalue:.3f}")
# near A/A: identical-headline vs different-headline 2-pkg tests
r = (best/worst-1)*100; sig = pd.Series({t: proportions_ztest(s.clicks.values, s.impressions.values)[1] for t,s in g})
for lab,m in [("same headline",same),("different headline",~same)]:
    print(lab, "n tests", m.sum(), "median rel diff %", r[m].median().round(1), "share p<.05", (sig[m]<0.05).mean().round(3))
aa = same & g.eyecatcher_id.nunique().eq(1) & g.excerpt.nunique().eq(1) & g.lede.nunique().eq(1)
print("fully identical (headline, image, excerpt, lede) tests:", aa.sum(), "share p<.05:", (sig[aa]<0.05).mean().round(3) if aa.sum() else None)
