## Quellen zu Open-Source MMM (PyMC-Marketing, Google Meridian, Meta Robyn) in International Marketing (Agentensuche, 26. Oktober 2026)
Resource guide for teaching open-source marketing mix modelling with PyMC-Marketing (1.3.0, Oct 2026), Google Meridian (2.1.0, Sep 2026; successor of LightweightMMM, archived Jan 2026) and Meta Robyn (CRAN 3.12.1, Jul 2025; robynpy 0.3.6 beta) in an international, multi-market setting. Six parallel research agents (26 Oct 2026) covered literature, websites/blogs/tutorials, cases/examples, software/data, people/communities, and a 49-dimension tool comparison with 26 method entries. 262 rows; links checked by script. Caveats: Robyn has no pooled multi-market model (one model per geo); none of the three tools converts currencies; Meridian 2.0 and PyMC-Marketing 1.0 introduced breaking API changes, so tutorials older than Aug/Sep 2026 may not run. The Google Sheet version also holds the tool comparison matrix.
### Bücher (8)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Bücher</td>
<td>Statistical Rethinking: A Bayesian Course with Examples in R and Stan (2nd ed.)</td>
<td>Richard McElreath, CRC Press / Chapman & Hall, 2020, textbook</td>
<td>[https://xcelab.net/rm/](https://xcelab.net/rm/)</td>
<td>Chapters 13-14 (multilevel models, partial pooling, varying slopes) are the most intuitive introduction to why a geo- or country-hierarchical MMM shrinks small markets toward the global mean. Free lecture videos and PyMC ports of all examples exist, so it fits a Python lab.</td>
<td>background reading for the hierarchical session; book paid (\~EUR 70), lectures and code free</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Bayesian Data Analysis (3rd ed.)</td>
<td>Andrew Gelman, John Carlin, Hal Stern, David Dunson, Aki Vehtari, Donald Rubin; CRC Press, 2013</td>
<td>[http://www.stat.columbia.edu/\~gelman/book/](http://www.stat.columbia.edu/~gelman/book/)</td>
<td>The reference text. Chapter 5 (hierarchical models, the eight-schools example) maps directly onto 'eight countries with noisy ROAS'. The authors have made the PDF freely available for non-commercial use. For instructors and advanced students.</td>
<td>instructor reference / advanced reading; free PDF</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Regression and Other Stories</td>
<td>Andrew Gelman, Jennifer Hill, Aki Vehtari; Cambridge University Press, 2020</td>
<td>[https://avehtari.github.io/ROS-Examples/](https://avehtari.github.io/ROS-Examples/)</td>
<td>Applied regression with a Bayesian slant: priors, simulation, causal inference chapters. A gentle path for marketing master students before PyMC-Marketing. A free PDF and all code are on the companion site.</td>
<td>background reading; free PDF</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Bayesian Statistics and Marketing</td>
<td>Peter E. Rossi, Greg M. Allenby, Robert McCulloch; Wiley, 2005</td>
<td>[https://doi.org/10.1002/0470863692](https://doi.org/10.1002/0470863692)</td>
<td>The marketing-specific source for hierarchical Bayes models (unit-level heterogeneity, hierarchical linear models) behind cross-market pooling. Notation is dense and the code is in R (bayesm). Use selected chapters only.</td>
<td>instructor reference; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>R for Marketing Research and Analytics (2nd ed.)</td>
<td>Chris Chapman & Elea McDonnell Feit; Springer (Use R!), 2019</td>
<td>[https://doi.org/10.1007/978-3-030-14316-9](https://doi.org/10.1007/978-3-030-14316-9)</td>
<td>Robyn is an R package. This book gets students fluent in R data handling, and its hierarchical-Bayes chapter covers multilevel models. Complements the Python companion that is already on the list. Springer eBook, likely in the WU package.</td>
<td>lab support for the Robyn track; WU-Lizenz prüfen (SpringerLink)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing</td>
<td>Ron Kohavi, Diane Tang, Ya Xu; Cambridge University Press, 2020</td>
<td>[https://doi.org/10.1017/9781108653985](https://doi.org/10.1017/9781108653985)</td>
<td>Experiments are the calibration input for all three tools. Chapters on validity threats, sample-ratio mismatch and long-term effects help students judge the lift tests fed into Robyn, Meridian or PyMC-Marketing. Practitioner-oriented.</td>
<td>background (calibration session); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>Global Brand Strategy: World-wise Marketing in the Age of Branding</td>
<td>Jan-Benedict E.M. Steenkamp; Palgrave Macmillan, 2017</td>
<td>[https://doi.org/10.1057/978-1-349-94994-6](https://doi.org/10.1057/978-1-349-94994-6)</td>
<td>Connects global vs local brand management, standardisation vs adaptation, and emerging vs developed markets to market-response evidence. Gives the international-marketing framing for why a global MMM must allow country-specific effects.</td>
<td>background reading (international framing); WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Controlling des Marketing Mix mit Marketing Mix Modeling (chapter in: Marketingcontrolling kompakt)</td>
<td>Sven Reinecke & Alexander Tombach; Springer Fachmedien Wiesbaden, 2025, book chapter (German)</td>
<td>[https://doi.org/10.1007/978-3-658-47820-9_13](https://doi.org/10.1007/978-3-658-47820-9_13)</td>
<td>German-language introduction to MMM for marketing controlling, by St. Gallen authors. Reports from a 2024 executive survey that about 25% of companies in the DACH region use MMM regularly. The best German entry text for students and for linking MMM to the controlling or finance function.</td>
<td>reading (German); WU-Lizenz prüfen (SpringerLink)</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Journal Articles (26)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Open-Source Media and Marketing Mix Modeling: Practice-Oriented Overview, Challenges, Opportunities</td>
<td>Julian Runge & Koen Pauwels, Customer Needs and Solutions, 2026, review article (also MSI Working Paper 26-106, March 2026)</td>
<td>[https://doi.org/10.1007/s40547-026-00161-4](https://doi.org/10.1007/s40547-026-00161-4)</td>
<td>The best single overview of the course topic: a narrative review comparing Meta Robyn, Google Meridian/LightweightMMM and the PyMC-Labs ecosystem (PyMC-Marketing). Frames the 2020s MMM revival as a response to privacy-enhancing technologies (ATT, cookie loss) and warns that automation can hide misspecification, too little variation in spend, and endogeneity. It recommends calibrating with experiments. Gives no explicit multi-country treatment, so pair it with the geo-hierarchical papers.</td>
<td>reading (session 1 anchor); journal version paid / WU-Lizenz prüfen, MSI working-paper PDF free (see reports row)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Media Mix Model Calibration With Bayesian Priors</td>
<td>Yingxiang Zhang, Mike Wurm, Eddie Li, Alexander Wakim, Joseph Kelly, Brenda Price, Ying Liu; Google, 2024, technical paper</td>
<td>[https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/](https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/)</td>
<td>The methodological core of Meridian's ROI priors. It reparameterises the MMM so that ROAS is a model parameter, which lets lift or geo-experiment results enter the model directly as a prior. Simulations show this reduces bias and uncertainty. Useful for teaching how a country team's local lift test becomes that market's prior. Short and readable for master students who know basic Bayes.</td>
<td>reading / lab (set ROI priors in Meridian); free PDF</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Bias Correction for Paid Search in Media Mix Modeling</td>
<td>Aiyou Chen, David Chan, Mike Perry, Yuxue Jin, Yunting Sun, Yueqing Wang, Jim Koehler; Google, 2018, technical paper (arXiv 1807.03292)</td>
<td>[https://research.google/pubs/pub46861/](https://research.google/pubs/pub46861/)</td>
<td>Uses causal diagrams (back-door criterion) to explain why paid-search ROAS is biased upward in MMM: search ads are targeted at existing demand. Proposes controlling for search query volume. This is the origin of Meridian's Google Query Volume control. The search-demand argument also matters across countries, because Google's search share differs strongly between markets (it is low in China, Korea and Russia).</td>
<td>reading (causal MMM session); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Primer on Out-of-the-Box AI Marketing Mix Models</td>
<td>Macarena Estévez, María Teresa Ballestar, Jorge Sáinz; IEEE Transactions on Engineering Management 72, 282-294, 2025</td>
<td>[https://doi.org/10.1109/TEM.2024.3519172](https://doi.org/10.1109/TEM.2024.3519172)</td>
<td>Fits a traditional econometric MMM and Meta Robyn to the same telecom dataset from a European (Spanish) firm, then compares them on technical, business and practical criteria. A clear case for a 'traditional vs automated' debate. Main caveat: Robyn's random initialisation and Pareto front of candidate models make results harder to replicate and explain.</td>
<td>reading / class discussion; paid, WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Marketing Mix Modeling in Lemonade</td>
<td>Roy Ravid, arXiv 2501.01276, 2025, industry case paper</td>
<td>[https://arxiv.org/abs/2501.01276](https://arxiv.org/abs/2501.01276)</td>
<td>A short end-to-end account of how a digital insurer built an in-house Bayesian MMM: seasonality, trend and macro controls, validation against A/B tests and sliding-window holdouts, then budget reallocation by convex optimisation. Good as a template for student project reports. It covers one company and does not name the software used.</td>
<td>reading / project template; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Structural Estimation of Marketing Mix Model Parameters from Geo-Experiments</td>
<td>Niklas Heusch, arXiv 2608.21128, 2026, methods preprint</td>
<td>[https://arxiv.org/abs/2608.21128](https://arxiv.org/abs/2608.21128)</td>
<td>Recovers adstock decay, saturation and effectiveness parameters directly from treated-vs-control geo-experiment time series, then pools several experiments to calibrate an MMM. This connects to the multi-market question of how geo tests run in a few countries can inform a global model. Demonstrated only on synthetic data; a very recent preprint, not peer reviewed.</td>
<td>background / advanced reading; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Synthetic Benchmark Dataset with Endogenous Marketing Spend for Validating Marketing Mix Models</td>
<td>Niklas Heusch, arXiv 2608.21130, 2026, data/methods preprint</td>
<td>[https://arxiv.org/abs/2608.21130](https://arxiv.org/abs/2608.21130)</td>
<td>Provides simulated data with known ground truth in which budgets respond to demand, the realistic case that standard simulators leave out. Lets students check whether Robyn, Meridian or PyMC-Marketing recover the true ROAS when spend is endogenous. Preprint; check that the data repository is available before you assign it.</td>
<td>lab (tool comparison against ground truth); open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>PyMC: A Modern and Comprehensive Probabilistic Programming Framework in Python</td>
<td>Oriol Abril-Pla, Virgile Andreani, Colin Carroll, Larry Dong, Christopher Fonnesbeck et al.; PeerJ Computer Science 9:e1516, 2023</td>
<td>[https://doi.org/10.7717/peerj-cs.1516](https://doi.org/10.7717/peerj-cs.1516)</td>
<td>The citable reference for the inference engine underneath PyMC-Marketing: NUTS sampling, model graphs, the ArviZ diagnostics workflow. Read it for the background behind convergence checks (r-hat, divergences) that students meet in PyMC-Marketing labs. Software paper, not marketing.</td>
<td>background for lab; open access</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Bayesian Workflow</td>
<td>Andrew Gelman, Aki Vehtari, Daniel Simpson et al., arXiv 2011.01808, 2020</td>
<td>[https://arxiv.org/abs/2011.01808](https://arxiv.org/abs/2011.01808)</td>
<td>The standard reference for the prior-predictive, fit, posterior-predictive and model-comparison loop that PyMC-Marketing's documentation follows. Gives students a vocabulary for judging any Bayesian MMM, including country-level ones. Long (77 pp.); assign sections 2-6.</td>
<td>reading (selected sections) / lab guide; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>TensorFlow Distributions</td>
<td>Joshua V. Dillon, Ian Langmore, Dustin Tran, Eugene Brevdo et al., arXiv 1711.10604, 2017</td>
<td>[https://arxiv.org/abs/1711.10604](https://arxiv.org/abs/1711.10604)</td>
<td>Meridian runs on TensorFlow Probability; its predecessor LightweightMMM used NumPyro/JAX. Optional background for students who want to know why Meridian needs a GPU or long MCMC runs for many geos. Technical; instructor reference only.</td>
<td>background (instructor); open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Forecasting at Scale (Prophet)</td>
<td>Sean J. Taylor & Benjamin Letham; The American Statistician 72(1), 37-45, 2018</td>
<td>[https://doi.org/10.1080/00031305.2017.1380080](https://doi.org/10.1080/00031305.2017.1380080)</td>
<td>Robyn uses Prophet to break the baseline into trend, seasonality and holidays, using country-specific holiday calendars, which matters in multi-country work. The paper explains the additive model behind that step, so students can see what Robyn's 'prophet_country' argument actually does.</td>
<td>background for Robyn lab; open access</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Ridge Regression: Biased Estimation for Nonorthogonal Problems</td>
<td>Arthur E. Hoerl & Robert W. Kennard; Technometrics 12(1), 55-67, 1970</td>
<td>[https://doi.org/10.1080/00401706.1970.10488634](https://doi.org/10.1080/00401706.1970.10488634)</td>
<td>The original ridge paper. Robyn is a ridge regression with Nevergrad hyperparameter search, used against collinear media spends. Contrasting ridge shrinkage with Bayesian priors (Meridian, PyMC-Marketing) is a good exam question. Classic, short.</td>
<td>background; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness</td>
<td>Garrett A. Johnson, Randall A. Lewis, Elmar I. Nubbemeyer; Journal of Marketing Research 54(6), 867-884, 2017</td>
<td>[https://doi.org/10.1509/jmr.15.0297](https://doi.org/10.1509/jmr.15.0297)</td>
<td>Explains how platform lift studies (the 'conversion lift' inputs to Robyn and Meridian calibration) create valid control groups. Helps students judge what a Meta or Google lift result does and does not measure before using it as an MMM prior.</td>
<td>reading (calibration session); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Cross-National Differences in Market Response: Line-Length, Price, and Distribution Elasticities in 14 Indo-Pacific Rim Economies</td>
<td>Hannes Datta, Harald J. van Heerde, Marnik G. Dekimpe, Jan-Benedict E.M. Steenkamp; Journal of Marketing Research 59(2), 251-270, 2022</td>
<td>[https://doi.org/10.1177/00222437211058102](https://doi.org/10.1177/00222437211058102)</td>
<td>Covers more than 1,600 brands in 14 categories across 7 developed and 7 emerging economies, using GfK data from 2004-2014. Average elasticities: price -0.42, distribution 0.37, line length 0.46. It finds no systematic emerging-vs-developed gap; power distance and income inequality explain most cross-country differences. Directly useful for choosing country-level priors and for arguing for partial pooling across markets. A replication package is on SAGE figshare, but the raw data are not included.</td>
<td>core reading (international session); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>An Investigation into the Evolution of Marketing-Mix Effectiveness: An Empirics-First Approach</td>
<td>Katrijn Gielens & Jan-Benedict E.M. Steenkamp; Journal of Marketing, 2025</td>
<td>[https://doi.org/10.1177/00222429251412261](https://doi.org/10.1177/00222429251412261)</td>
<td>Household-panel evidence on more than 16,000 brands in 85 CPG categories across 34 countries. Gives time-varying price (-0.64), assortment (0.31) and distribution (0.21) elasticities, and finds 98.5% of brands show significant drift. Arguments for time-varying coefficients and for refreshing country MMMs. Local vs global brand status matters for those trajectories.</td>
<td>reading / benchmark priors; open access per OpenAlex</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>In Brands We Trust? A Multicategory, Multicountry Investigation of Sensitivity of Consumers' Trust in Brands to Marketing-Mix Activities</td>
<td>Koushyar Rajavi, Tarun Kushwaha, Jan-Benedict E.M. Steenkamp; Journal of Consumer Research 46(4), 2019</td>
<td>[https://doi.org/10.1093/jcr/ucz026](https://doi.org/10.1093/jcr/ucz026)</td>
<td>Combines a 15,073-respondent survey with scanner data on 589 brands in 13 countries. Advertising raises brand trust, and that effect is moderated by national cultural values. Useful for discussing long-term brand effects that a weekly sales MMM misses and that differ by country.</td>
<td>background reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Understanding the Coevolution of Ad Spend by Media Channel and Retail Format Sales at the Country Level: A Multicountry Examination</td>
<td>Hannah S. Lee, Göksel Yalcinkaya, David A. Griffith; Journal of International Marketing, 2023 (online 2022)</td>
<td>[https://doi.org/10.1177/1069031X221143780](https://doi.org/10.1177/1069031X221143780)</td>
<td>A 29-country panel showing large cross-country differences in which media channels matter and how they move with retail formats. Supports the 'glocal' argument that one global media mix cannot be assumed. Use it to motivate country-specific channel sets in a geo-hierarchical MMM.</td>
<td>reading (international session); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>New Empirical Generalizations on the Determinants of Price Elasticity</td>
<td>Tammo H.A. Bijmolt, Harald J. van Heerde, Rik G.M. Pieters; Journal of Marketing Research 42(2), 141-156, 2005</td>
<td>[https://doi.org/10.1509/jmkr.42.2.141.62296](https://doi.org/10.1509/jmkr.42.2.141.62296)</td>
<td>Meta-analysis of 1,851 price elasticities (mean about -2.6), with moderators including Europe vs the US. A source of informative priors for price and promotion terms in an MMM, and a reminder that price-level and currency effects differ by market.</td>
<td>background (priors); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Manufacturer and Retailer Strategies to Impact Store Brand Share: Global Integration, Local Adaptation, and Worldwide Learning</td>
<td>Jan-Benedict E.M. Steenkamp & Inge Geyskens; Marketing Science 33(1), 2014 (online 2013)</td>
<td>[https://doi.org/10.1287/mksc.2013.0801](https://doi.org/10.1287/mksc.2013.0801)</td>
<td>Multi-country study framed around global integration, local adaptation and worldwide learning. A good conceptual mapping to complete pooling, no pooling and partial pooling in hierarchical MMM. Helps international-marketing students see why Bayesian shrinkage across countries is a strategic as well as a statistical choice.</td>
<td>background / conceptual bridge; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Privacy Regulation and Online Advertising</td>
<td>Avi Goldfarb & Catherine E. Tucker; Management Science 57(1), 57-71, 2011</td>
<td>[https://doi.org/10.1287/mnsc.1100.1246](https://doi.org/10.1287/mnsc.1100.1246)</td>
<td>A classic cross-country design: after the EU ePrivacy rules, display ads became about 65% less effective at changing purchase intent compared with non-EU countries. An early example of regulation creating country differences in measurability and ad effectiveness.</td>
<td>reading (privacy session); open access version available</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Regulating Privacy Online: An Economic Evaluation of the GDPR</td>
<td>Samuel G. Goldberg, Garrett A. Johnson, Scott K. Shriver; American Economic Journal: Economic Policy 16(1), 2024</td>
<td>[https://doi.org/10.1257/pol.20210309](https://doi.org/10.1257/pol.20210309)</td>
<td>Adobe Analytics data for 1,084 firms show about 12% lower recorded EU pageviews and revenue after the GDPR. The authors split this into lost data recording versus real effects. That split is the key point for MMM teaching: user-level attribution loses observability in the EU, while aggregate MMM inputs do not.</td>
<td>reading (privacy session); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Privacy and Market Concentration: Intended and Unintended Consequences of the GDPR</td>
<td>Garrett A. Johnson, Scott K. Shriver, Samuel G. Goldberg; Management Science 69(10), 2023</td>
<td>[https://doi.org/10.1287/mnsc.2023.4709](https://doi.org/10.1287/mnsc.2023.4709)</td>
<td>Covers 27,000+ websites: EU vendor use fell 15% and vendor concentration rose 17%, in favour of Google and Facebook. Context for why platform-supplied open-source MMMs (Meridian, Robyn) reached the market and for the neutrality question they raise.</td>
<td>background; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Impact of the General Data Protection Regulation (GDPR) on Online Tracking</td>
<td>Klaus M. Miller, Karlo Lukic, Bernd Skiera; International Journal of Research in Marketing, 2025</td>
<td>[https://doi.org/10.1016/j.ijresmar.2025.03.002](https://doi.org/10.1016/j.ijresmar.2025.03.002)</td>
<td>European authors. A difference-in-differences study of 294 publishers finds about 4 fewer trackers per site (-14.8%) because of the GDPR, but only limited effects on advertising trackers. A nuanced counterpoint to the 'GDPR killed attribution' story.</td>
<td>reading; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Evaluating the Impact of Privacy Regulation on E-Commerce Firms: Evidence from Apple's App Tracking Transparency</td>
<td>Guy Aridor, Yeon-Koo Che, Brett Hollenbeck, Maximilian Kaiser, Daniel McCarthy; Management Science, 2025</td>
<td>[https://doi.org/10.1287/mnsc.2024.06600](https://doi.org/10.1287/mnsc.2024.06600)</td>
<td>Covers more than 4,200 e-commerce advertisers: click-through rates on Meta conversion ads fell 37% after ATT; spend shifted to Google; revenue of Meta-dependent firms fell 8-40%, mostly at small firms. The clearest causal evidence for the signal loss behind Meta's investment in Robyn. Co-author Kaiser is at Universität Hamburg, and the findings fed into German and French competition cases.</td>
<td>core reading (why MMM now); paid, WU-Lizenz prüfen; MSI WP version free</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Estimating the Value of Offsite Tracking Data to Advertisers: Evidence from Meta</td>
<td>Nils Wernerfelt, Anna Tuchman, Bradley T. Shapiro, Robert Moakler; Marketing Science 44(2), 268-286, 2025</td>
<td>[https://doi.org/10.1287/mksc.2023.0274](https://doi.org/10.1287/mksc.2023.0274)</td>
<td>A randomized experiment with more than 70,000 advertisers: losing offsite (pixel/SDK) data raises the median cost per incremental customer by 31%, and hits small advertisers hardest. Quantifies what attribution loses under ATT/GDPR-type restrictions. Two authors were Meta employees, which is worth discussing.</td>
<td>reading (privacy session); paid, WU-Lizenz prüfen; NBER WP w32765 free</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Measuring Digital Advertising in a Post-Cookie Era: A Study of Marketing-Mix Models, Attribution and Incrementality</td>
<td>Shashank Hosahally, Madan Bharadwaj, Arkadiusz Zaremba, Olena Volkova; Journal of Digital & Social Media Marketing, 2025</td>
<td>[https://doi.org/10.69554/wsat6359](https://doi.org/10.69554/wsat6359)</td>
<td>A practitioner-journal piece framed explicitly around EU GDPR. Compares MMM, attribution and incrementality testing as complementary tools once cookies and fingerprinting are restricted. Accessible for students without econometric training; lighter on evidence than the academic papers.</td>
<td>reading (practitioner view); open access per OpenAlex</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Reports (11)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Reports</td>
<td>MSI Blue Ribbon Panel Report: Charting the Future of Marketing Mix Modeling Best Practices</td>
<td>Marketing Science Institute (Arora, Berman, Feit, Hanssens, Li, Lovett, Mela, Wilbur, Lynch), 2023, white paper</td>
<td>[https://www.msi.org/working-paper/msi-blue-ribbon-panel-report-preview-charting-the-future-of-marketing-mix-modeling-best-practices/](https://www.msi.org/working-paper/msi-blue-ribbon-panel-report-preview-charting-the-future-of-marketing-mix-modeling-best-practices/)</td>
<td>An academic panel's best-practice statement on MMM, written in response to privacy-driven signal loss: what MMM is used for (proving contribution, forecasting, optimisation), the challenges, and how to judge vendor claims. Useful for setting quality criteria for student projects. Only the preview is free; the full report needs MSI membership.</td>
<td>background reading; preview free, full report members only (check WU MSI access)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Open-Source Media and Marketing Mix Modeling (MSI Working Paper 26-106)</td>
<td>Julian Runge & Koen Pauwels, Marketing Science Institute / ARF, March 2026</td>
<td>[https://www.msi.org/working-paper/open-source-media-and-marketing-mix-modeling-overview-challenges-opportunities/](https://www.msi.org/working-paper/open-source-media-and-marketing-mix-modeling-overview-challenges-opportunities/)</td>
<td>Free working-paper version of the Customer Needs and Solutions review (see articles). Listed here because WU students can read the MSI PDF without a journal licence. Compares Robyn, Meridian and PyMC-Marketing, with warnings about misspecification and endogeneity.</td>
<td>reading; free PDF (registration may be required)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Econometrics Explained 2</td>
<td>Louise Cook, IPA (Institute of Practitioners in Advertising, UK), 2017, guide</td>
<td>[https://ipa.co.uk/knowledge/documents/econometrics-explained-2/](https://ipa.co.uk/knowledge/documents/econometrics-explained-2/)</td>
<td>A non-technical guide to commissioning and reading MMM: what econometrics can and cannot do, how to plan an analysis, how to read the outputs, with IPA Effectiveness Awards cases. Good for students in client or brand-manager roles who have to brief and challenge a modeller. UK/European agency perspective.</td>
<td>reading (manager perspective); PDF download on IPA site (check access)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Marketing Mix Modeling Guidebook</td>
<td>Hakuhodo DY Media Partners (Japan), published via Think with Google, 2023</td>
<td>[https://thinkwithgoogle.com/_qs/documents/18374/Marketing_Mix_Modeling_Guidebook.pdf](https://thinkwithgoogle.com/_qs/documents/18374/Marketing_Mix_Modeling_Guidebook.pdf)</td>
<td>A long practitioner guidebook from a Japanese media agency: measurement challenges, model structure, parameter estimation, validation, use in decisions. Brings a non-Western market perspective to a mostly US/UK literature, which helps in comparing MMM practice across markets. Very large PDF (\>10 MB).</td>
<td>reading / project reference; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Meridian marketing mix model (Think with Google article, German edition: Meridian Marketing-Mix-Modell)</td>
<td>Google, Think with Google / business.google.com, 2025</td>
<td>[https://business.google.com/de/think/measurement/meridian-marketing-mix-modell/](https://business.google.com/de/think/measurement/meridian-marketing-mix-modell/)</td>
<td>Google's launch article for Meridian (general availability January 2025), in German, with FR, ES, IT, UK and APAC editions. Explains calibration with experiments, reach and frequency, and geo-level modelling for marketers. Comparing the localised editions is a small exercise in how one tool is marketed globally. Vendor source, so not neutral.</td>
<td>background (vendor view); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Marketing Mix Model: The Opportunities Behind Open-Source Techniques</td>
<td>Deloitte España, 22 February 2024, consulting perspective (English text)</td>
<td>[https://www.deloitte.com/es/es/services/consulting/perspectives/marketing-mix-modeling-open-source.html](https://www.deloitte.com/es/es/services/consulting/perspectives/marketing-mix-modeling-open-source.html)</td>
<td>A short consultancy view on open-source MMM: cost, community and flexibility vs limited support, integration effort and the need for an in-house analytics team. Frames in-house vs outsourced vs hybrid operating models. A European consultancy view useful for 'build vs buy' discussions. Light on evidence.</td>
<td>class discussion (operating model); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>2025 Annual Marketing Report (From Chaos to Clarity)</td>
<td>Nielsen, May 2025, global survey report (1,400 senior marketers)</td>
<td>[https://www.nielsen.com/insights/2025/annual-marketing-report-2025/](https://www.nielsen.com/insights/2025/annual-marketing-report-2025/)</td>
<td>Global marketer survey with regional splits, e.g. Europe vs APAC on budget cuts and on confidence in measuring ROI. Nielsen's 2025 ROI findings show that few marketers measure traditional and digital media holistically. Gives students cross-regional context on measurement maturity. Vendor report; download is gated by a form.</td>
<td>background data for project motivation; free (registration)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Cross-Media Measurement (Halo framework and North Star principles)</td>
<td>World Federation of Advertisers (WFA), 2019-2025, programme pages and reports</td>
<td>[https://wfanet.org/leadership/cross-media-measurement](https://wfanet.org/leadership/cross-media-measurement)</td>
<td>The global advertiser body's privacy-safe cross-media reach and frequency framework. It is rolled out market by market (UK Origin with ISBA, US Aquila with ANA). Shows how multinational advertisers organise measurement country by country, and supplies the reach and frequency inputs that Meridian can use. Some documents are WFA members only.</td>
<td>background (multi-market measurement governance); partly free, partly login</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>The Long and the Short of It: Balancing Short and Long-Term Marketing Strategies</td>
<td>Les Binet & Peter Field, IPA, 2013, effectiveness report</td>
<td>[https://ipa.co.uk/knowledge/publications-reports/the-long-and-the-short-of-it-balancing-short-and-long-term-marketing-strategies/](https://ipa.co.uk/knowledge/publications-reports/the-long-and-the-short-of-it-balancing-short-and-long-term-marketing-strategies/)</td>
<td>Based on the IPA Effectiveness Databank. Argues that weekly sales MMMs capture short-term activation but underestimate brand-building effects (the often-cited 60:40 brand/activation split). A caveat to discuss for all three tools, whose adstock windows are short. UK-centric data.</td>
<td>reading (limits of MMM); paid / IPA members (summary materials widely available)</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Regulation (EU) 2016/679 (General Data Protection Regulation)</td>
<td>European Parliament and Council, Official Journal of the EU, 2016</td>
<td>[https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj)</td>
<td>Primary legal source for the privacy argument behind MMM adoption in Europe. Articles 6-7 (lawful basis, consent) explain why user-level tracking became consent-dependent in the EU. Aggregate, non-personal MMM data generally fall outside its scope, which is worth discussing with students. Available in German (DSGVO) and all EU languages.</td>
<td>background (privacy session); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>User Privacy and Data Use (App Tracking Transparency)</td>
<td>Apple Inc., App Store developer guidelines, since iOS 14.5 (2021)</td>
<td>[https://developer.apple.com/app-store/user-privacy-and-data-use/](https://developer.apple.com/app-store/user-privacy-and-data-use/)</td>
<td>Apple's official description of the ATT opt-in requirement for cross-app tracking. Pair it with the Aridor et al. and Wernerfelt et al. papers to show the platform-policy, not legal, source of signal loss. ATT applies globally, while GDPR applies only in the EU: a useful contrast for international marketing.</td>
<td>background (privacy session); free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Websites (29)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC-Marketing Example Gallery (MMM notebooks)</td>
<td>PyMC Labs, pymc-marketing.io, 2026, official docs (notebook gallery)</td>
<td>[https://www.pymc-marketing.io/en/latest/gallery/gallery.html](https://www.pymc-marketing.io/en/latest/gallery/gallery.html)</td>
<td>Central index of all MMM notebooks, grouped by theme: multidimensional/geo (Multidimensional Example, Custom Geo-Hierarchical MMM with Splines, Halo and Cannibalisation in Multi-Dimensional MMMs, Funnel-Aware Geo-Level Mediation), budget allocation (incl. risk assessment, multi-objective, Pareto across products with a shared budget), lift-test calibration (incl. geo-level lift tests), time-varying parameters, two end-to-end case studies. Good map for picking lab notebooks. Content tracks the latest release (1.x), so pin the version for a course.</td>
<td>reading / lab preparation (instructor picks notebooks); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>MMM Multidimensional Example Notebook (Geo-MMM)</td>
<td>PyMC Labs, pymc-marketing.io, 2025-2026, official docs (notebook)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multidimensional_example.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multidimensional_example.html)</td>
<td>Key notebook for multi-market teaching: simulated weekly sales for two markets (geo_a, geo_b), 2 channels, 2 event controls, built with dims=("geo",) and target scaled per geo. Shows mixed pooling choices in one model: hierarchical saturation beta per channel x geo (non-centred), fully pooled lambda, unpooled adstock alpha, geo-specific intercepts and Fourier seasonality. Explains full vs no vs partial pooling and recommends adding complexity step by step; prior predictive check, sampling diagnostics, budget optimisation per geo. Since v1.0 this multidimensional class IS the default MMM.</td>
<td>lab (core multi-country exercise: swap geos for countries); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Custom Geo-Hierarchical MMM with Splines</td>
<td>PyMC Labs, pymc-marketing.io, 2025-2026, official docs (notebook)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_custom_splines.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_custom_splines.html)</td>
<td>Shows how to build a custom hierarchical geo model by combining PyMC-Marketing components (adstock, saturation) with plain PyMC: each geo gets its own spline weights for the baseline, with shared hyperpriors. Useful to show students what happens 'under the hood' and to compare with Meridian's spline/knot baseline.</td>
<td>lab (advanced, optional); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>MMM Calibration with Geo-Level Lift Tests</td>
<td>PyMC Labs, pymc-marketing.io, 2026, official docs (notebook)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_geolift_calibration.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_geolift_calibration.html)</td>
<td>Simulates 8 geos x 104 weeks; 4 treated geos get extra spend for 8 weeks with 4 paired controls. Estimates per-geo lift, then fits an uncalibrated and a calibrated hierarchical MMM. Saturation parameters use (geo, channel) dims with channel-level hyperpriors, so evidence from treated geos informs control geos via partial pooling. Result: narrower mROAS intervals, closer to truth in 3 of 4 geos. Ideal for teaching 'test in a few countries, borrow strength for the rest'.</td>
<td>lab / homework; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Halo and Cannibalisation Effects in Multi-Dimensional MMMs</td>
<td>PyMC Labs, pymc-marketing.io, 2026, official docs (notebook)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_halo.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_halo.html)</td>
<td>Multi-dimensional MMM where spend in one dimension (product/brand/market) can lift or cannibalise another. Good discussion starter for cross-market spillovers (e.g. German TV spilling into Austria) and portfolio brands.</td>
<td>reading / advanced lab; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Multi-Objective Optimization and Pareto Optimization Across Products with a Shared Media Budget</td>
<td>PyMC Labs, pymc-marketing.io, 2026, official docs (notebooks)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multi_objective_optimization.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multi_objective_optimization.html)</td>
<td>Shows how to merge several fitted models into one optimiser and trade off objectives; the companion notebook mmm_pareto_optimization.html allocates one media budget across products. Directly transferable to allocating a central (HQ) budget across country models.</td>
<td>lab (budget allocation across markets); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Why and how to account for media inflation in your MMM</td>
<td>PyMC Labs, pymc-marketing.io, 2026, official docs (notebook)</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_media_inflation.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_media_inflation.html)</td>
<td>Explains why rising media prices distort spend-based effects and how to adjust. Relevant for international data where CPMs, inflation and currency movements differ by country; pair with the cost-per-unit notebook (mmm_cost_per_unit.html). None of the three tools has a built-in FX conversion, so this is the closest official guidance.</td>
<td>reading / discussion (currency and price differences across markets); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC-Marketing 1.0.0 release notes (multidimensional MMM becomes the default)</td>
<td>PyMC Labs, GitHub releases, August 2026, release notes</td>
<td>[https://github.com/pymc-labs/pymc-marketing/releases/tag/1.0.0](https://github.com/pymc-labs/pymc-marketing/releases/tag/1.0.0)</td>
<td>States 'Multidimensional MMM is now the MMM': geo, product and channel dims first-class, one xr.Dataset for all inputs; about 1.5x faster sampling; PyMC 6 / ArviZ 1.2 stack; new plotting API. Old MMM class removed, so tutorials before Aug 2026 (incl. many blogs) use an outdated API; see the MMM API and Dims Migration Guide notebooks. Latest at time of search: 1.3.0 (22 Oct 2026).</td>
<td>instructor reference (version pinning); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC-Marketing MMM resources page (talks, case studies, blogs)</td>
<td>PyMC Labs, pymc-marketing.io, ongoing, official docs (curated list)</td>
<td>[https://www.pymc-marketing.io/en/latest/guide/mmm/resources.html](https://www.pymc-marketing.io/en/latest/guide/mmm/resources.html)</td>
<td>Curated list of videos (Wiecki, Bolt, yearly catch-up), business cases (Bolt, Shell and Databricks, HelloFresh), and third-party blogs (Orduz, Kübler, O'Sullivan on multicollinearity), plus the JellyPop tutorial repo and the MMM Explainer Streamlit app. Fast way to build a reading list; most entries are undated.</td>
<td>reading list source; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC-Marketing GitHub Discussion #1486: example notebook for geo hierarchy with the MMM class</td>
<td>pymc-labs, GitHub Discussions, Feb-Mar 2025, community Q&A</td>
<td>[https://github.com/pymc-labs/pymc-marketing/discussions/1486](https://github.com/pymc-labs/pymc-marketing/discussions/1486)</td>
<td>Short thread showing how geo-hierarchical support entered the library (maintainer W. Dean points to the new multidimensional MMM, later the official notebook). Useful to show students how fast these tools change and how to read issues/discussions.</td>
<td>warm-up (reading open-source development); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC Discourse: Hierarchical MMM model for different geo using PyMC</td>
<td>PyMC Discourse community, Feb 2025, forum thread</td>
<td>[https://discourse.pymc.io/t/hierarchical-mmm-model-for-different-geo-using-pymc/16557](https://discourse.pymc.io/t/hierarchical-mmm-model-for-different-geo-using-pymc/16557)</td>
<td>Practitioner with 4 geos x 5 channels asks how to report per-geo and overall contributions, saturation curves and budget allocation; answers explain slicing xarray contributions by geo, plotting curves with actual spend, custom optimisers for hierarchies and back-transforming scaled data. Links further geo threads (2023-2025).</td>
<td>homework support / troubleshooting; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian documentation: About the project and full docs navigation</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/basics/about-the-project](https://developers.google.com/meridian/docs/basics/about-the-project)</td>
<td>Entry point to the three-stage workflow (pre-modeling, modeling, post-modeling) with links to loading geo-level data (with or without reach and frequency, organic media), national data, priors (ROI/mROI/contribution parameterisations, default priors, non-revenue KPI), calibration, optimisation scenarios and Scenario Planner. Use as the course's Meridian syllabus.</td>
<td>reading (orientation); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: Geo-level modeling (geo selection and national data)</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/pre-modeling/geo-selection-national-data](https://developers.google.com/meridian/docs/pre-modeling/geo-selection-national-data)</td>
<td>Why geo data beats national data (larger effective sample, tighter intervals, more knots, more spend variation, less omitted-variable bias); drop smallest geos first rather than aggregating; for the US, model the top 50-100 DMAs; impute national-only channels to geos by population share. Mentions countries as possible geo units but does not cover currencies, which is a good discussion point for an international course.</td>
<td>reading (before multi-country lab); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: National models</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/advanced-modeling/national-models](https://developers.google.com/meridian/docs/advanced-modeling/national-models)</td>
<td>The national model is a geo model with one geo: geo-level deviations (eta, xi) are set to zero, unique_sigma_for_each_geo=False, population scaling has no effect. Helps students see what is lost when each country is modelled alone.</td>
<td>reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: Model specification</td>
<td>Google, developers.google.com, 2025-2026, official docs (technical)</td>
<td>[https://developers.google.com/meridian/docs/advanced-modeling/model-spec](https://developers.google.com/meridian/docs/advanced-modeling/model-spec)</td>
<td>Formal hierarchical structure: geo media coefficients beta_g,i drawn from Normal(beta_i, eta_i) (or log-normal), geo intercepts tau_g with a baseline geo, geo-level control coefficients, shared time effects via knots, residual sigma per geo optional. Best compact source to explain partial pooling across countries mathematically.</td>
<td>reading (methods session); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: Input data (population scaling, revenue per KPI)</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/advanced-modeling/input-data](https://developers.google.com/meridian/docs/advanced-modeling/input-data)</td>
<td>Population per geo is required; KPI is divided by population and standardised so geos are comparable, which is needed for the hierarchy. Revenue (or revenue per KPI) converts units to a currency value for ROI. No guidance on mixing currencies, so students must convert to one currency before fitting (teaching point).</td>
<td>reading / lab preparation (data design for multi-country panels); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: Calibrate treatment priors (ROI priors and calibration)</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/advanced-modeling/roi-priors-and-calibration](https://developers.google.com/meridian/docs/advanced-modeling/roi-priors-and-calibration)</td>
<td>How to turn experiment results and domain knowledge into ROI priors; companion pages on setting custom priors from past experiments and on channel calibration recommendations. Basis for 'cross-market priors' exercises (use a lift test from market A as a prior in market B).</td>
<td>reading / lab; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian: Budget optimization scenarios</td>
<td>Google, developers.google.com, 2025-2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/user-guide/budget-optimization-scenarios](https://developers.google.com/meridian/docs/user-guide/budget-optimization-scenarios)</td>
<td>Fixed-budget vs flexible-budget (target ROI / mROI) scenarios, spend constraints per channel; linked pages on interpreting optimisations and on optimisation with reach and frequency. Since v2.0 scenarios can use flexible time frames.</td>
<td>lab (budget allocation); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian GeoX (open-source geo experiments)</td>
<td>Google, developers.google.com, 2026, official docs and repo</td>
<td>[https://developers.google.com/meridian/geox](https://developers.google.com/meridian/geox)</td>
<td>Google's open-source geo-experiment tool (GA since 9 Sept 2026); multi-cell designs; results feed Meridian as calibration priors. Links to Colab notebooks, guides, API reference and GitHub (google/meridian-geox). Caveat from commentators: experiments mostly cover Google/YouTube channels.</td>
<td>reading / lab (experiment design across regions); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian Scenario Planner (open beta)</td>
<td>Google, developers.google.com, 2026, official docs</td>
<td>[https://developers.google.com/meridian/docs/scenario-planning/meridian-scenario-planner](https://developers.google.com/meridian/docs/scenario-planning/meridian-scenario-planner)</td>
<td>No-code dashboard layer (Data/Looker Studio) generated from a Colab on top of a trained Meridian model; interactive budget scenarios. Useful to show how model output is handed to marketing managers in different countries. Requires a trained model in Drive/GCS.</td>
<td>demo / warm-up; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian 2.0 announcement (GitHub Discussion #1819)</td>
<td>Google Meridian team, GitHub Discussions, 4 Sept 2026, release announcement</td>
<td>[https://github.com/google/meridian/discussions/1819](https://github.com/google/meridian/discussions/1819)</td>
<td>Meridian v2.0 (2 Sept 2026): GeoX and automated calibration, full-funnel framework with brand equity signals (branded query volume), MCP-based agentic skills, JAX backend (about 2x faster, 4x more memory-efficient), flexible time frames. Breaking changes, so tutorials from 2025 may not run unchanged.</td>
<td>instructor reference (version check); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Meridian Studio (enterprise cloud platform)</td>
<td>Google, developers.google.com, 2026, product page</td>
<td>[https://developers.google.com/meridian/studio](https://developers.google.com/meridian/studio)</td>
<td>UI-based Google Cloud platform for running up to hundreds of Meridian models (e.g. one per market/brand). No pricing shown. Good for discussing open-source vs managed platforms and platform lock-in.</td>
<td>discussion; info page free (product access unclear)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>LightweightMMM documentation (archived predecessor of Meridian)</td>
<td>Google, Read the Docs / GitHub, 2022-2024 (repo archived Jan 2026), docs</td>
<td>[https://lightweight-mmm.readthedocs.io/en/latest/](https://lightweight-mmm.readthedocs.io/en/latest/)</td>
<td>Historical reference: LightweightMMM already offered a geo-level hierarchical model (e.g. states within a country). No longer supported; README recommends switching to Meridian. Use only to explain lineage (Sun et al. 2017 geo paper, LightweightMMM, Meridian) and to warn students about outdated tutorials.</td>
<td>background reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn: An Analyst's Guide to MMM</td>
<td>Meta Marketing Science, facebookexperimental.github.io, updated 2024, official docs</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/analysts-guide-to-MMM/](https://facebookexperimental.github.io/Robyn/docs/analysts-guide-to-MMM/)</td>
<td>Best Robyn reading: build options, data collection (recommends DMA/state-level data, national acceptable), feature engineering, model selection, calibration with experiments (incl. GeoLift), refresh, budget allocation. Mentions Prophet holidays for 59 countries and Meta MMM feed split by country, but no joint multi-market model.</td>
<td>reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn: Key Features</td>
<td>Meta Marketing Science, facebookexperimental.github.io, Dec 2024 (v3.12), official docs</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/features/](https://facebookexperimental.github.io/Robyn/docs/features/)</td>
<td>Ridge regression with Nevergrad multi-objective search, calibration via MAPE.LIFT objective, beta curve calibrator with reach and frequency, budget allocator (max response; target ROAS/CPA). prophet_country takes ONE country, which shows that Robyn is designed for single-market models.</td>
<td>reading (tool comparison); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn Python (Beta) documentation</td>
<td>Meta Marketing Science, facebookexperimental.github.io, 2023-2024, official docs</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/robyn-api/](https://facebookexperimental.github.io/Robyn/docs/robyn-api/)</td>
<td>RobynPy (pip install robynpy) is an LLM-assisted rewrite of R v3.11.1, still beta; tutorial notebooks tutorial1.ipynb (one-click) and tutorial1_src.ipynb (module by module). Lets Python-only classes try Robyn, but expect translation bugs; the R package remains the reference.</td>
<td>lab option for Python classes; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn Resources page (Blueprint, Medium deep dives, whitepaper)</td>
<td>Meta Marketing Science, facebookexperimental.github.io, 2024, official docs</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/resources/](https://facebookexperimental.github.io/Robyn/docs/resources/)</td>
<td>Links to the Blueprint course, four Medium deep dives by the Robyn team (budget allocator mROAS convergence, ROAS targets, calibration precision), HBR article, a survey of MMM providers whitepaper and case studies (Resident, Central Group, Bark).</td>
<td>reading list source; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn GitHub Discussion #856: Can Robyn enable geo or segment level analysis?</td>
<td>facebookexperimental/Robyn, GitHub Discussions, Nov 2023, community Q&A</td>
<td>[https://github.com/facebookexperimental/Robyn/discussions/856](https://github.com/facebookexperimental/Robyn/discussions/856)</td>
<td>Accepted maintainer answer: Robyn does not do geo hierarchies like LightweightMMM; workaround is to split data by geo and build one Robyn model per subset. Primary evidence for the comparison table (Robyn = one model per country, no pooling). See also closed feature request issue #494 on panel data.</td>
<td>reading (evidence for tool comparison); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Robyn demo.R (step-by-step R script)</td>
<td>Meta Marketing Science, GitHub, ongoing, code tutorial</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>Official end-to-end R workflow on the bundled simulated dataset: input specification, hyperparameters, robyn_run, Pareto models, calibration, refresh, allocator. Needs Python Nevergrad installed; budget setup time for students.</td>
<td>lab (Robyn session, run once per country); free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Blogs (32)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Blogs</td>
<td>PyMC-Marketing vs. Meridian: A Quantitative Comparison of Open Source MMM Libraries</td>
<td>Teemu Säilynoja, Luca Fiaschi, Jake Piekarski, PyMC Labs blog, Sept 2025, blog post (benchmark)</td>
<td>[https://www.pymc-labs.com/blog-posts/pymc-marketing-vs-google-meridian](https://www.pymc-labs.com/blog-posts/pymc-marketing-vs-google-meridian)</td>
<td>Benchmark on four synthetic datasets from 1 geo/4 channels to 50 geos/30 channels (10,400 rows), matched priors. Reports PyMC-Marketing 2-20x faster (ESS/s), better fit and about half the contribution error at small scale; Meridian residual autocorrelation and divergences at enterprise scale. Versions: pymc-marketing 0.15.1, Meridian 1.1.6 (both since superseded). Code: github.com/pymc-labs/mmm-param-recovery. Vendor-authored: treat as claims to replicate.</td>
<td>reading + critical discussion (who benchmarks whom?); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>PyMC-Marketing and Meridian Revisited: Approaches to Baseline Modeling for MMMs</td>
<td>Teemu Säilynoja, Luca Fiaschi, PyMC Labs blog, Dec 2025, blog post (12 min)</td>
<td>[https://www.pymc-labs.com/blog-posts/pymc-marketing-vs-meridian-baseline-modeling-mmm](https://www.pymc-labs.com/blog-posts/pymc-marketing-vs-meridian-baseline-modeling-mmm)</td>
<td>Fourier seasonality (PyMC-Marketing) vs Meridian v1.2.1 spline baseline with automated knot selection: more knots raise in-sample fit but absorb media effects (higher bias in contribution recovery). Clear illustration of 'good fit is not causal accuracy'. National-style data only, no geo results.</td>
<td>reading (methods); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Cracking the Funnel: How Nürnberger Quantified Cross-Channel Synergies</td>
<td>Timothy McWilliams, Teemu Säilynoja, Niall Oulton, PyMC Labs blog, 2026, case blog</td>
<td>[https://www.pymc-labs.com/blog-posts/funnel-aware-mmm](https://www.pymc-labs.com/blog-posts/funnel-aware-mmm)</td>
<td>German insurer (Nürnberger Versicherung) case: funnel-aware PyMC-Marketing MMM linking upper-funnel video to paid search demand, censored budget-capped channels, no user-level tracking (GDPR context). Reports over 27% lower cost per lead; multidimensional setup planned to scale across geos and products in 2026. Vendor case, figures unverified.</td>
<td>reading / case discussion (DACH, privacy); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Exploration vs Exploitation in Marketing Budget Allocation</td>
<td>PyMC Labs blog, 2025-2026, blog post</td>
<td>[https://www.pymc-labs.com/blog-posts/exploration-vs-exploitation-marketing-budget-allocation](https://www.pymc-labs.com/blog-posts/exploration-vs-exploitation-marketing-budget-allocation)</td>
<td>Uses posterior uncertainty to decide when to shift budget vs keep testing. Useful for discussing budgets in new or small markets where data are thin.</td>
<td>reading (optional); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Media Mix Model and Experimental Calibration: A Simulation Study</td>
<td>Juan Camilo Orduz, personal blog, Feb 2024, blog post with code</td>
<td>[https://juanitorduz.github.io/mmm_roas/](https://juanitorduz.github.io/mmm_roas/)</td>
<td>Simulation showing how unobserved confounders bias MMM and how lift-test calibration recovers true ROAS; code in PyMC/PyMC-Marketing. Strong foundation for the calibration session (pre-1.0 API).</td>
<td>reading / homework replication; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Geo-Experimentation via Time Based Regression in PyMC</td>
<td>Juan Camilo Orduz, personal blog, Dec 2022, blog post with code</td>
<td>[https://juanitorduz.github.io/time_based_regression_pymc/](https://juanitorduz.github.io/time_based_regression_pymc/)</td>
<td>Implements Google's time-based regression for geo experiments in PyMC. Bridges geo experiments (GeoLift/GeoX) and Bayesian MMM calibration; good for showing how regions serve as treatment and control.</td>
<td>reading / lab extension; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Bayesian Hierarchical Marketing Mix Modeling in PyMC</td>
<td>Robert Kübler, Towards Data Science, July 2022, blog post with code</td>
<td>[https://towardsdatascience.com/bayesian-hierarchical-marketing-mix-modeling-in-pymc-684f6024e57a/](https://towardsdatascience.com/bayesian-hierarchical-marketing-mix-modeling-in-pymc-684f6024e57a/)</td>
<td>Multi-country hierarchical MMM with country-level parameters and shared hyperpriors, with results shown for Germany, Austria and Switzerland (wide posteriors for the data-poor country). Very close to a WU teaching setting, but uses plain PyMC and an old API; use for intuition, not code.</td>
<td>reading (intuition for cross-market pooling); free (TDS)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Convenient Bayesian Marketing Mix Modeling with PyMC-Marketing</td>
<td>Robert Kübler, Towards Data Science, 2023, blog post</td>
<td>[https://towardsdatascience.com/convenient-bayesian-marketing-mix-modeling-with-pymc-marketing-8b02a9a9c4aa](https://towardsdatascience.com/convenient-bayesian-marketing-mix-modeling-with-pymc-marketing-8b02a9a9c4aa)</td>
<td>Gentle introduction to the PyMC-Marketing MMM class (adstock, saturation, priors, contributions). Listed on the official resources page. Old API (pre-1.0); pair with current quickstart.</td>
<td>warm-up reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Hitting ROAS target using Robyn's budget allocator</td>
<td>Gufeng Zhou (Meta Marketing Science), Medium, 2023, blog post</td>
<td>[https://medium.com/@gufengzhou/hitting-roas-target-using-robyns-budget-allocator-274ace3add4f](https://medium.com/@gufengzhou/hitting-roas-target-using-robyns-budget-allocator-274ace3add4f)</td>
<td>Explains the target_efficiency scenario in Robyn's allocator (find spend that meets a ROAS/CPA target). Useful when local market teams have ROAS targets rather than fixed budgets.</td>
<td>reading (Robyn lab support); free</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>More precision in MMM-experiment calibration with Robyn from Meta Marketing Science</td>
<td>Gufeng Zhou (Meta Marketing Science), Medium, 2023-2024, blog post</td>
<td>[https://medium.com/@gufengzhou/more-precision-in-mmm-experiment-calibration-with-robyn-from-meta-marketing-science-f608841fc6d4](https://medium.com/@gufengzhou/more-precision-in-mmm-experiment-calibration-with-robyn-from-meta-marketing-science-f608841fc6d4)</td>
<td>How Robyn uses lift results as an extra optimisation objective (MAPE.LIFT) and recent refinements. Contrast with Bayesian priors in Meridian/PyMC-Marketing.</td>
<td>reading (calibration comparison); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Meridian is now available to everyone</td>
<td>Harikesh Nair, Google Ads and Commerce blog, 29 Jan 2025, official blog post</td>
<td>[https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/](https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/)</td>
<td>Official general-availability announcement: Bayesian causal inference, experiments as priors, reach and frequency for video, privacy-centric aggregated data, partner programme (20+ partners), Finder case (AU/UK/US/CA). Short primary source for the privacy-driven MMM revival.</td>
<td>warm-up reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>First impressions: Meridian, Google's MMM software is finally released</td>
<td>Matt Triggs, Jaywing (UK), 29 Jan 2025, practitioner blog</td>
<td>[https://www.jaywing.com/views/news/first-impressions-meridian-google-s-mmm-software-is-finally-released/](https://www.jaywing.com/views/news/first-impressions-meridian-google-s-mmm-software-is-finally-released/)</td>
<td>Practitioner comparison: Meridian adds time-varying coefficients and lift calibration that LightweightMMM lacked, matches PyMC-Marketing in places, unique reach-and-frequency modelling, multi-geo support; lacks non-geo segmentation (e.g. product categories). Author prefers PyMC-Marketing over Robyn. Version-dated (Meridian 1.0).</td>
<td>reading (tool comparison); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Which marketing mix modelling platform should you use?</td>
<td>Harry Brace, Impression (UK agency), June 2026, agency blog (6 min)</td>
<td>[https://www.impressiondigital.com/blog/which-marketing-mix-modelling-platform-should-you-use/](https://www.impressiondigital.com/blog/which-marketing-mix-modelling-platform-should-you-use/)</td>
<td>Recent three-way comparison with a table: geo-level modelling in Meridian and PyMC-Marketing but not Robyn; PyMC-Marketing for hierarchies across geos/product lines and many test results, Meridian for Google-heavy budgets and reach/frequency, Robyn for quick readouts with few channels. Good decision-rule handout.</td>
<td>reading (comparison); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google Meridian vs Facebook Robyn</td>
<td>Merve Aslan, AnalyticaHouse blog, June 2025, agency blog</td>
<td>[https://analyticahouse.com/blogs/google-meridian-facebook-robyn](https://analyticahouse.com/blogs/google-meridian-facebook-robyn)</td>
<td>Side-by-side table: Bayesian vs ridge, Prophet seasonality and Nevergrad in Robyn, Google query volume, YouTube reach and geo analysis in Meridian, skills needed (R vs advanced stats/data engineering), documentation gaps. Simple, student-friendly.</td>
<td>warm-up reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google Meridian: honest guide for data teams</td>
<td>Agilytic (Belgium), Oct 2026, consultancy blog</td>
<td>[https://www.agilytic.com/blog/google-meridian-a-game-changer-for-marketing-mix-modeling](https://www.agilytic.com/blog/google-meridian-a-game-changer-for-marketing-mix-modeling)</td>
<td>European example of geo-level use: model Flanders and Wallonia separately instead of one national average; GeoX experiments for calibration; warns that free is not easy, priors need commercial knowledge, open source gives transparency not independence. Advice: start with one market, one decision, 2-3 years weekly data.</td>
<td>reading (international/regional angle); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>How to Run Multi-Country MMM</td>
<td>Ramanath, Presenc AI, May 2026, vendor guide</td>
<td>[https://presenc.ai/guides/how-to-run-multi-country-mmm](https://presenc.ai/guides/how-to-run-multi-country-mmm)</td>
<td>One of few guides explicitly on multi-country MMM: compares country-specific models, pooled model with country dummies, and hierarchical models with shared priors; says PyMC-Marketing supports hierarchy natively while Robyn/LightweightMMM need workarounds; covers country grouping (52+ weeks per country), channels missing in some countries, country-level holdouts, two-stage vs joint budget optimisation. No currency discussion; vendor sells AI-visibility data.</td>
<td>reading (framework for the international session); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Meridian: Marketing Mix Modeling (MMM) package by Google</td>
<td>Sellforte (Finland, MMM vendor), 2025-2026, vendor support article</td>
<td>[https://sellforte.com/support/meridian-marketing-mix-modeling-mmm-package-by-google](https://sellforte.com/support/meridian-marketing-mix-modeling-mmm-package-by-google)</td>
<td>Lists Meridian features (geo hierarchy based on Google's geo paper, priors from lift tests, query volume control) and limitations (no data connectors, no GUI, needs data-science team). Vendor framing, useful for a build-vs-buy debate.</td>
<td>discussion (build vs buy); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google Meridian Alternatives: A Practical Comparison</td>
<td>Dr Ramla Jarrar, MASS Analytics, Aug 2026, vendor blog</td>
<td>[https://mass-analytics.com/marketing-mix-modeling-blogs/the-google-meridian-alternative/](https://mass-analytics.com/marketing-mix-modeling-blogs/the-google-meridian-alternative/)</td>
<td>Positions Meridian (Bayesian, geo), Robyn (ridge, R) and PyMC-Marketing (most flexible, build your own stack) against commercial platforms; argues none covers data prep, refresh, governance. Vendor perspective for the build-vs-buy debate.</td>
<td>discussion; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Recast vs Robyn: Feature Comparison</td>
<td>Michael Kaminsky, Recast blog, July 2023, vendor blog</td>
<td>[https://getrecast.com/recast-vs-robyn-what-model-is-best/](https://getrecast.com/recast-vs-robyn-what-model-is-best/)</td>
<td>Critical list of Robyn's assumptions: static channel performance (problematic after iOS 14.5/ATT), seasonality independent of media, lift tests as point estimates, 20+ equally fitting candidate models, hard backtesting. Good for critical evaluation of Robyn; author is a competitor.</td>
<td>reading (critical evaluation); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Is Google's Meridian The Right Open-Source MMM Solution For You?</td>
<td>Brad Haag, Forrester blog, 31 Jan 2025, analyst blog</td>
<td>[https://www.forrester.com/blogs/is-googles-meridian-the-right-open-source-mmm-solution-for-you/](https://www.forrester.com/blogs/is-googles-meridian-the-right-open-source-mmm-solution-for-you/)</td>
<td>Analyst view: Meridian will not replace paid MMM services; DIY needs strong data engineering/science, extensive geo-level history and experiment experience; materials not executive-friendly; recommends layered measurement. Good managerial counterweight.</td>
<td>reading (managerial perspective); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Open-source MMM is having a moment (interview with Julian Runge)</td>
<td>Allison Schiff, AdExchanger, Aug 2026, trade press interview</td>
<td>[https://adexchanger.com/measurement/open-source-mmm-is-having-a-moment-and-sorry-about-the-new-acronym](https://adexchanger.com/measurement/open-source-mmm-is-having-a-moment-and-sorry-about-the-new-acronym)</td>
<td>Northwestern professor Julian Runge on why privacy rules (GDPR, IDFA deprecation) pushed open-source MMM, how AI agents lower the barrier, why human oversight stays necessary; Robyn easiest/frequentist, Meridian and PyMC Bayesian; Meridian suits impression inputs, Robyn spend data. Accessible for master students.</td>
<td>warm-up reading; free (may hit paywall)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google's Meridian and Meta's Robyn: a gift to measurement or Trojan horses?</td>
<td>James Hercher, AdExchanger, July 2026, trade press</td>
<td>[https://adexchanger.com/marketers/googles-meridian-and-metas-robyn-a-gift-to-measurement-or-trojan-horses](https://adexchanger.com/marketers/googles-meridian-and-metas-robyn-a-gift-to-measurement-or-trojan-horses)</td>
<td>Neutrality debate: Meridian's value tied to Google data, platforms have commercial motives, Meta reportedly no longer pushing Robyn; advises checking under the hood. Good for an ethics/governance debate in class.</td>
<td>discussion reading; free (may hit paywall)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Open source made MMM cheaper, not easier</td>
<td>Ben Vigneron, MarTech, July 2026, trade press column</td>
<td>[https://martech.org/open-source-made-mmm-cheaper-not-easier/](https://martech.org/open-source-made-mmm-cheaper-not-easier/)</td>
<td>Short practitioner take on all three tools: Robyn most approachable (Nevergrad, Pareto front), Meridian rigorous with geo priors and steeper curve, PyMC-Marketing most flexible and demanding; free software is not a free model.</td>
<td>warm-up reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Explaining Meridian</td>
<td>Luis Rijo, PPC Land, Sept 2026, trade press explainer</td>
<td>[https://ppc.land/explaining-meridian/](https://ppc.land/explaining-meridian/)</td>
<td>Up-to-date explainer: hierarchical Bayesian regression on geo-level data, adstock and Hill curves, calibration, timeline from 2024 preview to v2.0 (Sept 2026), Scenario Planner, Analytics 360 integration, and criticism (endogeneity preprint, platform governance, calibration cost).</td>
<td>reading (current state); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google's Meridian GeoX exits beta claiming 31% cheaper geo experiments</td>
<td>PPC Land, Sept 2026, trade press</td>
<td>[https://ppc.land/googles-meridian-geox-exits-beta-claiming-31-cheaper-geo-experiments/](https://ppc.land/googles-meridian-geox-exits-beta-claiming-31-cheaper-geo-experiments/)</td>
<td>News on GeoX general availability and Meridian 2.0.0 (JAX default, automated calibration, brand equity, agentic skills); time-varying media ROI announced for Q4 2026. Vendor claims flagged as unverified.</td>
<td>background reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Meta's Robyn: who really benefits when a platform builds your MMM?</td>
<td>Luis Rijo, PPC Land, Apr 2026, trade press analysis</td>
<td>[https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/](https://ppc.land/metas-robyn-who-really-benefits-when-a-platform-builds-your-mmm/)</td>
<td>Critical piece on neutrality: Resident case where a Robyn model coincided with a 15-20% higher Facebook budget share; notes Robyn docs last updated 2024 and the 'experimental' label. Pair with the Meridian Trojan-horse article.</td>
<td>discussion reading; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Podcast: Demystifying open-source MMM (with Michael Kaminsky)</td>
<td>Eric Seufert, Mobile Dev Memo (mdm.co), July 2026, podcast with transcript (approx. 60 min)</td>
<td>[https://mdm.co/podcast-demystifying-open-source-mmm-with-michael-kaminsky/](https://mdm.co/podcast-demystifying-open-source-mmm-with-michael-kaminsky/)</td>
<td>Are Robyn and Meridian platforms grading their own homework? How to validate MMMs (parameter recovery, holdouts, lift tests): 'the default assumption should be that MMMs in general are wrong'. Transcript available for students who prefer reading.</td>
<td>homework listening / discussion; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Marketing Mix Modeling 2026: Praxisleitfaden für moderne MMM-Stacks</td>
<td>Nick Meyer, Davies Meyer GmbH (Hamburg), Apr 2026, German agency blog (4 min)</td>
<td>[https://ai-solutions.daviesmeyer.com/de/blog/marketing-mix-modeling-mmm-guide-2026](https://ai-solutions.daviesmeyer.com/de/blog/marketing-mix-modeling-mmm-guide-2026)</td>
<td>German-language practitioner guide for DACH mid-market teams: compares Robyn (R, ridge), Meridian (Python, Bayesian), LightweightMMM and SaaS; recommends Robyn or Meridian plus internal analyst plus quarterly external validation. Efficiency figures are vendor claims; PyMC-Marketing not covered.</td>
<td>reading (DACH practice, German); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Marketing Mix Modeling: Meridian, Robyn und die Datenschwelle</td>
<td>Blck Alpaca e.U. (Austria), 2026, German agency knowledge base</td>
<td>[https://blckalpaca.at/de/wissen/social-media/social-media-analytics-kpis-measurement/marketing-mix-modeling-meridian-robyn](https://blckalpaca.at/de/wissen/social-media/social-media-analytics-kpis-measurement/marketing-mix-modeling-meridian-robyn)</td>
<td>Austrian agency article on data requirements (parameters vs observations, about 10 observations per variable; Meridian docs: 2 years weekly too little for 26 parameters; Robyn: 2+ years weekly), cost ranges for managed/SaaS/in-house MMM, calibration in Meridian (priors) vs Robyn (extra objective). Content checked in the English version; German URL from search.</td>
<td>reading (German, Austrian context); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Google stellt Open Source Marketing Mix Model Meridian vor</td>
<td>Niklas Lewanczik, OnlineMarketing.de, 11 Mar 2024, German trade press</td>
<td>[https://onlinemarketing.de/sea/google-open-source-marketing-mix-model-meridian](https://onlinemarketing.de/sea/google-open-source-marketing-mix-model-meridian)</td>
<td>German news on the Meridian preview: link to cookie phase-out and privacy-friendly measurement, open code as a starting point for own models, YouTube reach and frequency. Dated (pre-GA) but a good German-language warm-up on the privacy motive.</td>
<td>warm-up (German); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>New-Generation Marketing Mix Modelling with Meridian</td>
<td>Medium / Towards Data Science (data-science publication), 2025, blog post</td>
<td>[https://medium.com/data-science/new-generation-marketing-mix-modelling-with-meridian-e831a0906b40](https://medium.com/data-science/new-generation-marketing-mix-modelling-with-meridian-e831a0906b40)</td>
<td>Hands-on introduction to Meridian with the geo hierarchy idea (regions learn from each other but keep their own effects). Could not be opened (403); check version and code before assigning.</td>
<td>optional reading; free/metered (Medium)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Running Robyn in R</td>
<td>Saxifrage blog (Mike Taylor and team), 2022-2023, tutorial blog post</td>
<td>[https://www.saxifrage.xyz/post/running-robyn-in-r](https://www.saxifrage.xyz/post/running-robyn-in-r)</td>
<td>Practical walkthrough of installing and running Robyn in R, with pitfalls. Helpful for students without R background before the demo.R lab.</td>
<td>lab preparation; free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### (Video-) Tutorials (27)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Intro to Meridian</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=L2QmrfCVnBQ](https://www.youtube.com/watch?v=L2QmrfCVnBQ)</td>
<td>First episode of Google's official Meridian video series: MMM fundamentals and why Meridian. Series also covers demo, priors, knots, controls/mediators, ROI/mROI, geo vs national, Scenario Planner. Short format; good flipped-classroom material.</td>
<td>warm-up (pre-class video); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Geo Vs National Level Modeling</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=apaWURDjGX4](https://www.youtube.com/watch?v=apaWURDjGX4)</td>
<td>The episode most relevant to the international angle: when to use geo-level vs national models, pooling across geos, data needs. Pair with the geo-selection docs page.</td>
<td>pre-class video for the multi-market session; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Demo of Meridian</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=GXC8D0SMHMc](https://www.youtube.com/watch?v=GXC8D0SMHMc)</td>
<td>Tour of the end-to-end Meridian workflow (data loading, model configuration, fitting, diagnostics, outputs). Watch before the Getting Started Colab.</td>
<td>lab preparation; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Intro to Priors</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=v5S5jSholZI](https://www.youtube.com/watch?v=v5S5jSholZI)</td>
<td>Explains priors in Meridian (default LogNormal ROI prior etc.). Good bridge to cross-market priors.</td>
<td>pre-class video; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Calibrate Treatment Priors</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=TtM2pNDHRSI](https://www.youtube.com/watch?v=TtM2pNDHRSI)</td>
<td>How experiment results become calibrated ROI priors. Related episode 'Treatment Prior Types' (watch?v=brriIvu2TLY).</td>
<td>pre-class video (calibration session); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Incremental Outcome, ROI, mROI, and Response Curves</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=3GJ5PieyDIc](https://www.youtube.com/watch?v=3GJ5PieyDIc)</td>
<td>Interpreting Meridian outputs; pairs with the ROI/mROI/Response Curves Colab demo. Helps managers compare ROI vs marginal ROI across markets.</td>
<td>pre-class video; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Knots in Meridian</td>
<td>Google Analytics YouTube channel, 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=gP-mI82bpAE](https://www.youtube.com/watch?v=gP-mI82bpAE)</td>
<td>Explains the spline/knot baseline. Use together with the PyMC Labs baseline-modeling blog for a debate on baseline flexibility vs media attribution. Companion episode: 'Controls, Mediators and Treatments' (watch?v=rg-CL4hdD5o).</td>
<td>methods session; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Google Meridian \| Scenario Planner Overview</td>
<td>Google Analytics YouTube channel, Aug 2026, video (official series)</td>
<td>[https://www.youtube.com/watch?v=X3ksrQ1U1SI](https://www.youtube.com/watch?v=X3ksrQ1U1SI)</td>
<td>Walkthrough of the no-code Scenario Planner dashboard for budget scenarios on top of a trained model.</td>
<td>demo in class; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Meridian Livestream (Meridian 2.0 and GeoX launch)</td>
<td>Google Analytics YouTube channel, 9 Sept 2026, livestream recording (approx. 35 min)</td>
<td>[https://www.youtube.com/watch?v=KNAF5XCMT5g](https://www.youtube.com/watch?v=KNAF5XCMT5g)</td>
<td>Launch stream for GeoX general availability and Meridian 2.0 (JAX backend, automated calibration, agentic skills). Most current official overview; check that the recording is still online.</td>
<td>optional viewing (state of the art); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Meridian Getting Started guide (Colab)</td>
<td>Google, developers.google.com, 2025-2026, notebook tutorial</td>
<td>[https://developers.google.com/meridian/notebook/meridian-getting-started](https://developers.google.com/meridian/notebook/meridian-getting-started)</td>
<td>Official starter notebook on simulated geo-level data (install, load data, configure, fit, diagnostics, optimisation). Examples page also lists Reach and Frequency demo, ROI/mROI demo, Full-Funnel demo and GeoX prior calibration Colabs. Check compatibility with v2.0 (JAX) before class.</td>
<td>lab (Meridian session, Colab, no install); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Calibrate your Meridian model with Meridian GeoX (Colab)</td>
<td>Google, GitHub/Colab, Sept 2026, notebook tutorial</td>
<td>[https://colab.research.google.com/github/google/meridian/blob/main/demo/Meridian_Prior_Calibration_JAX.ipynb](https://colab.research.google.com/github/google/meridian/blob/main/demo/Meridian_Prior_Calibration_JAX.ipynb)</td>
<td>Runs a geo experiment analysis and feeds the lift into Meridian priors (JAX backend, v2.0). Lab counterpart to the PyMC-Marketing geo-lift calibration notebook, allowing a direct tool comparison.</td>
<td>lab / homework; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Meridian Tutorial: Building a National MMM for eCommerce</td>
<td>Cassandra (MMM vendor), YouTube, 2025, video tutorial</td>
<td>[https://www.youtube.com/watch?v=QJJtrMobx4I](https://www.youtube.com/watch?v=QJJtrMobx4I)</td>
<td>Code walkthrough of a national-level Meridian model for an e-commerce brand; same channel as the Python tutorial already in the generic guide. Use to contrast national vs geo modelling.</td>
<td>lab support video; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>MMM with PyMC-Marketing and Databricks (Corey Abshire, William Dean, Thomas Wiecki)</td>
<td>PyMC Labs YouTube channel, 23 Jan 2025, webinar recording (approx. 60 min)</td>
<td>[https://www.youtube.com/watch?v=_gM6YSMFF5M](https://www.youtube.com/watch?v=_gM6YSMFF5M)</td>
<td>Productionising PyMC-Marketing MMMs on Databricks (pipelines, model management, budget forecasting); agenda 5 min intro, 45 min talk/panel, 10 min Q&A. Shows how multi-market models are run at scale in companies.</td>
<td>optional viewing (MMM in production); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>PyMC-Marketing: Bayesian Approach to Marketing Data Science (webinar)</td>
<td>PyMC Labs YouTube channel, 2024, webinar recording</td>
<td>[https://www.youtube.com/watch?v=7a_HL5BRB-s](https://www.youtube.com/watch?v=7a_HL5BRB-s)</td>
<td>Overview of PyMC-Marketing's MMM and CLV modules by the developers; good introduction before the first lab (older API).</td>
<td>pre-class video; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Bolt's Evolution towards MMM with PyMC (Carlos Agostini)</td>
<td>PyMC Labs YouTube channel, 2023-2024, talk recording</td>
<td>[https://www.youtube.com/watch?v=djXoPq60bRM](https://www.youtube.com/watch?v=djXoPq60bRM)</td>
<td>Bolt (Estonian mobility platform active in many countries) on moving to Bayesian MMM with PyMC; companion blog bolt.eu 'Better budgeting with Bayesian models' (June 2024). European multi-market practitioner case.</td>
<td>case viewing (international practitioner); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>PyMC-Marketing Yearly Catch-up and New Use Cases (Niall Oulton, Carlos Agostini)</td>
<td>PyMC Labs YouTube channel, 2024, webinar recording</td>
<td>[https://www.youtube.com/watch?v=ikCK76gq65Q](https://www.youtube.com/watch?v=ikCK76gq65Q)</td>
<td>Developer update on new features and use cases. Useful to show the roadmap; pre-dates v1.0 multidimensional default.</td>
<td>optional viewing; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Bayesian Methods in Modern Marketing Analytics with Juan Orduz</td>
<td>PyMC Labs YouTube channel, 2023, talk recording</td>
<td>[https://www.youtube.com/watch?v=5QgiixYjmTM](https://www.youtube.com/watch?v=5QgiixYjmTM)</td>
<td>Juan Orduz on Bayesian MMM, calibration and causal inference in marketing; partly uses PyMC3-era code, so focus on concepts.</td>
<td>pre-class video (concepts); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>\[Webinar\] PyMC-Marketing vs. Google Meridian: A Scientific Benchmark for MMM</td>
<td>Luca Fiaschi, Teemu Säilynoja, Jake Piekarski (PyMC Labs), PyMC Discourse event page, autumn 2025, webinar</td>
<td>[https://discourse.pymc.io/t/webinar-pymc-marketing-vs-google-meridian-a-scientific-benchmark-for-mmm/17353](https://discourse.pymc.io/t/webinar-pymc-marketing-vs-google-meridian-a-scientific-benchmark-for-mmm/17353)</td>
<td>Webinar presenting the benchmark blog (speed, accuracy, scalability from start-up to enterprise data, when Meridian still fits). Page holds registration and blog link; check the PyMC Labs YouTube channel for the recording.</td>
<td>optional viewing with the benchmark blog; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>MMM Open-Source Showdown: A Practitioner's Benchmark of PyMC-Marketing vs. Google Meridian</td>
<td>Luca Fiaschi (PyMC Labs partner), PyData Boston 2025, conference talk</td>
<td>[https://pretalx.com/pydata-boston-2025/talk/XRQFLN](https://pretalx.com/pydata-boston-2025/talk/XRQFLN)</td>
<td>Benchmarks the two libraries on synthetic multi-geo data: speed (ESS/s), recovery of true channel contributions, convergence and memory, and ends with a playbook for choosing. The speaker is from PyMC Labs, so flag the vendor bias. No video or repo is linked on the page; look for a PyData YouTube upload.</td>
<td>Example in lecture or a lab extension (students replicate the comparison). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Hierarchical Models in MMM: Can Structure beat data size?</td>
<td>Mohamed Amine Jebari (Berlin), PyCon DE and PyData 2026, conference talk (15 Apr 2026) + GitHub repo</td>
<td>[https://pretalx.com/pyconde-pydata-2026/talk/EL7X8C/](https://pretalx.com/pyconde-pydata-2026/talk/EL7X8C/)</td>
<td>Shows a simple hierarchical PyMC/ArviZ MMM where partial pooling stabilises ROAS for sparse channels and countries; compares pooled, unpooled and partially pooled models and discusses when hierarchies fail. Code: github.com/MedAmineGBerry/tributary. Recording likely on the PyCon DE YouTube channel.</td>
<td>lab inspiration / homework (pooling across countries); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Marketing Media Mix Models with Python and PyMC: a Case Study</td>
<td>Emanuele Fabbiani (xtream), PyCon DE and PyData Berlin 2024, conference talk</td>
<td>[https://2024.pycon.de/program/D7AEQY/](https://2024.pycon.de/program/D7AEQY/)</td>
<td>Bayesian MMM built in PyMC for an Italian tour operator: challenges, insights, roadmap. European practitioner case; check PyCon DE YouTube for the recording.</td>
<td>case viewing; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Fortgeschrittenes Marketing Mix Modeling mit Metas Open-Source-Projekt Robyn</td>
<td>Meta Blueprint, 2023-2024, online course in German (1.3 h)</td>
<td>[https://www.facebookblueprint.com/student/path/264859](https://www.facebookblueprint.com/student/path/264859)</td>
<td>German version of Meta's official Robyn course: 4 lessons of 20 min (Einführung, Datensammlung und -exploration, Ausführung von Robyn, Kalibrierung, Modellaktualisierung und Budgetzuweisung), completion credential. Robyn docs warn some content may be outdated.</td>
<td>homework (German self-study before Robyn lab); free, Blueprint login likely</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Advanced marketing mix modeling using Meta Open Source project Robyn</td>
<td>Meta Blueprint, 2023-2024, online course in English (1.3 h)</td>
<td>[https://www.facebookblueprint.com/student/path/253121-marketing-mix-models](https://www.facebookblueprint.com/student/path/253121-marketing-mix-models)</td>
<td>English version of the official course (same 4 chapters). Only official Robyn training; no multi-market content.</td>
<td>homework (self-study); free, Blueprint login likely</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Robyn Python tutorial notebooks (tutorial1.ipynb, tutorial1_src.ipynb)</td>
<td>Meta Marketing Science, GitHub, 2024, notebook tutorials</td>
<td>[https://github.com/facebookexperimental/Robyn/tree/main/python/src/robyn/tutorials](https://github.com/facebookexperimental/Robyn/tree/main/python/src/robyn/tutorials)</td>
<td>End-to-end RobynPy notebooks on the bundled simulated data: one-click flow and module-by-module flow (clustering, one-pagers, allocator). Lets a Python-only class run all three tools; beta quality.</td>
<td>lab (Python alternative to demo.R); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Data Analytics for Marketing (Module 12: Media Mix Modeling with PyMC Marketing)</td>
<td>Packt, Coursera, 2025-2026, online course (13 modules; MMM module approx. 2 h)</td>
<td>[https://www.coursera.org/learn/packt-data-analytics-for-marketing](https://www.coursera.org/learn/packt-data-analytics-for-marketing)</td>
<td>Only MOOC found with a dedicated PyMC-Marketing MMM module (granularity, adstock, saturation, model selection, interpretation, assignment). No audit option; likely pre-1.0 API; no multi-country content.</td>
<td>optional self-study; paid (Coursera Plus subscription or course purchase; financial aid available)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>On-Demand: Modern MMM in Action (Meridian with Alaska Airlines)</td>
<td>Adswerve (Google partner), 2025-2026, on-demand webinar</td>
<td>[https://adswerve.com/webinars-videos/mmm-in-action](https://adswerve.com/webinars-videos/mmm-in-action)</td>
<td>Partner webinar on implementing Meridian for an airline (multi-region business) and turning results into budget decisions. Registration may be required; partner perspective.</td>
<td>optional case viewing; free (registration)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>MMM Explainer App (interactive adstock, saturation and priors)</td>
<td>PyMC-Marketing community, Streamlit, 2024-2025, interactive app</td>
<td>[https://pymc-marketing-app.streamlit.app/](https://pymc-marketing-app.streamlit.app/)</td>
<td>Browser app to play with adstock decay, saturation curves and Bayesian priors without code; linked from the official resources page. Ideal 10-minute warm-up before any of the three tools.</td>
<td>warm-up in class; free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Cases for Teaching (10)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Pernod Ricard: Uncorking Digital Transformation</td>
<td>Iavor Bojinov, Edward McFowland III, François Candelon, Nikolina Jonsson, Emer Moloney; Harvard Business School, 2024 (HBS 624-095), case, 24 pp.</td>
<td>[https://store.hbr.org/product/pernod-ricard-uncorking-digital-transformation/624095](https://store.hbr.org/product/pernod-ricard-uncorking-digital-transformation/624095)</td>
<td>French wine and spirits multinational. Centres on two AI programmes: Matrix, which optimises how ad spend is split across brands and markets, and D-STAR, a sales recommender. The decision is how to roll Matrix out to more markets and raise adoption where it already runs. Marketers resisted Matrix because it challenged their judgement. Works as an international case on the organisation and adoption side of MMM-based budget allocation; pair it with an open-source lab (Meridian or PyMC-Marketing). Proprietary tool, not one of the three open-source packages.</td>
<td>Case discussion (rolling out budget allocation across countries; resistance from local marketers). Paid: list price USD 11.95, educator price lower via HBP Education; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>BBVA Compass: Marketing Resource Allocation</td>
<td>Sunil Gupta, Joseph Davies-Gavin; Harvard Business School, 2011 (HBS 9-511-096, rev. 2012), case</td>
<td>[https://hbsp.harvard.edu/product/511096-PDF-ENG](https://hbsp.harvard.edu/product/511096-PDF-ENG)</td>
<td>US subsidiary of Spain's BBVA. In December 2010 the CMO must split a budget of under USD 50m between offline media (sponsorships such as the NBA, brand building) and online media (paid search, display), using funnel data. A classic allocation case to set up the question an MMM answers. Students can then rebuild the decision with a Robyn or PyMC-Marketing budget optimiser. MIT OCW 15.810 publishes discussion questions for it.</td>
<td>Case discussion before an MMM lab (from intuition to a model-based allocation). Paid: HBP, about USD 9-10 educator price; WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Advertising Experiments at the Ohio Art Company</td>
<td>Rajkumar Venkatesan, Paul W. Farris; Darden Business Publishing (UVA-M-0752), 2007/2017, case with teaching note; distributed via Emerald (DOI 10.1108/case.darden.2016.000012)</td>
<td>[https://www.emerald.com/insight/content/doi/10.1108/case.darden.2016.000012/full/html](https://www.emerald.com/insight/content/doi/10.1108/case.darden.2016.000012/full/html)</td>
<td>Two real advertising experiments by a toy maker, with the difficulties of executing them and the biases in field tests. Teaching note available. Use it to motivate calibrating an MMM with lift tests and geo experiments: Robyn calibration_input, Meridian ROI priors, PyMC-Marketing lift-test calibration. Pairs with the Darden note 'Designing Marketing Experiments' (M-0839).</td>
<td>Case discussion on causality and experiments as ground truth for MMM. Paid: Darden/Emerald; WU-Lizenz prüfen (Emerald case collections).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Measuring Price Promotion Effects: An Econometric Exercise in Measuring the Impact of Marketing Decision Making</td>
<td>Klaus Wertenbroch; INSEAD, 2006, distributed by Ivey Publishing (IN-S413, student spreadsheet IN-S415), short case/exercise, 2 pp.</td>
<td>[https://www.iveypublishing.ca/s/product/measuring-price-promotion-effects-an-econometric-exercise-in-measuring-the-impact-of-marketing-decision-making/01tOF000009xkFsYAI](https://www.iveypublishing.ca/s/product/measuring-price-promotion-effects-an-econometric-exercise-in-measuring-the-impact-of-marketing-decision-making/01tOF000009xkFsYAI)</td>
<td>A European business school exercise that turns scanner data into estimates of promotion effects, with a student spreadsheet. Good as a gentle regression warm-up before adstock and saturation are introduced. Ivey says registered educators get teaching notes free; it does not say whether this case has one.</td>
<td>Warm-up lab (OLS on sales data) before Bayesian MMM. Paid: about USD 10.50; free educator copy.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Building Marketing Mix Models with Google Pixel Data Using Meridian (Wharton AI & Analytics Accelerator)</td>
<td>Wharton AI & Analytics Accelerator with Google LLC, 2025, student project case study (web page)</td>
<td>[https://ai-analytics.wharton.upenn.edu/student-programs/analytics-accelerator/building-marketing-mix-models-with-google-pixel-data-using-meridian/](https://ai-analytics.wharton.upenn.edu/student-programs/analytics-accelerator/building-marketing-mix-models-with-google-pixel-data-using-meridian/)</td>
<td>A real student project on Meridian. Data: 2-3 years of anonymised, indexed daily US data on Pixel activations, spend and impressions across 20+ channels, plus branded and generic search queries. Lessons: tuning knots and priors improved fit; holdout tests struggled on the most recent periods; pooling regions (LA, New York) gave a more generalisable model. US only, but the region-pooling lesson carries straight over to multi-country models.</td>
<td>Template for a student project or capstone brief, and a discussion of a realistic project process. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Introduction to Meridian Demo (Meridian Getting Started notebook, Colab)</td>
<td>Google Meridian team, Google for Developers, 2025, Colab notebook / lab</td>
<td>[https://developers.google.com/meridian/notebook/meridian-getting-started](https://developers.google.com/meridian/notebook/meridian-getting-started)</td>
<td>End-to-end Meridian walkthrough on simulated geo-level weekly data. The data has a KPI (conversions), revenue per conversion, population, 5 paid channels with impressions and spend, one organic channel, a promotion and two controls. Steps: ROI priors, MCMC sampling (about 25 minutes on a T4 GPU), diagnostics (R-hat, fit), a two-page summary, budget optimisation, and the Scenario Planner. Colab: [https://colab.research.google.com/github/google/meridian/blob/main/demo/Meridian_Getting_Started.ipynb](https://colab.research.google.com/github/google/meridian/blob/main/demo/Meridian_Getting_Started.ipynb). Students can relabel the geos as countries for an international framing.</td>
<td>Hands-on lab (session 1 with Meridian); the geo hierarchy can be reframed as countries. Free; needs a Google account for Colab and a GPU runtime.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>MMM Multidimensional Example Notebook (one product, two countries, hierarchical pooling)</td>
<td>PyMC Labs / PyMC-Marketing documentation, 2025, Jupyter notebook / lab</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multidimensional_example.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_multidimensional_example.html)</td>
<td>Imagines one product sold in two countries (geo_a, geo_b). Uses 159 simulated weeks per geo (2022-2025), channels x1 (always on) and x2 (campaigns), and two event controls. Shows explicit pooling choices: partially pooled saturation beta, fully pooled lambda, unpooled adstock per geo and channel, geo-specific intercept and seasonality. Includes the budget optimiser wrapper. The most direct lab for 'one model, several markets'.</td>
<td>Core lab for the international session (pooled vs unpooled vs hierarchical across countries). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>MMM End-to-End Case Study (PyMC-Marketing)</td>
<td>PyMC Labs / PyMC-Marketing documentation, based on a PyData Global 2022 talk, Jupyter notebook / lab</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_case_study.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_case_study.html)</td>
<td>Weekly sales with 7 channels (direct mail, insert, newspaper, radio, TV, social, online display) and holidays; 183 training and 26 test weeks. Covers EDA, priors scaled by spend share, prior and posterior predictive checks, ROAS and saturation by channel, out-of-sample CRPS, and budget optimisation within ±50% of spend. The notebook reports about +10% sales in-sample but a negligible effect out of sample, which is a good discussion point about over-optimistic optimiser claims.</td>
<td>Lab or homework case (single market) before the multi-country notebook. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Robyn demo script (demo.R): simulated weekly data, calibration, allocator, refresh</td>
<td>Meta Marketing Science, Robyn GitHub repository (v3.12.x), R script / lab</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>Full Robyn workflow on dt_simulated_weekly (2016-2018). Prophet holidays cover 123 countries, and the demo sets prophet_country = 'DE', so it is easy to switch to AT or other markets. Steps: hyperparameter bounds, robyn_run (2,000 iterations x 5 trials), Pareto model selection, robyn_allocator (max_response and target_efficiency), robyn_refresh, robyn_response. Calibration with lift tests and reach-and-frequency curves is included but commented out. Ridge regression with Nevergrad search, not Bayesian, so a useful contrast to Meridian and PyMC-Marketing.</td>
<td>Lab (R): run one market, then rerun with another country's holiday calendar. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Tributary / 'Volta' synthetic case: hierarchical MMM across eight European markets with known ground truth</td>
<td>Mohamed Amine Jebari (TD Reply, Berlin); PyCon DE & PyData 2026 talk 'Hierarchical Models in MMM: Can Structure beat data size?' plus GitHub repo (MIT licence)</td>
<td>[https://github.com/MedAmineGBerry/tributary](https://github.com/MedAmineGBerry/tributary)</td>
<td>A fictional brand in eight European markets with deliberately unequal data: Germany and the UK about 2 years of good data, France 18 months, the Netherlands, Italy and Spain about 1 year (Spain with gaps), Poland and Sweden 6 months (sparse). A generator writes the data and a ground_truth.json, so students can check whether partial pooling recovers the true ROAS. Includes a walkthrough notebook with failure modes (groups too different, sparse data everywhere). Built in PyMC (not PyMC-Marketing). Talk page: [https://pycon.de/archive/2026/talks/hierarchical-models-in-mmm-can-structure-beat-data-size/](https://pycon.de/archive/2026/talks/hierarchical-models-in-mmm-can-structure-beat-data-size/). Small project (1 star), so check the code before class.</td>
<td>Ideal international lab or project: should small markets borrow strength from large ones? Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Praxisbeispiele (22)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Nürnberger Versicherung: funnel-aware Bayesian MMM cut cost per lead by 27%</td>
<td>PyMC Labs, 2026, client case study (web)</td>
<td>[https://www.pymc-labs.com/case-studies/nurnberger](https://www.pymc-labs.com/case-studies/nurnberger)</td>
<td>German insurer (Germany). Built with PyMC-Marketing plus custom extensions. Two-stage model: upper-funnel video and demand generation create demand that paid search converts. Uses a censored likelihood for budget-capped search and a joint optimiser over spend and caps to minimise cost per lead. Claims a cost per lead more than 27% lower over June to November, a production rollout, and an in-house team that now runs the model. Vendor claim.</td>
<td>Lecture example (DACH; funnel structure; capped channels). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>bonprix Germany achieves a 30% ROI through Meridian optimisation</td>
<td>e-dialog (Vienna-based digital agency, certified Meridian partner), 2026, agency success story</td>
<td>[https://e-dialog.group/en/success-story/bonprix-germany-achieves-a-30-roi-through-meridian-optimization-mmm/](https://e-dialog.group/en/success-story/bonprix-germany-achieves-a-30-roi-through-meridian-optimization-mmm/)</td>
<td>Otto Group fashion brand (Hamburg), German market. Meridian on 3 years of data from 40+ online and offline channels, consolidated into 13 variables; the model explains 88% of revenue. Used the built-in budget optimiser for scenarios. Claims +6.8% incremental revenue and +30% ROI. Agency/vendor claim, no independent check. Austrian agency, so a possible WU guest speaker.</td>
<td>Lecture example (DACH, Meridian in practice); guest speaker lead. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Better budgeting with Bayesian models: Bolt's story with PyMC-Marketing</td>
<td>Bolt (Estonian mobility platform), Bolt Tech Blog, 11 June 2024, engineering blog (about 10 min read); related talk 'Bolt's Evolution towards MMM with PyMC' (Carlos Agostini, video)</td>
<td>[https://bolt.eu/en/blog/budgeting-with-bayesian-models-pymc-marketing/](https://bolt.eu/en/blog/budgeting-with-bayesian-models-pymc-marketing/)</td>
<td>Bolt runs in many countries across Europe, Africa and Asia, and the PyMC-Marketing docs list it as the reference user. The Databricks blog (separate row) says Bolt models different markets with a shared structure. The blog body could not be extracted automatically, so check the details. Talk video: [https://youtu.be/djXoPq60bRM](https://youtu.be/djXoPq60bRM). A rare in-house example of switching to PyMC-Marketing at a multi-market company.</td>
<td>Lecture example or reading (in-house open-source MMM at a multi-country firm). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Revolutionizing Tech Marketing: The Synergy of PyMC and Databricks</td>
<td>Databricks blog, 26 Feb 2024, technical blog</td>
<td>[https://www.databricks.com/blog/revolutionizing-tech-marketing](https://www.databricks.com/blog/revolutionizing-tech-marketing)</td>
<td>Shows how to run PyMC-Marketing models per market in production, using one model structure per market scaled out with Python UDFs, MLflow, Unity Catalog and Workflows. Names Bolt and Shell as companies that need MMMs shared across the organisation. No performance results. Useful for the 'many countries = many models or one hierarchical model' discussion and for MLOps.</td>
<td>Example in lecture (scaling MMM across markets). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Marketing Media Mix Models with Python & PyMC: a Case Study (WeRoad, Italy)</td>
<td>Emanuele Fabbiani (xtream, Milan); PyCon DE & PyData Berlin 2024, conference talk with transcript and slides</td>
<td>[https://pycon.de/archive/2024/talks/marketing-media-mix-models-with-python-pymc-a-case-study/](https://pycon.de/archive/2024/talks/marketing-media-mix-models-with-python-pymc-a-case-study/)</td>
<td>Bayesian MMM for WeRoad, an Italian tour operator: online ads, social media and promotions driving new customers. Moves from attribution to contribution because of cookie loss. Covers adstock, saturation and expert priors; the talk reports error falling about 65% after adding saturation and a further 14% after priors. Synthetic data is shown. A Streamlit front end for marketers. Slides: [https://speakerdeck.com/donlelef/is-your-marketing-effective-let-bayes-decide](https://speakerdeck.com/donlelef/is-your-marketing-effective-let-bayes-decide)</td>
<td>Example or talk to watch (European SME, PyMC). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Bouygues Telecom (B&You): Meridian as base for an internal MMM platform</td>
<td>fifty-five (Paris), Oct 2025, agency case study</td>
<td>[https://resources.fifty-five.com/bouygues-telecom-meridian-mmm](https://resources.fifty-five.com/bouygues-telecom-meridian-mmm)</td>
<td>French telecom (France). Meridian chosen for simplicity, granularity and ease of use, and customised with price sensitivity and weekly updates. Used for strategic, tactical and operational decisions. No quantified results; more granular versions and other offers are planned. Agency source.</td>
<td>Lecture example (Meridian in an EU telecom; build vs buy). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Everything you need to know about Meridian (costs, timelines, alpha testers)</td>
<td>fifty-five Tea House, 2025, agency explainer</td>
<td>[https://fr.fifty-five.com/tea-house/everything-you-need-to-know-about-meridian](https://fr.fifty-five.com/tea-house/everything-you-need-to-know-about-meridian)</td>
<td>Gives rare practical numbers: about EUR 40-50k for Meridian setup, first results in a few weeks, and a claimed 5-15% media productivity gain for advertisers spending EUR 1-5m a year. Says two of the five 2024 alpha testers worked with fifty-five, and mentions a TotalEnergies case. Agency claims.</td>
<td>Example in lecture (business case for open-source MMM; cost discussion). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Alaska Airlines sees USD 100M revenue opportunity with Google's Meridian</td>
<td>Marketing Dive, 8 July 2025, trade press article (Alaska Airlines with Adswerve)</td>
<td>[https://www.marketingdive.com/news/alaska-airlines-100m-revenue-opportunity-google-meridian/752345/](https://www.marketingdive.com/news/alaska-airlines-100m-revenue-opportunity-google-meridian/752345/)</td>
<td>US airline. Adswerve ran a 3-month Meridian implementation covering TV, radio, out-of-home and digital, with Google Query Volume, seasonality and priors. The figures are projections, not realised revenue: up to USD 100m addressable revenue (+11%) and +3% ROI from optimisation. The client admits it is too early to know whether Meridian favours Google media. Good for discussing platform neutrality.</td>
<td>Example in lecture and discussion of vendor bias. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Meridian is now available to everyone (launch post; Finder case)</td>
<td>Google Ads & Commerce Blog, 29 Jan 2025, official announcement</td>
<td>[https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/](https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/)</td>
<td>Official general-availability post. Says Meridian was tested with hundreds of brands worldwide and launches a programme of 20+ certified partners. Finder (Australian, also in the UK, US and Canada) replaced in-house linear regression models with Meridian. Lists features: reach and frequency, experiments as priors, Google Query Volume. Vendor source.</td>
<td>Example in lecture (tool history; a multi-country brand). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Google Meridian: maximise ROI with MMM (Akulaku, Indonesia; NoBroker, India)</td>
<td>Think with Google APAC / Google Business, 2025, vendor case studies (with Analytic Edge)</td>
<td>[https://business.google.com/us/think/measurement/google-meridian-maximise-roi/](https://business.google.com/us/think/measurement/google-meridian-maximise-roi/)</td>
<td>Emerging-market examples. Akulaku (Indonesian fintech) moved from last-click to Meridian with Google Query Volume. Paid media reportedly drove about 75% of GMV; reallocation at the same budget suggested about +16% GMV; analysis took under 3 months. NoBroker (Indian property platform, regional page) redefined its KPI as owner contacts rather than transactions. Google and partner claims. Overlaps with the existing Think with Google 'growth engine' row, but this is a separate page with figures.</td>
<td>Example in lecture (emerging markets; KPI choice). Free; Google consent page may appear in the EU.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Meridian: the future of marketing mix modelling is now (Pandora early adopter)</td>
<td>Think with Google / Google Business (EMEA editions incl. DE: business.google.com/de/think/measurement/meridian-marketing-mix-modell/), 2025, vendor article with brand quote</td>
<td>[https://business.google.com/uk/think/measurement/meridian-marketing-mix-model/](https://business.google.com/uk/think/measurement/meridian-marketing-mix-model/)</td>
<td>Pandora, a Danish jewellery brand present in 70+ countries, was among the first testers. It began with Meridian in markets that had no other measurement solution, to compare ROI across channels (quote from its media planning specialist). Also explains geo-level modelling and Google Query Volume. A good hook for 'which markets get an MMM first?'. Vendor source, no numbers.</td>
<td>Example in lecture (rolling out measurement across countries). Free; German version available.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How Expedia Group redefined brand performance with Meridian</td>
<td>Aleksandra Coombes (Expedia Group), Think with Google / Google Business, 2025, brand-authored case article</td>
<td>[https://business.google.com/uk/think/measurement/brand-performance-measurement-marketing-mix-model/](https://business.google.com/uk/think/measurement/brand-performance-measurement-marketing-mix-model/)</td>
<td>Expedia replaced slow brand-tracking surveys with branded Google Search data as a brand-health signal inside Meridian, linking brand and performance. Whether the model covers several markets could not be confirmed from the excerpt. Vendor-hosted.</td>
<td>Example in lecture (brand vs performance; search data as mediator). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How measurement, not spend, can drive success for brands in Central and Eastern Europe</td>
<td>Jarosław Bednarczyk, Think with Google (EMEA), 2025, vendor opinion article</td>
<td>[https://business.google.com/en-all/think/measurement/how-measurement-drives-cee-growth/](https://business.google.com/en-all/think/measurement/how-measurement-drives-cee-growth/)</td>
<td>Regional CEE piece (Poland and neighbours). Argues that open-source MMM (Meridian) lets smaller CEE brands 'outsmart rather than outspend', and that MMM is privacy-safe because it uses aggregate data. Country-specific examples could not be verified. Relevant for Austria/CEE regional management.</td>
<td>Example in lecture or reading (CEE regional view). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How we increased ROI 7x with Google Meridian (AnalyticaHouse, Turkey)</td>
<td>AnalyticaHouse (Istanbul), Google Meridian partner, agency case study (also featured on Think with Google Turkey)</td>
<td>[https://analyticahouse.com/case-studies/analytica-house-google-meridian-mmm-case-study](https://analyticahouse.com/case-studies/analytica-house-google-meridian-mmm-case-study)</td>
<td>Turkish market. Meridian with BigQuery and marginal-ROI curves; quote from SuperStep Group's CDO. Claims 7x ROI, 6x faster analysis, +7% prediction accuracy and 'potential +360% revenue'. No baseline or time window is given. A textbook example of inflated vendor claims for students to critique.</td>
<td>Discussion exercise: critique a vendor MMM case study (emerging market). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How the travel industry can harness Robyn (four Spanish hotel chains)</td>
<td>Deloitte Spain, 13 July 2022, consulting study (English)</td>
<td>[https://www.deloitte.com/es/es/services/consulting/research/how-the-travel-industry-can-harness-robyn.html](https://www.deloitte.com/es/es/services/consulting/research/how-the-travel-industry-can-harness-robyn.html)</td>
<td>Robyn on weekly data (Oct 2018 to Sep 2021) for four Spanish hotel chains. Unusually transparent data sources: SimilarWeb, SEMrush, Meta, Google mobility and trends, Kantar and Infoadex TV, Eurostat and INE macro data. Claims R² of 81%, Meta at 16.8% of internet bookings with CPA below EUR 30 and not saturated, and +8.8% bookings from an optimised mix. Probably Meta-linked, so flag the bias. Good template for assembling European public data.</td>
<td>Example and data-sourcing template for a student project (EU/Eurostat data). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Marketing & Media Measurement Report: Robyn vs. Graphical Causal Model pilot with five international FMCG brands</td>
<td>Artefact in partnership with Meta, c. 2023, gated whitepaper</td>
<td>[https://www.artefact.com/ressource-document/ebook-marketing-media-measurement-report/](https://www.artefact.com/ressource-document/ebook-marketing-media-measurement-report/)</td>
<td>Pilot comparing Meta's Robyn with Artefact's Graphical Causal Model on five unnamed international FMCG brands, with guidance on where to start. Findings are behind a lead form (business email). Useful as a cross-brand model comparison, but it is co-authored by an agency and the platform.</td>
<td>Optional reading or example (model comparison); download needs registration.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Unilever Poland and Wittchen: measuring media performance with Robyn (Poland)</td>
<td>Meta for Business success stories, listed on the Robyn case-studies page, vendor case studies</td>
<td>[https://www.facebook.com/business/success/unilever-poland](https://www.facebook.com/business/success/unilever-poland)</td>
<td>Two Polish Robyn adopters listed by Meta: Unilever Poland measured media channel performance, and Wittchen (Polish leather goods retailer, [https://www.facebook.com/business/success/wittchen](https://www.facebook.com/business/success/wittchen)) sped up campaign analysis. The listing was verified on the Robyn site; the Facebook pages returned 404 to automatic fetching (they may need a browser or login). CEE examples of the same tool in a multinational subsidiary and a local brand. Vendor claims.</td>
<td>Example in lecture (CEE: multinational subsidiary vs local firm). Free; check in a browser.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Coppel: optimising advertising investment with Meta's Robyn (Mexico)</td>
<td>Meta for Business success story (Spanish, LatAm), listed on the Robyn case-studies page, vendor case study</td>
<td>[https://www.facebook.com/business/success/3-coppel?locale=es_LA](https://www.facebook.com/business/success/3-coppel?locale=es_LA)</td>
<td>Coppel, a large Mexican retailer, used Robyn to optimise ad investment. Listed on the official Robyn case-studies page; the page could not be fetched automatically, so check the results claimed. A Latin American emerging-market example.</td>
<td>Example in lecture (emerging markets, retail). Free; check in a browser.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Central Retail Corporation: in-house marketing mix modelling with Robyn (Thailand)</td>
<td>Meta for Business success story, listed on the Robyn case-studies page, vendor case study</td>
<td>[https://www.facebook.com/business/success/central-retail-corporation](https://www.facebook.com/business/success/central-retail-corporation)</td>
<td>Central Retail Corporation (Central Group, Thailand; also operates in Vietnam and Italy) ran an in-house MMM with Robyn. The existing guide row mentions this only in passing; this is the direct page. It could not be fetched automatically, so check the details in a browser.</td>
<td>Example in lecture (Asian retail conglomerate builds in-house). Free; check in a browser.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Macromill adds Meta's Robyn to its 'Brand Dynamics Modeling' MMM service (Japan)</td>
<td>Web Tan (Impress) news, 13 Nov 2024, Japanese-language trade news based on a Macromill press release</td>
<td>[https://webtan.impress.co.jp/n/2024/11/13/48125](https://webtan.impress.co.jp/n/2024/11/13/48125)</td>
<td>Japanese market research firm Macromill customised Robyn's open-source code and combined it with its own algorithm. The service models short-term sales effects and long-term branding effects through brand-metric mediators, using Meta Business Portfolio spend exports. Shows open-source MMM being localised by a research supplier in a non-Western market. Japanese only.</td>
<td>Short example (localisation; brand-building effects). Free (Japanese).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Marketing Mix Modeling mit Meridian und Robyn: Datenanforderungen und Kosten (German)</td>
<td>Blck Alpaca (Austrian social media agency), knowledge base article, German (Slovak version also available)</td>
<td>[https://blckalpaca.at/de/wissen/social-media/social-media-analytics-kpis-measurement/marketing-mix-modeling-meridian-robyn](https://blckalpaca.at/de/wissen/social-media/social-media-analytics-kpis-measurement/marketing-mix-modeling-meridian-robyn)</td>
<td>German-language practitioner view from an Austrian agency. Collects official guidance on data needs: per the Meridian docs, about 2 years of weekly data is too little and about 3 years gives only directional insight; Robyn needs at least 2 years weekly or 4-5 years if monthly. Gives rough cost ranges for managed, SaaS and in-house setups. Useful for Austrian SMEs and smaller CEE markets with short histories.</td>
<td>Reading or example (German; data sufficiency for small markets). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Can we use incrementality evidence from one country to calibrate an MMM in another?</td>
<td>Sellforte (Helsinki), 'Asked by Marketers' blog series, Aug 2026, vendor Q&A article</td>
<td>[https://sellforte.com/blog/asked-by-marketers/cross-country-incrementality-evidence-mmm](https://sellforte.com/blog/asked-by-marketers/cross-country-incrementality-evidence-mmm)</td>
<td>Directly addresses an international MMM problem: transferring lift-test priors across countries. Related Sellforte posts say to map each test to a model feature, allocate it with a defensible key, and shrink its influence when mapping is weak. Only the title was seen, so read the full article before using it. Vendor source.</td>
<td>Discussion prompt for the international session (cross-country priors in Meridian or PyMC). Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Software (25)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing 1.3.0 (Bayesian MMM, CLV, customer choice)</td>
<td>PyMC Labs; PyPI/GitHub; v1.3.0 released 22 Oct 2026; Apache-2.0; Python package</td>
<td>[https://pypi.org/project/pymc-marketing/](https://pypi.org/project/pymc-marketing/)</td>
<td>Current release of the core Python MMM library (about 1.3k GitHub stars). Requires Python 3.12+; install with pip install pymc-marketing (optional extras \[dag\], \[pie\]); a Dockerfile is in the repo. Modules: MMM with adstock, saturation, time-varying effects and out-of-sample forecasting; multidimensional (geo/market) MMM; budget optimizer; lift-test and ROAS calibration; CLV (BG/NBD, Pareto/NBD, Gamma-Gamma); customer choice (MVITS, discrete choice, MaxDiff, BLP). Repo: [https://github.com/pymc-labs/pymc-marketing](https://github.com/pymc-labs/pymc-marketing)</td>
<td>Main Python lab tool for Bayesian MMM; free, open licence</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing notebook: MMM Multidimensional Example (Geo-MMM)</td>
<td>PyMC Labs; pymc-marketing.io documentation; Jupyter notebook; Apache-2.0</td>
<td>[https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_multidimensional_example.html](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_multidimensional_example.html)</td>
<td>Worked example of a hierarchical geo-level MMM: MMM(..., dims=("geo",)) with partially pooled saturation beta across geos, pooled lam and unpooled adstock, per-geo scaling, prior predictive checks, NUTS fitting and diagnostics. Uses mmm_multidimensional_example.csv (2 geos, 159 weeks each, 2 channels). This is the template for a country-level (international) MMM.</td>
<td>Lab: build a multi-market MMM and discuss pooling across countries; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing notebooks: Lift-test calibration and geo-level lift calibration</td>
<td>PyMC Labs; pymc-marketing.io example gallery; Jupyter notebooks; Apache-2.0</td>
<td>[https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_geolift_calibration.html](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_geolift_calibration.html)</td>
<td>Shows how to calibrate an MMM with geo-level lift tests. Related notebooks in the same gallery: Introduction to Lift Test Calibration (mmm_lift_test.html), Calibrating an MMM with ROAS Estimates (mmm_roas_calibration.html), Mitigating Unobserved Confounders with Lift Test Likelihoods (mmm_roas.html), and How Much Would One Lift Test Reduce ROAS Uncertainty? (mmm_roas_experimentation.html).</td>
<td>Homework: combine experiment results with an MMM; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing notebooks: Budget allocation, risk assessment and multi-objective optimisation</td>
<td>PyMC Labs; pymc-marketing.io example gallery; Jupyter notebooks; Apache-2.0</td>
<td>[https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_budget_allocation_example.html](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_budget_allocation_example.html)</td>
<td>Budget optimizer workflow based on posterior response curves. The gallery also has Budget Allocation and Risk Assessment, Multi-Objective Optimization, Pareto Optimization Across Products with a Shared Media Budget, MMM + Bayesian VAR budget decision, and Halo and Cannibalisation Effects in Multi-Dimensional MMMs (mmm_halo.html), which fits spillovers across markets.</td>
<td>Lab: reallocate a budget across channels and markets; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing notebooks: time-varying parameters and geo-hierarchical splines</td>
<td>PyMC Labs; pymc-marketing.io example gallery; Jupyter notebooks; Apache-2.0</td>
<td>[https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_time_varying_media_example.html](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_time_varying_media_example.html)</td>
<td>Time-varying media effects (Gaussian-process based). Related: MMM with time-varying media baseline (mmm_tvp_example.html), Custom Geo-Hierarchical MMM with Splines (mmm_custom_splines.html), and Advanced Funnel-Aware MMM with geo-level mediation (mmm_funnel_mueffect_advanced.html).</td>
<td>Advanced lab or project: effects that change over time and differ by country; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Google Meridian 2.1.0 (google-meridian)</td>
<td>Google; PyPI/GitHub; v2.1.0 released 25 Sep 2026; Apache-2.0; Python package (TensorFlow Probability/JAX)</td>
<td>[https://pypi.org/project/google-meridian/](https://pypi.org/project/google-meridian/)</td>
<td>Google's official Bayesian MMM (about 1.6k GitHub stars). Use Python 3.11-3.13. Install with pip install google-meridian; extras: \[colab\], \[and-cuda\] (GPU), \[mlflow\], \[jax\], \[schema\], \[scenarioplanner\], \[geox\]. Features: hierarchical geo-level model (national models also possible), reach and frequency channels with optimal-frequency analysis, ROI priors and experiment calibration, organic and non-media treatments, budget optimisation, GPU-accelerated NUTS. It replaces LightweightMMM, which Google archived on 19 Jan 2026 and no longer supports. Repo: [https://github.com/google/meridian](https://github.com/google/meridian)</td>
<td>Main Python lab tool for geo-level (country/region) MMM; free, open licence; GPU optional (Colab)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Meridian Getting Started and Full-Funnel Colab notebooks</td>
<td>Google; GitHub google/meridian demo folder; Colab notebooks; Apache-2.0</td>
<td>[https://colab.sandbox.google.com/github/google/meridian/blob/main/demo/Meridian_Full_Funnel.ipynb](https://colab.sandbox.google.com/github/google/meridian/blob/main/demo/Meridian_Full_Funnel.ipynb)</td>
<td>Runnable Colab demos linked from the repo README. Getting Started: [https://developers.google.com/meridian/notebook/meridian-getting-started](https://developers.google.com/meridian/notebook/meridian-getting-started) (load simulated geo data, set priors, fit, model fit and ROI reports, optimise). Full-Funnel: upper- and lower-funnel KPIs. Students need no local install.</td>
<td>Lab session in Colab with no install; free (Google account for Colab)</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Meridian Scenario Planner (Looker Studio dashboards, open beta)</td>
<td>Google; Meridian scenarioplanner module (google-meridian\[scenarioplanner\]); launched Feb 2026, open beta Aug 2026; Apache-2.0 code, Looker Studio front end</td>
<td>[https://developers.google.com/meridian/reference/api/scenarioplanner](https://developers.google.com/meridian/reference/api/scenarioplanner)</td>
<td>Code-free planning interface on top of a trained Meridian model. A Colab notebook turns model output (MMM schema) into a shareable Looker Studio dashboard with three tabs: Analyze (fit, contributions), Plan (fixed or flexible budgets, per-channel spend limits) and Optimize (recommended shifts, response curves). Needs a trained model stored in Google Drive or GCS. Stand-alone reach-and-frequency optimisation specs are not supported yet. Coverage: [https://ppc.land/google-opens-meridian-scenario-planner-beta-with-per-channel-spend-constraints/](https://ppc.land/google-opens-meridian-scenario-planner-beta-with-per-channel-spend-constraints/)</td>
<td>Demo for managers: turn MMM output into budget scenarios; free with a Google account</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Meridian GeoX (meridian-geox): geo experiments for MMM calibration</td>
<td>Google; GitHub google/meridian-geox and PyPI; released 2026 (docs updated 28 Aug 2026); Apache-2.0; Python package (JAX)</td>
<td>[https://github.com/google/meridian-geox](https://github.com/google/meridian-geox)</td>
<td>Open-source library for designing and analysing geo experiments (holdback, go-dark, heavy-up; multi-cell designs with a shared control) using time-based regression. Its main purpose is calibrating Meridian. Install with pip install meridian-geox or pip install 'google-meridian\[meridian-geox\]'. Python 3.10+ (3.11+ with Meridian). Includes a Getting Started Colab and single- and multi-cell Colabs. Docs: [https://developers.google.com/meridian/geox/install-geox](https://developers.google.com/meridian/geox/install-geox)</td>
<td>Lab or project: design a regional test, then feed the lift into the MMM; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Robyn 3.12.1 (CRAN)</td>
<td>Meta Marketing Science; CRAN; v3.12.1 published 2 Jul 2025; MIT; R package</td>
<td>[https://cran.r-project.org/package=Robyn](https://cran.r-project.org/package=Robyn)</td>
<td>Meta's MMM: ridge regression, Nevergrad multi-objective hyperparameter search, Prophet decomposition, Pareto-front model selection with clustering, and a budget allocator. Requires R 4.0.0+; imports reticulate and prophet. Nevergrad (Python) must be set up once via reticulate (see demo/install_nevergrad.R). Install with install.packages("Robyn") or remotes::install_github("facebookexperimental/Robyn/R"). The GitHub repo has about 1.5k stars. A plumber-based Robyn API for Python has been in beta since Nov 2023.</td>
<td>Main R lab tool, good comparison with the Bayesian tools; free, open licence</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Robyn Python port (robynpy 0.3.6, beta)</td>
<td>Meta Marketing Science; PyPI robynpy and GitHub Robyn/python folder; v0.3.6 released 3 Apr 2025; MIT; Python package (beta)</td>
<td>[https://github.com/facebookexperimental/Robyn/tree/main/python](https://github.com/facebookexperimental/Robyn/tree/main/python)</td>
<td>Native object-oriented Python rewrite of Robyn R version 3.11.1. Still needs R plus the glmnet R package. Install with pip install robynpy (Python 3.8+). It is a beta and translation issues from R may remain. Note that the PyPI package 'robyn' is an unrelated web framework.</td>
<td>Optional for Python-only students; free. Warn students about beta status</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Robyn demo script (demo.R)</td>
<td>Meta Marketing Science; GitHub facebookexperimental/Robyn; R script; MIT</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>End-to-end walkthrough: loads dt_simulated_weekly and dt_prophet_holidays, sets prophet_country = "DE", defines paid media, organic and context variables, hyperparameters, calibration input, model selection and budget allocation. Changing the country code shows how holiday effects differ by country.</td>
<td>Step-by-step R lab script; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>siMMMulator: simulated data for MMM with known ground truth</td>
<td>Meta (facebookexperimental); GitHub; MIT; R package</td>
<td>[https://github.com/facebookexperimental/siMMMulator](https://github.com/facebookexperimental/siMMMulator)</td>
<td>Generates synthetic MMM datasets from scratch (baseline, channels, adstock, saturation, noise) with a known true ROI, so students can test whether Robyn, Meridian or PyMC-Marketing recover the truth. Has about 65 stars and no formal releases.</td>
<td>Homework: simulate several markets with different true ROIs and compare tools; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>AMSS: Aggregate Marketing System Simulator (R)</td>
<td>Google; GitHub google/amss; v1.0.1; Apache-2.0; R package; archived 7 Sep 2022</td>
<td>[https://github.com/google/amss](https://github.com/google/amss)</td>
<td>Simulates aggregate marketing time series with ground-truth metrics (Zhang and Vaver 2017). Archived and read-only, so use it only for illustration; siMMMulator or the Meridian simulated data are the maintained options.</td>
<td>Instructor background or optional simulation; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>GeoLift (R)</td>
<td>Meta (facebookincubator); GitHub; MIT; R package (R 4.0.0+); project status active</td>
<td>[https://github.com/facebookincubator/GeoLift](https://github.com/facebookincubator/GeoLift)</td>
<td>Geo experiments with augmented synthetic control: data-driven market selection, power calculators, multi-cell tests, commuting zones (vignettes). Gives lift estimates you can feed into Robyn calibration. Has about 271 stars.</td>
<td>Lab: pick test markets and estimate lift; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>CausalPy 0.9.0 (synthetic control, geo lift, DiD, ITS)</td>
<td>PyMC Labs; PyPI/GitHub; v0.9.0 released 28 Jul 2026 (1.0.0rc1 pre-release 6 Oct 2026); Apache-2.0; Python package</td>
<td>[https://github.com/pymc-labs/CausalPy](https://github.com/pymc-labs/CausalPy)</td>
<td>Bayesian (PyMC) and OLS quasi-experimental methods: synthetic control, geographical lift, difference-in-differences, interrupted time series. Python 3.12+. Install with pip install CausalPy or from conda-forge. Has about 1.2k stars. It pairs with PyMC-Marketing lift-test calibration.</td>
<td>Lab: estimate the lift of a country-level campaign; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>tfp-causalimpact (Python CausalImpact)</td>
<td>Google; GitHub google/tfp-causalimpact; Apache-2.0; Python package (TensorFlow Probability)</td>
<td>[https://github.com/google/tfp-causalimpact](https://github.com/google/tfp-causalimpact)</td>
<td>Python/TFP version of the Bayesian structural time-series CausalImpact method for the effect of an intervention on a time series. Install with pip install tfp-causalimpact; import causalimpact. The original R package is at [https://google.github.io/CausalImpact/](https://google.github.io/CausalImpact/).</td>
<td>Lab: effect of a market launch or campaign in one country; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Matched Markets / Time-Based Regression (TBR) for geo experiments</td>
<td>Google; GitHub google/matched_markets; Apache-2.0; Python; research code (not an official Google product)</td>
<td>[https://github.com/google/matched_markets](https://github.com/google/matched_markets)</td>
<td>Designs geo experiments with a greedy matched-markets search under budget and assignment constraints (TBRMM), and analyses them with time-based regression (Kerman 2017). Includes Colab design and post-analysis notebooks. Small (17 commits) and research-only.</td>
<td>Optional lab on geo-test design; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Uber Orbit 1.1.5.1 (Bayesian time series, KTR)</td>
<td>Uber; PyPI orbit-ml/GitHub uber/orbit; v1.1.5.1 released 22 May 2026; Apache-2.0; Python package</td>
<td>[https://github.com/uber/orbit](https://github.com/uber/orbit)</td>
<td>Bayesian forecasting with exponential smoothing (ETS/LGT/DLT) and Kernel Time-varying Regression (KTR), which Uber has used for time-varying-coefficient MMM (see arXiv 2106.03322). Python 3.12+. Install with pip install orbit-ml. Has about 2.1k stars.</td>
<td>Advanced option for time-varying effects; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Prophet 1.5.0</td>
<td>Meta; PyPI/CRAN; v1.5.0 released 5 Oct 2026; MIT; Python and R package</td>
<td>[https://pypi.org/project/prophet/](https://pypi.org/project/prophet/)</td>
<td>Decomposes trend, seasonality and holidays. Robyn uses it for baseline decomposition, and its country holiday support helps multi-country work. Python 3.10+.</td>
<td>Pre-processing: build trend, season and holiday controls per country; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Nevergrad 1.0.12</td>
<td>Meta Research; PyPI/GitHub facebookresearch/nevergrad; v1.0.12 released 23 Apr 2025; MIT; Python package</td>
<td>[https://pypi.org/project/nevergrad/](https://pypi.org/project/nevergrad/)</td>
<td>Gradient-free optimisation library that Robyn calls through reticulate for multi-objective hyperparameter search. Common install problem in class: point reticulate at a Python 3.8+ environment with nevergrad installed.</td>
<td>Needed for the Robyn lab; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>python-holidays 0.107 (holiday calendars for 250 country codes)</td>
<td>vacanza community; PyPI holidays; v0.107 released 19 Oct 2026; MIT; Python package</td>
<td>[https://pypi.org/project/holidays/](https://pypi.org/project/holidays/)</td>
<td>Generates national and subdivision (state/region) public holidays for about 250 country codes, with no download step. Use it for holiday dummies in country-level MMM controls with PyMC-Marketing or Meridian. Python 3.10+.</td>
<td>Lab: build holiday controls for each country in a multi-market panel; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>mmm_stan: Python/Stan multiplicative MMM with adstock, ROAS and mROAS</td>
<td>Sibyl He; GitHub sibylhe/mmm_stan; MIT; Python + Stan repo and notebook</td>
<td>[https://github.com/sibylhe/mmm_stan](https://github.com/sibylhe/mmm_stan)</td>
<td>Popular tutorial (about 403 stars) that implements the Google Jin et al. Bayesian MMM in Stan. Covers adstock, a multiplicative model, ROAS and marginal ROAS. Includes a 209-week retail dataset. Good for showing what the packages do under the hood.</td>
<td>Instructor or advanced students: from-scratch Bayesian MMM; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Mamimo: lightweight MMM utilities (scikit-learn style)</td>
<td>Robert Kübler (Garve); GitHub; licence not stated; Python package</td>
<td>[https://github.com/Garve/mamimo](https://github.com/Garve/mamimo)</td>
<td>Small library with saturation and carryover transformers and time features that fit into scikit-learn pipelines. Useful for a frequentist baseline next to the Bayesian tools. Has about 74 stars and no visible licence or recent releases, so treat it as a teaching illustration only.</td>
<td>Optional warm-up lab (pipeline with adstock and saturation); free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>MMM-Guide: Bayesian MMM worked example on a multi-region dataset</td>
<td>Mark Stent; GitHub markstent/MMM-Guide (fork of mark-allwyn/MMM-Guide); licence not stated; notebooks + FastAPI/Next.js dashboard</td>
<td>[https://github.com/markstent/MMM-Guide](https://github.com/markstent/MMM-Guide)</td>
<td>PyMC/ArviZ notebooks (additive and multiplicative MMM, Shapley decomposition, elasticity-based budget optimisation) using the Figshare multi-region eCommerce MMM dataset (conjura_mmm_data.csv plus data dictionary). Also contains a concept dashboard (MMMpact).</td>
<td>Template for a student project with real multi-region data; free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Data (16)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Data</td>
<td>Robyn dt_simulated_weekly</td>
<td>Meta Marketing Science; bundled in the Robyn R package (CRAN 3.12.1); MIT; simulated dataset</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>Weekly simulated data loaded with data("dt_simulated_weekly"). Variables: DATE, revenue; spend tv_S, ooh_S, print_S, facebook_S, search_S; exposures facebook_I, search_clicks_P; context competitor_sales_B, events; organic newsletter. The demo models 2016-01-01 to 2018-12-31.</td>
<td>Standard Robyn lab data; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Robyn dt_prophet_holidays (holiday table for 123 countries)</td>
<td>Meta Marketing Science; bundled in the Robyn R package; MIT; reference dataset</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>Holiday and event table covering 123 countries, used through prophet_country (for example "DE" or "AT"). You can add school breaks or local events, and you must add countries that are missing. This is the main hook for international adaptation in Robyn.</td>
<td>Lab: rerun the same model with AT, DE or CH holidays and compare baselines; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Meridian simulated geo datasets (geo_all_channels, geo_media, geo_media_rf, geo_full_funnel_data)</td>
<td>Google; GitHub google/meridian, meridian/data/simulated_data (csv, xlsx, pkl); Apache-2.0; simulated datasets</td>
<td>[https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv](https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv)</td>
<td>CSV files: geo_all_channels.csv (media, R&F, organic and non-media treatments), geo_media.csv, geo_media_rf.csv (reach and frequency channels), geo_full_funnel_data.csv and hypothetical_geo_all_channels.csv. They are multi-geo weekly panels with population, controls, KPI and revenue per KPI. Students can treat the geos as countries or regions. The same files are also provided as xlsx and pkl.</td>
<td>Meridian lab data for geo-hierarchical models; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Meridian simulated national datasets (national_all_channels, national_media, national_media_rf)</td>
<td>Google; GitHub google/meridian simulated_data/csv; Apache-2.0; simulated datasets</td>
<td>[https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv](https://github.com/google/meridian/tree/main/meridian/data/simulated_data/csv)</td>
<td>National-level (single market) versions of the simulated data, including reach and frequency. Good for contrasting national and geo models: how much precision do geos add?</td>
<td>Lab comparison of national and geo models; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>PyMC-Marketing mmm_multidimensional_example.csv (2-geo panel with true parameters)</td>
<td>PyMC Labs; GitHub pymc-marketing/data; Apache-2.0; simulated dataset</td>
<td>[https://github.com/pymc-labs/pymc-marketing/tree/main/data](https://github.com/pymc-labs/pymc-marketing/tree/main/data)</td>
<td>318 rows: 2 geos x 159 weeks (2022-06-06 to 2025-06-16), channels x1 (always-on) and x2 (tactical), controls event_1 and event_2, target y. The true parameters are in mmm_multidimensional_example_true_parameters.nc, so students can check whether the model recovers them. The folder also has multidimensional_mock_data.csv.</td>
<td>Lab data for the geo-MMM notebook and parameter-recovery exercise; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>PyMC-Marketing example data: mmm_example, mmm_roas_data, media_tvp_data, funnel_data, credibility_\* files</td>
<td>PyMC Labs; GitHub pymc-labs/pymc-marketing/data; Apache-2.0; simulated datasets</td>
<td>[https://github.com/pymc-labs/pymc-marketing/tree/main/data](https://github.com/pymc-labs/pymc-marketing/tree/main/data)</td>
<td>mmm_example.csv (quickstart MMM), mmm_roas_data.csv (ROAS calibration), media_tvp_data.csv (time-varying effects), funnel_data.csv (funnel mediation), credibility_\* files (campaign reach, audience overlap, ground-truth contributions) and fivetran_examples. The folder also holds CLV data (clv_quickstart.csv, cdnow_transactions.csv) and choice data.</td>
<td>Lab and homework data for every PyMC-Marketing notebook; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Multi-Region Marketing Mix Modeling (MMM) Dataset for Several eCommerce Brands (Conjura)</td>
<td>Conjura; figshare article 25314841; anonymised real-world dataset (licence on the figshare page, not checked)</td>
<td>[https://figshare.com/articles/dataset/Multi-Region_Marketing_Mix_Modeling_MMM_Dataset_for_Several_eCommerce_Brands/25314841](https://figshare.com/articles/dataset/Multi-Region_Marketing_Mix_Modeling_MMM_Dataset_for_Several_eCommerce_Brands/25314841)</td>
<td>Anonymised multi-region marketing and online purchase data for close to 100 eCommerce brands. Channels: Google, Meta, TikTok. Comes with a data dictionary and is intended for benchmarking CAC and ROAS estimation. Used in the MMM-Guide repo with weekly aggregation. One of the few free real-data, multi-region MMM sets. Check the licence and the regions covered before using it in class.</td>
<td>Project data for multi-region or international MMM with real spend; free download</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>mmm_stan retail dataset (209 weeks, 13 channels, macro controls)</td>
<td>Sibyl He; GitHub sibylhe/mmm_stan data.csv; MIT; semi-real anonymised dataset</td>
<td>[https://github.com/sibylhe/mmm_stan](https://github.com/sibylhe/mmm_stan)</td>
<td>209 weekly records with sales; impressions (mdip_) and spend (mdsp_) for 13 channels (TV, radio, SEM, email and others); controls for CPI, gas price, store count, markdowns, retail holidays and seasonality. Single market. Useful because it already contains macro controls such as CPI.</td>
<td>Homework: fit the same data in all three tools; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>World Bank World Development Indicators (WDI)</td>
<td>World Bank; Data Catalog; version 131, updated 9 Oct 2026; CC BY 4.0; statistical database and API</td>
<td>[https://datatopics.worldbank.org/world-development-indicators/](https://datatopics.worldbank.org/world-development-indicators/)</td>
<td>Over 1,500 annual indicators for more than 200 countries (1960-2025): GDP per capita (PPP), CPI inflation, population, internet users, mobile subscriptions. Access through the API or the R/Python packages wbstats and wbgapi. Use for country-level covariates and for scaling (population) in geo MMM.</td>
<td>Country controls for multi-country MMM projects; open licence</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>ITU ICT Statistics (internet use, mobile broadband, by country)</td>
<td>International Telecommunication Union (ITU-D); statistics portal; time series 2005-2025; Excel download</td>
<td>[https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx](https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx)</td>
<td>Free Excel series of individuals using the Internet (by sex, age, urban/rural), mobile phone ownership, and fixed and mobile broadband subscriptions and traffic. Useful for explaining cross-country differences in digital channel effectiveness. The page does not state reuse terms.</td>
<td>Country moderators for comparing digital ROI across markets; free download</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>ECB Data Portal: Exchange Rates (EXR)</td>
<td>European Central Bank; ECB Data Portal; daily, monthly and annual series; SDMX API; free reuse with source attribution</td>
<td>[https://data.ecb.europa.eu/data/datasets/EXR](https://data.ecb.europa.eu/data/datasets/EXR)</td>
<td>Euro reference exchange rates against about 30 currencies, daily and averaged by period. Needed to convert multi-country media spend and revenue into one currency (EUR) before pooling markets in an MMM. API: [https://data-api.ecb.europa.eu/](https://data-api.ecb.europa.eu/) (SDMX REST).</td>
<td>Data preparation: currency harmonisation for international panels; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat HICP monthly price index (prc_hicp_midx)</td>
<td>Eurostat; Eurostat data browser and API; monthly; free reuse with attribution</td>
<td>[https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_midx/default/table](https://ec.europa.eu/eurostat/databrowser/view/prc_hicp_midx/default/table)</td>
<td>Harmonised Index of Consumer Prices by EU/EEA country and COICOP category, monthly. Use it to deflate spend and sales, or as a price or inflation control in European multi-country MMM. Access through the eurostat R package or the Python eurostat package.</td>
<td>Country controls and deflation for EU market panels; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat: Internet use and e-commerce by individuals (isoc_ci_ifp_iu, isoc_ec_ib20)</td>
<td>Eurostat; ICT usage in households and by individuals survey; annual; free reuse with attribution</td>
<td>[https://ec.europa.eu/eurostat/databrowser/view/isoc_ci_ifp_iu/default/table](https://ec.europa.eu/eurostat/databrowser/view/isoc_ci_ifp_iu/default/table)</td>
<td>Annual country-level shares of internet users and online shoppers in EU countries. Use them as moderators of digital channel effects across European markets, or to explain why pooled priors differ by country.</td>
<td>Project: explain country differences in channel ROI; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>OECD Data Explorer (CPI, consumer confidence, GDP, PPPs)</td>
<td>OECD; OECD Data Explorer; SDMX API; monthly, quarterly and annual; free reuse (OECD terms)</td>
<td>[https://data-explorer.oecd.org/](https://data-explorer.oecd.org/)</td>
<td>Monthly consumer confidence (CCI), CPI, unemployment, quarterly GDP and PPP conversion factors for OECD and partner countries. Higher frequency than WDI, so better suited to weekly or monthly MMM controls after interpolation.</td>
<td>Macro controls for multi-country MMM; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Google Trends (search interest by country and region)</td>
<td>Google; Google Trends web interface (CSV export); free; index data (0-100)</td>
<td>[https://trends.google.com/trends/](https://trends.google.com/trends/)</td>
<td>Weekly search interest for brand or category terms by country and subregion. Use it as a demand or brand-interest proxy or a competitive control in MMM. Values are relative indices, and samples can change between downloads.</td>
<td>Homework: build a brand-search control for each market; free</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Nager.Date public holiday API</td>
<td>Nager (open-source project); REST API and GitHub nager/Nager.Date; free; holiday data</td>
<td>[https://date.nager.at/](https://date.nager.at/)</td>
<td>Free JSON API for public holidays across many countries, with no API key. An alternative to python-holidays and Robyn's dt_prophet_holidays for building holiday dummies in R or Python. The URL currently redirects to nagerholidays.com.</td>
<td>Data preparation: holiday calendars for each market; free</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Statistische Methoden (26)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Geometric adstock (carryover decay)</td>
<td>Broadbent, S. (1979), J. Market Research Society; tool docs (PyMC-Marketing, Meridian, Robyn)</td>
<td>[https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.components.adstock.html](https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.components.adstock.html)</td>
<td>Ad effect decays by constant rate per period. PyMC-Marketing GeometricAdstock(l_max=..., alpha prior; half-life option); Meridian default adstock_decay_spec='geometric' with max_lag; Robyn adstock='geometric' (theta). Pitfall: l_max/max_lag truncation and decay bounds drive ROI; theta ranges differ by medium.</td>
<td>Lecture 2 (MMM building blocks); spreadsheet exercise computing adstock by hand; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Weibull adstock (CDF/PDF, delayed peak)</td>
<td>Robyn docs; Zhou, Lares et al. (Meta)</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/features](https://facebookexperimental.github.io/Robyn/docs/features)</td>
<td>Flexible time-varying decay; PDF variant allows lagged peak. Robyn adstock='weibull_cdf'/'weibull_pdf' (shape, scale); PyMC-Marketing WeibullCDFAdstock/WeibullPDFAdstock (kernel length fix in 1.3.0). Pitfall: needs more iterations, overfits short series.</td>
<td>Lab: compare geometric vs Weibull fit in Robyn on demo data; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Delayed / binomial adstock</td>
<td>Jin et al. (2017) Google; Meridian 1.2.0 changelog</td>
<td>[https://github.com/google/meridian/blob/main/CHANGELOG.md](https://github.com/google/meridian/blob/main/CHANGELOG.md)</td>
<td>Delayed adstock with peak lag (PyMC-Marketing DelayedAdstock); binomial decay (Meridian adstock_decay_spec='binomial', PyMC-Marketing BinomialAdstock). Pitfall: peak lag weakly identified without strong flighting variation.</td>
<td>Lecture slot on TV vs digital carryover; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Hill saturation (diminishing returns)</td>
<td>Jin, Wang, Sun, Chan & Koehler (2017), Google Research</td>
<td>[https://research.google/pubs/pub46001/](https://research.google/pubs/pub46001/)</td>
<td>S-shaped response with half-saturation (ec/gamma) and slope/alpha. Meridian Hill(ec, slope), hill_before_adstock flag; Robyn Hill (alpha, gamma); PyMC-Marketing HillSaturation/HillSaturationSigmoid. Pitfall: saturation is poorly identified without spend variation; geo data helps.</td>
<td>Lecture 2; interactive response-curve plotting exercise; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Logistic / Michaelis-Menten / tanh saturation</td>
<td>PyMC-Marketing docs (PyMC Labs)</td>
<td>[https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.components.saturation.html](https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.components.saturation.html)</td>
<td>Alternative concave curves: LogisticSaturation (default in many PyMC-Marketing examples), MichaelisMentenSaturation, TanhSaturation. Pitfall: different curves yield different marginal ROI at the same fit; compare with LOO.</td>
<td>Advanced lab: swap saturation classes, compare mROAS; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Bayesian MMM with carryover and shape effects</td>
<td>Jin, Y., Wang, Y., Sun, Y., Chan, D., Koehler, J. (2017), Google Inc. technical report</td>
<td>[https://research.google/pubs/pub46001/](https://research.google/pubs/pub46001/)</td>
<td>Foundational Bayesian MMM paper (priors, ROAS/mROAS from posterior); basis for LightweightMMM and Meridian. Pitfall: priors dominate in small samples (paper's own finding).</td>
<td>Core reading week 1-2; free PDF.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Hierarchical Bayesian partial pooling across geos/countries</td>
<td>Sun, Y., Wang, Y., Jin, Y., Chan, D., Koehler, J. (2017), 'Geo-level Bayesian Hierarchical Media Mix Modeling', Google</td>
<td>[https://research.google/pubs/pub46000/](https://research.google/pubs/pub46000/)</td>
<td>Geo coefficients drawn around a national mean; tighter intervals than national models. Meridian built-in (eta_m, xi_c; media_effects_dist); PyMC-Marketing via dims=('geo',) and Prior(..., dims=('channel','geo'), centered=False). Robyn: not supported. Pitfall: pooling countries with different KPI definitions or currencies.</td>
<td>Lecture on international MMM; lab: DACH panel with AT as small geo; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Population scaling / per-capita modelling</td>
<td>Meridian input-data docs (Google)</td>
<td>[https://developers.google.com/meridian/docs/basics/input-data](https://developers.google.com/meridian/docs/basics/input-data)</td>
<td>Meridian requires geo population and scales KPI and media per capita; control_population_scaling_id for controls; 2.1.0 ModelSpec population scaling. PyMC-Marketing: scaling argument (per-geo max-abs). Pitfall: per-capita ignores purchasing power differences.</td>
<td>Exercise: compute per-capita spend for EU countries; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>ROI / mROI prior parameterisation</td>
<td>Wurm, M., Price, B., Liu, Y. (2024), 'Media Mix Model Calibration With Bayesian Priors', Google Research</td>
<td>[https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/](https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/)</td>
<td>Reparameterise model so ROI is a parameter; set LogNormal priors from experiments/benchmarks. Meridian media_prior_type='roi'\|'mroi'\|'contribution'\|'coefficient', roi_m/roi_rf, lognormal_dist_from_range; PyMC-Marketing add_cost_per_target_calibration. Pitfall: too-tight priors become the answer; check prior-posterior shift.</td>
<td>Lecture on priors; elicitation exercise with country managers' beliefs; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Lift-test / experiment calibration</td>
<td>PyMC-Marketing lift-test notebook; Robyn calibration docs; Meridian CalibrationBuilder</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_lift_test.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_lift_test.html)</td>
<td>PyMC-Marketing add_lift_test_measurements (channel, x, delta_x, delta_y, sigma) as observations of saturation curve; Robyn calibration_input + MAPE.LIFT objective; Meridian experiments -\> ROI priors (CalibrationBuilder, GeoX). Pitfall: estimand mismatch (experiment counterfactual vs MMM zero-spend baseline), spend mismatch (Robyn: within 10%).</td>
<td>Lab: calibrate model with a synthetic lift test; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Ridge regression + Nevergrad multi-objective hyperparameter search</td>
<td>Runge, J., Skokan, I., Zhou, G., Pauwels, K. (2024), arXiv:2403.14674</td>
<td>[https://arxiv.org/abs/2403.14674](https://arxiv.org/abs/2403.14674)</td>
<td>Robyn: glmnet ridge for coefficients; Nevergrad TwoPointsDE searches adstock/saturation/lambda/train_size; robyn_run(iterations, trials). Pitfall: many equally good models; results vary by seed and analyst choice.</td>
<td>Lecture on frequentist vs Bayesian MMM; Robyn demo lab; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>DECOMP.RSSD and Pareto-front model selection</td>
<td>Robyn features docs (Meta)</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/features](https://facebookexperimental.github.io/Robyn/docs/features)</td>
<td>Decomposition root-sum-squared distance between spend shares and effect shares; minimised jointly with NRMSE (and MAPE.LIFT); Pareto front then k-means clusters; objective_weights. Pitfall: penalises true outliers (very efficient small channels) — a business prior, not a statistical truth.</td>
<td>Discussion: is RSSD a sensible assumption in a new market?; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Prophet time-series decomposition</td>
<td>Taylor, S. J., Letham, B. (2018), 'Forecasting at Scale', The American Statistician 72(1)</td>
<td>[https://doi.org/10.1080/00031305.2017.1380080](https://doi.org/10.1080/00031305.2017.1380080)</td>
<td>Robyn prophet_vars (trend, season, monthly, weekday, holiday), prophet_country with bundled holidays (123 countries). Pitfall: prophet trend can absorb media effects; two-stage approach ignores uncertainty.</td>
<td>Lab: inspect Robyn decomposition for AT vs DE holidays; paper paid, preprint free (PeerJ).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Fourier seasonality</td>
<td>Harvey (1990); PyMC-Marketing fourier module</td>
<td>[https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html](https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html)</td>
<td>PyMC-Marketing yearly_seasonality=n Fourier modes (gamma_fourier priors, per-geo dims). Pitfall: too many modes overfit; hemisphere differences across countries.</td>
<td>Short lecture block; free docs.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Time-varying intercept via knots (Meridian AKS)</td>
<td>Meridian docs: setting knots</td>
<td>[https://developers.google.com/meridian/docs/advanced-modeling/setting-knots](https://developers.google.com/meridian/docs/advanced-modeling/setting-knots)</td>
<td>Baseline interpolated between knots (knots argument); automatic knot selection (enable_aks, AIC since 1.2.1). Pitfall: one knot per period saturates national models.</td>
<td>Lab: vary knots and observe ROI shifts; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Gaussian-process (HSGP) time-varying coefficients</td>
<td>Riutort-Mayol, G., et al. (2023), 'Practical Hilbert space approximate Bayesian Gaussian processes', Statistics and Computing 33</td>
<td>[https://doi.org/10.1007/s11222-022-10167-2](https://doi.org/10.1007/s11222-022-10167-2)</td>
<td>PyMC-Marketing time_varying_intercept / time_varying_media with HSGP config; composable HSGP terms (1.3.0). Not in Meridian (media) or Robyn. Pitfall: confounds with trend; needs priors on lengthscale.</td>
<td>Advanced seminar; open access paper.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Reach & frequency modelling</td>
<td>Zhang, Y., Wurm, M., Liu, Y., et al. (2023), 'Bayesian Hierarchical Media Mix Model Incorporating Reach and Frequency Data', Google</td>
<td>[https://research.google/pubs/bayesian-hierarchical-media-mix-model-incorporating-reach-and-frequency-data/](https://research.google/pubs/bayesian-hierarchical-media-mix-model-incorporating-reach-and-frequency-data/)</td>
<td>Effect = reach x Hill(frequency), adstocked; Meridian native R&F inputs and optimal_freq(); Robyn curve calibrator (beta). Pitfall: R&F availability differs by country/platform.</td>
<td>Lecture on frequency planning for YouTube/Meta campaigns; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Geo experiments / synthetic control (GeoLift)</td>
<td>Meta Open Source, GeoLift (R package); Abadie, Diamond & Hainmueller (2010) JASA synthetic control</td>
<td>[https://github.com/facebookincubator/GeoLift](https://github.com/facebookincubator/GeoLift)</td>
<td>Market selection, power analysis and inference for geo tests via synthetic control (augsynth); output feeds Robyn calibration_input. Pitfall: few comparable regions in small countries.</td>
<td>Lab: design a GeoLift test across Austrian regions; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Matched markets / trimmed match geo experiments (GeoX)</td>
<td>Chen, A., Au, T. C. (2022), 'Robust causal inference for incremental return on ad spend with randomized paired geo experiments', Annals of Applied Statistics 16(1)</td>
<td>[https://doi.org/10.1214/21-AOAS1493](https://doi.org/10.1214/21-AOAS1493)</td>
<td>Google's trimmed match underpins GeoX; Meridian 2.0 imports GeoX results as priors (with_meridian_geox_experiment_result, \[geox\] extra). Pitfall: requires many geos; often infeasible for single small countries.</td>
<td>Lecture on incrementality testing; paper paid (arXiv preprint free).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Budget optimisation with response curves</td>
<td>Tool docs: Meridian BudgetOptimizer, PyMC-Marketing BudgetOptimizer, Robyn robyn_allocator</td>
<td>[https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_budget_allocation_example.html](https://www.pymc-marketing.io/en/latest/notebooks/mmm/mmm_budget_allocation_example.html)</td>
<td>Equalise marginal ROI under constraints. PyMC-Marketing SLSQP with budget_bounds per channel x geo; Meridian optimize(fixed_budget, target_roi/target_mroi, spend_constraint_lower/upper); Robyn max_response / target_efficiency with channel_constr_low/up. Pitfall: extrapolating beyond observed spend ranges; ignoring uncertainty.</td>
<td>Case exercise: allocate a DACH budget; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Posterior predictive checks & MCMC diagnostics</td>
<td>Gelman, A., et al. (2013), Bayesian Data Analysis, 3rd ed., CRC; ArviZ</td>
<td>[https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html](https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html)</td>
<td>sample_posterior_predictive (PyMC-Marketing), R-hat/PPP check/ModelReviewer (Meridian). Not applicable to Robyn. Pitfall: good in-sample fit does not imply causal validity.</td>
<td>Lab checkpoint after every fit; BDA free PDF on author site.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Causal DAG thinking in MMM</td>
<td>Pearl (2009) Causality; PyMC-Marketing dag / treatment_nodes / outcome_node</td>
<td>[https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html](https://www.pymc-marketing.io/en/latest/api/generated/pymc_marketing.mmm.mmm.MMM.html)</td>
<td>Use DAG to choose controls (confounders vs mediators); PyMC-Marketing supports DAG-based identification and pm.do interventions; Meridian distinguishes controls vs treatments. Pitfall: controlling for mediators (e.g. branded search) removes media effect.</td>
<td>Workshop: draw DAG for a multi-country FMCG brand; free docs.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Out-of-sample / time-series validation</td>
<td>Robyn ts_validation; Meridian holdout_id</td>
<td>[https://facebookexperimental.github.io/Robyn/docs/features](https://facebookexperimental.github.io/Robyn/docs/features)</td>
<td>Robyn train/val/test split with NRMSE on test; Meridian holdout_id / ModelSpec holdouts; PyMC-Marketing out-of-sample prediction. Pitfall: fit-based validation does not validate causal ROI; combine with experiments.</td>
<td>Lab: hold out last 13 weeks per country; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Model refresh</td>
<td>Robyn robyn_refresh docs/demo</td>
<td>[https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R](https://github.com/facebookexperimental/Robyn/blob/main/demo/demo.R)</td>
<td>robyn_refresh() for incremental updates (\<=50% new data); Bayesian tools refit with previous posterior as prior (manual). Pitfall: refresh drift, inconsistent specs across countries.</td>
<td>Discussion of governance for multi-market MMM programmes; free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Currency / PPP normalisation for multi-country spend</td>
<td>OECD/Eurostat PPP statistics; World Bank ICP</td>
<td>[https://www.oecd.org/en/data/indicators/purchasing-power-parities-ppp.html](https://www.oecd.org/en/data/indicators/purchasing-power-parities-ppp.html)</td>
<td>Convert local spend/revenue to a common currency (fixed or period-average FX) and optionally PPP before pooling countries; none of the three tools does this automatically (Meridian only labels currency_code). Pitfall: FX swings create artificial spend variation; PPP vs market FX change efficiency rankings.</td>
<td>Exercise: convert CEE spend to EUR and PPP, rerun pooled model; free data.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Lightweight / packaging perspective on MMM adoption</td>
<td>Runge, Skokan, Zhou, Pauwels (2024) arXiv; Chan & Perry (2017) 'Challenges and Opportunities in Media Mix Modeling', Google</td>
<td>[https://research.google/pubs/pub45998/](https://research.google/pubs/pub45998/)</td>
<td>Critical overview of MMM limitations (data, selection bias, endogeneity). Pitfall: treating tool output as truth.</td>
<td>Opening lecture reading; free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Communities & Events (8)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Google Meridian Discord and GitHub Discussions</td>
<td>Google Meridian team; Discord server plus GitHub Q&A; official tool community</td>
<td>[https://developers.google.com/meridian/support](https://developers.google.com/meridian/support)</td>
<td>Official support channels: Discord for real-time discussion and peer learning with Meridian experts (discord.gg/PU7Prfjc8U), GitHub Discussions Q&A for troubleshooting, pull requests for bugs and features, plus a Meridian newsletter. English.</td>
<td>Students join Discord (free account) to read and ask questions during a Meridian lab; GitHub Q&A readable without login.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>PyMC-Marketing GitHub Discussions</td>
<td>PyMC Labs and contributors; GitHub; official tool community</td>
<td>[https://github.com/pymc-labs/pymc-marketing/discussions](https://github.com/pymc-labs/pymc-marketing/discussions)</td>
<td>Q&A and ideas forum of the library, linked from the README alongside PyMC Discourse, the Bayesian Discord and MMM Hub Slack; maintainers answer questions on multidimensional (multi-market) MMM, priors and budget optimisation. English.</td>
<td>Read without login, post with a GitHub account; students search solved threads during assignments.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Measure Slack (Measure Chat)</td>
<td>Founded by Lee Isensee, volunteer admins; Slack; practitioner community</td>
<td>[https://thehiveindex.com/communities/measure-chat/](https://thehiveindex.com/communities/measure-chat/)</td>
<td>Free Slack community for digital and marketing analytics since 2014/2015, roughly 15,000-25,000 members; channels on analytics tools, measurement and conferences; complements MMM Hub for attribution vs MMM debates. English.</td>
<td>Free sign-up; students follow measurement discussions and can ask practitioners; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna Data Science Group (VDSG)</td>
<td>Non-profit association in Wien (headed by Wolfgang Weidinger per published author bios); Meetup plus own events; local data science community</td>
<td>[https://vdsg.at/](https://vdsg.at/)</td>
<td>Volunteer community since 2015 with 5,000+ Meetup members and 130+ public events (ML, analytics, data engineering); co-organised a Data Analytics in Business Jamboree with CEU (2025). No MMM-specific event found, so an opening for a practitioner or student MMM talk. English, German.</td>
<td>Students RSVP free on Meetup; possible venue to present course projects on open-source MMM; on site Vienna.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>PyCon Austria</td>
<td>Volunteer, non-profit Python conference; Eisenstadt (FH Burgenland); conference</td>
<td>[https://pycon.at/](https://pycon.at/)</td>
<td>Annual free Python conference in Austria (2025 and 2026 held; next 11-12 April 2027 in Eisenstadt); call for speakers via Sessionize, talks mainly English with German allowed. Good stage for PyMC-Marketing or Meridian talks with an Austrian audience.</td>
<td>Students attend free; teams could submit a talk on a multi-market MMM project; about one hour from Vienna.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna\<-R user group</td>
<td>Vienna R community on Meetup (named with VDSG and Vienna Deep Learning Meetup as the main Vienna data groups); local community</td>
<td>[https://www.r-bloggers.com/2022/09/financial-industry-supports-robust-vienna-r-community/](https://www.r-bloggers.com/2022/09/financial-industry-supports-robust-vienna-r-community/)</td>
<td>Local R community, relevant for Robyn (an R package); talks and networking with Vienna R users from finance and industry. English, German.</td>
<td>Join via Meetup; suggest an R/Robyn lightning talk by students; on site Vienna.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>MMA Global (Marketing + Media Alliance)</td>
<td>Global trade association of marketers; events, think tanks, speaker network; industry community</td>
<td>[https://mmaglobal.com/](https://mmaglobal.com/)</td>
<td>Runs marketing effectiveness and measurement initiatives with brands, agencies and research firms across regions; its speaker profiles (e.g. Kantar analytics leads) are a source of MMM practitioners. English.</td>
<td>Use speaker lists to find guest speakers; some content needs membership login.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>MARKETING X and Tag des Marketing (Austrian Marketing Confederation)</td>
<td>Austrian marketing conferences in Wien; industry events</td>
<td>[https://www.unternehmerweb.at/?p=27294](https://www.unternehmerweb.at/?p=27294)</td>
<td>MARKETING X (Novotel Wien Hauptbahnhof, Oct 2025, 60 speakers incl. ÖBB and WPP Media) and the Tag des Marketing of the Austrian Marketing Confederation are the main Austrian marketing practitioner stages; no MMM session found in the 2024/2025 programmes, so measurement is a gap there. German.</td>
<td>Students attend to network with Austrian marketers and scout DACH guest speakers; German.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### People (22)
<table fit-page-width="true" header-row="true">
<tr>
<td>Kategorie</td>
<td>Titel / Name</td>
<td>Autor / Quelle / Firma</td>
<td>Link</td>
<td>Notiz</td>
<td>Verwendung im Kurs</td>
<td>Status</td>
</tr>
<tr>
<td>People</td>
<td>Gufeng Zhou</td>
<td>Meta Marketing Science, Robyn creator and core team; Global; practitioner</td>
<td>[https://cran.r-project.org/web/packages/Robyn/index.html](https://cran.r-project.org/web/packages/Robyn/index.html)</td>
<td>Lead author of Meta's open-source R package Robyn (ridge regression, Nevergrad hyperparameter search, calibration with lift tests, budget allocator); co-author of 'Packaging Up Media Mix Modeling: An Introduction to Robyn's Open-Source Approach' (Runge, Skokan, Zhou, Pauwels, arXiv 2024/2025) and of a survey of MMM providers. Updated tool-specific row (already in the earlier MMM guide). English.</td>
<td>Remote guest talk or recorded interview on the design choices behind Robyn and how Meta supports advertisers across markets; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Bernardo Lares</td>
<td>Robyn maintainer (CRAN maintainer, Meta Robyn core team), Madrid; Global; practitioner</td>
<td>[https://github.com/laresbernardo](https://github.com/laresbernardo)</td>
<td>Listed as CRAN maintainer of Robyn 3.12.1 (July 2025) and as member of the Robyn core team at community events; also author of the R package lares. Good contact for practical questions on running Robyn, release roadmap and the Python port. English, Spanish.</td>
<td>Remote Q&A for an R lab session with Robyn; European time zone fits the Vienna schedule; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Igor Skokan and Leonel Sentana</td>
<td>Meta Marketing Science (Robyn co-authors); Global; practitioners</td>
<td>[https://arxiv.org/abs/2403.14674](https://arxiv.org/abs/2403.14674)</td>
<td>Both listed as Robyn authors on CRAN; Skokan co-authored the Robyn introduction paper with Julian Runge, Gufeng Zhou and Koen Pauwels and the MMM-provider survey. Meta Marketing Science works with advertisers in many countries (e.g. regional Marketing Science partner roles for CEE), useful for the multi-market angle. English.</td>
<td>Remote session on calibrating Robyn with Conversion Lift and geo experiments; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Yuxue Jin</td>
<td>Google (Research / ads measurement), co-author of the Google MMM papers behind Meridian; Global; practitioner-researcher</td>
<td>[https://research.google/people/104888/](https://research.google/people/104888/)</td>
<td>Co-author of 'Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects' (2017), 'Geo-level Bayesian Hierarchical Media Mix Modeling' (2017), 'A Hierarchical Bayesian Approach to Improve Media Mix Models Using Category Data' (2017) and 'Bias Correction for Paid Search in Media Mix Modeling' (2018); cited by PyMC-Marketing and the basis of Meridian's geo-hierarchical design. English.</td>
<td>Papers as core readings; the geo-level model is a direct template for multi-country (country-as-geo) MMM; use as reading rather than speaker.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Jim Koehler, David Chan, Yunting Sun, Yueqing Wang</td>
<td>Google (statistics and ads measurement), authors of the 2017-2018 Google MMM papers; Global; practitioner-researchers</td>
<td>[https://research.google/pubs/geo-level-bayesian-hierarchical-media-mix-modeling/](https://research.google/pubs/geo-level-bayesian-hierarchical-media-mix-modeling/)</td>
<td>The group that defined the Bayesian adstock / Hill-saturation MMM and the geo-level hierarchical MMM later implemented in LightweightMMM and Meridian. The geo-level paper shows tighter credible intervals with sub-national data, a key argument for country or region panels in international marketing. English.</td>
<td>Reading pair for a session on hierarchical (geo/country) pooling; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Yingxiang Zhang, Mike Wurm, Brenda Price (and co-authors)</td>
<td>Google, Meridian team; Global; practitioner-researchers</td>
<td>[https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/](https://research.google/pubs/media-mix-model-calibration-with-bayesian-priors/)</td>
<td>Authors (with Eddie Li, Alexander Wakim, Joseph Kelly, Ying Liu) of 'Media Mix Model Calibration With Bayesian Priors' (2024): ROI reparameterisation so that experiment results set the priors, the calibration approach used in Meridian. English.</td>
<td>Reading for a calibration and experiments session; compare with Robyn's calibration and PyMC-Marketing lift-test likelihood; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Harikesh Nair</td>
<td>Google, Senior Director Data Science & Engineering (byline of the Meridian general-availability launch, Jan 2025); Global; practitioner-academic</td>
<td>[https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/](https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/)</td>
<td>Announced Meridian's open release to all advertisers; long academic record in quantitative marketing (formerly Stanford GSB faculty), bridging marketing science and industry measurement. English.</td>
<td>Keynote-style remote talk on why a platform open-sources an MMM and how advertisers in many markets use it; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Thomas Wiecki</td>
<td>PyMC Labs, founder; PyMC core developer; Global (remote team); practitioner and communicator</td>
<td>[https://www.pymc-labs.com/team](https://www.pymc-labs.com/team)</td>
<td>Founder of PyMC Labs, the consultancy behind PyMC-Marketing; frequent PyData / PyCon DE speaker ('Bayesian Marketing Science: Solving Marketing's 3 Biggest Problems', PyCon DE & PyData Berlin 2023). Updated tool-specific row (already in the earlier MMM guide). English, German.</td>
<td>Remote guest lecture in English or German on Bayesian MMM and PyMC-Marketing; strong speaking history.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>William (Will) Dean</td>
<td>PyMC Labs, Principal Data Scientist; lead author of the PyMC-Marketing JOSS paper; Global; practitioner</td>
<td>[https://joss.theoj.org/papers/10.21105/joss.10805](https://joss.theoj.org/papers/10.21105/joss.10805)</td>
<td>Lead author of 'PyMC-Marketing: Bayesian Marketing Mix Models and Customer Analytics in Python' (Journal of Open Source Software, 2026) with Juan Orduz, Colt Allen, Carlos Trujillo, Ricardo Vieira, Benjamin Vincent, Thomas Wiecki, Luciano Paz and others; core maintainer of the library (MMM, CLV, Bass diffusion, customer choice). English.</td>
<td>Cite the JOSS paper as the software reference; remote Q&A on library architecture and multidimensional (multi-market) MMM; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Juan Camilo Orduz</td>
<td>PyMC Labs, Principal Data Scientist; Berlin-connected; Global; practitioner and communicator</td>
<td>[https://juanitorduz.github.io/](https://juanitorduz.github.io/)</td>
<td>Co-author and core contributor of PyMC-Marketing; widely used blog posts ('Media Effect Estimation with PyMC: Adstock, Saturation & Diminishing Returns', 'Media Mix Model and Experimental Calibration: A Simulation Study', 'Ads, ROAS and Budgets: Interpreting and Communicating Statistical Models', 2026); talks at PyData Berlin. Updated tool-specific row. English, Spanish.</td>
<td>Blog posts as lab tutorials; remote guest talk (CET time zone); English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Carlos Trujillo</td>
<td>PyMC Labs core member and Principal Data Scientist; marketing data science at Wise (previously Bolt, Omnicom Media Group Latin America); Estonia; Global; practitioner</td>
<td>[https://cfp.pydata.org/berlin2025/talk/3XMJM3/](https://cfp.pydata.org/berlin2025/talk/3XMJM3/)</td>
<td>PyMC-Marketing co-author; talks 'Using Causal thinking to make Media Mix Modeling' (PyCon DE & PyData 2025) and 'Risk Budget Optimization for Causal Mix Models' (PyData Berlin 2025). Career spans agency-side MMM in Latin America and multi-country tech firms in Europe, ideal for the international angle. English, Spanish.</td>
<td>Remote guest talk on risk-aware budget allocation across markets and causal DAGs for MMM; European time zone; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Luca Fiaschi</td>
<td>PyMC Labs, Partner (formerly Mistplay, HelloFresh, Stitch Fix, Rocket Internet); Global; practitioner</td>
<td>[https://pretalx.com/pydata-boston-2025/talk/XRQFLN](https://pretalx.com/pydata-boston-2025/talk/XRQFLN)</td>
<td>Talk 'MMM Open-Source Showdown: A Practitioner's Benchmark of PyMC-Marketing vs. Google Meridian' (PyData Boston, Dec 2025): speed, recovery of channel contributions, convergence and memory; asks whether splines vs Fourier seasonality change budget decisions. English.</td>
<td>Use the benchmark as basis for a tool-comparison exercise; remote guest talk; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Niall Oulton</td>
<td>PyMC Labs, Vice President (marketing analytics); Global; practitioner</td>
<td>[https://www.pymc-labs.com/team](https://www.pymc-labs.com/team)</td>
<td>Leads PyMC Labs' marketing analytics client work; contributor to the PyMC-Marketing MMM webinar and consultations. English.</td>
<td>Remote industry perspective on how brands adopt open-source Bayesian MMM vs vendor tools; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Emanuele Fabbiani</td>
<td>xtream (Milan), Head of AI; Global; practitioner and communicator</td>
<td>[https://pretalx.com/pyconde-pydata-2024/talk/D7AEQY](https://pretalx.com/pyconde-pydata-2024/talk/D7AEQY)</td>
<td>Talk 'Marketing Media Mix Models with Python & PyMC: a Case Study' (PyCon DE & PyData Berlin 2024; also PyData Paris 2024) on a Bayesian MMM for WeRoad, an Italian travel operator, incl. adstock, saturation and a Streamlit front end; recording and transcript available. English, Italian.</td>
<td>Recorded talk as a worked case; remote guest speaker; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Raj Sethuraman (with Gerard J. Tellis and Richard Briesch)</td>
<td>Southern Methodist University (Sethuraman), USC Marshall (Tellis); Global; academics</td>
<td>[https://www.smu.edu/cox/academics/faculty/raj-sethuraman](https://www.smu.edu/cox/academics/faculty/raj-sethuraman)</td>
<td>Meta-analysis of brand advertising elasticities (Journal of Marketing 2011): 872 estimates from 57 studies, mean short-term elasticity about .12, higher for durables, early life cycle and TV; benchmark for plausible priors in Bayesian MMM and for cross-market comparisons. English.</td>
<td>Reading for setting informative priors in Meridian / PyMC-Marketing; discussion whether elasticities generalise across countries; English.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Tobias Kellner</td>
<td>e-dialog (HQ Opernring 1, Wien; offices Berlin, München, Zürich), Director Cloud & Data Science; Österreich (DACH); practitioner</td>
<td>[https://e-dialog.group/en/?p=13724](https://e-dialog.group/en/?p=13724)</td>
<td>Leads a 12-person team building AI and cloud marketing solutions incl. the budget recommendation engine BREE; e-dialog is a Google-certified Meridian partner (one of few in DACH) with a published bonprix Germany Meridian case (6.8% revenue increase, 30% ROI improvement). Previously head of Marketing Tech & Analytics at Share Now. German, English.</td>
<td>Strong on-site Vienna guest-speaker candidate (German or English) on running Meridian for DACH clients; contact via e-dialog.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Kristina Niederer-Nierlich</td>
<td>e-dialog, Director Digital Analytics; Wien; practitioner</td>
<td>[https://e-dialog.group/news/e-dialog-als-meridian-partner-zertifiziert](https://e-dialog.group/news/e-dialog-als-meridian-partner-zertifiziert)</td>
<td>Named in e-dialog's announcement of its Meridian partner certification; leads digital analytics at a Vienna-headquartered agency offering MMM, incrementality testing and consulting in DACH. German, English.</td>
<td>On-site Vienna guest or panel member on measurement practice in Austrian/DACH agencies; German.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Alexander Igelsböck</td>
<td>Adverity (marketing data platform, HQ Wien), CEO and co-founder; Wien; practitioner</td>
<td>[https://greatminds.advertisingweek360.com/ep329-alexander-igelsbock-ceo-at-adverity/](https://greatminds.advertisingweek360.com/ep329-alexander-igelsbock-ceo-at-adverity/)</td>
<td>Adverity launched 'Adverity Intelligence' (2025) incl. an MMM Agent for Google Meridian that automates data preparation for MMM; clients reportedly include IKEA, Red Bull, Mediacom and Mindshare. Shows the data-engineering side of multi-market MMM. German, English.</td>
<td>On-site Vienna guest talk on marketing data integration for MMM across markets; podcast episode as listening material; English or German.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Andreas Hofmaier</td>
<td>Marketing consultancy (sayg.eu, marketingQED), CEE media agency management background; Wien; practitioner</td>
<td>[https://at.linkedin.com/in/andreas-hofmaier](https://at.linkedin.com/in/andreas-hofmaier)</td>
<td>Vienna-based; shares work on MMM Labs and strataQED (MMM) and ROIvenue (MTA); posts that MMM Labs connects to AI assistants via MCP to run models across Robyn, Meridian and PyMC; argues MMM and MTA are complementary. CEE regional focus suits international marketing. German, English.</td>
<td>On-site Vienna guest on CEE media planning and running open-source MMM for regional clients; check current role before inviting.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Lucas Blochberger</td>
<td>Blck Alpaca (data-driven marketing agency, Wien), CEO and owner; Wien; practitioner and communicator</td>
<td>[https://blckalpaca.at/de/ueber-uns.md](https://blckalpaca.at/de/ueber-uns.md)</td>
<td>Agency publishes a German-language knowledge article on Marketing Mix Modeling with Meridian and Robyn that stresses DACH-specific constraints (platform rules, data protection, language areas) and data requirements (e.g. 2+ years of weekly data). German, English.</td>
<td>German reading for students; possible on-site Vienna guest from a young Austrian agency; verify MMM project experience first.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Maren Seitz</td>
<td>Analytic Partners, Head of DACH (München); Global/DACH; practitioner</td>
<td>[https://analyticpartners.com/knowledge-hub/newsroom/maren-seitz-appointed-as-head-of-dach-at-analytic-partners/](https://analyticpartners.com/knowledge-hub/newsroom/maren-seitz-appointed-as-head-of-dach-at-analytic-partners/)</td>
<td>Leads the DACH business of one of the largest independent MMM consultancies (commercial mix modelling across many countries); useful counterpoint to open-source tools. German, English.</td>
<td>Remote or on-site guest on vendor vs open-source MMM for multinational brands; German.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Lutz Moellmann</td>
<td>Kantar, Head of Analytics; Global; practitioner</td>
<td>[https://mmaglobal.com/node/47027](https://mmaglobal.com/node/47027)</td>
<td>MMA (Marketing + Media Alliance) speaker profile: built and led a EUR 3M marketing mix modelling practice at Kantar; Kantar runs MMM (LIFT ROI) for multinational advertisers. German, English.</td>
<td>Remote guest on how research agencies deliver MMM across markets; German or English; confirm current role.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
