## Quellen zu AB-Testing/Experiments in (Digital) Marketing/Retail (Agentensuche, 6. Oktober 2026)
Sechs parallele Rechercheagenten (A: Bücher, Artikel, Reports; B: Websites, Blogs, Tutorials; C: Lehrfälle und Praxisbeispiele; C2: Nachsuche Österreich und Deutschland; D: Software, Daten, statistische Methoden; E: Personen und Communities), Suche auf Englisch und Deutsch. 323 Fundstellen zu Online-Experimenten und A/B-Tests (Design, Power und Stichprobengröße, SRM, Peeking und sequentielles Testen, CUPED, Bandits, Uplift und heterogene Effekte), Feldexperimenten in Marketing und Handel (Preis, Promotion, Werbewirkung, Geo- und Switchback-Experimente, Ghost Ads) sowie Ethik und Experimentierkultur. Hinweise: Statsig gehört seit 2025/2026 zu OpenAI bzw. Amplitude, Eppo zu Datadog; expan, pycausalimpact, scikit-uplift und obp werden nicht mehr gepflegt; scipy, pymc, bambi, pymc-marketing und tea-tasting benötigen Python 3.12 oder neuer. HBS- und Darden-Fälle sind pro Kurs zu lizenzieren (ca. USD 5 pro Kopie). Die Recherche lief in einer Cloud-Umgebung mit gesperrtem Netzzugang: Links konnten fast nur über Suchtreffer bestätigt werden (geprüft sind v. a. PyPI-Seiten); Status "Link geprüft" = Seite abgerufen; "in Suchergebnis bestätigt" = nur über Suchtreffer bestätigt; "Link ungeprüft" = vor Verwendung prüfen (u. a. aus dem Gedächtnis ergänzte Profil- und Verlagslinks). Rollen von Personen vor einer Gastvortragsanfrage prüfen. Vollständiger Guide und rows.json: GitHub-Repository arnefloh-wu/search-teaching-materials, Ordner topics/AB-Testing & Experiments in (Digital) Marketing & Retail.
### Bücher (18)
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
<td>Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing</td>
<td>Ron Kohavi, Diane Tang, Ya Xu, Cambridge University Press, 2020, book (ISBN 9781108724265)</td>
<td>[https://doi.org/10.1017/9781108653985](https://doi.org/10.1017/9781108653985)</td>
<td>The standard practitioner text from Microsoft, Google and LinkedIn experimentation leads. Part I motivating examples and Twyman's law; Part II metrics and the OEC; chapters on SRM and trustworthiness checks, A/A tests, variance reduction (CUPED), triggering, leakage and interference, long-term and novelty effects, ethics (Ch. 9). Short chapters, about 290 pages.</td>
<td>Core textbook for the whole unit; assign Ch. 1-3, 17-21 (statistics, A/A tests, pitfalls) as readings. Paperback approx. EUR 35; e-book via Cambridge Core, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>Field Experiments: Design, Analysis, and Interpretation</td>
<td>Alan S. Gerber, Donald P. Green, W. W. Norton, 2012, book</td>
<td>[https://wwnorton.com/books/9780393979954](https://wwnorton.com/books/9780393979954)</td>
<td>Rigorous yet readable introduction to randomized field experiments: potential outcomes, sampling distributions, blocking and clustering, covariate adjustment, one-sided and two-sided noncompliance (relevant to ad exposure and ghost ads), attrition, interference/spillovers, heterogeneous effects, meta-analysis. Exercises with data online.</td>
<td>Methods backbone for the design and analysis sessions; Ch. 2-4 and 5-6 (noncompliance) as background readings. Paid approx. EUR 60-90, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Experimentation Works: The Surprising Power of Business Experiments</td>
<td>Stefan H. Thomke, Harvard Business Review Press, 2020, book (ISBN 9781633697102)</td>
<td>[https://books.google.com/books/about/Experimentation_Works.html?id=C49owQEACAAJ](https://books.google.com/books/about/Experimentation_Works.html?id=C49owQEACAAJ)</td>
<td>Managerial perspective on building an experimentation organization: Booking.com, Microsoft Bing, Amazon, IBM, Kohl's store-hours test; experimentation culture, leadership role, seven myths. Accessible for business students without statistics.</td>
<td>Background and discussion reading for the opening session (why experiment, culture); pairs with the HBR culture article. Paid approx. EUR 25.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>Statistical Methods in Online A/B Testing: Statistics for Data-Driven Business Decisions and Risk Management in E-commerce</td>
<td>Georgi Z. Georgiev, independently published, 2019, book (ISBN 9781694079725), 302 pages</td>
<td>[https://books.google.com/books/about/Statistical_Methods_in_Online_A_B_Testin.html?id=9MkpygEACAAJ](https://books.google.com/books/about/Statistical_Methods_in_Online_A_B_Testin.html?id=9MkpygEACAAJ)</td>
<td>Builds the statistics of A/B tests from the ground up with website-testing examples: p-values, confidence intervals, one-sided tests, power and sample size, sequential testing (AGILE), multiple testing, risk-reward framing of test decisions. Author runs Analytics-Toolkit.com.</td>
<td>Reference for students writing power and sequential-testing labs in Python; selected chapters as reading. Paid approx. EUR 40.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>Causal Inference for Statistics, Social, and Biomedical Sciences: An Introduction</td>
<td>Guido W. Imbens, Donald B. Rubin, Cambridge University Press, 2015, book</td>
<td>[https://doi.org/10.1017/CBO9781139025751](https://doi.org/10.1017/CBO9781139025751)</td>
<td>Authoritative potential-outcomes treatment of randomized experiments: Fisher exact p-values, Neyman repeated sampling, regression adjustment, stratified and paired designs, noncompliance. Part II (Ch. 4-11) is the classical randomized-experiment material.</td>
<td>Advanced background for the instructor and strong students (randomization inference lab). Paid, Cambridge Core e-book, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>The Power of Experiments: Decision Making in a Data-Driven World</td>
<td>Michael Luca, Max H. Bazerman, MIT Press, 2020, book</td>
<td>[https://mitpress.mit.edu/9780262043878/the-power-of-experiments/](https://mitpress.mit.edu/9780262043878/the-power-of-experiments/)</td>
<td>Business-school narrative on experiments at tech firms and in policy: Uber, Airbnb discrimination experiments, eBay paid search, Facebook emotional contagion debate, behavioural insights units. Short (about 230 pages), good for ethics and external-validity discussions.</td>
<td>Discussion reading for the ethics session; non-technical. Paid approx. EUR 25.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Practical Statistics for Data Scientists (2nd ed.) / Praktische Statistik für Data Scientists</td>
<td>Peter Bruce, Andrew Bruce, Peter Gedeck, O'Reilly, 2020 (German edition O'Reilly/dpunkt 2021), book</td>
<td>[https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/](https://www.oreilly.com/library/view/practical-statistics-for/9781492072935/)</td>
<td>Ch. 3 Statistical Experiments and Significance Testing covers A/B testing, permutation tests, t-tests, multiple testing, power and sample size and multi-armed bandits, with Python and R code. German edition available for German-language courses.</td>
<td>Python lab companion for business students; Ch. 3 as hands-on reading. Paid approx. EUR 45; O'Reilly Learning, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Causal Inference in Python: Applying Causal Inference in the Tech Industry</td>
<td>Matheus Facure, O'Reilly, 2023, book; free companion online book Causal Inference for the Brave and True</td>
<td>[https://matheusfacure.github.io/python-causality-handbook/landing-page.html](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)</td>
<td>Python-first causal inference for industry: randomized experiments, regression and CUPED-style variance reduction, heterogeneous effects and uplift (CATE, meta-learners), plus geo and switchback-type designs in the book. All notebooks open source.</td>
<td>Lab material for Python sessions on variance reduction and uplift; free online version, print approx. EUR 55.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>The Effect: An Introduction to Research Design and Causality</td>
<td>Nick Huntington-Klein, Chapman and Hall/CRC, 2021 (2nd ed. 2025), book, free online</td>
<td>[https://theeffectbook.net/](https://theeffectbook.net/)</td>
<td>Very readable causal inference text; Ch. 10 treatment effects, chapter on experiments, with Python, R and Stata code. Useful bridge from A/B tests to quasi-experiments (DiD, synthetic control) for geo tests.</td>
<td>Free background reading for students without econometrics; experiments chapter as reading. Free online, print approx. EUR 50.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Causal Inference: The Mixtape</td>
<td>Scott Cunningham, Yale University Press, 2021, book, free online</td>
<td>[https://mixtape.scunning.com/](https://mixtape.scunning.com/)</td>
<td>Ch. 4 Potential Outcomes Causal Model covers randomization, SUTVA and Fisher exact tests; later chapters on DiD and synthetic control are relevant for matched-market and geo experiments. Python and R code.</td>
<td>Free supplementary reading; randomization-inference lab. Free online, print approx. EUR 35.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Applied Causal Inference Powered by ML and AI</td>
<td>Victor Chernozhukov, Christian Hansen, Nathan Kallus, Martin Spindler, Vasilis Syrgkanis, online book, 2024</td>
<td>[https://causalml-book.org/](https://causalml-book.org/)</td>
<td>Free graduate-level book with Python notebooks: randomized experiments with covariate adjustment, double machine learning, heterogeneous treatment effects and policy learning. Spindler (Hamburg) makes it relevant to the German-speaking community.</td>
<td>Advanced reading for the uplift and HTE session; notebooks reusable in labs. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Bandit Algorithms</td>
<td>Tor Lattimore, Csaba Szepesvari, Cambridge University Press, 2020, book, free PDF from authors</td>
<td>[https://tor-lattimore.com/downloads/book/book.pdf](https://tor-lattimore.com/downloads/book/book.pdf)</td>
<td>Comprehensive reference on multi-armed bandits (UCB, Thompson sampling, contextual bandits). Mathematically demanding; Ch. 1-4 and 36 (Thompson sampling) are the parts usable for marketing students.</td>
<td>Instructor background for adaptive experiments session. Free PDF; print approx. EUR 60.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Bandit Algorithms for Website Optimization</td>
<td>John Myles White, O'Reilly, 2012, book (about 90 pages)</td>
<td>[https://www.oreilly.com/library/view/bandit-algorithms-for/9781449341565/](https://www.oreilly.com/library/view/bandit-algorithms-for/9781449341565/)</td>
<td>Short, code-driven introduction to epsilon-greedy, softmax and UCB for website testing, with simulation framework. Code originally Python 2 and Julia, easy to port.</td>
<td>Lab template: students simulate bandits vs. fixed A/B split in Python. Paid approx. EUR 20; O'Reilly Learning, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>A/B Testing: The Most Powerful Way to Turn Clicks Into Customers</td>
<td>Dan Siroker, Pete Koomen, Wiley, 2013, book</td>
<td>[https://www.wiley.com/en-us/A+B+Testing%3A+The+Most+Powerful+Way+to+Turn+Clicks+Into+Customers-p-9781118536094](https://www.wiley.com/en-us/A+B+Testing%3A+The+Most+Powerful+Way+to+Turn+Clicks+Into+Customers-p-9781118536094)</td>
<td>Optimizely founders' practitioner book; Obama 2008 campaign landing-page tests, what to test, building a testing culture. Dated on statistics (fixed-horizon peeking issues later fixed by Optimizely's Stats Engine).</td>
<td>Practitioner warm-up reading and source of classroom examples; contrast with Johari et al. on peeking. Paid approx. EUR 25.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Python for Marketing Research and Analytics</td>
<td>Jason S. Schwarz, Chris Chapman, Elea McDonnell Feit, Springer, 2020, book</td>
<td>[https://link.springer.com/book/10.1007/978-3-030-49720-0](https://link.springer.com/book/10.1007/978-3-030-49720-0)</td>
<td>Marketing analytics in Python with chapters on comparing groups, statistical tests, regression and Bayesian methods; Feit is co-author of the Test and Roll paper. Simulated marketing datasets suited to business students.</td>
<td>Python lab foundation for students before the A/B test analysis sessions. SpringerLink e-book, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Running Randomized Evaluations: A Practical Guide</td>
<td>Rachel Glennerster, Kudzai Takavarasha, Princeton University Press, 2013, book</td>
<td>[https://press.princeton.edu/books/paperback/9780691159270/running-randomized-evaluations](https://press.princeton.edu/books/paperback/9780691159270/running-randomized-evaluations)</td>
<td>J-PAL guide on the practical side of field experiments: choosing randomization unit, power (Ch. 6), threats (spillovers, attrition, noncompliance), ethics. Development context but transferable to store and geo tests.</td>
<td>Background for designing retail or store-level field experiments; power chapter as reading. Paid approx. EUR 40.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>The Voltage Effect: How to Make Good Ideas Great and Great Ideas Scale</td>
<td>John A. List, Currency (Penguin Random House), 2022, book</td>
<td>[https://www.penguinrandomhouse.com/books/646210/the-voltage-effect-by-john-a-list/](https://www.penguinrandomhouse.com/books/646210/the-voltage-effect-by-john-a-list/)</td>
<td>Field-experiment pioneer (Uber, Lyft chief economist) on why effects shrink at scale: false positives, unrepresentative samples, spillovers. Directly addresses external validity of marketing experiments.</td>
<td>Discussion reading on external validity and scaling; popular-science level. Paid approx. EUR 20.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Empirical Generalizations about Marketing Impact (2nd ed.)</td>
<td>Dominique M. Hanssens (ed.), Marketing Science Institute, 2015, book/report</td>
<td>[https://www.msi.org/](https://www.msi.org/)</td>
<td>Compilation of benchmark elasticities and effect sizes for advertising, price and promotion. Useful as realistic priors for minimum detectable effect and power calculations in marketing experiments.</td>
<td>Background for setting realistic MDEs in power labs. MSI members or purchase; check availability.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Journal Articles (49)
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
<td>A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook</td>
<td>Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, Dan Chapsky, Marketing Science 38(2), 193-225, 2019, article</td>
<td>[https://doi.org/10.1287/mksc.2018.1135](https://doi.org/10.1287/mksc.2018.1135)</td>
<td>15 Facebook conversion-lift RCTs (1.6 bn impressions) compared with observational methods (matching, regression, inverse probability weighting): observational methods mostly overestimate lift. Key paper for why incrementality needs experiments.</td>
<td>Core reading for the ad-effectiveness session; class discussion on RCT vs. observational attribution. Paywalled, WU-Lizenz prüfen; working paper free on SSRN.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Close Enough? A Large-Scale Exploration of Non-Experimental Approaches to Advertising Measurement</td>
<td>Brett R. Gordon, Robert Moakler, Florian Zettelmeyer, Marketing Science 42(4), 768-793, 2023, article</td>
<td>[https://doi.org/10.1287/mksc.2022.1413](https://doi.org/10.1287/mksc.2022.1413)</td>
<td>Follow-up with about 600 Facebook experiments: double/debiased ML and rich features still fail to recover experimental lift reliably. Updates the 2019 finding with modern ML methods.</td>
<td>Advanced reading paired with Gordon et al. 2019; supports debate on whether ML can replace experiments. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Test and Roll: Profit-Maximizing A/B Tests</td>
<td>Elea McDonnell Feit and Ron Berman, Marketing Science 38(6), 1038-1058, 2019</td>
<td>[https://doi.org/10.1287/mksc.2019.1194](https://doi.org/10.1287/mksc.2019.1194)</td>
<td>Reframes A/B tests as a profit decision: optimal test size is much smaller than hypothesis-testing sample sizes when the population is small or responses noisy. Three marketing applications (website design, display advertising, catalogue mailing) with priors from past tests; free preprint on arXiv (1811.00457) and online calculator.</td>
<td>Advanced session on sample size; students compare power-based vs. test-and-roll sizes in Python. Free preprint; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness</td>
<td>Garrett A. Johnson, Randall A. Lewis, Elmar I. Nubbemeyer, Journal of Marketing Research 54(6), 867-884, 2017, article</td>
<td>[https://doi.org/10.1509/jmr.15.0297](https://doi.org/10.1509/jmr.15.0297)</td>
<td>Introduces ghost ads and predicted ghost ads: logging would-be exposures in the control group to measure ad lift without paying for PSA ads; application with a retailer on Google Display Network. Paul E. Green and Weitz-Winer-O'Dell awards.</td>
<td>Core reading for incrementality measurement design (intent-to-treat vs. treatment-on-treated). WU-Lizenz prüfen; SSRN version free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Unfavorable Economics of Measuring the Returns to Advertising</td>
<td>Randall A. Lewis, Justin M. Rao, Quarterly Journal of Economics 130(4), 1941-1973, 2015, article</td>
<td>[https://academic.oup.com/qje/article-abstract/130/4/1941/1914592](https://academic.oup.com/qje/article-abstract/130/4/1941/1914592)</td>
<td>25 large field experiments with US retailers and brokerages: median ROI confidence interval wider than 100 percentage points; explains why ad effects are hard to detect given noisy sales. Excellent motivation for power analysis.</td>
<td>Reading for the power and sample size session; classroom calculation of required sample size for ad lift. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Online Ads and Offline Sales: Measuring the Effect of Retail Advertising via a Controlled Experiment on Yahoo!</td>
<td>Randall A. Lewis, David H. Reiley, Quantitative Marketing and Economics 12(3), 235-266, 2014, article</td>
<td>[https://link.springer.com/article/10.1007/s11129-014-9146-6](https://link.springer.com/article/10.1007/s11129-014-9146-6)</td>
<td>Randomized experiment with 1.6 million customers of a major retailer linking online display ads to in-store sales; ads increased purchases by about 5 percent, mostly offline. Classic omnichannel retail ad experiment.</td>
<td>Reading for retail ad effectiveness; illustrates matching online exposure to offline sales. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>When Less Is More: Data and Power in Advertising Experiments</td>
<td>Garrett A. Johnson, Randall A. Lewis, David H. Reiley, Marketing Science 36(1), 2017, article</td>
<td>[https://doi.org/10.1287/mksc.2016.0998](https://doi.org/10.1287/mksc.2016.0998)</td>
<td>Shows how to gain statistical power in ad experiments by filtering out noise (e.g. restricting to exposed users and relevant outcome windows); Yahoo retail experiment.</td>
<td>Reading for variance reduction in ad experiments; pairs with CUPED. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment</td>
<td>Thomas Blake, Chris Nosko and Steven Tadelis, 'Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment', Econometrica 83(1), 155-174, 2015</td>
<td>[https://doi.org/10.3982/ECTA12423](https://doi.org/10.3982/ECTA12423)</td>
<td>eBay stopped brand-keyword ads and ran geo-randomised non-brand experiments: brand ads have no measurable short-term benefit; non-brand ads help only new/infrequent users, average returns negative. Observational estimates hugely overstated ROI. Accessible summaries: VoxEU column and Chicago Booth Review; free working paper at faculty.haas.berkeley.edu/stadelis/BNT_ECMA_rev.pdf.</td>
<td>Core example for incrementality vs. attribution; discussion: why did eBay's agency report positive ROI? Paywalled journal, NBER w20171 free; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)</td>
<td>Alex Deng, Ya Xu, Ron Kohavi, Toby Walker, WSDM 2013 (Proceedings of the 6th ACM International Conference on Web Search and Data Mining), 123-132, conference paper</td>
<td>[https://doi.org/10.1145/2433396.2433413](https://doi.org/10.1145/2433396.2433413)</td>
<td>Introduces CUPED, a control-variate estimator using pre-period metrics; about 50 percent variance reduction on Bing. Now standard in all experimentation platforms.</td>
<td>Reading plus Python lab: implement CUPED on simulated or e-commerce data and compare confidence interval widths. Free PDF on exp-platform.com.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Controlled Experiments on the Web: Survey and Practical Guide</td>
<td>Ron Kohavi, Roger Longbotham, Dan Sommerfield, Randal M. Henne, Data Mining and Knowledge Discovery 18(1), 140-181, 2009, article</td>
<td>[https://doi.org/10.1007/s10618-008-0114-1](https://doi.org/10.1007/s10618-008-0114-1)</td>
<td>Foundational survey of web A/B testing: OEC, power and sample size, A/A tests, ramp-up, randomization and hashing, limitations; HiPPO concept. Free PDF from Stanford.</td>
<td>Introductory reading for the first session. Open access via author PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained</td>
<td>Ron Kohavi, Alex Deng, Brian Frasca, Roger Longbotham, Toby Walker, Ya Xu, KDD 2012, conference paper</td>
<td>[https://dl.acm.org/doi/abs/10.1145/2339530.2339653](https://dl.acm.org/doi/abs/10.1145/2339530.2339653)</td>
<td>Five real Bing puzzles (e.g. a bug that raised revenue, carryover effects, misleading metrics) and their root causes. Great case material on Twyman's law and metric choice.</td>
<td>Discussion session: students diagnose each puzzle before reading the explanation. Free author PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Seven Rules of Thumb for Web Site Experimenters</td>
<td>Ron Kohavi, Alex Deng, Roger Longbotham, Ya Xu, KDD 2014, conference paper</td>
<td>[https://dl.acm.org/doi/10.1145/2623330.2623341](https://dl.acm.org/doi/10.1145/2623330.2623341)</td>
<td>Empirical rules from thousands of experiments: small changes can have big impact, changes rarely have big positive impact, your mileage will vary, speed matters, reducing abandonment is hard, avoid complex designs, ensure enough users.</td>
<td>Short reading for intuition-building; slides and video on exp-platform.com/rules-of-thumb. Free author PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners</td>
<td>Aleksander Fabijan, Jayant Gupchup, Somit Gupta, Jeff Omhover, Wen Qin, Lukas Vermeer, Pavel Dmitriev, KDD 2019, conference paper</td>
<td>[https://doi.org/10.1145/3292500.3330722](https://doi.org/10.1145/3292500.3330722)</td>
<td>Taxonomy of SRM causes (assignment, execution, log processing, analysis, interference) from Booking.com, Microsoft, Outreach and Online Dialogue; chi-square SRM check.</td>
<td>Lab: students run an SRM chi-square test before analysing a dataset. Free PDF on exp-platform.com.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Top Challenges from the First Practical Online Controlled Experiments Summit</td>
<td>Somit Gupta, Ronny Kohavi, Diane Tang, Ya Xu et al., SIGKDD Explorations 21(1), 20-35, 2019, article</td>
<td>[https://exp-platform.com/top-challenges-from-first-practical-online-controlled-experiments-summit/](https://exp-platform.com/top-challenges-from-first-practical-online-controlled-experiments-summit/)</td>
<td>34 experts from 13 firms (Amazon, Booking, Facebook, Google, LinkedIn, Microsoft, Netflix, Uber ...) list open problems: OEC and long-term effects, heterogeneous effects, interference in marketplaces, culture. Good map of the field.</td>
<td>Overview reading or group presentations (one challenge per team). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Statistical Challenges in Online Controlled Experiments: A Review of A/B Testing Methodology</td>
<td>Nicholas Larsen, Jonathan Stallrich, Srijan Sengupta, Alex Deng, Ron Kohavi, Nathaniel T. Stevens, The American Statistician 78(2), 135-149, 2024, article</td>
<td>[https://doi.org/10.1080/00031305.2023.2257237](https://doi.org/10.1080/00031305.2023.2257237)</td>
<td>Up-to-date statistical review: variance reduction, heterogeneous effects, sequential testing and peeking, interference, long-term effects, small-sample and heavy-tail issues. Open access on arXiv (2212.11366).</td>
<td>Instructor reference and advanced student reading; good structure for a methods lecture. Open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Always Valid Inference: Continuous Monitoring of A/B Tests</td>
<td>Ramesh Johari, Pete Koomen, Leonid Pekelis, David Walsh, Operations Research 70(3), 1806-1821, 2022, article</td>
<td>[https://doi.org/10.1287/opre.2021.2135](https://doi.org/10.1287/opre.2021.2135)</td>
<td>Shows how peeking inflates false positives and derives always-valid p-values (mSPRT) implemented in Optimizely's Stats Engine.</td>
<td>Reading for the peeking and sequential testing session; Python simulation of peeking inflation. WU-Lizenz prüfen; arXiv preprint free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>False Discovery in A/B Testing</td>
<td>Ron Berman, Christophe Van den Bulte, Management Science 68(9), 6762-6782, 2022, article</td>
<td>[https://doi.org/10.1287/mnsc.2021.4207](https://doi.org/10.1287/mnsc.2021.4207)</td>
<td>4,964 effects from 2,766 Optimizely experiments: about 70 percent true nulls, false discovery rate 18-25 percent at 5 percent significance. Implications for multiple testing and two-stage designs.</td>
<td>Reading for multiple testing and false discoveries; discussion of what significant results mean in practice. Author PDF free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A/B Testing with Fat Tails</td>
<td>Eduardo M. Azevedo, Alex Deng, Jose Luis Montiel Olea, Justin Rao, E. Glen Weyl, Journal of Political Economy 128(12), 4614-4672, 2020, article</td>
<td>[https://doi.org/10.1086/710607](https://doi.org/10.1086/710607)</td>
<td>Uses Bing experiment data to show innovation effects are fat-tailed; optimal strategy then is many small, lean experiments rather than few large ones. Links experimentation to innovation strategy.</td>
<td>Advanced reading on experimentation strategy and portfolio of tests. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Experimentation and Start-up Performance: Evidence from A/B Testing</td>
<td>Rembrand Koning, Sharique Hasan, Aaron Chatterji, Management Science 68(9), 2022, article</td>
<td>[https://doi.org/10.1287/mnsc.2021.4209](https://doi.org/10.1287/mnsc.2021.4209)</td>
<td>Panel of tech start-ups: adopting A/B testing tools raises performance by 30-100 percent after a year, via more product launches and faster failure. Evidence that experimentation pays off at firm level.</td>
<td>Reading for the business case and culture session. NBER WP w26278 free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Surprising Power of Online Experiments</td>
<td>Ron Kohavi, Stefan Thomke, Harvard Business Review 95(5), September-October 2017, 74-82, article</td>
<td>[https://exp-platform.com/hbr-the-surprising-power-of-online-experiments/](https://exp-platform.com/hbr-the-surprising-power-of-online-experiments/)</td>
<td>Managerial introduction: Bing headline test worth over 100 million USD, Amazon credit-card offer move, only 10-20 percent of tests positive at Google and Bing, OEC and pitfalls.</td>
<td>First-session reading for business students. HBR, WU-Lizenz prüfen (Business Source Premier); reprint PDF circulates.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Building a Culture of Experimentation</td>
<td>Stefan Thomke, Harvard Business Review 98(2), March-April 2020, article</td>
<td>[https://hbr.org/2020/03/building-a-culture-of-experimentation](https://hbr.org/2020/03/building-a-culture-of-experimentation)</td>
<td>Booking.com runs about 25,000 tests per year; describes democratized experimentation, the 2017 radical homepage redesign test, and leadership behaviours that enable experimentation.</td>
<td>Discussion reading on organization and culture. HBR, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Step-by-Step Guide to Smart Business Experiments</td>
<td>Eric T. Anderson, Duncan Simester, Harvard Business Review 89(3), 98-105, March 2011, article</td>
<td>[https://hbr.org/2011/03/a-step-by-step-guide-to-smart-business-experiments](https://hbr.org/2011/03/a-step-by-step-guide-to-smart-business-experiments)</td>
<td>Seven rules for marketing field experiments (e.g. focus on individual customers, use control groups, exploit natural experiments) with catalog and retail pricing examples.</td>
<td>Short managerial reading for designing a student field-experiment proposal. HBR, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Field Experimentation in Marketing Research</td>
<td>Ayelet Gneezy, Journal of Marketing Research 54(1), 140-143, 2017, article (special section on field experiments)</td>
<td>[https://doi.org/10.1509/jmr.16.0225](https://doi.org/10.1509/jmr.16.0225)</td>
<td>Short argument for more field experiments in marketing, their defining features and practical considerations. Introduces the JMR 2017 special section on field experiments (a useful reading pool).</td>
<td>Short opening reading; point students to the special section for project ideas. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Field Experiments in Marketing</td>
<td>Duncan Simester, in: Handbook of Economic Field Experiments Vol. 1 (eds. Banerjee and Duflo), Elsevier, Ch. 11, 465-497, 2017, book chapter</td>
<td>[https://www.sciencedirect.com/science/chapter/handbook/abs/pii/S2214658X16300010](https://www.sciencedirect.com/science/chapter/handbook/abs/pii/S2214658X16300010)</td>
<td>Survey of marketing field experiments on pricing, advertising, product and model validation, both online and in physical stores, by a leading retail experimenter.</td>
<td>Background reading to map the literature; good reading list source. ScienceDirect, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Econometrics of Randomized Experiments</td>
<td>Susan Athey, Guido W. Imbens, in: Handbook of Economic Field Experiments Vol. 1, Elsevier, Ch. 3, 2017, book chapter (arXiv 1607.00698)</td>
<td>[https://arxiv.org/abs/1607.00698](https://arxiv.org/abs/1607.00698)</td>
<td>Design-based analysis of randomized experiments: randomization inference, stratification, clustering, regression adjustment, heterogeneous effects and network experiments. Free preprint.</td>
<td>Instructor background for the analysis sessions. Free on arXiv.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Effects of \$9 Price Endings on Retail Sales: Evidence from Field Experiments</td>
<td>Eric T. Anderson, Duncan I. Simester, Quantitative Marketing and Economics 1(1), 93-110, 2003, article</td>
<td>[https://doi.org/10.1023/A:1023581927405](https://doi.org/10.1023/A:1023581927405)</td>
<td>Three catalog field experiments manipulating price endings: \$9 endings increased demand, more for new items. Classic retail pricing experiment with simple design.</td>
<td>Reading for pricing experiments; replicate the analysis logic in class. Author PDF free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Competitive Price Targeting with Smartphone Coupons</td>
<td>Jean-Pierre Dube, Zheng Fang, Nathan Fong, Xueming Luo, Marketing Science 36(6), 944-975, 2017, article</td>
<td>[https://www.nber.org/papers/w22067](https://www.nber.org/papers/w22067)</td>
<td>Large mobile field experiment with two rival movie theatres randomizing coupon prices by location and past behaviour; traces out best-response functions and shows competitive effects of targeting.</td>
<td>Reading for price and promotion experiments and personalization. NBER WP free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Personalization in Email Marketing: The Role of Noninformative Advertising Content</td>
<td>Navdeep S. Sahni, S. Christian Wheeler, Pradeep K. Chintagunta, Marketing Science 37(2), 236-258, 2018, article</td>
<td>[https://doi.org/10.1287/mksc.2017.1066](https://doi.org/10.1287/mksc.2017.1066)</td>
<td>Randomized email experiments with three firms and millions of recipients: adding the recipient's name to the subject line raises opens and sales leads and reduces unsubscribes.</td>
<td>Reading and template for an email A/B test lab. SSRN version free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Estimating Marketing Component Effects: Double Machine Learning from Targeted Digital Promotions</td>
<td>Paul B. Ellickson, Wreetabrata Kar, James C. Reeder III, Marketing Science 42(4), 704-728, 2023, article</td>
<td>[https://doi.org/10.1287/mksc.2022.1401](https://doi.org/10.1287/mksc.2022.1401)</td>
<td>Decomposes effects of targeted email promotions (content, framing, discount type) along the funnel with double ML; clearance-framed discounts outperform product-specific ones.</td>
<td>Advanced reading on analysing many promotion variants. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>When Does Retargeting Work? Information Specificity in Online Advertising</td>
<td>Anja Lambrecht, Catherine Tucker, Journal of Marketing Research 50(5), 561-576, 2013, article</td>
<td>[https://lbsresearch.london.edu/388/](https://lbsresearch.london.edu/388/)</td>
<td>Field experiment with a travel website: dynamic (product-specific) retargeting underperforms generic retargeting unless consumers' preferences are well defined. O'Dell Award.</td>
<td>Reading on ad personalization experiments and heterogeneous effects. Author version free at LBS; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Customer Acquisition via Display Advertising Using Multi-Armed Bandit Experiments</td>
<td>Eric M. Schwartz, Eric T. Bradlow, Peter S. Fader, Marketing Science 36(4), 500-522, 2017, article</td>
<td>[https://doi.org/10.1287/mksc.2016.1023](https://doi.org/10.1287/mksc.2016.1023)</td>
<td>Hierarchical Thompson sampling to allocate display impressions across ad creatives and sites in a live campaign; about 8 percent more customer acquisitions than balanced A/B testing.</td>
<td>Core reading for the bandit session; Python lab simulating Thompson sampling vs. A/B. Penn repository version free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Tutorial on Thompson Sampling</td>
<td>Daniel J. Russo, Benjamin Van Roy, Abbas Kazerouni, Ian Osband, Zheng Wen, Foundations and Trends in Machine Learning 11(1), 1-96, 2018, article/monograph</td>
<td>[https://arxiv.org/abs/1707.02038](https://arxiv.org/abs/1707.02038)</td>
<td>Accessible tutorial on Thompson sampling with Bernoulli bandit examples, product recommendation and assortment; Ch. 1-3 suitable for business students with probability basics.</td>
<td>Reading for adaptive experiments; Bernoulli bandit example as lab. Free on arXiv.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Website Morphing</td>
<td>John R. Hauser, Glen L. Urban, Guilherme Liberali, Michael Braun, Marketing Science 28(2), 202-223, 2009, article</td>
<td>[https://doi.org/10.1287/mksc.1080.0459](https://doi.org/10.1287/mksc.1080.0459)</td>
<td>Early marketing application of bandits (Gittins index) to adapt website look and feel to inferred cognitive styles; BT broadband field test.</td>
<td>Background on adaptive personalization in marketing. WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Retention Futility: Targeting High-Risk Customers Might Be Ineffective</td>
<td>Eva Ascarza, Journal of Marketing Research 55(1), 80-98, 2018, article</td>
<td>[https://doi.org/10.1509/jmr.16.0163](https://doi.org/10.1509/jmr.16.0163)</td>
<td>Two field experiments plus ML: customers with highest churn risk are not the ones most responsive to retention offers; target on uplift (treatment effect), not risk. Paul E. Green Award.</td>
<td>Core reading for uplift modeling; motivates CATE-based targeting lab. SSRN version free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Estimation and Inference of Heterogeneous Treatment Effects using Random Forests</td>
<td>Stefan Wager, Susan Athey, Journal of the American Statistical Association 113(523), 1228-1242, 2018, article</td>
<td>[https://doi.org/10.1080/01621459.2017.1319839](https://doi.org/10.1080/01621459.2017.1319839)</td>
<td>Introduces causal forests with valid confidence intervals for heterogeneous treatment effects; basis of the grf and EconML implementations.</td>
<td>Methods reference for the HTE session; students apply causal forest (EconML) to experiment data. arXiv version free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Heterogeneous Treatment Effects and Optimal Targeting Policy Evaluation</td>
<td>Guenter J. Hitsch, Sanjog Misra, Walter W. Zhang, Quantitative Marketing and Economics 22, 115-168, 2024, article</td>
<td>[https://doi.org/10.1007/s11129-023-09278-5](https://doi.org/10.1007/s11129-023-09278-5)</td>
<td>Framework for targeting from randomized experiments: CATE estimation with ML methods, off-policy evaluation of targeting policies, profit comparisons on a large catalog-retailer experiment.</td>
<td>Advanced reading linking A/B tests to targeting policies. SpringerLink, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Targeting Prospective Customers: Robustness of Machine-Learning Methods to Typical Data Challenges</td>
<td>Duncan Simester, Artem Timoshenko, Spyros I. Zoumpoulis, Management Science 66(6), 2495-2522, 2020, article</td>
<td>[https://doi.org/10.1287/mnsc.2019.3308](https://doi.org/10.1287/mnsc.2019.3308)</td>
<td>Two large field experiments at a retailer: train seven ML targeting methods on the first, validate the targeting policies in the second. Shows effects of covariate shift and concept shift.</td>
<td>Reading on experiment-based targeting and external validity across waves. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Efficiently Evaluating Targeting Policies: Improving on Champion vs. Challenger Experiments</td>
<td>Duncan Simester, Artem Timoshenko, Spyros I. Zoumpoulis, Management Science 66(8), 3412-3424, 2020, article</td>
<td>[https://ideas.repec.org/a/inm/ormnsc/v66y2020i8p3412-3424.html](https://ideas.repec.org/a/inm/ormnsc/v66y2020i8p3412-3424.html)</td>
<td>Shows that comparing targeting policies only on customers where they disagree gives large precision gains over standard champion-vs-challenger tests.</td>
<td>Short reading for a design-efficiency discussion. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Causal Inference and Uplift Modelling: A Review of the Literature</td>
<td>Pierre Gutierrez, Jean-Yves Gerardy, Proceedings of Machine Learning Research 67 (PAPIs 2016), 1-13, 2017, conference paper</td>
<td>[https://proceedings.mlr.press/v67/gutierrez17a.html](https://proceedings.mlr.press/v67/gutierrez17a.html)</td>
<td>Compact review of uplift approaches (two-model, class transformation, uplift trees) and evaluation with Qini and uplift curves. Practitioner-friendly.</td>
<td>Reading before an uplift-modeling lab (e.g. with the Hillstrom email dataset). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Design and Analysis of Switchback Experiments</td>
<td>Iavor Bojinov, David Simchi-Levi, Jinglong Zhao, Management Science 69(7), 3759-3777, 2023, article</td>
<td>[https://doi.org/10.1287/mnsc.2022.4583](https://doi.org/10.1287/mnsc.2022.4583)</td>
<td>Optimal design and randomization-based inference for switchback (time-alternating) experiments under carryover effects; motivated by marketplace and pricing tests.</td>
<td>Reading for experiments under interference (marketplaces, delivery, dynamic pricing). WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Experimental Design in Two-Sided Platforms: An Analysis of Bias</td>
<td>Ramesh Johari, Hannah Li, Inessa Liskovich, Gabriel Y. Weintraub, Management Science 68(10), 7069-7089, 2022, article</td>
<td>[https://doi.org/10.1287/mnsc.2021.4247](https://doi.org/10.1287/mnsc.2021.4247)</td>
<td>Shows how interference in two-sided marketplaces biases customer-side and listing-side randomization, and when each design is less biased.</td>
<td>Reading on interference and SUTVA violations in marketplaces. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>From Infrastructure to Culture: A/B Testing Challenges in Large Scale Social Networks</td>
<td>Ya Xu, Nanyu Chen, Addrian Fernandez, Omar Sinno, Anmol Bhasin, KDD 2015, conference paper</td>
<td>[https://doi.org/10.1145/2783258.2788602](https://doi.org/10.1145/2783258.2788602)</td>
<td>LinkedIn's experimentation platform (XLNT): scaling, metrics, network effects and building experimentation culture.</td>
<td>Industry case reading on platforms and culture. Free author PDF.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Focusing on the Long-term: It's Good for Users and Business</td>
<td>Henning Hohnhold, Deirdre O'Brien, Diane Tang, KDD 2015, 1849-1858, conference paper</td>
<td>[https://research.google.com/pubs/archive/43887.pdf](https://research.google.com/pubs/archive/43887.pdf)</td>
<td>Google method for measuring long-term user learning (ads blindness) with long-running holdouts; led to 50 percent ad load reduction on mobile. Central for novelty and long-term effects and OEC choice.</td>
<td>Reading on short-term vs. long-term metrics. Free PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Experimental Evidence of Massive-Scale Emotional Contagion through Social Networks</td>
<td>Adam Kramer, Jamie Guillory and Jeffrey Hancock, PNAS 111(24), 2014</td>
<td>[https://doi.org/10.1073/pnas.1320040111](https://doi.org/10.1073/pnas.1320040111)</td>
<td>News feeds of 689,003 users were manipulated to show fewer positive or fewer negative posts; users then posted correspondingly. Public outrage over consent and manipulation; PNAS issued an editorial expression of concern. Classic case for the ethics of online experiments vs. 'normal' product tests.</td>
<td>Ethics debate: where is the line between A/B testing and manipulation? Pair with OkCupid. Open access.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Objecting to Experiments that Compare Two Unobjectionable Policies or Treatments</td>
<td>Michelle N. Meyer, Patrick R. Heck, Geoffrey S. Holtzman et al., PNAS 116(22), 10723-10728, 2019, article</td>
<td>[https://doi.org/10.1073/pnas.1820701116](https://doi.org/10.1073/pnas.1820701116)</td>
<td>16 studies (n=5,873): people approve of implementing A or B untested but object to an A/B test comparing them (A/B effect). Follow-up debate in PNAS (Mislavsky et al.; 2023 replication).</td>
<td>Ethics discussion counterpoint to the Facebook study; classroom replication survey possible. Open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Shining a Light on Dark Patterns</td>
<td>Jamie Luguri, Lior Jacob Strahilevitz, Journal of Legal Analysis 13(1), 43-109, 2021, article</td>
<td>[https://academic.oup.com/jla/article/13/1/43/6180579](https://academic.oup.com/jla/article/13/1/43/6180579)</td>
<td>Randomized online experiments: mild dark patterns doubled, aggressive ones nearly quadrupled acceptance of a dubious subscription; less educated users more susceptible. Shows A/B testing used to optimize manipulation.</td>
<td>Ethics and regulation session reading. Open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites</td>
<td>Arunesh Mathur, Gunes Acar, Michael J. Friedman, Elena Lucherini, Jonathan Mayer, Marshini Chetty, Arvind Narayanan, Proceedings of the ACM on Human-Computer Interaction 3 (CSCW), 2019, article</td>
<td>[https://arxiv.org/abs/1907.07032](https://arxiv.org/abs/1907.07032)</td>
<td>Automated crawl finding 1,818 dark-pattern instances on e-commerce sites (fake urgency, scarcity, sneaking) and third-party vendors that sell them, many tied to optimization and testing tools.</td>
<td>Ethics session reading for retail e-commerce; dataset is public. Free on arXiv.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Online Controlled Experiments and A/B Testing</td>
<td>Ron Kohavi, Roger Longbotham, in: Encyclopedia of Machine Learning and Data Mining, Springer, 2017, encyclopedia entry</td>
<td>[https://link.springer.com/rwe/10.1007/978-1-4899-7687-1_891](https://link.springer.com/rwe/10.1007/978-1-4899-7687-1_891)</td>
<td>Concise (about 10 pages) definition-level overview of A/B testing terminology, OEC, pitfalls and history. Good glossary-style reading.</td>
<td>Short pre-reading before the first session. SpringerLink, WU-Lizenz prüfen; author PDF free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A/B Testing: A Systematic Literature Review</td>
<td>Federico Quin, Danny Weyns, Matthias Galster, Camila Costa Silva, Journal of Systems and Software, 2024 (arXiv 2308.04929), article</td>
<td>[https://arxiv.org/abs/2308.04929](https://arxiv.org/abs/2308.04929)</td>
<td>Systematic review of 141 primary studies on A/B testing: subjects tested, designs, metrics, statistical methods, open problems. Software-engineering perspective complements the marketing literature.</td>
<td>Reference map for student literature reviews or seminar papers. Free on arXiv.</td>
<td>neu; in Suchergebnis bestätigt</td>
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
<td>Measuring Ad Effectiveness Using Geo Experiments</td>
<td>Jon Vaver and Jim Koehler, Google Inc. technical report, 2011</td>
<td>[https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)</td>
<td>Google's method for randomising ad spend across geographic regions and estimating return on ad spend with a regression model; basis of later GeoLift/Meta and Google matched-markets tools. Good for offline and TV-like campaigns where users cannot be randomised.</td>
<td>Background for geo test design; link to Zalando location-based tests. Free. URL constructed from memory, verify.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Reports</td>
<td>Periodic Measurement of Advertising Effectiveness Using Multiple-Test-Period Geo Experiments</td>
<td>Jon Vaver, Jim Koehler, Google Inc., 2012, technical report</td>
<td>[https://research.google.com/pubs/archive/38356.pdf](https://research.google.com/pubs/archive/38356.pdf)</td>
<td>Extends geo experiments to repeated on/off test periods for ongoing measurement of campaign ROAS; useful design alternative when few regions exist (e.g. Austria's nine Bundeslaender).</td>
<td>Follow-up reading for advanced geo-experiment design. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Reports</td>
<td>Estimating Ad Effectiveness using Geo Experiments in a Time-Based Regression Framework</td>
<td>Jouni Kerman, Peng Wang, Jon Vaver, Google Inc., 2017, technical report</td>
<td>[https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/)</td>
<td>Time-based regression (TBR) for matched-market geo tests with a single treatment and control aggregate; basis for Google's matched-markets tools.</td>
<td>Background for a matched-market lab. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Online Choice Architecture: How Digital Design Can Harm Competition and Consumers</td>
<td>Competition and Markets Authority (UK), Discussion Paper CMA155, April 2022, government report</td>
<td>[https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers](https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers)</td>
<td>Taxonomy of 21 harmful choice-architecture practices (drip pricing, scarcity claims, sludge); discusses how firms use A/B testing to optimize such designs and how regulators can run their own experiments.</td>
<td>Ethics and regulation session reading; contrast commercial vs. regulatory testing. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Dark Commercial Patterns</td>
<td>OECD, OECD Digital Economy Papers No. 336, 2022, report</td>
<td>[https://www.oecd.org/en/publications/dark-commercial-patterns_44f5e846-en.html](https://www.oecd.org/en/publications/dark-commercial-patterns_44f5e846-en.html)</td>
<td>International overview of dark patterns, evidence on prevalence and effects (including experimental studies) and policy responses in OECD countries including the EU.</td>
<td>Background for ethics session, European perspective. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Behavioural Study on Unfair Commercial Practices in the Digital Environment: Dark Patterns and Manipulative Personalisation</td>
<td>European Commission, DG JUST (study by LE Europe, VVA, ConPolicy, Ipsos), 2022, government report</td>
<td>[https://op.europa.eu/en/search-results?queryText=dark%20patterns%20manipulative%20personalisation](https://op.europa.eu/en/search-results?queryText=dark%20patterns%20manipulative%20personalisation)</td>
<td>EU-wide mystery shopping of websites plus online behavioural experiments with consumers testing the effect of dark patterns and personalisation; relevant for EU legal context of A/B testing (UCPD, DSA).</td>
<td>Ethics and EU regulation reading; experiment design examples from a regulator. Free; link is a Publications Office search, check final URL.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Bringing Dark Patterns to Light</td>
<td>US Federal Trade Commission, Staff Report, September 2022, government report</td>
<td>[https://www.ftc.gov/reports/bringing-dark-patterns-light](https://www.ftc.gov/reports/bringing-dark-patterns-light)</td>
<td>FTC staff report on dark patterns in e-commerce and subscriptions with enforcement cases; useful contrast to EU approach.</td>
<td>Optional background for ethics debate. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Bayesian A/B Testing at VWO (SmartStats technical white paper)</td>
<td>Chris Stucchio, Visual Website Optimizer (VWO), 2015, white paper</td>
<td>[https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf](https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf)</td>
<td>Explains Bayesian A/B testing with Beta-binomial posteriors, probability to beat control and expected loss decision rule as implemented in a commercial tool.</td>
<td>Reading for the Bayesian A/B testing lab (students implement expected-loss rule in Python). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Evolution of Experimentation: Lessons from 127,000 Experiments</td>
<td>Optimizely, 2023, industry report</td>
<td>[https://www.optimizely.com/insights/](https://www.optimizely.com/insights/)</td>
<td>Benchmark report from a major testing vendor: win rates, typical uplifts, test velocity and which test types (e.g. personalization, multi-variant) perform better. Vendor data, interpret critically.</td>
<td>Discussion material on realistic effect sizes and win rates; compare with Berman and Van den Bulte. Free with registration; check exact report URL.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>What Works in E-commerce: A Meta-Analysis of 6,700 Online Experiments</td>
<td>Will Browne, Mike Swarbrick Jones, Qubit, 2017, industry white paper</td>
<td>[https://scholar.google.com/scholar?q=What+works+in+e-commerce+a+meta-analysis+of+6700+online+experiments](https://scholar.google.com/scholar?q=What+works+in+e-commerce+a+meta-analysis+of+6700+online+experiments)</td>
<td>Meta-analysis of e-commerce A/B tests by treatment category (scarcity, social proof, urgency, cosmetic changes): most cosmetic changes have near-zero effect, scarcity and social proof have small positive effects.</td>
<td>Discussion on realistic effect sizes for retail website tests and on behavioural levers. Free; link is a Scholar search, original Qubit URL may have moved.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>A Comparison of Approaches to Advertising Measurement (MSI Report 18-113)</td>
<td>Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, Dan Chapsky, Marketing Science Institute Working Paper Series Report 18-113, 2018, report</td>
<td>[https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf](https://thearf-org-unified-admin.s3.amazonaws.com/MSI_Report_18-113.pdf)</td>
<td>Free report version of the Facebook conversion-lift study; describes Facebook's lift-test infrastructure and the gap between observational and experimental estimates. Freely downloadable alternative to the paywalled journal article.</td>
<td>Free substitute reading for students without journal access. Free PDF.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Websites (18)
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
<td>How Not To Run an A/B Test</td>
<td>Evan Miller, evanmiller.org, 2010, essay/reference page</td>
<td>[https://www.evanmiller.org/how-not-to-run-an-ab-test.html](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)</td>
<td>The classic short explanation of the peeking problem: checking a running test repeatedly and stopping at significance inflates the false positive rate from 5% to well above 20%. Includes the n = 16 sigma\^2/delta\^2 rule of thumb. Companion pages on the low base rate problem and sequential testing on the same site.</td>
<td>Pre-reading for the session on test duration and stopping rules; replicate the peeking simulation in Python as a lab. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Evan Miller's A/B Testing Tools: Sample Size Calculator</td>
<td>Evan Miller, evanmiller.org, interactive web tool (also chi-squared, sequential sampling and t-test tools)</td>
<td>[https://www.evanmiller.org/ab-testing/sample-size.html](https://www.evanmiller.org/ab-testing/sample-size.html)</td>
<td>Interactive calculator: enter baseline conversion rate, minimum detectable effect, power and alpha; returns sample size per variant. Widely used as the cross-check in CRO teams.</td>
<td>In-class demo before students compute the same numbers with statsmodels NormalIndPower; good for an exercise comparing relative vs absolute MDE. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Experiment Guide (companion site to Trustworthy Online Controlled Experiments)</td>
<td>Ron Kohavi, Diane Tang, Ya Xu, experimentguide.com, companion website to the Cambridge University Press book (2020)</td>
<td>[https://experimentguide.com/](https://experimentguide.com/)</td>
<td>Additional material, errata and free download of Chapter 1 in several languages (EN, ZH, RU, KO, PL). Chapter 1 gives the core vocabulary (OEC, randomisation unit, guardrails) plus motivating examples such as the Bing ad headline test.</td>
<td>Assign free Chapter 1 PDF as the opening reading; site as reference for students. Free (book itself paid, WU-Lizenz prüfen).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Microsoft Research Experimentation Platform (ExP): Articles</td>
<td>Microsoft Research, Experimentation Platform group, article series 2019-2026</td>
<td>[https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/)</td>
<td>Practitioner articles from the team that runs tens of thousands of experiments a year: Deep Dive Into Variance Reduction (2022), A/B Interactions: A Call to Relax (2023), External Validity of Online Experiments (2024), Event-based A/B tests, EU data protection and experimentation (2025). Includes the three-part Patterns of Trustworthy Experimentation series (pre-, during-, post-experiment).</td>
<td>Background reading for the advanced session (variance reduction, interactions, external validity); the EU data protection article fits a European IB audience. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Patterns of Trustworthy Experimentation: Pre-Experiment Stage</td>
<td>Microsoft Research ExP, 2020, article (part 1 of 3; during- and post-experiment parts linked)</td>
<td>[https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/patterns-of-trustworthy-experimentation-pre-experiment-stage/)</td>
<td>Checklist-style patterns for hypothesis and metric formulation and engineering choices that bias results; parts 2 and 3 cover SRM checks, monitoring and post-experiment learning. Very usable as a design checklist.</td>
<td>Use as checklist template for student experiment proposals (group project). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>statsmodels.stats.power: NormalIndPower.solve_power and proportion_effectsize</td>
<td>statsmodels developers, statsmodels.org, Python library documentation</td>
<td>[https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.solve_power.html](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.NormalIndPower.solve_power.html)</td>
<td>Reference for solving for sample size, power, MDE or alpha of a two-sample z-test; combined with proportion_effectsize (Cohen's h) this is the standard Python route for conversion-rate test planning. Also tt_ind_solve_power for continuous metrics such as revenue per visitor.</td>
<td>Core reference for the Python lab on sample size planning. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Causal Inference for the Brave and True, Chapter 2: Randomised Experiments</td>
<td>Matheus Facure (Nubank), free online book with Python notebooks, GitHub pages, 2021-2022</td>
<td>[https://matheusfacure.github.io/python-causality-handbook/02-Randomised-Experiments.html](https://matheusfacure.github.io/python-causality-handbook/02-Randomised-Experiments.html)</td>
<td>Light-hearted but rigorous open book; early chapters explain why randomisation solves selection bias and how to compute standard errors and CIs for A/B tests in Python; later chapters cover regression adjustment, heterogeneous effects and uplift, linking A/B testing to causal inference.</td>
<td>Reading plus notebooks for students who know pandas; bridges A/B testing to the causal inference block. Free, open source.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>GrowthBook Statistics documentation</td>
<td>GrowthBook (open-source experimentation platform), docs.growthbook.io, documentation</td>
<td>[https://docs.growthbook.io/statistics/overview](https://docs.growthbook.io/statistics/overview)</td>
<td>Clear documentation of a Bayesian (default) and frequentist engine, sequential testing, CUPED, SRM detection, multiple-comparison corrections and custom priors; the Statistical Details page shows the formulas. Good for showing how a real tool computes Chance to Win vs confidence intervals.</td>
<td>Reference when comparing Bayesian vs frequentist output; GrowthBook is open source so students can self-host for a project. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Optimizely Support: Statistical analysis methods overview (Stats Engine) and glossary</td>
<td>Optimizely, support.optimizely.com, knowledge base</td>
<td>[https://support.optimizely.com/hc/en-us/articles/39714777161229-Statistical-analysis-methods-overview](https://support.optimizely.com/hc/en-us/articles/39714777161229-Statistical-analysis-methods-overview)</td>
<td>Explains the three analysis modes Optimizely offers (fixed-horizon frequentist, Bayesian, sequential Stats Engine with false discovery rate control); glossary defines guardrail metrics, CUPED and other terms in marketer language.</td>
<td>Show students how a market-leading commercial tool frames statistics for marketers; compare with GrowthBook docs. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Statsig Docs: Power Analysis</td>
<td>Statsig, docs.statsig.com, product documentation</td>
<td>[https://docs.statsig.com/experiments/power-analysis](https://docs.statsig.com/experiments/power-analysis)</td>
<td>Documents how a power calculator uses a metric's historical mean, variance and traffic to trade off MDE, duration and allocation, with week-by-week projections. Sister page on SRM checks (docs.statsig.com/stats-engine/methodologies/srm-checks).</td>
<td>Reference for the planning step of a student experiment design; compare with own statsmodels calculation. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Eppo Docs: CUPED++</td>
<td>Eppo (Datadog), docs.geteppo.com, product documentation</td>
<td>[https://docs.geteppo.com/statistics/cuped/](https://docs.geteppo.com/statistics/cuped/)</td>
<td>Documentation of regression-based variance reduction using pre-experiment data and assignment properties; explains when CUPED helps and how CUPED++ extends it. Companion guide: running well-powered experiments with smaller samples.</td>
<td>Reference for the variance-reduction session alongside the Microsoft ExP deep dive. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Google Ads Help: Set up a custom experiment / Experiments page</td>
<td>Google, Google Ads Help Center, documentation</td>
<td>[https://support.google.com/google-ads/answer/6261395?hl=en](https://support.google.com/google-ads/answer/6261395?hl=en)</td>
<td>How marketers run split tests on campaigns: traffic split (recommended 50/50), cookie-based vs search-based split, fixed split after setup, scaled reporting for uneven splits. Shows A/B testing inside an ad platform rather than on a website. Related FAQ: support.google.com/google-ads/answer/13826584.</td>
<td>Marketing application session: discuss what randomisation unit Google uses and threats to validity in platform experiments. Free (Google Ads account needed to try).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Google Ads API: Experiments overview</td>
<td>Google, developers.google.com, API documentation</td>
<td>[https://developers.google.com/google-ads/api/docs/experiments/overview](https://developers.google.com/google-ads/api/docs/experiments/overview)</td>
<td>Developer view of campaign experiments including campaign mix experiments; useful to show that ad-platform tests are programmable and how arms and splits are defined.</td>
<td>Optional reference for data-science oriented students. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>VWO SmartStats: Bayesian A/B Testing at VWO (technical whitepaper)</td>
<td>Chris Stucchio, Visual Website Optimizer (VWO), whitepaper PDF, ca. 2015</td>
<td>[https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf](https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf)</td>
<td>Technical explanation of Beta-Binomial Bayesian testing, expected loss and decision rules as implemented in a commercial CRO tool; the PyMC Bayesian A/B notebook implements these models.</td>
<td>Reading for the Bayesian A/B session; pair with PyMC notebook. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>CXL: A/B Testing Statistics - An Easy-to-Understand Guide</td>
<td>CXL (ConversionXL), cxl.com blog/guide</td>
<td>[https://cxl.com/blog/ab-testing-statistics/](https://cxl.com/blog/ab-testing-statistics/)</td>
<td>Marketer-friendly explanation of mean, variance, significance, confidence intervals and sample size for conversion tests; companion articles on 10 statistics traps and analysing test results. Includes the CRO rule of thumb of at least 1,000 conversions per month.</td>
<td>Accessible pre-reading for business students before the formal statistics; discuss rules of thumb critically. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Sample Ratio Mismatch (SRM) Checker</td>
<td>Lukas Vermeer (formerly Director of Experimentation, Booking.com), lukasvermeer.nl, web tool and Chrome extension</td>
<td>[https://www.lukasvermeer.nl/srm/microsite/](https://www.lukasvermeer.nl/srm/microsite/)</td>
<td>Enter observed counts per variant to test for SRM with a chi-squared test; site links to the KDD paper on automated SRM detection. SRM occurs in roughly 6-10% of experiments even at big tech firms.</td>
<td>Lab exercise: students check an SRM by hand in scipy and verify with the tool. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Analytics-Toolkit.com: statistical tools for online A/B tests</td>
<td>Georgi Georgiev, Analytics-Toolkit.com, web tools (paid) with free calculators</td>
<td>[https://www.analytics-toolkit.com/](https://www.analytics-toolkit.com/)</td>
<td>Sequential (AGILE) test planning, power and sample-size calculators, non-binomial metric significance (e.g. average revenue per user). Companion book site abtestingstats.com.</td>
<td>Reference for sequential testing; some calculators free, full toolkit paid (subscription).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>e-dialog Signifikanzrechner für A/B- und multivariate Tests</td>
<td>e-dialog (Vienna-based digital marketing agency), e-dialog.group, German-language tool and guide</td>
<td>[https://e-dialog.group/at/whitepaper/signifikanzrechner-fur-a-b-und-multivariate-tests/](https://e-dialog.group/at/whitepaper/signifikanzrechner-fur-a-b-und-multivariate-tests/)</td>
<td>Austrian agency tool for chi-squared significance across up to 8 variants; accompanying blog post explains the three calculation steps in German. Local practice link for a Vienna audience.</td>
<td>German-language resource; possible local guest-speaker link. Free (may require form).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Blogs (21)
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
<td>Netflix Technology Blog: Decision Making at Netflix (multi-part series)</td>
<td>Martin Tingley et al., Netflix Technology Blog (Medium), 2021-2022, blog series (7 parts)</td>
<td>[https://netflixtechblog.com/decision-making-at-netflix-33065fa06481](https://netflixtechblog.com/decision-making-at-netflix-33065fa06481)</td>
<td>Accessible series: What is an A/B Test?, false positives and statistical significance, false negatives and power, building confidence in a decision, experimentation as a learning culture. Uses Netflix UI examples (artwork, rows) that students know.</td>
<td>Best non-technical intro series; assign parts 2-4 as weekly readings. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Netflix Technology Blog: Sequential A/B Testing Keeps the World Streaming (Part 1: Continuous Data)</td>
<td>Netflix Technology Blog (Medium), 2024, blog post</td>
<td>[https://netflixtechblog.com/sequential-a-b-testing-keeps-the-world-streaming-netflix-part-1-continuous-data-cba6c7ed49df](https://netflixtechblog.com/sequential-a-b-testing-keeps-the-world-streaming-netflix-part-1-continuous-data-cba6c7ed49df)</td>
<td>How Netflix uses anytime-valid sequential tests for software rollouts; good follow-up to Evan Miller's peeking essay. Related Netflix posts: Quasi Experimentation at Netflix, Interleaving for personalisation, Heterogeneous Treatment Effects at Netflix.</td>
<td>Advanced reading on sequential testing. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>How Booking.com increases the power of online experiments with CUPED</td>
<td>Simon Jackson, Booking.com data science, booking.ai (Medium), 2018, blog post</td>
<td>[https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d](https://booking.ai/how-booking-com-increases-the-power-of-online-experiments-with-cuped-995d186fff1d)</td>
<td>Retail/travel example of CUPED: as products mature, effects shrink and pre-experiment covariates are needed to detect them; includes R code intuition. Booking.com is the canonical experimentation-culture company.</td>
<td>Reading for variance reduction; students reimplement CUPED in Python on simulated data. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Spotify Engineering: Risk-Aware Product Decisions in A/B Tests with Multiple Metrics</td>
<td>Spotify Experimentation Platform team, engineering.atspotify.com, March 2024, blog post</td>
<td>[https://engineering.atspotify.com/2024/03/risk-aware-product-decisions-in-a-b-tests-with-multiple-metrics](https://engineering.atspotify.com/2024/03/risk-aware-product-decisions-in-a-b-tests-with-multiple-metrics)</td>
<td>How success, guardrail (non-inferiority), deterioration and quality metrics combine into one ship decision, with error-rate implications. Companion post: Choosing a Sequential Testing Framework (2023).</td>
<td>Discussion piece for the metrics and decision-rule session. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Spotify Confidence blog (Experiment like Spotify series)</td>
<td>Spotify, confidence.spotify.com/blog, company blog 2023-2026</td>
<td>[https://confidence.spotify.com/blog](https://confidence.spotify.com/blog)</td>
<td>Posts on experiment analysis, experiments with smaller samples, and when proxy metrics break; practical, product-oriented.</td>
<td>Supplementary reading; small-sample post useful for marketers with low traffic. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Beyond A/B Test: Speeding up Airbnb Search Ranking Experimentation through Interleaving</td>
<td>Qing Zhang, Michelle Du, Reid Andersen, Liwei He, The Airbnb Tech Blog (Medium), October 2022</td>
<td>[https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e](https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e)</td>
<td>Why low-frequency purchases (travel bookings) limit experiment bandwidth and how interleaving gave about 50x sensitivity for ranking tests. Good example of retail/marketplace constraints.</td>
<td>Case-style reading for the session on alternatives to classic A/B tests. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Zalando Engineering Blog: Experimentation Platform at Zalando, Part 1 - Evolution</td>
<td>Zalando Engineering, engineering.zalando.com, January 2021, blog post (tag page has further posts)</td>
<td>[https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html)</td>
<td>European fashion e-commerce: why Zalando built its own platform (Octopus), standardised randomisation and t-test analysis, internal A/B testing training. Related: Marketing A/B Testing at Zalando (location-based tests) and the open-source ExpAn Python library.</td>
<td>European retail example; good for IB students. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Etsy Code as Craft: Experimentation category</td>
<td>Etsy Engineering, etsy.com/codeascraft, company blog 2014-2024</td>
<td>[https://www.etsy.com/codeascraft/category/experimentation](https://www.etsy.com/codeascraft/category/experimentation)</td>
<td>Marketplace experimentation posts: How Etsy Handles Peeking in A/B Testing, Imbalance Detection, Double-bucketing, Control Variates for accuracy and speed, Interleaving, experiments with new visitors, collective impact of experiments.</td>
<td>Pick-and-choose readings; peeking post pairs with Evan Miller. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Under the Hood of Uber's Experimentation Platform</td>
<td>Uber Engineering Blog, uber.com/blog, 2018, blog post</td>
<td>[https://www.uber.com/us/en/blog/xp/](https://www.uber.com/us/en/blog/xp/)</td>
<td>Covers A/B/N tests, causal inference and multi-armed bandits for marketing campaigns and promotions; classifies metrics into proportion, continuous and ratio metrics (ratio metrics need delta method).</td>
<td>Overview reading on platform architecture and metric types. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Analytics-Toolkit Blog (Georgi Georgiev)</td>
<td>Georgi Georgiev, blog.analytics-toolkit.com, blog 2017-2026</td>
<td>[https://blog.analytics-toolkit.com/author/analytic/](https://blog.analytics-toolkit.com/author/analytic/)</td>
<td>Rigorous yet marketer-oriented posts: significance for non-binomial metrics (ARPU, AOV), one- vs two-tailed tests, sequential testing Q&A, interpretation mistakes. Author of Statistical Methods in Online A/B Testing.</td>
<td>Advanced readings for statistically keen students. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Eppo blog: CUPED and CUPED++ - Bending time in experimentation</td>
<td>Eppo, geteppo.com/blog, 2023, company blog post (also Eppo Substack)</td>
<td>[https://www.geteppo.com/blog/cuped-bending-time-in-experimentation](https://www.geteppo.com/blog/cuped-bending-time-in-experimentation)</td>
<td>Intuitive explanation of CUPED as regression adjustment and how much runtime it can save; companion post Reducing Experiment Durations.</td>
<td>Intuition reading before the technical Microsoft deep dive. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Statsig blog: A quick guide to sample ratio mismatch (SRM)</td>
<td>Statsig, statsig.com/blog, company blog post</td>
<td>[https://www.statsig.com/blog/sample-ratio-mismatch](https://www.statsig.com/blog/sample-ratio-mismatch)</td>
<td>What SRM is, how to detect it with a chi-squared test and common root causes (bots, redirects, logging). Statsig Perspectives hub has many short explainers (power, sample size).</td>
<td>Short reading for the data quality session. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Understanding CUPED (with Python code)</td>
<td>Matteo Courthoud, personal blog / Towards Data Science, 2022, blog post with notebook on GitHub</td>
<td>[https://matteocourthoud.github.io/post/cuped/](https://matteocourthoud.github.io/post/cuped/)</td>
<td>Shows CUPED is a residualised outcome regression, compares with difference-in-differences and regression adjustment on simulated data; code in github.com/matteocourthoud/Blog-Posts. Same author: Bayesian AB Testing post on priors.</td>
<td>Python lab template for variance reduction. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Bytepawn: A/B testing posts (Marton Trencseni)</td>
<td>Marton Trencseni, bytepawn.com, personal blog 2020-2025</td>
<td>[https://bytepawn.com/tag/ab-testing.html](https://bytepawn.com/tag/ab-testing.html)</td>
<td>Dozens of simulation-based Python posts: early stopping, five ways to reduce variance, CUPED and A/A false positives, A/B testing on social networks, review of the Gordon et al. advertising measurement paper (observational vs experimental lift).</td>
<td>Source of Monte Carlo exercises students can reproduce. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>The ultimate guide to A/B testing (Ronny Kohavi on Lenny's Newsletter/Podcast)</td>
<td>Lenny Rachitsky with Ronny Kohavi, Lenny's Newsletter, July 2023, newsletter post with transcript</td>
<td>[https://www.lennysnewsletter.com/p/the-ultimate-guide-to-ab-testing](https://www.lennysnewsletter.com/p/the-ultimate-guide-to-ab-testing)</td>
<td>Kohavi on when to start experimenting, building an experimentation culture, Twyman's law, typical success rates of ideas; transcript makes it citeable.</td>
<td>Reading or listening assignment; video version listed under tutorials. Free (some newsletter content paywalled).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>konversionsKRAFT: Statistik und Analytics fuer A/B-Tests (Data Science Rubrik)</td>
<td>konversionsKRAFT (Web Arts AG), konversionskraft.de, German-language CRO blog</td>
<td>[https://www.konversionskraft.de/data-science](https://www.konversionskraft.de/data-science)</td>
<td>German articles on Konfidenz and Signifikanz, test power (70% of A/B tests are underpowered), test planning, Bayesian revenue/uplift evaluation and 10 Statistik-Fallen beim Testing; includes free calculators.</td>
<td>German-language readings for students who prefer German; good for practitioner perspective. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>A/B-Testing: Der grosse Starter-Guide</td>
<td>t3n, t3n.de, German-language article</td>
<td>[https://t3n.de/news/ab-test-anleitung-600782/](https://t3n.de/news/ab-test-anleitung-600782/)</td>
<td>German practitioner guide with four-step process: identify problem, research factors, form hypothesis, build variant. Good for the hypothesis-design part, weak on statistics.</td>
<td>Short German warm-up reading; let students critique missing statistical planning. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>e-dialog Blog: Wann ist Ihr Testergebnis signifikant? Die Statistik hinter dem A/B-Test</td>
<td>e-dialog (Vienna), e-dialog.group/blog, German-language blog post</td>
<td>[https://e-dialog.group/blog/wann-ist-ihr-testergebnis-signifikant-die-statistik-hinter-dem-a-b-test/](https://e-dialog.group/blog/wann-ist-ihr-testergebnis-signifikant-die-statistik-hinter-dem-a-b-test/)</td>
<td>Austrian agency explains the chi-squared significance calculation in three steps (critical value 3.84 at 95%); note the common but imprecise interpretation of confidence, useful for a misconception discussion.</td>
<td>German reading; ask students to spot the p-value misinterpretation. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>A/B-Test: Wie berechne ich Stichproben und Testdauer?</td>
<td>Kameleoon, kameleoon.com/de/blog, German-language blog post</td>
<td>[https://www.kameleoon.com/de/blog/ab-test-wie-berechne-ich-stichproben-und-testdauer](https://www.kameleoon.com/de/blog/ab-test-wie-berechne-ich-stichproben-und-testdauer)</td>
<td>German explanation of sample size and test duration planning by a European A/B testing vendor; complements AB Tasty German post on statistische Signifikanz.</td>
<td>German supplementary reading for the planning session. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>AB Tasty Blog: Which Statistical Model is Best for A/B Testing - Bayesian, Frequentist, CUPED, or Sequential?</td>
<td>AB Tasty, abtasty.com/blog, company blog post</td>
<td>[https://www.abtasty.com/blog/best-statistical-model-for-ab-testing/](https://www.abtasty.com/blog/best-statistical-model-for-ab-testing/)</td>
<td>Vendor comparison of four analysis approaches; useful to show vendor framing (AB Tasty prefers Bayesian). German version of the significance article at abtasty.com/de/blog/statistische-signifikanz-a-b-tests/.</td>
<td>Critical reading: compare vendor claims with Kohavi/Georgiev. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Blogs</td>
<td>Experiment Nation (newsletter and podcast)</td>
<td>Rommil Santiago, Experiment Nation, Substack and podcast, ongoing</td>
<td>[https://experimentnation.substack.com/](https://experimentnation.substack.com/)</td>
<td>Community newsletter and podcast with interviews of CRO and experimentation practitioners; episode 47 features Ronny Kohavi on statistics concepts experimenters must know.</td>
<td>Optional listening; source of potential guest speakers. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### (Video-) Tutorials (19)
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
<td>A/B Testing (Introduction to A/B Testing) by Google</td>
<td>Carrie Grimes, Caroline Buckey, Diane Tang (Google), Udacity, MOOC, ca. 21 hours, beginner-intermediate</td>
<td>[https://www.udacity.com/course/ab-testing--ud257](https://www.udacity.com/course/ab-testing--ud257)</td>
<td>Five lessons: overview, policy and ethics, choosing and characterising metrics, designing an experiment (sizing, MDE), analysing results; final project with data. Still the most-cited free course; lesson 2 on ethics is rare elsewhere.</td>
<td>Self-study companion; assign lessons 3-5 before the corresponding sessions. Free (Udacity login).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B Testing in Python</td>
<td>Moe Lotfy, DataCamp, interactive course, 4 hours, intermediate</td>
<td>[https://www.datacamp.com/courses/ab-testing-in-python](https://www.datacamp.com/courses/ab-testing-in-python)</td>
<td>Four chapters: overview and metrics, design and planning (power, MDE, sample size), data processing, sanity checks and analysis of proportions, means and non-parametric tests; uses statsmodels, scipy and pingouin. Close match to a Python-based business course.</td>
<td>Homework track; DataCamp for the Classroom gives free access for instructors and students. Otherwise paid subscription (\~USD 25/month).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Customer Analytics and A/B Testing in Python</td>
<td>DataCamp, interactive course, ca. 4 hours</td>
<td>[https://www.classcentral.com/course/datacamp-customer-analytics-and-a-b-testing-in-python-24535](https://www.classcentral.com/course/datacamp-customer-analytics-and-a-b-testing-in-python-24535)</td>
<td>Combines KPI/customer analytics with A/B test design and analysis on a subscription-app case; good marketing framing.</td>
<td>Alternative DataCamp track; DataCamp Classroom free for teaching, else paid.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Accelerating Innovation with A/B Testing</td>
<td>Ronny Kohavi, Maven, live cohort course, 5 sessions x 2-2.5 hours over 2 weeks, practitioner level</td>
<td>[https://maven.com/kohavi](https://maven.com/kohavi)</td>
<td>The leading practitioner course: concepts, culture, trust, pitfalls with examples from Amazon, Microsoft, Airbnb; 30+ cohorts. Not for students but ideal instructor upskilling.</td>
<td>Instructor preparation; paid (several hundred to ca. USD 2,000 per seat, check current price on Maven).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>The ultimate guide to A/B testing \| Ronny Kohavi (Airbnb, Microsoft, Amazon)</td>
<td>Lenny's Podcast, YouTube, 2023, video interview ca. 1.5 hours</td>
<td>[https://www.youtube.com/watch?v=hEzpiDuYFoE](https://www.youtube.com/watch?v=hEzpiDuYFoE)</td>
<td>Wide-ranging interview: experimentation culture, OEC, Twyman's law, failure rates of ideas, institutional memory. Transcript on lennysnewsletter.com for picking segments.</td>
<td>Clip segments for the opening session; full episode as optional viewing. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B Testing Statistics Concepts Experimenters must know with Ronny Kohavi</td>
<td>Experiment Nation, YouTube, video talk/interview</td>
<td>[https://www.youtube.com/watch?v=tH4tjpbziCo](https://www.youtube.com/watch?v=tH4tjpbziCo)</td>
<td>Kohavi on p-value misinterpretation, false positive risk, power, SRM and variance reduction; statistics-focused complement to the Lenny interview.</td>
<td>Video for the inference session. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Ronny Kohavi YouTube channel</td>
<td>Ronny Kohavi, YouTube channel</td>
<td>[https://www.youtube.com/c/RonnyKohavi](https://www.youtube.com/c/RonnyKohavi)</td>
<td>Collects Kohavi's talks and course trailers; his talks page robotics.stanford.edu/\~ronnyk/ronnyk-talks.html lists slide decks such as Pitfalls in Online Controlled Experiments (CODE@MIT 2016) and Metric Pitfalls (CODE@MIT 2017).</td>
<td>Browse for talks to embed. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Statistical Power, Clearly Explained!!!</td>
<td>Josh Starmer, StatQuest, YouTube, ca. 8 minutes, beginner</td>
<td>[https://www.youtube.com/watch?v=Rsc5znwR5FA](https://www.youtube.com/watch?v=Rsc5znwR5FA)</td>
<td>Visual explanation of power via overlapping distributions; follow-up video Power Analysis, Clearly Explained. StatQuest p-value videos also fit.</td>
<td>Flipped-classroom video before the sample-size lab. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B Testing in Data Science (playlist)</td>
<td>Emma Ding, Data Interview Pro, YouTube playlist, multiple videos 10-25 minutes, intermediate</td>
<td>[https://www.youtube.com/playlist?list=PLY1Fi4XflWSvgsaD9eXng6N5kxcMtcxGK](https://www.youtube.com/playlist?list=PLY1Fi4XflWSvgsaD9eXng6N5kxcMtcxGK)</td>
<td>Interview-oriented but compact explanations of experiment design, metrics, sample size, novelty and network effects, common analysis mistakes. Key video: Crack A/B Testing Problems for Data Science Interviews (youtube.com/watch?v=X8u6kr4fxXc).</td>
<td>Review material before exams; motivates students with career relevance. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B Testing Course: A/B Test like a Pro! (full course)</td>
<td>Tomi Mester, Data36, YouTube playlist, 2021, 37 videos ca. 3 hours, beginner</td>
<td>[https://www.youtube.com/playlist?list=PLHS1p0ot3SVjQg0q1eEPrmOmPUY_AT1vB](https://www.youtube.com/playlist?list=PLHS1p0ot3SVjQg0q1eEPrmOmPUY_AT1vB)</td>
<td>Free beginner course from an online-business perspective: success metrics, hypotheses, test design, evaluation; course site data36.com/ab-testing-course-ab-test-like-a-pro/ has materials.</td>
<td>Entry-level self-study for students without statistics background. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Easy as ABC: A Quick Introduction to Bayesian A/B Testing in Python</td>
<td>Will Barker, YouTube, conference talk, beginner-intermediate</td>
<td>[https://www.youtube.com/watch?v=nRLI_KbvZTQ](https://www.youtube.com/watch?v=nRLI_KbvZTQ)</td>
<td>Beta-Binomial Bayesian A/B testing in Python with probability-to-beat-control; good bridge to the PyMC notebook.</td>
<td>Video for the Bayesian session. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Usable A/B testing - A Bayesian approach (PyData Berlin 2016)</td>
<td>PyData Berlin 2016, PyVideo, conference talk recording</td>
<td>[https://pyvideo.org/pydata-berlin-2016/usable-ab-testing-a-bayesian-approach.html](https://pyvideo.org/pydata-berlin-2016/usable-ab-testing-a-bayesian-approach.html)</td>
<td>Why conventional results are hard to interpret for stakeholders and a visual Bayesian alternative; Berlin e-commerce context.</td>
<td>Optional video for Bayesian A/B. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Introduction to Bayesian A/B Testing (PyMC example notebook)</td>
<td>PyMC developers (Cuong Duong), PyMC example gallery, 2021, Jupyter notebook</td>
<td>[https://www.pymc.io/projects/examples/en/latest/causal_inference/bayesian_ab_testing_introduction.html](https://www.pymc.io/projects/examples/en/latest/causal_inference/bayesian_ab_testing_introduction.html)</td>
<td>Implements the VWO whitepaper models: Beta-Binomial conversion model, prior predictive checks, revenue model, multi-variant tests, with code.</td>
<td>Lab notebook for the Bayesian session (students run in Colab). Free, open source.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>CausalML documentation and example notebooks (uplift modelling, meta-learners)</td>
<td>Uber, causalml.readthedocs.io, Python package documentation with notebooks</td>
<td>[https://causalml.readthedocs.io/en/latest/examples.html](https://causalml.readthedocs.io/en/latest/examples.html)</td>
<td>Notebooks on S/T/X/R-learners, uplift trees, uplift curves and validation with TMLE; shows how experiment data feed targeting decisions (who to send a coupon to). Related talk: Juan Camilo Orduz, Introduction to Uplift Modeling, PyConDE and PyData Berlin 2022 (juanitorduz.github.io/uplift/).</td>
<td>Advanced lab: from average treatment effect to targeted marketing. Free, open source.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>CODE@MIT 2024 (Conference on Digital Experimentation) - YouTube playlist</td>
<td>MIT Initiative on the Digital Economy, YouTube playlist, 2024 conference recordings</td>
<td>[https://www.youtube.com/playlist?list=PLNmZUX7tW6t9w6oXVpr72fMpVT9Ie_32J](https://www.youtube.com/playlist?list=PLNmZUX7tW6t9w6oXVpr72fMpVT9Ie_32J)</td>
<td>Research and industry talks on digital experimentation (interference, marketplaces, advertising lift, adaptive experiments). Earlier years on ide.mit.edu event pages; 2019 fireside chat at youtube.com/watch?v=gfXlpdnFlmM.</td>
<td>Pick one academic talk for a research-oriented session or thesis students. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B Testing in a Marketing Campaign (Python) - Kaggle notebook</td>
<td>Kaggle community notebook (seanlayer), uses Kaggle Marketing A/B Testing dataset</td>
<td>[https://www.kaggle.com/code/seanlayer/a-b-testing-in-a-marketing-campaign-python](https://www.kaggle.com/code/seanlayer/a-b-testing-in-a-marketing-campaign-python)</td>
<td>Worked analysis of an ad vs PSA marketing experiment with conversion tests; Kaggle also hosts Cookie Cats retention A/B notebooks. Quality varies, useful as critique material.</td>
<td>Lab starter; ask students to find and fix analysis weaknesses (e.g. no power analysis, SRM). Free (Kaggle login to run).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>The Math Behind A/B Testing with Example Python Code</td>
<td>Nguyen Ngo, Towards Data Science (Medium), 2018, written tutorial with code</td>
<td>[https://medium.com/data-science/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f](https://medium.com/data-science/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f)</td>
<td>Classic tutorial deriving the two-proportion z-test, power and sample size from Bernoulli/binomial and CLT with plotting code; very close to what a stats-for-business lab needs.</td>
<td>Lab handout basis. Free (Medium metered paywall possible).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Run Smart A/B Tests (Coursera short course)</td>
<td>Coursera, short course for marketing professionals, beginner</td>
<td>[https://www.coursera.org/learn/run-smart-ab-tests](https://www.coursera.org/learn/run-smart-ab-tests)</td>
<td>Email-marketing focused A/B testing: hypothesis-driven design, test parameters, analysis. Light on statistics but squarely in marketing practice.</td>
<td>Optional marketing-practice module; audit free, certificate paid.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>A/B-Testing im Online-Shop (Webinar)</td>
<td>conversionboosting, conversionboosting.com, German-language webinar recording</td>
<td>[https://conversionboosting.com/webinare/ab-testing-online-shop/](https://conversionboosting.com/webinare/ab-testing-online-shop/)</td>
<td>German e-commerce webinar on running A/B tests in online shops; same site has a Leitfaden for A/B tests on product detail pages.</td>
<td>German practitioner input for the retail application session. Free (registration may be required).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Cases for Teaching (20)
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
<td>Booking.com</td>
<td>Stefan Thomke and Daniela Beyersdorfer, Harvard Business School Case 619-015, October 2018, case, 28 pages; Teaching Note 620-080 (2020); distributed via HBP and The Case Centre</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=55158](https://www.hbs.edu/faculty/Pages/item.aspx?num=55158)</td>
<td>Flagship teaching case on large-scale online experimentation: how Booking.com runs thousands of concurrent A/B tests, democratised testing (about 75 percent of core staff can launch tests), failure rates of experiments, culture and governance vs. design intuition. Good for discussing experimentation culture, guardrail metrics and when not to test. Teaching note exists (620-080). No dataset.</td>
<td>Opening case discussion for the experimentation block; pair with Kohavi/Thomke HBR 2017 and the HBR IdeaCast 'At Booking.com, Innovation Means Constant Failure'. Paid, HBP educator account, approx. USD 5 per student copy; per Kurs zu lizenzieren. Also listed at The Case Centre: [https://www.thecasecentre.org/products/view?id=157117](https://www.thecasecentre.org/products/view?id=157117)</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Experimentation at Yelp</td>
<td>Iavor Bojinov and Karim R. Lakhani, Harvard Business School Case 621-064, October 2020 (revised March 2024), case, 20 pages</td>
<td>[https://hbsp.harvard.edu/product/621064-PDF-ENG](https://hbsp.harvard.edu/product/621064-PDF-ENG)</td>
<td>Yelp's path from ad-hoc team tests to a central experimentation platform, plus a pivotal experiment on geographically constrained ads with a trade-off between user experience and revenue that the protagonist must resolve. Good for metric choice (OEC vs. guardrails), platform build vs. buy, and decision-making under conflicting results.</td>
<td>Case discussion after the basics of A/B testing; decision question works well as a vote at the start of class. Paid, HBP educator account, approx. USD 5 per student copy; per Kurs zu lizenzieren; teaching note availability check on HBP.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Orchadio's First Two Split Experiments</td>
<td>Iavor Bojinov, Marco Iansiti and David Lane, Harvard Business School Case 622-015, August 2021, case</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=61073](https://www.hbs.edu/faculty/Pages/item.aspx?num=61073)</td>
<td>Direct-to-consumer grocery e-commerce firm plans its first two A/B tests: a redesigned website (functionality and effectiveness) and four banner variants. Uses feature flags (Split platform). Managers must decide test design and whether/how to sequence the experiments. Very close to a typical retail/marketing setting; good for hypothesis, metrics, sample size, interaction of concurrent tests.</td>
<td>Beginner-friendly case for designing an A/B test before any statistics; students draft an experiment plan in groups. Paid, HBP, approx. USD 5 per student copy; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Innovation at Uber: The Launch of Express POOL</td>
<td>Chiara Farronato, Alan D. MacCormack and Sarah Mehta, Harvard Business School Case 619-003, 2018, case</td>
<td>[https://www.thecasecentre.org/products/view?id=162387](https://www.thecasecentre.org/products/view?id=162387)</td>
<td>Describes a five-week synthetic control experiment (Feb 2018, six US cities) testing an extension of the matching window from two to five minutes: 5.2 percent more double matches, 7.4 percent fewer single matches. Shows why simple user-level A/B tests fail in two-sided marketplaces (interference) and how city-level or synthetic control designs help; efficiency vs. customer experience trade-off.</td>
<td>Advanced session on experiments beyond simple A/B (interference, switchbacks, synthetic controls). Paid, HBP/Case Centre, approx. USD 5 per student copy; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>A/B Testing at Vungle</td>
<td>Yael Grushka-Cockayne, Kenneth C. Lichtendahl Jr. (Darden), Bert De Reyck and Ioannis Fragkos (UCL), Darden Business Publishing UVA-QA-0821, 2015, case; teaching note UVA-QA-0821TN (5 pages)</td>
<td>[https://store.darden.virginia.edu/ab-testing-at-vungle-1](https://store.darden.virginia.edu/ab-testing-at-vungle-1)</td>
<td>Two recent MBA graduates built a new ad-serving algorithm for a mobile ad network that seems to beat the incumbent; students must evaluate the A/B 'horse race' with hypothesis tests on profitability. Written explicitly for a course covering hypothesis testing, so it maps directly onto a quantitative A/B testing lesson. Teaching note available; check for student spreadsheet.</td>
<td>Lab case: students replicate the test in Python (two-proportion test, revenue per impression). Paid, Darden Business Publishing or The Case Centre ([https://www.thecasecentre.org/products/view?id=127736](https://www.thecasecentre.org/products/view?id=127736)); per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Advertising Experiments at the Ohio Art Company</td>
<td>Rajkumar Venkatesan and Paul W. Farris, Darden Business Publishing UVA-M-0752, 2007, case with student spreadsheet and teaching note</td>
<td>[https://store.darden.virginia.edu/advertising-experiments-at-the-ohio-art-company](https://store.darden.virginia.edu/advertising-experiments-at-the-ohio-art-company)</td>
<td>Two real advertising field experiments of a toy maker (Etch A Sketch) with retailer partners; discusses measuring return on marketing and the biases that threaten causal inference in field experiments (non-random markets, confounding, spillover). Student spreadsheet included, so it doubles as a data exercise on offline/retail experiments.</td>
<td>Bridge from online A/B tests to retail/advertising field experiments; spreadsheet can be analysed in Python. Paid, Darden or The Case Centre ([https://www.thecasecentre.org/products/view?id=83359](https://www.thecasecentre.org/products/view?id=83359)); per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Designing Marketing Experiments (technical note)</td>
<td>Rajkumar Venkatesan, Darden Business Publishing UVA-M-0839, August 2012, technical note</td>
<td>[https://store.darden.virginia.edu/designing-marketing-experiments-3](https://store.darden.virginia.edu/designing-marketing-experiments-3)</td>
<td>Short technical note used in Darden's core marketing and marketing analytics courses: test and control design, randomisation, measuring lift. Designed to pair with the Ohio Art case.</td>
<td>Pre-reading for business students before the first experiment case. Paid, Darden; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Winning an Election (Obama 2008 splash page experiment)</td>
<td>Vishal Gupta, USC Marshall School of Business, BUAD 425 course case, PDF, year not stated</td>
<td>[http://faculty.marshall.usc.edu/Vishal-Gupta/Papers/Election_Case.pdf](http://faculty.marshall.usc.edu/Vishal-Gupta/Papers/Election_Case.pdf)</td>
<td>Free short classroom case built on the Obama 2008 campaign's multivariate test of the donation splash page (4 buttons x 6 media, 310,382 visitors). Lets students analyse a factorial A/B/n test and compute the business value of the winner.</td>
<td>Free warm-up or homework case; works with Python for multiple-comparison discussion. Free PDF; check whether data are included.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Pilgrim Bank (A): Customer Profitability</td>
<td>Frances X. Frei and Dennis Campbell, Harvard Business School Case 602-104, October 2001 (revised October 2017), case with Excel dataset; sequels (B) Customer Retention and (C) Electronic Billpay</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=28546](https://www.hbs.edu/faculty/Pages/item.aspx?num=28546)</td>
<td>Classic data case: does online banking make customers more profitable? Data are observational, not randomised, so students meet selection bias and see why an experiment would be needed. Regression, sampling, profitability. Useful as the contrast case 'what if you cannot randomise'.</td>
<td>Python lab on observational vs. experimental evidence; follow with a discussion of how Pilgrim could design a field experiment. Paid, HBP approx. USD 5 per student copy; per Kurs zu lizenzieren; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>J.C. Penney's 'Fair and Square' Pricing Strategy</td>
<td>Elie Ofek and Jill Avery, Harvard Business School Case 513-036, September 2012 (revised January 2013), case; abridged version 514-063; supplements (B) and (C)</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=43132](https://www.hbs.edu/faculty/Pages/item.aspx?num=43132)</td>
<td>CEO Ron Johnson's rollout of everyday low pricing without prior market tests; sales collapsed. The famous quote that Apple did not test is the hook for discussing why pricing changes should be piloted in test stores or online price experiments. Strategy case, no dataset.</td>
<td>Motivational case on 'the cost of not testing'; ask students to design the test JCPenney should have run (store-level randomisation, duration, metrics). Paid, HBP approx. USD 5 per student copy; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Building an e-Commerce Brand at Wayfair</td>
<td>Thales S. Teixeira and Elizabeth Anne Watkins, Harvard Business School Case 516-028, August 2015, case</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=49570](https://www.hbs.edu/faculty/Pages/item.aspx?num=49570)</td>
<td>Online furniture retailer decides on its advertising budget (TV brand advertising vs. performance marketing) and on how to measure its effect. Useful entry point to incrementality and why attribution data mislead; experiment design is a discussion extension rather than the case's main content.</td>
<td>Case discussion on advertising measurement; extension task: design a geo or holdout test for Wayfair's TV campaign. Paid, HBP approx. USD 5 per student copy; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Marketplace Tutorial: Price Elasticity in Practice</td>
<td>Harvard Business Publishing Education, product MP0035-HTM-ENG, interactive tutorial; also in Marketplace Tutorial Bundle: Pricing (MP0059)</td>
<td>[https://hbsp.harvard.edu/product/MP0035-HTM-ENG](https://hbsp.harvard.edu/product/MP0035-HTM-ENG)</td>
<td>Interactive exercise in which students run a pricing experiment and use the experiment data to estimate price elasticity of demand. A safe environment to practise price tests before discussing real price experiments.</td>
<td>In-class or homework exercise for the price-experiment session. Paid, HBP per student licence; per Kurs zu lizenzieren.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Udacity A/B Testing (by Google): Final Project 'Free Trial Screener'</td>
<td>Udacity in collaboration with Google, free online course (ud257), final project with real experiment data</td>
<td>[https://www.classcentral.com/course/udacity-a-b-testing-3528](https://www.classcentral.com/course/udacity-a-b-testing-3528)</td>
<td>Real Udacity experiment: after clicking 'start free trial', users were asked how many hours they can study; under 5 hours they were nudged to the free materials. Students choose invariant and evaluation metrics, compute variability, sample size and duration, run sanity checks and sign tests, and make a launch decision. Many worked solutions on GitHub and Medium for instructor reference.</td>
<td>Complete free lab or graded project in Python; ideal end-to-end exercise for business students. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Cookie Cats mobile game A/B test (gate 30 vs. gate 40)</td>
<td>Tactile Entertainment data, originally a DataCamp project, Kaggle dataset; many public GitHub analyses</td>
<td>[https://github.com/Paramartha248/mobile-game-retention-analysis](https://github.com/Paramartha248/mobile-game-retention-analysis)</td>
<td>90,189 players randomised to gate_30 or gate_40; variables sum_gamerounds, retention_1, retention_7. Moving the gate to level 40 lowered 7-day retention from 19.0 to 18.2 percent (significant), so the change should not ship. Great for proportions tests, bootstrap, outliers in engagement data and the 'counter-intuitive result' discussion.</td>
<td>First Python lab on A/B test analysis (60-90 min); exam-style question possible. Free; Kaggle login for download.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Marketing A/B Testing dataset (ad vs. PSA)</td>
<td>Favio Vazquez, Kaggle dataset, open</td>
<td>[https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)</td>
<td>588,101 users, 96 percent saw the ad and 4 percent a public service announcement (holdout control); variables converted, total_ads, most_ads_day, most_ads_hour. Ad group converts 2.55 vs. 1.79 percent (about 43 percent relative lift). Good for holdout/incrementality logic, unbalanced allocation and dose-response pitfalls (total_ads is post-treatment).</td>
<td>Python lab on incrementality testing; discussion question: is the ad worth its cost? Free; Kaggle login.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Advanced A/B Testing Workshop (Marketing Analytics Summit 2019)</td>
<td>Elea McDonnell Feit (Drexel), GitHub repository eleafeit/ab_test, workshop materials with code and data</td>
<td>[https://github.com/eleafeit/ab_test](https://github.com/eleafeit/ab_test)</td>
<td>Hands-on workshop on analysing marketing experiments (email/website tests), heterogeneous effects and test planning, by a leading marketing experiments researcher. Code is R, but data and logic port easily to Python. Related: Test & Roll replication files (github.com/eleafeit/testandroll) for profit-maximising test sizes.</td>
<td>Instructor material and lab template; students translate one notebook to Python. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>HBS publications search: A/B testing (case finder)</td>
<td>Harvard Business School Faculty & Research, publications filtered by keyword 'A/b Testing'</td>
<td>[https://www.hbs.edu/faculty/research/publications/Pages/default.aspx?q=A/b](https://www.hbs.edu/faculty/research/publications/Pages/default.aspx?q=A/b)</td>
<td>Running list of HBS cases, notes and articles tagged A/B testing; useful to check for newer experimentation cases (e.g. by Bojinov, Thomke, Farronato) before each semester.</td>
<td>Instructor tool for case selection; then buy via HBP. Free to browse.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>bauMax - ISMS Practice Prize 2005 video (dynamic pricing and promotion planning)</td>
<td>Natter, Reutterer, Mild, Taudes with bauMax, ISMS/Lilien Practice Prize video archive, 2005, video case; Österreich</td>
<td>[https://lilienpracticeprizevideos.org/baumax/](https://lilienpracticeprizevideos.org/baumax/)</td>
<td>Recorded practice-prize presentation of the bauMax pricing system: how model-based price changes were rolled out in rounds and evaluated against benchmarks inside an Austrian retailer; also on YouTube (BauMax - 2005 ISMS Practice Prize). Lesson: organisational side of testing (getting management to accept test rounds, measuring profit not just sales).</td>
<td>Video case (approx. 20-30 min) before discussing the Marketing Science paper; teaching-case substitute with Austrian context; possible guest-talk lead via WU (Reutterer). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>A/B Testing in action: Trivago case study (take-home analysis)</td>
<td>Nidhal (nidhalios), personal blog/GitHub, 2016, student-style case analysis; trivago, Düsseldorf, Deutschland</td>
<td>[https://nidhalios.github.io/AB-Testing-Trivago-post/](https://nidhalios.github.io/AB-Testing-Trivago-post/)</td>
<td>Worked analysis of a trivago A/B testing case task (data-based). trivago tech blog adds context: in-house C-test analytics app, example hypothesis of ranking hotels by city-centre distance vs. relevance, and a 2023 post on simulations to shorten A/B tests (tech.trivago.com). Evidence thin: unofficial write-up, verify data origin before class use.</td>
<td>Lab exercise template: students replicate the analysis; pair with trivago tech blog. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Case Study zu KPIs beim A/B-Testing: Conversion, Retouren, Deckungsbeitrag</td>
<td>konversionsKRAFT (Invesp/Web Arts), with BI partner nextel, undated, German agency case study; Deutschland</td>
<td>[https://www.konversionskraft.de/conversion-optimierung/conversion-deckungsbeitrag-case-study.html](https://www.konversionskraft.de/conversion-optimierung/conversion-deckungsbeitrag-case-study.html)</td>
<td>German fashion e-commerce test where the winning variant raised add-to-cart by 244 percent and orders through checkout by 43 percent, then examined whether returns eat up the uplift, measuring contribution margin instead of conversion. konversionsKRAFT also documents shoe retailer GÖRTZ (+5.7 percent revenue via value propositions; untested rollout could have cost up to -8.7 percent conversion). Agency sources, selective reporting likely. Lesson: choosing the right OEC in retail with high return rates.</td>
<td>German-language mini-case for the session on metrics/OEC; students argue conversion vs. margin. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Praxisbeispiele (37)
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
<td>Bing ad headline test: 12 percent revenue, over USD 100 million per year</td>
<td>Ron Kohavi and Stefan Thomke, 'The Surprising Power of Online Experiments', Harvard Business Review, Sept-Oct 2017 (reprint R1705E)</td>
<td>[https://hbr.org/2017/09/the-surprising-power-of-online-experiments](https://hbr.org/2017/09/the-surprising-power-of-online-experiments)</td>
<td>A shelved low-priority idea (lengthening ad title lines) was finally A/B tested and raised revenue by 12 percent, over USD 100M per year in the US, without hurting user-experience metrics; Bing's best revenue idea ever. Article also covers 10-25 percent annual revenue-per-search gains from many small tests, and the low success rate of ideas. Free reprint PDF via NYU Stern: [https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf](https://web-docs.stern.nyu.edu/executive/The%20Surprising%20Power%20of%20Online%20Experiments.pdf)</td>
<td>Warm-up story for session 1 and required reading. HBR paywall; WU-Lizenz prüfen (Business Source); free PDF copy exists.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Obama 2008 campaign: the USD 60 million splash page experiment</td>
<td>Dan Siroker (Director of Analytics, Obama 2008; later Optimizely co-founder), Optimizely blog</td>
<td>[https://www.optimizely.com/insights/blog/how-obama-raised-60-million-by-running-a-simple-experiment/](https://www.optimizely.com/insights/blog/how-obama-raised-60-million-by-running-a-simple-experiment/)</td>
<td>Full-factorial test of 4 buttons x 6 media (Google Website Optimizer), 310,382 visitors, about 13,000 per cell. 'Learn More' button plus family photo: 11.6 vs. 8.26 percent sign-up (+40.6 percent). Extrapolated to 2.88M extra emails, 288,000 volunteers and USD 60M donations. Lesson: videos the staff loved performed worst.</td>
<td>Warm-up and calculation exercise (back out the value per email). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Facebook ad lift studies vs. observational methods</td>
<td>Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, 'A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook', Marketing Science 38(2), 193-225, 2019</td>
<td>[https://ideas.repec.org/a/inm/ormksc/v38y2019i2p193-225.html](https://ideas.repec.org/a/inm/ormksc/v38y2019i2p193-225.html)</td>
<td>12 US Facebook conversion lift RCTs (435M user-study observations, 1.4B impressions) compared with exposed vs. unexposed, matching, regression adjustment, matched-market and before-after estimates; observational methods often miss the experimental lift, sometimes by a factor of three, even with thousands of covariates. Free Kellogg white paper version available.</td>
<td>Reading for the advertising measurement session; table of estimates is a strong exam discussion item. Journal paywalled, WU-Lizenz prüfen; free white paper at kellogg.northwestern.edu.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Where A/B testing goes wrong: divergent delivery in ad platform tests</td>
<td>Michael Braun and Eric M. Schwartz, Journal of Marketing, 2025</td>
<td>[https://journals.sagepub.com/doi/10.1177/00222429241275886](https://journals.sagepub.com/doi/10.1177/00222429241275886)</td>
<td>Shows that A/B tests run inside Meta/Google ad tools deliver each ad to differently optimised audiences, so the comparison is not randomised between creatives; what such tests can and cannot tell marketers. Very relevant pitfall for students who will use platform 'experiments'.</td>
<td>Pitfalls session; short in-class reading of the managerial summary. Paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Artwork Personalization at Netflix</td>
<td>Netflix Technology Blog, 2017</td>
<td>[https://netflixtechblog.com/artwork-personalization-c589f074ad76](https://netflixtechblog.com/artwork-personalization-c589f074ad76)</td>
<td>Netflix tests and personalises title artwork per member using contextual bandits after classic A/B tests showed artwork drives viewing choices; rolled out to 130M+ members, most helpful for lesser-known titles. Bridges A/B tests to bandits and personalisation; good discussion of metrics (take rate vs. watch time).</td>
<td>Example for creative testing and the step from A/B to bandits. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Experiments at Airbnb (price filter test and peeking)</td>
<td>Airbnb Engineering and Data Science blog (Jan Overgoor), nerds.airbnb.com, about 2014; follow-ups 'Experiment Reporting Framework' and 'Scaling Airbnb's Experimentation Platform' on Medium</td>
<td>[http://nerds.airbnb.com/experiments-at-airbnb/](http://nerds.airbnb.com/experiments-at-airbnb/)</td>
<td>Test raising the search price filter maximum from USD 300 to 1000; shows how p-values cross the 0.05 line early and then drift back (peeking), why to wait for convergence, and how to segment results by browser to detect bugs. Ideal pitfall illustration with real plots.</td>
<td>Pitfalls session (peeking, novelty, segment bugs); pair with a Python simulation of repeated significance testing. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Avoid the Pitfalls of A/B Testing (LinkedIn and Netflix)</td>
<td>Iavor Bojinov, Guillaume Saint-Jacques and Martin Tingley, Harvard Business Review 98(2), 48-53, March-April 2020</td>
<td>[https://hbr.org/2020/03/avoid-the-pitfalls-of-a-b-testing](https://hbr.org/2020/03/avoid-the-pitfalls-of-a-b-testing)</td>
<td>Three practitioner pitfalls with LinkedIn and Netflix examples: averages hide segment effects (heterogeneity), network interference between connected customers, and short tests missing changing reactions over time (novelty/primacy).</td>
<td>Short reading for pitfalls session. HBR paywall; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>OkCupid: 'We Experiment On Human Beings!'</td>
<td>Christian Rudder, OkCupid OkTrends blog, July 2014; coverage by Forbes (Kashmir Hill) and TIME</td>
<td>[https://www.forbes.com/sites/kashmirhill/2014/07/28/okcupid-experiment-compatibility-deception/](https://www.forbes.com/sites/kashmirhill/2014/07/28/okcupid-experiment-compatibility-deception/)</td>
<td>Dating site told poorly matched pairs they were a 90 percent match (and vice versa) to test the power of suggestion; also 'Love is Blind' day without photos. Rudder argued every website experiments on users. Strong contrast for consent, deception and the business-research boundary.</td>
<td>Ethics discussion (10-15 minutes), possibly a role play with the Facebook case. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Experimentation Platform at Zalando: Part 1 - Evolution (Octopus)</td>
<td>Zalando Engineering Blog, January 2021</td>
<td>[https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html](https://engineering.zalando.com/posts/2021/01/experimentation-platform-part1.html)</td>
<td>How Europe's largest online fashion retailer (Berlin) moved from team-by-team manual tests to the central platform Octopus (2015), with standardised randomisation and two-sided t-tests at 5 percent; links to the open-source Python library ExpAn. Close-to-home DACH retail example.</td>
<td>Example for the 'experimentation organisation' session; ExpAn can be shown in the Python lab. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Marketing A/B Testing at Zalando: location-based tests for marketing</td>
<td>Zalando data scientists, Towards Data Science (Medium)</td>
<td>[https://medium.com/data-science/marketing-a-b-testing-at-zalando-c069195bfe14](https://medium.com/data-science/marketing-a-b-testing-at-zalando-c069195bfe14)</td>
<td>Why user-level randomisation does not work for many marketing channels and how Zalando uses location (geo) based A/B tests to measure marketing incrementality. Good link between online A/B tests and geo experiments for campaigns.</td>
<td>Reading for the advertising incrementality session. Free (Medium metered).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>A/B testing at Zalando: concepts and tools (PyData Berlin 2018)</td>
<td>Shan Huang and Grigory Bordyugov, Zalando, PyData Berlin 2018 talk, YouTube recording</td>
<td>[https://www.youtube.com/watch?v=wmEAUfkLk50](https://www.youtube.com/watch?v=wmEAUfkLk50)</td>
<td>Practitioner talk on concepts (metrics, power, sequential testing) and the Python tools used at Zalando; good bridge to a Python-based course.</td>
<td>Optional video for students; excerpt in class. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Is A/B testing effective? Evidence from 35,000 startups</td>
<td>Rembrand Koning, Sharique Hasan and Aaron Chatterji, 'Experimentation and Start-up Performance: Evidence from A/B Testing', Management Science 68(9), 6434-6453, 2022; HBS Working Knowledge summary</td>
<td>[https://www.library.hbs.edu/working-knowledge/is-ab-testing-effective-evidence-from-35000-startups](https://www.library.hbs.edu/working-knowledge/is-ab-testing-effective-evidence-from-35000-startups)</td>
<td>Panel of 35,262 startups (2015-2019): adopters of A/B testing tools see 30 to 100 percent performance gains after a year and both scale and fail faster. Evidence for the business value of experimentation, plus a nice discussion of how the authors identify a causal effect without an experiment.</td>
<td>Short reading on the value of experimentation; meta-discussion of methods. Summary free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Lessons from More Than 1,000 E-Commerce Pricing Tests</td>
<td>Harvard Business Review, March 2024, article</td>
<td>[https://hbr.org/2024/03/lessons-from-more-than-1000-e-commerce-pricing-tests](https://hbr.org/2024/03/lessons-from-more-than-1000-e-commerce-pricing-tests)</td>
<td>Practitioner synthesis of over 1,000 online price tests: what price experiments typically find and how to run them. Search snippet confirms title and date only; check authors and content before use.</td>
<td>Reading for a price experiments session. HBR paywall; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Experimentation in marketplaces: switchbacks at Uber, Lyft and DoorDash (lecture slides)</td>
<td>Nikhil Garg, Cornell ORIE 5355 Lecture 14 'Experimentation in marketplaces', Fall 2022; Bojinov, Simchi-Levi and Zhao, 'Design and Analysis of Switchback Experiments' (arXiv 2009.00148)</td>
<td>[https://orie5355.github.io/Fall_2022/static_files/lectures/Lecture14_Experimentation_marketplaces.pdf](https://orie5355.github.io/Fall_2022/static_files/lectures/Lecture14_Experimentation_marketplaces.pdf)</td>
<td>Why user-level A/B tests are biased in two-sided marketplaces (pricing, matching) and how time-and-region switchback designs (e.g. Uber switching every \~160 minutes per city) fix it. Complements the Uber Express POOL case.</td>
<td>Advanced extension; slides as instructor background. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>The Unfavorable Economics of Measuring the Returns to Advertising</td>
<td>Randall A. Lewis and Justin M. Rao, Quarterly Journal of Economics 130(4), 2015</td>
<td>[https://doi.org/10.1093/qje/qjv023](https://doi.org/10.1093/qje/qjv023)</td>
<td>25 large field experiments with US retailers on Yahoo! show that ad effects are tiny relative to sales noise, so even experiments with millions of users can barely detect profitable campaigns. Excellent for power and minimum detectable effect discussions in a retail setting.</td>
<td>Power analysis session; students reproduce an MDE calculation in Python. Paywalled, WU-Lizenz prüfen. Link from memory, not checked in this run.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>An Assortmentwide Decision-Support System for Dynamic Pricing and Promotion Planning in DIY Retailing (bauMax)</td>
<td>Natter, Reutterer, Mild and Taudes (WU Wien), Marketing Science 26(4), 576-583, 2007, article / ISMS Practice Prize 2005; Österreich</td>
<td>[https://ideas.repec.org/a/inm/ormksc/v26y2007i4p576-583.html](https://ideas.repec.org/a/inm/ormksc/v26y2007i4p576-583.html)</td>
<td>Austrian DIY retailer bauMax: weekly demand model (price, reference price, seasonality, features, discounts, cross-item effects) drives price and promotion decisions. Eight pricing rounds with thousands of SKUs served as testing ground, evaluated against several benchmarks; reported gross profit +8.1 percent and sales +2.1 percent. Lesson: price/promotion testing in brick-and-mortar retail is quasi-experimental (rounds, benchmarks, holdouts) rather than a clean A/B split; good contrast to online A/B tests. WU authors, so strong local hook.</td>
<td>Case discussion on offline price experiments vs. online A/B tests; ask students how they would design a cleaner store-level test (matched stores, holdout SKUs). Article paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>A dynamic segmentation approach for targeting and customizing direct marketing campaigns</td>
<td>Reutterer, Mild, Natter and Taudes (WU Wien), Journal of Interactive Marketing 20(3-4), 2006, article; Österreich</td>
<td>[https://journals.sagepub.com/doi/abs/10.1002/dir.20066](https://journals.sagepub.com/doi/abs/10.1002/dir.20066)</td>
<td>Controlled field experiment with several thousand loyalty-program members of a do-it-yourself retailer (Austrian research team; retailer presumably bauMax, not confirmed in snippet): segment-specific tailored direct-mail campaigns vs. control group; significant positive impact on sales and profitability. Lesson: test vs. control design for CRM/direct-mail campaigns, measuring incremental profit of personalisation.</td>
<td>Reading for the session on email/direct-mail and personalisation tests; students identify treatment, control, unit of randomisation, KPI. Paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>A/B testing to improve recommender products (willhaben real-time recommender)</td>
<td>Adevinta Tech Blog (Medium), ca. 2021-2022, company blog; willhaben, Österreich</td>
<td>[https://medium.com/adevinta-tech-blog/a-b-testing-to-improve-recommender-products-8b18c77af1c3](https://medium.com/adevinta-tech-blog/a-b-testing-to-improve-recommender-products-8b18c77af1c3)</td>
<td>willhaben (Austria's largest classifieds marketplace, Adevinta group) replaced an offline batch user-based recommender suffering from cold start with an online recommender built on real-time user profiles; the switch was validated with an A/B test of reactiveness to recent user interactions. Post also covers metric choice for recommender tests. Exact effect sizes for willhaben not in the snippet; check the post. Lesson: A/B tests for algorithm changes, choosing engagement vs. conversion metrics.</td>
<td>Warm-up: Austrian marketplace students know; guest-talk lead (willhaben data/product team, Vienna). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Runtastic: user review on the paywall instead of promo copy (+44 percent paid subscriptions)</td>
<td>abtest.design (test library) and Designfolio Substack, undated, secondary write-up; Runtastic / adidas Running, Pasching/Linz, Österreich</td>
<td>[https://abtest.design/tests/user-reviews-on-paywall](https://abtest.design/tests/user-reviews-on-paywall)</td>
<td>Runtastic replaced the promotional statement on its in-app premium paywall with a real user review plus 5-star rating (social proof); reported +44 percent paid subscriptions. Evidence thin: secondary sources only, no sample size, duration or significance reported. Lesson: social proof on paywalls, but also a good critical-reading exercise (what is missing to trust a +44 percent claim?).</td>
<td>Warm-up or critique exercise on reported uplifts; Austrian app brand. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Kleine Zeitung tackles branding, ad and subscription sales in a single campaign</td>
<td>INMA blog (International News Media Association), ca. 2019-2020, practitioner article; Kleine Zeitung, Styria Media Group, Graz, Österreich</td>
<td>[https://www.inma.org/blogs/marketing/post.cfm/kleine-zeitung-tackles-branding-ad-and-subscription-sales-in-a-single-campaign](https://www.inma.org/blogs/marketing/post.cfm/kleine-zeitung-tackles-branding-ad-and-subscription-sales-in-a-single-campaign)</td>
<td>Launch campaign for the digital subscription Kleine Web + App. Banner tests on website and Facebook varied price communication (per week vs. per month vs. no price), colours, fact- vs. image-based copy, CTA wording and button design: simple static fact-based banners beat animated ones, and a banner without price beat banners with price. Also reports brand-tracking uplift (aided recall 27 percent). Sample sizes not in snippet. Lesson: creative/message testing in an Austrian publisher, price framing in ads.</td>
<td>Short case discussion: students predict which banner wins before revealing results. INMA posts may need free registration.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How A1 Telekom Austria is using AI to unlock more customer value</td>
<td>BCG / BCG X, client story, ca. 2023-2024, consultancy case; A1 Telekom Austria, Österreich</td>
<td>[https://www.bcg.com/x/mark-your-moment/how-an-austrian-telcom-company-is-using-ai-to-unlock-more-customer-value](https://www.bcg.com/x/mark-your-moment/how-an-austrian-telcom-company-is-using-ai-to-unlock-more-customer-value)</td>
<td>BCG X built cross-/upsell propensity models and next-best-action targeting for A1 within 16 weeks, with an agile, experimental way of working across channels; reports up to 40 percent higher sales conversion in campaigns. Evidence thin on design: consultancy marketing piece, test/control set-up not documented. Lesson: personalisation in telco CRM and why uplift claims need a holdout group.</td>
<td>Discussion prompt: what experiment would you need to verify the 40 percent claim? Austrian telco context. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Converting Online News Visitors to Subscribers: Exploring the Effectiveness of Paywall Strategies Using Behavioural Data</td>
<td>Xu, Thurman, Berhami, Strasser Ceballos and Fehling (LMU München / City St Georges), Journalism Studies, 2025, article (open access); Deutschland und Österreich</td>
<td>[https://www.tandfonline.com/doi/full/10.1080/1461670X.2024.2438229](https://www.tandfonline.com/doi/full/10.1080/1461670X.2024.2438229)</td>
<td>Behavioural data from 21 regional and local news sites (20 German, 1 Austrian): showing a standfirst below a paywalled headline cut the odds of clicking subscribe by 86.3 percent; higher price, paid trial and small gifts reduced subscription odds (4.5, 35.6, 14.0 percent); discounts and device bundles helped only for non-local visitors. Observational (cross-site variation), not randomised. Lesson: what A/B tests on paywall design should test, and why correlational evidence differs from experiments.</td>
<td>Reading plus contrast with Zeit Online/FAZ A/B tests: design an A/B test that would confirm the standfirst finding. Open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Onlinehändlerbefragung (ZHAW with Handelsverband Österreich), A/B-Testing usage among online retailers</td>
<td>ZHAW School of Management and Law with Handelsverband Österreich, Onlinehändlerbefragung 2022 (also 2021, 2023 A-CH editions), survey report; Österreich und Schweiz</td>
<td>[https://www.zhaw.ch/storage/hochschule/medien/news/2022/Onlinehaendlerbefragung_2022.pdf](https://www.zhaw.ch/storage/hochschule/medien/news/2022/Onlinehaendlerbefragung_2022.pdf)</td>
<td>Survey of Austrian and Swiss online retailers; per search snippet, about 15 percent of 509 respondents use a system for A/B or multivariate tests, and larger, more successful shops use them far more than small ones. Exact edition of the 15 percent figure not verified (may be 2021 or 2022). Lesson: diffusion of experimentation in DACH retail is low; motivates why SMEs do not test (traffic, skills).</td>
<td>Opening statistic for a lecture; discussion of barriers to A/B testing for small Austrian shops. Free PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Dynamic Pricing for otto.de (A/B tests of pricing algorithms on article subgroups)</td>
<td>OTTO Tech Blog (Medium / otto.de techblog), ca. 2021, company blog; OTTO, Hamburg, Deutschland</td>
<td>[https://medium.com/otto-tech/dynamic-pricing-for-otto-de-ffc244601180](https://medium.com/otto-tech/dynamic-pricing-for-otto-de-ffc244601180)</td>
<td>OTTO evaluates dynamic-pricing algorithm changes by running versions on two or more homogeneous subgroups of articles in production (group A priced by algorithm X, group B by Y), with demand forecasts from OLS, XGBoost and LightGBM. Lesson: product-level (not user-level) randomisation for price tests, which avoids showing different customers different prices; discuss interference and fairness.</td>
<td>Case discussion on price experiments: why randomise products rather than customers? Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Learning to Rank: deep neural networks that learn to rank what you love (8-week A/B test on otto.de)</td>
<td>OTTO Tech Blog, ca. 2022-2023, company blog; OTTO, Hamburg, Deutschland</td>
<td>[https://www.otto.de/jobs/en/technology/techblog/blogpost/learning-to-rank-otto.php](https://www.otto.de/jobs/en/technology/techblog/blogpost/learning-to-rank-otto.php)</td>
<td>Neural ranking model for product search/listing tested for 8 weeks against the previous ranking: +1.86 percent clicks and +0.56 percent revenue, then rolled out to all users. Lesson: small relative lifts matter at scale; test duration, primary vs. secondary metrics.</td>
<td>Warm-up: is +0.56 percent revenue worth it? Compute absolute value with OTTO revenue. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>A story of experimentation culture at HelloFresh</td>
<td>HelloFresh Tech Blog (Medium), ca. 2019-2020, company blog; HelloFresh, Berlin, Deutschland</td>
<td>[https://engineering.hellofresh.com/a-story-of-experimentation-culture-at-hellofresh-be0f0ceb171b](https://engineering.hellofresh.com/a-story-of-experimentation-culture-at-hellofresh-be0f0ceb171b)</td>
<td>Experimentation platform team serving 30+ product teams from Berlin to Toronto; Optimizely chosen as single framework in 2018; won Optimizely Best Experimentation Program award. Related PyMC Labs post describes speeding HelloFresh's Bayesian A/B test pipeline from 5-6 hours to 5-6 minutes. Lesson: organisational scaling of experimentation in a Berlin subscription e-commerce firm.</td>
<td>Background reading on experimentation culture; guest-talk lead (HelloFresh experimentation team, Berlin). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Creating a culture of experimentation at Delivery Hero (Vol. I) and the Fun with Flags platform</td>
<td>Delivery Hero Tech Blog, 2018 (plus later platform posts), company blog; Delivery Hero, Berlin, Deutschland</td>
<td>[https://tech.deliveryhero.com/creating-a-culture-of-experimentation-at-delivery-hero-vol-i-2/](https://tech.deliveryhero.com/creating-a-culture-of-experimentation-at-delivery-hero-vol-i-2/)</td>
<td>Product manager interview on building experimentation culture; related posts describe the in-house platform Fun with Flags (over 1 billion requests per week, used by about 90 percent of brands). No Delivery Hero switchback post found in search, so use DoorDash for switchbacks. Lesson: experimentation in a multi-brand delivery marketplace.</td>
<td>Background for a session on marketplace experiments; guest-talk lead. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>How Sequential Testing Accelerates Our Experimentation Velocity (Basemath)</td>
<td>GetYourGuide careers/tech blog (Konrad Richter et al.), ca. 2023-2024, company blog plus open-source repo; GetYourGuide, Zürich/Berlin, Schweiz und Deutschland</td>
<td>[https://www.getyourguide.careers/posts/how-sequential-testing-accelerates-our-experimentation-velocity](https://www.getyourguide.careers/posts/how-sequential-testing-accelerates-our-experimentation-velocity)</td>
<td>GetYourGuide developed its own sequential test (Basemath, open source on GitHub) to allow early stopping without inflating false positives; sibling posts cover clustered standard errors for ranking metrics and scaling A/B testing, and a PyData Berlin 2025 talk on democratising the platform. Lesson: peeking problem and sequential testing in a travel marketplace.</td>
<td>Methods session on peeking; students run the Basemath repo on simulated data. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Embeddings based complementary product recommendations at idealo (A/B test doubled engagement)</td>
<td>idealo Tech Blog (Medium), ca. 2021-2022, company blog; idealo, Berlin, Deutschland</td>
<td>[https://medium.com/idealo-tech-blog/embedding-based-complementary-product-recommendations-at-idealo-850e5a6dc25f](https://medium.com/idealo-tech-blog/embedding-based-complementary-product-recommendations-at-idealo-850e5a6dc25f)</td>
<td>Price-comparison site idealo built complementary-product recommendations without purchase data; online A/B test doubled user engagement with the module. Companion post on how to formulate A/B test hypotheses (medium.com/idealo-tech-blog/how-to-come-up-with-the-right-hypothesis-for-your-a-b-tests-dd5824967003). Lesson: offline vs. online metrics; hypothesis writing.</td>
<td>Hypothesis-writing exercise using the companion post. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>4 learnings about subscription A/B testing from ZEIT ONLINE</td>
<td>The Audiencers (practitioner media), ca. 2022-2023, interview/article; ZEIT ONLINE, Hamburg/Berlin, Deutschland</td>
<td>[https://theaudiencers.com/4-learnings-about-a-b-testing-after-5-years-working-on-paid-content-at-zeit-online/](https://theaudiencers.com/4-learnings-about-a-b-testing-after-5-years-working-on-paid-content-at-zeit-online/)</td>
<td>Five years of paywall testing at ZEIT ONLINE: example test on which subscription benefits to promote; baseline conversion about 1.5 percent and target uplift 10 percent drive sample-size planning; alpha 5 or 10 percent depending on risk; one KPI per test to avoid false positives; complement with qualitative user tests. Lesson: realistic power calculation for low base rates.</td>
<td>Lab: compute required sample size for 1.5 percent baseline and 10 percent MDE. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Dynamic paywall testing at Germany's FAZ</td>
<td>The Audiencers, 2024, practitioner article; also AVS/Medienhaus Next blog Warum A/B-Tests für die F.A.Z. unverzichtbar sind; Frankfurter Allgemeine Zeitung, Deutschland</td>
<td>[https://theaudiencers.com/dynamic-paywall-testing-how-faz-is-working-to-reach-300000-digital-subscribers-by-2025/](https://theaudiencers.com/dynamic-paywall-testing-how-faz-is-working-to-reach-300000-digital-subscribers-by-2025/)</td>
<td>FAZ ran 32 A/B tests in a year, 18 on the paywall; strikethrough reference prices lifted new-customer acquisition by 18 percent; first dynamic-paywall test (June 2024) used an in-house propensity-to-buy score: more paywalled content for highly engaged users gave +48 percent, about 20 extra orders per day. Lesson: price framing tests and targeting-based (heterogeneous treatment) paywalls; German-language companion post available.</td>
<td>Case discussion on reference prices and personalised paywalls; German source usable in German-taught courses. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Bild's subscription testing drives its reader revenue plan</td>
<td>INMA Ideas blog, ca. 2019-2021, practitioner article; BILD / Axel Springer, Berlin, Deutschland</td>
<td>[https://www.inma.org/blogs/ideas/post.cfm/bild-s-subscription-testing-drives-its-reader-revenue-plan](https://www.inma.org/blogs/ideas/post.cfm/bild-s-subscription-testing-drives-its-reader-revenue-plan)</td>
<td>A/B tests on Bild's offer page showed more products and higher price points were not worth it; fewer products converted better; Bild then removed the offer page and placed the offer directly in the article; price increase first raised churn but paid off long-term. Numbers sparse in snippet. Lesson: choice overload, funnel friction, and short- vs. long-term metrics in price tests.</td>
<td>Discussion on long-term effects of price tests (churn). INMA may require free registration.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Personalized Online Advertising Effectiveness: The Interplay of What, When, and Where</td>
<td>Bleier and Eisenbeiss, Marketing Science 34(5), 669-688, 2015, article; field experiments with a large German fashion and sports retailer, Deutschland</td>
<td>[https://pubsonline.informs.org/doi/10.1287/mksc.2015.0930](https://pubsonline.informs.org/doi/10.1287/mksc.2015.0930)</td>
<td>Two large-scale field experiments plus two lab studies on retargeting banners: highly personalised banners work best right after a store visit but decay fast (overpersonalization); medium personalisation is more persistent; personalisation helps view-through only on motive-congruent sites. Lesson: personalisation tests need time and placement moderators; heterogeneity of treatment effects.</td>
<td>Reading for the personalisation/retargeting session. Paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Pay What You Want: A New Participative Pricing Mechanism</td>
<td>Kim, Natter and Spann (Frankfurt/LMU), Journal of Marketing 73(1), 44-58, 2009, article; field studies in Germany, Deutschland</td>
<td>[https://www.researchgate.net/publication/242376590_Pay_What_You_Want_A_New_Participative_Pricing_Mechanism](https://www.researchgate.net/publication/242376590_Pay_What_You_Want_A_New_Participative_Pricing_Mechanism)</td>
<td>Three field studies (restaurant buffet, cinema, delicatessen) in Germany: prices paid were well above zero; vs. regular prices, buffet payments were 19.4 percent lower, hot drinks at the deli 10.6 percent higher; PWYW can raise revenue. Design is before/after per outlet rather than randomised A/B. Lesson: price-mechanism field tests in retail and how to read non-randomised field evidence.</td>
<td>Classic reading for price experiments; class debate on design weaknesses. Article paywalled, preprint on ResearchGate, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Shipping fee schedules and return behavior</td>
<td>Lepthien and Clement (Universität Hamburg), Marketing Letters 30(2), 2019, article; randomized field experiment with an online shop, Deutschland</td>
<td>[https://link.springer.com/article/10.1007/s11002-019-09486-8](https://link.springer.com/article/10.1007/s11002-019-09486-8)</td>
<td>Shop visitors randomly assigned to one of seven shipping-fee schedules (minimum order values, flat fees, free-shipping thresholds). Shipping fees raised purchase value; threshold free shipping lowered purchase incidence and triggered strategic purchases that were returned later; minimum order values had no negative effect on purchases. Lesson: multi-arm price/promo field experiment, and why post-return metrics matter.</td>
<td>Reading plus exercise: design the seven-arm test and choose KPIs. Paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>From gut feeling to test culture (Vom Bauchgefühl zur Test-Kultur) incl. CO2 compensation checkout A/B test</td>
<td>Digitec Galaxus, company magazine article, ca. 2020-2021, company blog; Zürich, Schweiz</td>
<td>[https://www.digitec.ch/en/page/from-gut-feeling-to-test-culture-17636](https://www.digitec.ch/en/page/from-gut-feeling-to-test-culture-17636)</td>
<td>Switzerland's largest online retailer explains why it replaced an external testing tool with its own (page performance), and gives an example: two-week A/B test of a CO2-compensation option in checkout (A without, B with). Follow-up reports: about one in ten orders compensated, CHF 1.3 million in a year; under-30s compensate most (about 16 percent). Lesson: testing a sustainability feature for adoption and possible conversion side-effects.</td>
<td>Warm-up on testing non-revenue features (guardrail metrics: did checkout conversion drop?). German version on galaxus.de. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>The Cliffhanger Effect: how Blick's paywall strategy drives digital subscription growth</td>
<td>INMA Best Practice / INMA Ideas blog, 2024, practitioner article; Blick (Ringier), Zürich, Schweiz</td>
<td>[https://www.inma.org/best-practice/Digital-Subscriptions/2024-53/The-Cliffhanger-Effect-How-Blicks-Paywall-Strategy-Drives-Digital-Subscription-Growth](https://www.inma.org/best-practice/Digital-Subscriptions/2024-53/The-Cliffhanger-Effect-How-Blicks-Paywall-Strategy-Drives-Digital-Subscription-Growth)</td>
<td>Blick tested a Cliffhanger paywall (summary that stops at the key point) against a standard and a marketing-oriented paywall: +7 percent conversion vs. standard, +21 percent vs. marketing paywall on web. The Audiencers also covers Blick's Wheel of Luck gamified paywall experiment. Lesson: three-arm creative test on paywall copy in a Swiss tabloid.</td>
<td>Short case: students predict the ranking of the three paywalls. INMA best-practice pages may need login.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Software (36)
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
<td>statsmodels (stats.proportion, stats.power, multipletests)</td>
<td>statsmodels developers, Python package, version 0.15.0 (PyPI, 27 Aug 2026), BSD-3-Clause, Python \>=3.10</td>
<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
<td>Workhorse for classical A/B analysis: proportions_ztest and confint_proportions_2indep for conversion rates, proportion_effectsize plus NormalIndPower / TTestIndPower for sample size and MDE, multipletests for Holm and Benjamini-Hochberg, OLS with covariates as regression adjustment (CUPED equivalent).</td>
<td>Core lab library for sessions 1-3 (test, power, multiple metrics). Open source (BSD-3), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>SciPy (scipy.stats)</td>
<td>SciPy developers, Python package, version 1.18.1 (PyPI, 21 Aug 2026), BSD-3-Clause, Python \>=3.12</td>
<td>[https://pypi.org/project/scipy/](https://pypi.org/project/scipy/)</td>
<td>ttest_ind(equal_var=False) for Welch tests on revenue per user, chisquare for the sample ratio mismatch check, chi2_contingency for multi-arm conversion tables, mannwhitneyu, scipy.stats.bootstrap and permutation_test for skewed basket values. Note: new version needs Python 3.12.</td>
<td>Lab: SRM check and Welch vs. bootstrap comparison on Hillstrom spend. Open source, free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pingouin</td>
<td>Raphael Vallat, Python package, version 0.7.0 (PyPI, 26 Sep 2026), GPL-3.0, Python \>=3.11</td>
<td>[https://pypi.org/project/pingouin/](https://pypi.org/project/pingouin/)</td>
<td>Student-friendly statistics API returning tidy DataFrames with effect size, CI, Bayes factor and achieved power in one call (ttest, anova, pairwise_tests, power_ttest). Good bridge for business students coming from SPSS-style output.</td>
<td>Warm-up lab for t-test and ANOVA on multi-arm promotion data (Fast Food dataset). Open source (GPL-3.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>scikit-posthocs</td>
<td>Maksim Terpilovskii, Python package, version 0.17.0 (PyPI, 10 Sep 2026), MIT, Python \>=3.9</td>
<td>[https://pypi.org/project/scikit-posthocs/](https://pypi.org/project/scikit-posthocs/)</td>
<td>Post-hoc pairwise comparisons (Tukey HSD, Dunn, Conover, Nemenyi) with p-value adjustment after an omnibus test on A/B/n tests with three or more arms.</td>
<td>Short demo in the multiple-testing session (three promotions in the Fast Food data). Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>spotify-confidence</td>
<td>Spotify, Python package, version 4.1.0 (PyPI, 26 Feb 2026), Apache-2.0, Python \>=3.9</td>
<td>[https://pypi.org/project/spotify-confidence/](https://pypi.org/project/spotify-confidence/)</td>
<td>Industry library from Spotify's experimentation platform: z-tests and t-tests on summary statistics, sequential group tests with alpha spending, multiple-comparison correction, non-inferiority margins, built-in plots. Works on aggregated data, which mirrors how platforms compute results.</td>
<td>Lab on group sequential testing and guardrail (non-inferiority) metrics. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>tea-tasting</td>
<td>Evgeny Ivanov (e10v), Python package, version 2.0.0 (PyPI, 7 Jun 2026), MIT, Python \>=3.12</td>
<td>[https://pypi.org/project/tea-tasting/](https://pypi.org/project/tea-tasting/)</td>
<td>Modern A/B analysis package: Welch t-test, z-test, bootstrap, CUPED/CUPAC, delta method for ratio metrics (e.g. orders per session), SRM check, power analysis; computes statistics inside data backends via Ibis (DuckDB, BigQuery, Polars). Includes example data generator. Docs at tea-tasting.e10v.me.</td>
<td>Recommended main package for a full A/B lab notebook in Positron/Quarto (metrics, CUPED, ratio metrics). Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Ambrosia</td>
<td>MTS AI (MobileTeleSystems), Python package, version 0.5.3.post1 (PyPI, 11 Jun 2026), Apache-2.0, Python 3.9-3.13</td>
<td>[https://pypi.org/project/ambrosia/](https://pypi.org/project/ambrosia/)</td>
<td>End-to-end experiment pipeline in three steps: Designer (sample size, MDE, duration from historical data), Splitter (hash-based and stratified group splits), Tester (t-test, bootstrap, multiple metrics). Shows the design side students rarely see.</td>
<td>Lab or project: design an experiment from historic retail data before running it. Open source (Apache-2.0), free; Python \<3.14.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>ExpAn (Zalando)</td>
<td>Zalando SE, Python package, version 1.4.0 (PyPI, 5 Jul 2019), MIT, no longer maintained</td>
<td>[https://pypi.org/project/expan/](https://pypi.org/project/expan/)</td>
<td>Historic e-commerce library from Zalando: delta method for ratio metrics, early-stopping and Bayesian variants. Unmaintained since 2019, so useful as reading code and for the history of retail experimentation, not as lab dependency.</td>
<td>Background only; point students to source code for delta-method implementation. Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>CausalML (Uber)</td>
<td>Uber Technologies, Python package, version 0.17.0 (PyPI, 4 Jul 2026), Apache-2.0, Python \>=3.11</td>
<td>[https://pypi.org/project/causalml/](https://pypi.org/project/causalml/)</td>
<td>Uplift modelling and heterogeneous treatment effects: S/T/X/R/DR meta-learners, uplift trees and random forests, Qini and uplift curves, synthetic data generators (causalml.dataset). Directly matched to coupon and email targeting cases.</td>
<td>Lab on uplift targeting with Hillstrom or Criteo uplift data; student project. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>EconML (Microsoft / PyWhy)</td>
<td>Microsoft Research ALICE / PyWhy, Python package, version 0.17.0 (PyPI, 31 Jul 2026), MIT, Python \>=3.9</td>
<td>[https://pypi.org/project/econml/](https://pypi.org/project/econml/)</td>
<td>Double machine learning, causal forests (CausalForestDML), DR-learner and policy trees with confidence intervals for CATE; SHAP interpretation of who responds to a promotion. More inference-oriented than CausalML.</td>
<td>Advanced lab on heterogeneous treatment effects and targeting policies. Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>DoWhy (PyWhy)</td>
<td>PyWhy (originally Microsoft), Python package, version 0.14 (PyPI, 8 Nov 2025), MIT, Python 3.9-3.13</td>
<td>[https://pypi.org/project/dowhy/](https://pypi.org/project/dowhy/)</td>
<td>Four-step causal workflow (model, identify, estimate, refute) with DAGs; refutation tests (placebo treatment, random common cause). Good for contrasting experiments with observational marketing data; datasets.linear_dataset simulates data.</td>
<td>Demo in the quasi-experiments session: why randomisation removes the need for back-door adjustment. Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>scikit-uplift (sklift)</td>
<td>Maksim Shevchenko and contributors, Python package, version 0.5.1 (PyPI, 11 Aug 2022), MIT per repository</td>
<td>[https://pypi.org/project/scikit-uplift/](https://pypi.org/project/scikit-uplift/)</td>
<td>scikit-learn style uplift models (two-model, class transformation) and metrics (Qini AUC, uplift@k). Main value: one-line loaders fetch_hillstrom, fetch_criteo, fetch_x5, fetch_lenta, fetch_megafon for the standard marketing experiment datasets.</td>
<td>Data loader for labs; simple uplift baseline before CausalML. Open source, free; low maintenance since 2022, pin versions.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC</td>
<td>PyMC developers, Python package, version 6.3.2 (PyPI, 8 Sep 2026), Apache-2.0, Python \>=3.12</td>
<td>[https://pypi.org/project/pymc/](https://pypi.org/project/pymc/)</td>
<td>Probabilistic programming for Bayesian A/B tests: Beta-Binomial conversion models, hierarchical models across segments or markets, posterior probability to beat control and expected loss. PyMC example gallery has a Bayesian A/B testing introduction.</td>
<td>Lab on Bayesian A/B testing as contrast to frequentist tests. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Bambi</td>
<td>Bambi developers (PyMC ecosystem), Python package, version 0.21.0 (PyPI, 10 Sep 2026), MIT, Python \>=3.12</td>
<td>[https://pypi.org/project/bambi/](https://pypi.org/project/bambi/)</td>
<td>Formula interface (like lme4/brms) on top of PyMC: Bayesian logistic regression of conversion on treatment plus covariates in one line. Lowers the coding barrier for business students.</td>
<td>Bayesian regression adjustment lab; compare with statsmodels logit. Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyMC-Marketing (lift-test calibration)</td>
<td>PyMC Labs, Python package, version 1.2.0 (PyPI, 29 Sep 2026), Apache-2.0, Python \>=3.12</td>
<td>[https://pypi.org/project/pymc-marketing/](https://pypi.org/project/pymc-marketing/)</td>
<td>Bayesian media mix models that can be calibrated with results of geo or lift experiments (add_lift_test_measurements), linking incrementality tests to MMM; also CLV and customer choice modules.</td>
<td>Demo connecting experiments to marketing-mix modelling; capstone project. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>tfcausalimpact (Python port of Google CausalImpact)</td>
<td>Willian Fuks, Python package, version 0.0.19 (PyPI, 20 Sep 2026), Apache-2.0, Python 3.8-3.13; based on Google's R package CausalImpact (Brodersen et al. 2015)</td>
<td>[https://pypi.org/project/tfcausalimpact/](https://pypi.org/project/tfcausalimpact/)</td>
<td>Bayesian structural time series counterfactual for a single treated series (one market, one campaign launch) with point and cumulative effect plots. Depends on TensorFlow Probability. The older pycausalimpact (0.1.1, 2020) is unmaintained.</td>
<td>Lab on quasi-experimental campaign evaluation when no randomisation is possible. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>CausalImpact (R)</td>
<td>Google (Kay Brodersen, Alain Hauser), R package on CRAN, Apache-2.0</td>
<td>[https://cran.r-project.org/package=CausalImpact](https://cran.r-project.org/package=CausalImpact)</td>
<td>Original reference implementation of BSTS-based causal impact analysis with a very readable vignette; the standard tool in marketing analytics for campaign and pricing interventions.</td>
<td>Optional R comparison in Positron/Quarto. Open source, free. CRAN page not reachable from this session, check version.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>GeoLift (Meta, R)</td>
<td>Meta Open Source (facebookincubator), R package on GitHub, MIT licence</td>
<td>[https://github.com/facebookincubator/GeoLift](https://github.com/facebookincubator/GeoLift)</td>
<td>End-to-end geo experimentation: market selection, power analysis by simulation, augmented synthetic control inference; walkthrough vignette with example data GeoLift_PreTest / GeoLift_Test; official tutorial for calling it from Python via rpy2.</td>
<td>Lab or project on geo lift tests for offline retail and post-cookie measurement. Open source (MIT), free; R install from GitHub.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>GeoexperimentsResearch (Google, R)</td>
<td>Google, R package on GitHub, version 1.0.3, Apache-2.0</td>
<td>[https://rdrr.io/github/google/GeoexperimentsResearch/](https://rdrr.io/github/google/GeoexperimentsResearch/)</td>
<td>Implements geo-based regression (GBR) and time-based regression (TBR) for ROAS estimation from Vaver and Koehler; includes sample geo assignment and sales/cost data.</td>
<td>Background or advanced lab on geo experiments and iROAS. Open source, free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>trimmed_match and matched_markets (Google)</td>
<td>Google, Python libraries on GitHub (not on PyPI), Apache-2.0</td>
<td>[https://github.com/google/trimmed_match](https://github.com/google/trimmed_match)</td>
<td>trimmed_match: robust estimator of iROAS for paired geo experiments with outlier geos (Chen and Au 2022); matched_markets (github.com/google/matched_markets): designs and analyses matched-market experiments with TBR. Show how Google measures search ad incrementality.</td>
<td>Advanced demo for geo experiment design. Open source, free; installed from GitHub, notebooks in repos. Links not reachable from this session.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pysyncon</td>
<td>Stuart Lynn, Python package, version 1.7.0 (PyPI, 13 Sep 2026), MIT</td>
<td>[https://pypi.org/project/pysyncon/](https://pypi.org/project/pysyncon/)</td>
<td>Synthetic control in Python (standard, robust, augmented, penalised) with placebo tests; replicates Abadie's classic examples. Python alternative to GeoLift for market-level interventions.</td>
<td>Lab on synthetic control for a single-market campaign or store remodel. Open source (MIT), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>MABWiser</td>
<td>Fidelity Investments AI Center of Excellence, Python package, version 2.7.4 (PyPI, 30 Aug 2024), Apache-2.0</td>
<td>[https://pypi.org/project/mabwiser/](https://pypi.org/project/mabwiser/)</td>
<td>Multi-armed and contextual bandits (epsilon-greedy, UCB, Thompson sampling, LinUCB) with simulation utilities; simple fit/predict API suitable for showing explore-exploit trade-offs against fixed-horizon A/B tests.</td>
<td>Lab: simulate a headline or banner test as A/B vs. Thompson sampling and compare regret. Open source (Apache-2.0), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Open Bandit Pipeline (obp)</td>
<td>ZOZO Research / Yuta Saito et al., Python package, version 0.5.7 (PyPI, 14 Apr 2023), Apache-2.0</td>
<td>[https://pypi.org/project/obp/](https://pypi.org/project/obp/)</td>
<td>Bandit policies and off-policy evaluation estimators (IPW, DR, DM) shipped with the Open Bandit Dataset from ZOZOTOWN fashion e-commerce; answers whether a new recommendation policy would beat the logged one without a new A/B test.</td>
<td>Advanced lab or thesis topic on off-policy evaluation. Open source (Apache-2.0), free; last release 2023.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Vowpal Wabbit</td>
<td>Vowpal Wabbit (originally Yahoo and Microsoft Research), Python package vowpalwabbit 9.11.9 (PyPI, 27 Sep 2026), BSD-3-Clause, Python \>=3.10</td>
<td>[https://pypi.org/project/vowpalwabbit/](https://pypi.org/project/vowpalwabbit/)</td>
<td>Production-grade online learning and contextual bandits (used in Microsoft Personalizer); tutorials on simulating content personalisation with contextual bandits.</td>
<td>Demo of industrial contextual bandits; optional for advanced students. Open source (BSD-3), free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>GrowthBook</td>
<td>GrowthBook Inc., open source feature flagging and experimentation platform on GitHub (MIT core), Python SDK growthbook 3.2.0 (PyPI, 5 Oct 2026)</td>
<td>[https://github.com/growthbook/growthbook](https://github.com/growthbook/growthbook)</td>
<td>Warehouse-native platform with Bayesian (default), frequentist and sequential engines, CUPED, SRM detection, multiple-comparison corrections, bandits and power calculator; stats engine is open Python code (gbstats), so students can inspect what a commercial-grade tool computes.</td>
<td>Platform demo or self-hosted lab via Docker; cloud free tier for small teams. Open source (MIT core), free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>PostHog Experiments</td>
<td>PostHog Inc., product analytics with experiments; Python SDK posthog 7.64.0 (PyPI, 6 Oct 2026), MIT</td>
<td>[https://posthog.com/docs/experiments](https://posthog.com/docs/experiments)</td>
<td>Bayesian and frequentist experiment analysis with CUPED and running-time calculator; docs explain the statistics in plain language. Free tier: 1 million feature-flag requests and 1 million events per month.</td>
<td>Platform walkthrough; docs as reading on Bayesian vs. frequentist reporting. Free tier, then usage-based pricing.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>Statsig</td>
<td>Statsig (acquired by OpenAI Sept 2025; product, brand and customers taken over by Amplitude May 2026); Python SDK statsig 0.72.1 (PyPI, 19 Aug 2026), ISC</td>
<td>[https://www.statsig.com/](https://www.statsig.com/)</td>
<td>Commercial experimentation and feature-flag platform with CUPED, sequential testing, SRM and holdouts; its Perspectives blog is a good practitioner reading source. Ownership changes are themselves a talking point on the experimentation tool market.</td>
<td>Industry context and guest-talk topic; free developer tier available (check current terms after Amplitude takeover).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>Eppo (Datadog Experiments)</td>
<td>Eppo, acquired by Datadog May 2025, now branded Datadog Experiments; Python SDK eppo-server-sdk 4.4.1 (PyPI, 7 Jan 2026), MIT</td>
<td>[https://www.geteppo.com/](https://www.geteppo.com/)</td>
<td>Warehouse-native experimentation platform known for CUPED++, sequential and Bayesian analysis and strong statistical documentation; integrates experimentation with observability.</td>
<td>Industry context; documentation as reading. Commercial, pricing on request.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>Optimizely Web Experimentation</td>
<td>Optimizely, commercial SaaS; Stats Engine based on always-valid inference (Johari et al.)</td>
<td>[https://www.optimizely.com/products/web-experimentation/](https://www.optimizely.com/products/web-experimentation/)</td>
<td>Market leader in website A/B testing for marketing teams; visual editor, Stats Engine with sequential testing and FDR control, i.e. a real-world implementation of mSPRT.</td>
<td>Case illustration of sequential testing in practice. Paid, enterprise pricing on request.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>VWO (Visual Website Optimizer)</td>
<td>Wingify, commercial SaaS for testing and CRO</td>
<td>[https://vwo.com/](https://vwo.com/)</td>
<td>Widely used marketer-facing tool with visual editor, Bayesian SmartStats reporting, heatmaps; useful to show what non-technical marketing teams see.</td>
<td>Demo of a marketer-facing testing UI; free trial, paid plans.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>AB Tasty</td>
<td>AB Tasty (France), commercial SaaS for experimentation and personalisation</td>
<td>[https://www.abtasty.com/](https://www.abtasty.com/)</td>
<td>European vendor popular in retail and e-commerce (Bayesian reporting, personalisation, feature experimentation); relevant for DACH employers.</td>
<td>Industry context, potential guest speaker company. Paid, pricing on request.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Unleash</td>
<td>Unleash (Bricks Software AS, Norway), open source feature-flag server Apache-2.0; Python SDK UnleashClient 6.8.0 (PyPI, 21 Jul 2026), MIT</td>
<td>[https://pypi.org/project/UnleashClient/](https://pypi.org/project/UnleashClient/)</td>
<td>Open source feature flags with gradual rollouts and variants; shows the randomisation and assignment layer (sticky hashing) separately from the analysis layer.</td>
<td>Short demo on how users are bucketed into variants. Open source, free self-hosted.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Mixpanel (Experiments report)</td>
<td>Mixpanel Inc., product analytics SaaS; Python SDK mixpanel 5.4.0 (PyPI, 2 Sep 2026), Apache-2.0</td>
<td>[https://pypi.org/project/mixpanel/](https://pypi.org/project/mixpanel/)</td>
<td>Event analytics with an experiments report that reads results of tests run in other flagging tools; illustrates the analytics-side workflow in digital marketing teams.</td>
<td>Industry context; free tier for students. Freemium.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pwr (R)</td>
<td>Stephane Champely et al., R package on CRAN, GPL-3</td>
<td>[https://cran.r-project.org/package=pwr](https://cran.r-project.org/package=pwr)</td>
<td>Cohen-style power functions (pwr.2p.test for two proportions, pwr.t.test); compact and well known from methods courses, useful for an R/Python comparison in Quarto.</td>
<td>Optional R exercise for power analysis. Open source, free. CRAN not reachable from this session, check version.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>grf (R) - generalized random forests</td>
<td>Tibshirani, Athey, Wager et al., R package on CRAN, GPL-3</td>
<td>[https://cran.r-project.org/package=grf](https://cran.r-project.org/package=grf)</td>
<td>Reference implementation of causal forests with honest splitting, doubly robust ATE, best linear projection and RATE/Qini metrics for targeting; excellent vignettes.</td>
<td>Advanced lab on heterogeneous treatment effects, R alternative to EconML. Open source, free. Check current version.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Evan Miller A/B testing tools (sample size calculator, chi-squared test, sequential sampling)</td>
<td>Evan Miller, free web calculators</td>
<td>[https://www.evanmiller.org/ab-testing/sample-size.html](https://www.evanmiller.org/ab-testing/sample-size.html)</td>
<td>Classic browser calculators for sample size, two-proportion test, sequential sampling and t-tests; paired with his essay How Not To Run an A/B Test on peeking.</td>
<td>In-class warm-up before coding power analysis in Python. Free, no login.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Data (18)
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
<td>Criteo Uplift Prediction Dataset (v2.1)</td>
<td>Criteo AI Lab (Diemert et al. 2018/2021), 13,979,592 rows, CC BY-NC-SA 4.0 (non-commercial; check on download page)</td>
<td>[https://huggingface.co/datasets/criteo/criteo-uplift](https://huggingface.co/datasets/criteo/criteo-uplift)</td>
<td>Pooled incrementality tests from display advertising: 12 anonymised features f0-f11, treatment (85/15 split), exposure, visit (about 4.7 percent), conversion (about 0.29 percent). Ideal for ITT vs. treatment-on-treated, uplift models and power with rare outcomes. Also loadable via sklift.fetch_criteo.</td>
<td>Project data for uplift and incrementality; subsample for labs. Free download, academic use.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Criteo Attribution Modeling for Bidding Dataset</td>
<td>Criteo AI Lab, about 16.5 million impressions, 45k conversions, 700 campaigns, 30 days of traffic; non-commercial licence (check)</td>
<td>[https://ailab.criteo.com/criteo-attribution-modeling-bidding-dataset/](https://ailab.criteo.com/criteo-attribution-modeling-bidding-dataset/)</td>
<td>Impression-level log with click, conversion and whether the conversion was attributed to Criteo; used to contrast last-click attribution with causal (experimental) measurement. Not itself randomised.</td>
<td>Discussion and lab: why attribution is not incrementality. Free download; also on Hugging Face and Kaggle mirrors.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Hillstrom MineThatData E-Mail Analytics Challenge</td>
<td>Kevin Hillstrom, MineThatData (2008), 64,000 customers, about 5 MB CSV, free for research and teaching</td>
<td>[https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_hillstrom.html)</td>
<td>Real retail email RCT: customers randomised to Mens email, Womens email or no email (about 21.3k each); covariates recency, history, mens, womens, zip_code, newbie, channel; outcomes visit, conversion, spend over two weeks. The best single dataset for a semester of A/B, CUPED-style adjustment and uplift exercises. Also in TensorFlow Datasets.</td>
<td>Main lab dataset (multi-arm test, revenue metric, HTE). Free, no login via sklift.fetch_hillstrom.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Marketing A/B Testing (ad vs. PSA)</td>
<td>Favio Vazquez, Kaggle dataset, 588,101 users, licence on Kaggle page</td>
<td>[https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)</td>
<td>Users assigned to ad or public service announcement (PSA, ghost-ad style control, 96/4 split); variables test group, converted, total ads, most ads day, most ads hour. Lift about 2.55 vs 1.79 percent; strong dose-response by exposure, which invites a discussion of post-treatment conditioning.</td>
<td>Lab on two-proportion test with unbalanced allocation and PSA controls. Free with Kaggle login.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Cookie Cats mobile game A/B test</td>
<td>Kaggle dataset (yufengsui, from DataCamp project), 90,189 players, licence on Kaggle page</td>
<td>[https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing](https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing)</td>
<td>Gate at level 30 (control) vs. level 40; variables userid, version, sum_gamerounds, retention_1, retention_7. 7-day retention drops about 0.8 pp. Good for retention metrics, bootstrap CIs and heavy-tailed engagement data.</td>
<td>Warm-up lab on proportion tests and bootstrap. Free with Kaggle login.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>E-commerce landing page A/B test (Udacity ab_data.csv)</td>
<td>Udacity Data Analyst Nanodegree project data, 294,478 rows, 5 columns; mirrored on Kaggle and GitHub</td>
<td>[https://github.com/jemc36/Udacity-DAND-AB-test-ecommerce](https://github.com/jemc36/Udacity-DAND-AB-test-ecommerce)</td>
<td>user_id, timestamp, group, landing_page, converted (about 12 percent conversion), plus countries.csv for segment analysis. Contains about 3,900 mismatched group/page rows and a duplicate user, a realistic data-cleaning and SRM teaching moment.</td>
<td>First lab: clean, check assignment integrity, z-test, logistic regression. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Fast Food Marketing Campaign A/B Test</td>
<td>Kaggle dataset (chebotinaa, originally IBM Watson Analytics sample), 548 rows, 7 columns</td>
<td>[https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test)</td>
<td>Three promotions randomised across store locations, weekly sales over four weeks; MarketID, MarketSize, LocationID, AgeOfStore, Promotion, week, SalesInThousands. Small and retail-specific: ANOVA, cluster structure (stores in markets), repeated weeks.</td>
<td>Lab on multi-arm tests, post-hoc comparisons and clustering by market. Free with Kaggle login.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>X5 RetailHero uplift dataset</td>
<td>X5 Retail Group (Russia) RetailHero competition 2019, via scikit-uplift fetch_x5; clients, train and purchases tables (purchase log several million rows)</td>
<td>[https://www.uplift-modeling.com/en/latest/api/datasets/fetch_x5.html](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_x5.html)</td>
<td>Grocery retailer SMS campaign with treatment_flg and purchase target, client demographics and raw transaction history before the communication. Requires feature engineering from purchases, which makes it a realistic retail project.</td>
<td>Student project on uplift targeting with feature engineering. Free via sklift.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Lenta uplift dataset</td>
<td>Lenta (Russian hypermarket chain) via scikit-uplift fetch_lenta, about 687k customers and about 190 features</td>
<td>[https://www.uplift-modeling.com/en/latest/api/datasets/fetch_lenta.html](https://www.uplift-modeling.com/en/latest/api/datasets/fetch_lenta.html)</td>
<td>SMS campaign RCT for a grocery retailer: group (test/control), response_att (visit), gender, age, store type and many purchase-behaviour aggregates. Large but tidy; good for CATE and Qini curves.</td>
<td>Project data for uplift modelling. Free via sklift.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>MegaFon Uplift Competition dataset (synthetic)</td>
<td>MegaFon (telecom) via scikit-uplift fetch_megafon, 600,000 rows, 50 features, synthetic</td>
<td>[https://www.uplift-modeling.com/en/v0.4.0/api/datasets/fetch_megafon.html](https://www.uplift-modeling.com/en/v0.4.0/api/datasets/fetch_megafon.html)</td>
<td>Synthetic data designed to resemble real telecom campaigns; binary treatment and conversion. Clean benchmark when real data are too messy.</td>
<td>Benchmark for comparing uplift models. Free via sklift.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Open Bandit Dataset (ZOZOTOWN)</td>
<td>ZOZO Research, Saito et al. (NeurIPS Datasets 2021), about 26 million impressions, CC BY 4.0 (check)</td>
<td>[https://research.zozo.com/data.html](https://research.zozo.com/data.html)</td>
<td>Logged data from an A/B test of two recommendation policies (Bernoulli Thompson sampling vs. uniform random) on a fashion e-commerce site with true propensity scores, item features and clicks; a 10k-row sample ships with obp.</td>
<td>Advanced lab on bandits and off-policy evaluation. Free download.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Upworthy Research Archive</td>
<td>Matias, Munger, Aubin Le Quere and Ebersole, Scientific Data 8 (2021); 32,487 headline experiments, 150,817 arms, 538 million assignments; open access on OSF</td>
<td>[https://osf.io/jd64p/](https://osf.io/jd64p/)</td>
<td>Headline and image package A/B tests (impressions and clicks per arm) from 2013-2015, split into exploratory and confirmatory sets. Lets students run thousands of tests, see the distribution of effects, winner's curse and multiple testing.</td>
<td>Lab on meta-analysis of many A/B tests, CTR copy testing; exploratory sample for projects. Free, open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Udacity Free Trial Screener experiment</td>
<td>Udacity and Google A/B Testing course (UD257) final project, two CSVs (control, experiment) with about 37 days of daily aggregates</td>
<td>[https://github.com/XHuang2046/Udacity_AB_Test_Project](https://github.com/XHuang2046/Udacity_AB_Test_Project)</td>
<td>Daily pageviews, clicks, enrollments, payments for control and treatment; teaches invariant vs. evaluation metrics, sanity checks, unit of diversion (cookie vs. user-id) and Bonferroni. Course itself is free on Udacity.</td>
<td>Lab on metric design and sanity checks with aggregated data. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Starbucks rewards app offer data (Udacity capstone)</td>
<td>Starbucks and Udacity Data Scientist Nanodegree, simulated; portfolio (10 offers), profile (17,000 customers), transcript (306,534 events); JSON</td>
<td>[https://github.com/prateekparasher/Starbucks_Capstone](https://github.com/prateekparasher/Starbucks_Capstone)</td>
<td>Simulated BOGO, discount and informational offers with demographics and event logs. Not a clean RCT, so useful for discussing what is missing compared with a proper experiment and for offer-response modelling.</td>
<td>Project data with critical discussion of design. Free via GitHub mirrors; licence unclear, teaching use only.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Geo experiment sample data (GeoexperimentsResearch and GeoLift)</td>
<td>Google GeoexperimentsResearch (100 geos, daily sales and ad cost from 2015) and Meta GeoLift (GeoLift_PreTest / GeoLift_Test, US cities, daily conversions); both open source</td>
<td>[https://github.com/facebookincubator/GeoLift/blob/main/vignettes/GeoLift_Walkthrough.md](https://github.com/facebookincubator/GeoLift/blob/main/vignettes/GeoLift_Walkthrough.md)</td>
<td>Ready-made panel data for market selection, power simulation and synthetic-control or TBR analysis of geo lift tests.</td>
<td>Lab on geo experiments; data load with the packages. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Replication data: The Surrogate Index (Athey, Chetty, Imbens, Kang)</td>
<td>Opportunity Insights, Harvard Dataverse, doi:10.7910/DVN/QCKJYL</td>
<td>[https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QCKJYL](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QCKJYL)</td>
<td>Code and (simulated/public) data to reproduce surrogate index estimates of long-term effects from short-term outcomes; transferable to CLV or retention as long-run marketing outcomes.</td>
<td>Advanced reading lab on long-term effects. Free, open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Yahoo! Front Page Today Module click log (R6)</td>
<td>Yahoo Webscope, R6A/R6B, about 45 million user visits with uniformly random article display; academic licence on application</td>
<td>[https://webscope.sandbox.yahoo.com/catalog.php?datatype=r](https://webscope.sandbox.yahoo.com/catalog.php?datatype=r)</td>
<td>The classic benchmark for unbiased offline evaluation of contextual bandits (Li et al. 2010/2011): random logging policy enables replay evaluation of news recommendation.</td>
<td>Background for bandit session; access requires university application. Free for research, login.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Synthetic experiment generators (causalml.dataset, dowhy.datasets, tea-tasting make_users_data)</td>
<td>Uber CausalML, PyWhy DoWhy and tea-tasting packages, open source</td>
<td>[https://causalml.readthedocs.io/en/latest/](https://causalml.readthedocs.io/en/latest/)</td>
<td>Functions such as synthetic_data(mode=1..4), make_uplift_classification, linear_dataset and make_users_data simulate experiments with known true effects, so students can check whether estimators recover the truth and run power simulations.</td>
<td>Simulation labs on power, CUPED gains and HTE recovery. Free, open source.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Statistische Methoden (20)
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
<td>Two-sample proportion test, chi-square and Welch t-test</td>
<td>Kohavi, Tang and Xu (2020) Trustworthy Online Controlled Experiments, Cambridge University Press, ch. 2 and 17; companion site experimentguide.com</td>
<td>[https://experimentguide.com/](https://experimentguide.com/)</td>
<td>Baseline inference for conversion (z-test, chi-square) and revenue per user (Welch t-test, CLT with large n, bootstrap for heavy tails). Chapter 1 is a free download on the companion site.</td>
<td>Session 1 reading and lab with statsmodels and scipy. Book paid (about 40 EUR), WU-Lizenz prüfen; chapter 1 free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Power analysis, sample size and minimum detectable effect (MDE)</td>
<td>Key reference: All about sample-size calculations for A/B testing: novel extensions and practical guide (arXiv 2305.16459, 2023)</td>
<td>[https://arxiv.org/abs/2305.16459](https://arxiv.org/abs/2305.16459)</td>
<td>Covers sample size for proportions and means, ratio metrics, unequal allocation, multiple arms and how MDE trades off against test duration; connects to the 16 sigma squared over delta squared rule of thumb.</td>
<td>Lab: compute duration for a retail test given traffic; compare with Evan Miller calculator. Free, open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Sample ratio mismatch (SRM) check</td>
<td>Fabijan, Gupchup, Gupta, Omhover, Qin, Vermeer and Dmitriev (2019), KDD, Diagnosing Sample Ratio Mismatch in Online Controlled Experiments</td>
<td>[https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf](https://exp-platform.com/Documents/2019_KDDFabijanGupchupFuptaOmhoverVermeerDmitriev.pdf)</td>
<td>Chi-square goodness-of-fit test on group counts as the first trust check; taxonomy of SRM causes (assignment, execution, log processing, interference, bots) with rules of thumb.</td>
<td>Reading plus 10-minute lab step on every dataset. Free PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>CUPED / CUPAC variance reduction (regression adjustment)</td>
<td>Deng, Xu, Kohavi and Walker (2013), WSDM, Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data, doi 10.1145/2433396.2433413</td>
<td>[https://doi.org/10.1145/2433396.2433413](https://doi.org/10.1145/2433396.2433413)</td>
<td>Uses pre-period covariates as control variates; about 50 percent variance reduction at Bing. CUPAC (DoorDash) replaces the covariate with an ML prediction. Equivalent to ANCOVA/OLS with centred covariate, a link business students know.</td>
<td>Lab with tea-tasting or OLS on Hillstrom (history as covariate). Paper free on exp-platform.com.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Sequential testing: mSPRT and always-valid p-values</td>
<td>Johari, Koomen, Pekelis and Walsh (2022), Operations Research 70(3), 1806-1821, Always Valid Inference: Continuous Monitoring of A/B Tests, doi 10.1287/opre.2021.2135</td>
<td>[https://doi.org/10.1287/opre.2021.2135](https://doi.org/10.1287/opre.2021.2135)</td>
<td>Explains why peeking inflates false positives and how mixture SPRT gives p-values valid at any stopping time; basis of Optimizely's Stats Engine. arXiv preprint 1512.04922 is free.</td>
<td>Simulation lab: peeking inflates type I error; then apply always-valid test. Preprint free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Group sequential designs and alpha spending</td>
<td>Spotify Engineering (2023), Choosing a Sequential Testing Framework: Comparisons and Discussions; classic: O'Brien and Fleming (1979), Lan and DeMets (1983)</td>
<td>[https://engineering.atspotify.com/2023/03/choosing-sequential-testing-framework-comparisons-and-discussions](https://engineering.atspotify.com/2023/03/choosing-sequential-testing-framework-comparisons-and-discussions)</td>
<td>Practitioner comparison of group sequential tests vs. always-valid approaches with simulation evidence; implemented in spotify-confidence.</td>
<td>Reading for the sequential testing session. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Bayesian A/B testing (Beta-Binomial, probability to beat control, expected loss)</td>
<td>PyMC example gallery: Introduction to Bayesian A/B Testing (PyMC Labs); critical view: Deng (2015) Objective Bayesian two sample hypothesis testing for online controlled experiments, WWW</td>
<td>[https://www.pymc.io/projects/examples/en/latest/causal_inference/bayesian_ab_testing_introduction.html](https://www.pymc.io/projects/examples/en/latest/causal_inference/bayesian_ab_testing_introduction.html)</td>
<td>Conjugate and PyMC models for conversion and revenue, decision rules based on expected loss; discuss priors and why Bayesian results are not immune to peeking problems.</td>
<td>Lab in PyMC or Bambi; compare to frequentist result on the same data. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Multiple testing corrections (Bonferroni, Holm, Benjamini-Hochberg)</td>
<td>Benjamini and Hochberg (1995), Journal of the Royal Statistical Society B 57(1), 289-300, doi 10.1111/j.2517-6161.1995.tb02031.x</td>
<td>[https://doi.org/10.1111/j.2517-6161.1995.tb02031.x](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)</td>
<td>Needed for many metrics, segments and arms; FDR vs. FWER, primary vs. guardrail metrics; Upworthy archive shows the problem at scale.</td>
<td>Lab with statsmodels multipletests on segment analyses. Paper paywalled, WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Ratio metrics and the delta method</td>
<td>Deng, Knoblich and Lu (2018), KDD, Applying the Delta Method in Metric Analytics: A Practical Guide with Novel Ideas, arXiv 1803.06336</td>
<td>[https://arxiv.org/abs/1803.06336](https://arxiv.org/abs/1803.06336)</td>
<td>Click-through rate, revenue per session or basket size have randomisation unit (user) different from analysis unit; naive t-tests understate variance. Delta method gives correct standard errors.</td>
<td>Lab with tea-tasting ratio metrics. Free preprint.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Geo experiments and synthetic control (incl. cluster randomisation)</td>
<td>Vaver and Koehler (2011), Measuring Ad Effectiveness Using Geo Experiments, Google; Abadie (2021), Journal of Economic Literature 59(2), Using Synthetic Controls; implemented in GeoLift</td>
<td>[https://facebookincubator.github.io/GeoLift/docs/intro/](https://facebookincubator.github.io/GeoLift/docs/intro/)</td>
<td>When users cannot be randomised (TV, offline stores, privacy limits), randomise or match markets and build counterfactuals; covers power with few clusters and iROAS.</td>
<td>Session on offline/omnichannel retail; GeoLift docs as hands-on guide. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Switchback experiments</td>
<td>Bojinov, Simchi-Levi and Zhao (2023), Management Science 69(7), 3759-3777, Design and Analysis of Switchback Experiments, doi 10.1287/mnsc.2022.4583</td>
<td>[https://doi.org/10.1287/mnsc.2022.4583](https://doi.org/10.1287/mnsc.2022.4583)</td>
<td>Alternate treatment over time periods when units interfere (pricing, delivery fees, marketplace algorithms); optimal period length under carryover effects; randomisation inference.</td>
<td>Reading for advanced session on marketplace and pricing experiments. Paywalled, WU-Lizenz prüfen; HBS working paper free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Difference-in-differences and Bayesian structural time series (CausalImpact) as quasi-experiments</td>
<td>Brodersen, Gallusser, Koehler, Remy and Scott (2015), Annals of Applied Statistics 9(1), Inferring causal impact using Bayesian structural time-series models, doi 10.1214/14-AOAS788; Cunningham, Causal Inference: The Mixtape, ch. 9</td>
<td>[https://doi.org/10.1214/14-AOAS788](https://doi.org/10.1214/14-AOAS788)</td>
<td>For campaigns launched without randomisation: parallel trends, event-study plots, and BSTS counterfactuals; contrast with RCT evidence (Gordon et al. 2019).</td>
<td>Lab with tfcausalimpact or statsmodels DiD regression. Paper open access; Mixtape free online.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Multi-armed bandits and Thompson sampling</td>
<td>Russo, Van Roy, Kazerouni, Osband and Wen (2018), A Tutorial on Thompson Sampling, Foundations and Trends in ML, arXiv 1707.02038; marketing application: Schwartz, Bradlow and Fader (2017), Marketing Science 36(4), doi 10.1287/mksc.2016.1023</td>
<td>[https://arxiv.org/abs/1707.02038](https://arxiv.org/abs/1707.02038)</td>
<td>Adaptive allocation to minimise regret during the test (display ads, headlines, offers); trade-off between earning and learning, and the bias of estimates from adaptive designs.</td>
<td>Simulation lab with MABWiser; Schwartz et al. as marketing reading (WU-Lizenz prüfen). Tutorial free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Heterogeneous treatment effects and uplift: meta-learners (S, T, X, R, DR)</td>
<td>Kuenzel, Sekhon, Bickel and Yu (2019), PNAS 116(10), 4156-4165, Metalearners for estimating heterogeneous treatment effects using machine learning, doi 10.1073/pnas.1804597116</td>
<td>[https://doi.org/10.1073/pnas.1804597116](https://doi.org/10.1073/pnas.1804597116)</td>
<td>Framework behind CausalML and EconML; Qini/uplift curves for targeting decisions; links A/B testing to customer targeting and CRM.</td>
<td>Lab on Hillstrom or Criteo with CausalML. Open access.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Causal forests and targeting on treatment effect (not risk)</td>
<td>Wager and Athey (2018), JASA 113(523), doi 10.1080/01621459.2017.1319839; marketing application: Ascarza (2018), Journal of Marketing Research 55(1), 80-98, Retention Futility, doi 10.1509/jmr.16.0163</td>
<td>[https://doi.org/10.1509/jmr.16.0163](https://doi.org/10.1509/jmr.16.0163)</td>
<td>Ascarza shows with two field experiments that targeting customers with highest churn risk is less effective than targeting by estimated sensitivity to the intervention; causal forests (grf, EconML) estimate that sensitivity.</td>
<td>Core reading for the uplift session; lab with grf or EconML. JMR paywalled, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Interference and experiments in two-sided marketplaces</td>
<td>Johari, Li, Liskovich and Weintraub (2022), Management Science 68(10), Experimental Design in Two-Sided Platforms: An Analysis of Bias, doi 10.1287/mnsc.2021.4247</td>
<td>[https://doi.org/10.1287/mnsc.2021.4247](https://doi.org/10.1287/mnsc.2021.4247)</td>
<td>SUTVA violations when treated and control buyers compete for the same supply (Airbnb, eBay, ride-hailing); customer-side vs. listing-side randomisation and bias direction.</td>
<td>Reading for advanced session on platforms. Paywalled, WU-Lizenz prüfen; arXiv preprint free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Long-term effects and surrogate indices</td>
<td>Athey, Chetty, Imbens and Kang, The Surrogate Index, NBER Working Paper 26463 (2019), Review of Economic Studies (2026)</td>
<td>[https://www.nber.org/papers/w26463](https://www.nber.org/papers/w26463)</td>
<td>Combines short-term outcomes into an index predicting long-term outcomes (e.g. CLV, retention) under surrogacy assumptions; motivates holdout groups and novelty/primacy discussion.</td>
<td>Reading for the session on short-term metrics vs. long-term value. Free working paper.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Ghost ads, PSA controls and advertising lift tests</td>
<td>Johnson, Lewis and Nubbemeyer (2017), Journal of Marketing Research 54(6), 867-884, Ghost Ads: Improving the Economics of Measuring Online Ad Effectiveness, doi 10.1509/jmr.15.0297</td>
<td>[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2620078](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2620078)</td>
<td>Compares ITT, PSA and ghost-ad designs for ad experiments; ghost ads log the would-be exposures in control, raising precision by an order of magnitude at lower cost. Retargeting case: plus 17 percent visits, 10.5 percent purchases.</td>
<td>Core reading for ad incrementality; pairs with the Kaggle ad vs. PSA data. SSRN version free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Intent-to-treat vs. treatment-on-the-treated (non-compliance, exposure)</td>
<td>Gordon, Zettelmeyer, Bhargava and Chapsky (2019), Marketing Science 38(2), 193-225, A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook, doi 10.1287/mksc.2018.1135</td>
<td>[https://ideas.repec.org/a/inm/ormksc/v38y2019i2p193-225.html](https://ideas.repec.org/a/inm/ormksc/v38y2019i2p193-225.html)</td>
<td>15 Facebook lift experiments with 500 million user observations: ITT, exposure-based effects via Wald/IV scaling, and why observational methods overestimate ad effects. Also Blake, Nosko and Tadelis (2015) Econometrica on eBay paid search.</td>
<td>Reading and lab with Criteo uplift (treatment vs. exposure columns). Paywalled, WU-Lizenz prüfen; MSI working paper version free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Off-policy evaluation of recommendation and targeting policies</td>
<td>Saito, Aihara, Matsutani and Narita (2021), Open Bandit Dataset and Pipeline: Towards Realistic and Reproducible Off-Policy Evaluation, NeurIPS Datasets and Benchmarks, arXiv 2008.07146</td>
<td>[https://arxiv.org/abs/2008.07146](https://arxiv.org/abs/2008.07146)</td>
<td>Evaluate a new policy with logged randomised data (IPW, doubly robust) before an online test; shows how experiments generate reusable data assets.</td>
<td>Advanced reading with obp lab. Free preprint.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Communities & Events (16)
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
<td>MeasureCamp Vienna</td>
<td>MeasureCamp Vienna committee (volunteers), Vienna; annual unconference since 18 Nov 2023 (first at The Social Hub Vienna)</td>
<td>[https://vienna.measurecamp.org/](https://vienna.measurecamp.org/)</td>
<td>Free analytics unconference where attendees propose sessions on the day; typical topics include tracking, consent, attribution and A/B testing. Part of the global MeasureCamp network (26 events in 2025).</td>
<td>Students can attend for free (registration fills quickly) and observe or run a session; good place to scout Vienna practitioners as guest speakers. German and English, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna Data Science Group (VDSG)</td>
<td>Non-profit association, Vienna; regular meetups and workshops (e.g. 29 Oct 2026)</td>
<td>[https://viennadatasciencegroup.at/](https://viennadatasciencegroup.at/)</td>
<td>Largest Vienna data-science community; meetups on ML and AI. No experimentation-specific session found in search, but a fitting venue for a talk on A/B testing.</td>
<td>Students can join meetups for free; the instructor can find speakers or co-host a session on experimentation. English and German, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>PyData Vienna</td>
<td>PyData Vienna meetup (NumFOCUS network), Vienna; meetups several times per year</td>
<td>[https://www.meetup.com/pydata-vienna/](https://www.meetup.com/pydata-vienna/)</td>
<td>Python data community; causal-inference and A/B-testing talks are common at PyData events internationally (e.g. PyData Global, PyCon DE & PyData), not confirmed for Vienna.</td>
<td>Free meetups for students with Python skills; place to recruit technical speakers. English, on-site.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>SUPERWEEK</td>
<td>SUPERWEEK (Zoltán Bánóczy), near Budapest, Hungary; annual, late January/early February (2027: 31 Jan to 5 Feb)</td>
<td>[https://www.superweek.hu/](https://www.superweek.hu/)</td>
<td>'Five Days of Analytics' conference with talks on measurement, privacy, attribution and experimentation; Austrian speakers attend (e.g. Thomas Tauchner, JENTIS).</td>
<td>Speaker lists for finding guest speakers; recorded talks for class. Paid, English, on-site in Hungary.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>CODE@MIT (Conference on Digital Experimentation)</td>
<td>MIT Initiative on the Digital Economy, Cambridge MA; annual, autumn</td>
<td>[https://ide.mit.edu/](https://ide.mit.edu/)</td>
<td>Leading academic and industry conference on online experiments: interference, adaptive designs, ad measurement; speakers from Meta, Microsoft, Amazon and top business schools.</td>
<td>Programme and recorded sessions as source of current research and speakers; for master or PhD level. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Experimentation Culture Awards</td>
<td>Experimentation Culture Awards (community-run, international); annual awards with online ceremony</td>
<td>[https://experimentationcultureawards.com/](https://experimentationcultureawards.com/)</td>
<td>Awards for companies and individuals building experimentation cultures; finalist case write-ups show how firms organise testing programmes.</td>
<td>Finalist cases as short reading or student presentation material; English, online.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>CXL (CXL Institute, blog and former CXL Live)</td>
<td>CXL, Estonia / online; courses, blog; CXL Live conference not held regularly in recent years (check)</td>
<td>[https://cxl.com/blog/ab-testing-guide/](https://cxl.com/blog/ab-testing-guide/)</td>
<td>Large practitioner knowledge base on A/B testing and CRO (complete A/B testing guide, statistics articles); paid courses and certificates.</td>
<td>Blog articles as free reading; courses optional for interested students. English, online.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Conversion Hotel (#CH2026)</td>
<td>Online Dialogue, Texel, Netherlands; annual, November</td>
<td>[https://conversionhotel.com/](https://conversionhotel.com/)</td>
<td>Leading European conference for CRO and experimentation practitioners; strong speaker line-up on behavioural science and testing programmes.</td>
<td>Speaker lists to find European guest speakers; paid, English, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Experimentation Island</td>
<td>Experimentation Island (community conference), Europe; annual (location and organiser to check)</td>
<td>[https://www.experimentationisland.com/](https://www.experimentationisland.com/)</td>
<td>Small practitioner retreat on experimentation culture and statistics; attracts senior experimentation leads.</td>
<td>Scouting for speakers rather than for students; English. Details not verified.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>JETZT Conversion (JETZT Konferenzen)</td>
<td>JETZT Konferenzen series, Vienna; conversion edition held repeatedly (e.g. 23-24 May 2023, also April and November editions)</td>
<td>[https://internetworld.at/jetzt-das-aktualisierte-programm-der-jetzt-konferenzen-downloaden/](https://internetworld.at/jetzt-das-aktualisierte-programm-der-jetzt-konferenzen-downloaden/)</td>
<td>Vienna conference on conversion optimization, growth marketing, customer journey analysis and data; main local stage for Austrian CRO practitioners.</td>
<td>Speaker list as the best source for Austrian CRO guest speakers; possibly student tickets. German, on-site in Vienna. Next date to check.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Experimentation Unite (Kameleoon tour, Vienna stop)</td>
<td>Kameleoon (A/B testing vendor); European tour with a Vienna stop on 21 May (year to check)</td>
<td>[https://pages.kameleoon.com/en/experimentation-unite-europe](https://pages.kameleoon.com/en/experimentation-unite-europe)</td>
<td>Vendor-hosted meet-up on experimentation with practitioner talks; one of the few experimentation-specific events in Vienna.</td>
<td>Free or low-cost practitioner networking; good for finding Vienna experimentation leads. Vendor event. English or German, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Measure Slack (#measure community)</td>
<td>Measure community (analytics practitioners), online Slack workspace; continuous</td>
<td>[https://www.measure.chat/](https://www.measure.chat/)</td>
<td>Global analytics Slack with channels on testing, attribution and tooling; practitioners answer questions on A/B test setups.</td>
<td>Students can join for free and ask questions for projects. English, online.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Experimental Mind (newsletter)</td>
<td>Kevin Anderson, Substack newsletter; weekly</td>
<td>[https://kevinanderson.substack.com/](https://kevinanderson.substack.com/)</td>
<td>Weekly round-up of experimentation and CRO news, articles, jobs and events; good entry point into the community.</td>
<td>Recommend to students for keeping up to date; free, English, online.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>OMR Festival</td>
<td>OMR (Online Marketing Rockstars), Hamburg; annual, May</td>
<td>[https://omr.com/](https://omr.com/)</td>
<td>Largest German-language digital-marketing festival; sessions on performance marketing, CRO and A/B testing; OMR Reviews has A/B-testing tool comparisons.</td>
<td>Talks on OMR's channels as German-language input; speaker scouting in DACH. German, on-site in Hamburg, paid.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Handelsverband events and eCommerce Studie Österreich</td>
<td>Handelsverband (Austrian Retail Association), Vienna; annual study (with KMU Forschung Austria) and retail and e-commerce events</td>
<td>[https://www.handelsverband.at/publikationen/studien/ecommerce-studie-oesterreich/ecommerce-studie-oesterreich-2026/](https://www.handelsverband.at/publikationen/studien/ecommerce-studie-oesterreich/ecommerce-studie-oesterreich-2026/)</td>
<td>Context for Austrian online retail; events gather Austrian retailers' e-commerce leads, a route to practitioner speakers from retail chains.</td>
<td>Study as background reading; events for networking with Austrian retailers. German, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Predictive Analytics Konferenz Wien</td>
<td>Predictive Analytics Austria, Vienna; annual conference</td>
<td>[https://www.predictive-analytics.at/main.asp?kat1=108&kat2=715](https://www.predictive-analytics.at/main.asp?kat1=108&kat2=715)</td>
<td>Vienna conference on analytics and data science in business; source of Austrian analytics speakers. Experimentation focus not confirmed.</td>
<td>Programme for speaker scouting in Vienna. German, on-site.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### People (40)
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
<td>Christina Schamp</td>
<td>WU Wien, Full Professor, Head of Institute for Digital Marketing and Behavioral Insights; Wien; academic</td>
<td>[https://www.wu.ac.at/en/digital/team/christina-schamp](https://www.wu.ac.at/en/digital/team/christina-schamp)</td>
<td>Behavioral experiments are the core of her work; runs lab and field experiments, e.g. pre-commitment pricing field experiment with a language-learning app, and the first field study of sales effects of cause-related marketing promotions in retail (Schamp, Heitmann, Peers, Leeflang, JMR 2024). Strongest WU match for experiments in digital marketing and retail.</td>
<td>Very good fit for an on-site guest lecture or Q&A in Vienna: how to set up a field experiment with a company partner, and what a JMR-level field study in retail looks like. English or German. Colleague in-house, easy to arrange.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Nils Wlömert</td>
<td>WU Wien, Professor of Marketing, Head of Institute for Retailing and Data Science (Stand Suchergebnis 2026); Wien; academic</td>
<td>[https://www.wu.ac.at/en/retail/about-us/team-1/prof-nils-wloemert](https://www.wu.ac.at/en/retail/about-us/team-1/prof-nils-wloemert)</td>
<td>Empirical work on digital platforms, streaming and media markets with causal inference methods (e.g. cancel-culture streaming study with Winkler and Liaukonyte). Responsible for the open WU course book Marketing Research Design and Analysis (imsmwu.github.io), with R code for hypothesis tests and experimental data analysis. Caution: a search snippet linked him to the auto-renewal newspaper field experiment, but that paper is by Miller, Sahni and Strulov-Shlain.</td>
<td>On-site input on analysing experimental and quasi-experimental marketing data in R; the MRDA materials can be reused in labs. German or English.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Martin Schreier</td>
<td>WU Wien, Professor of Marketing, Head of Department of Marketing and Institute for Marketing Management; Wien; academic</td>
<td>[https://www.wu.ac.at/en/mm/team/martin-schreier](https://www.wu.ac.at/en/mm/team/martin-schreier)</td>
<td>Co-author of two randomized field experiments in retail on the market value of crowdsourced products (Nishikawa, Schreier, Fuchs, Ogawa, JMR 2017, with Japanese retailer Muji). A retail field-experiment example rather than online A/B testing.</td>
<td>Short on-site talk or Q&A on running randomized field experiments in a retail context. German or English.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Daniel Winkler</td>
<td>Postdoctoral fellow UNSW Sydney School of Marketing and research fellow WU Wien (according to CV, Stand Suchergebnis; check current role); Wien / Global; academic</td>
<td>[https://dwinkler.org/](https://dwinkler.org/)</td>
<td>WU PhD; works on causal inference, Bayesian statistics and digital markets (streaming, social media boycotts). No experimentation-specific publication confirmed; the link to the topic is through causal-inference methods.</td>
<td>Remote session on causal inference for marketing data in R or Python. German or English. Location may be Sydney, which makes timing hard.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Julia Neidhardt</td>
<td>TU Wien Informatics, Assistant Professor, Head of Christian Doppler Lab for Recommender Systems in Multi-Domain Settings; Wien; academic</td>
<td>[https://informatics.tuwien.ac.at/people/julia-neidhardt](https://informatics.tuwien.ac.at/people/julia-neidhardt)</td>
<td>Her CD lab works with the Austrian media house Falter and YKMB on recommender systems. The industry partnership allows live observation of system changes over long periods, i.e. online evaluation and A/B testing of recommenders in news and tourism. Diversity and fairness of recommendations.</td>
<td>On-site guest talk on online experiments for recommender systems in Austrian media; good for the bridge between offline metrics and A/B tests. German or English.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Siegfried Stepke</td>
<td>e-dialog (Vienna analytics and Google Marketing Platform agency), founder and managing director; Wien; practitioner</td>
<td>[https://about.me/siegfried.stepke](https://about.me/siegfried.stepke)</td>
<td>Founder of the ProgrammatiCon conference in Vienna; presented Google Optimize 360 testing and personalisation and the Google Marketing Platform including testing. Long-standing speaker at Austrian analytics conferences. Optimize has since been discontinued, so ask about current testing tools.</td>
<td>Practitioner guest talk in Vienna on how Austrian brands organise testing, analytics and personalisation in agencies. German, likely English too.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Thomas Tauchner</td>
<td>JENTIS (Vienna, server-side tracking), CEO and co-founder; earlier founder of analytics agency Webrocket; Wien; practitioner</td>
<td>[https://saas.group/podcasts/creating-true-ai-value-in-a-privacy-first-analytics-world-with-thomas-tauchner-jentis/](https://saas.group/podcasts/creating-true-ai-value-in-a-privacy-first-analytics-world-with-thomas-tauchner-jentis/)</td>
<td>Indirect topic link: consent loss and tracking gaps distort conversion data and therefore experiment results. JENTIS Synthetic Users (2024) model untracked conversions for ad networks. Speaker at SUPERWEEK 2023 and 2025.</td>
<td>Guest talk in Vienna on data quality, GDPR consent and measurement limits for A/B tests and campaign experiments. German or English. Note: this is a vendor perspective.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Armin Larndorfer</td>
<td>KlickImpuls (Linz agency), contact for tracking and CRO, over 15 years experience; Österreich; practitioner</td>
<td>[https://www.klickimpuls.at/conversion-rate-optimierung/](https://www.klickimpuls.at/conversion-rate-optimierung/)</td>
<td>Weakly evidenced: named on agency page as CRO and tracking lead. No public talks or publications on experimentation found.</td>
<td>Possible remote or on-site practitioner talk on CRO for Austrian SMEs. German. Check speaking experience first.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Matthias Wieser</td>
<td>Lecturer, Master Digital Marketing and Kommunikation, FH St. Pölten (USTP); Österreich; practitioner / lecturer</td>
<td>[https://www.fhstp.ac.at/de/newsroom/news/umfassende-weiterbildung-in-online-marketing](https://www.fhstp.ac.at/de/newsroom/news/umfassende-weiterbildung-in-online-marketing)</td>
<td>Weakly evidenced: FH news names him for student projects on website analysis and conversion optimization with Google Analytics, Hotjar and UsabilityHub. No dedicated experimentation publications found.</td>
<td>Peer exchange about teaching CRO projects; possible short practitioner input. German.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Ron Kohavi</td>
<td>Independent consultant and Maven instructor; formerly Airbnb, Microsoft (ExP), Amazon; Global; practitioner / communicator</td>
<td>[https://maven.com/kohavi](https://maven.com/kohavi)</td>
<td>Lead author of Trustworthy Online Controlled Experiments (Cambridge UP 2020, with Tang and Xu), the reference book for A/B testing. Teaches Maven courses Accelerating Innovation with A/B Testing and Advanced Topics in Practical A/B Testing (cohorts Oct and Nov/Dec 2026). Twyman's law, OEC, sample ratio mismatch.</td>
<td>Top choice for a remote keynote or recorded interview (English); his course and LinkedIn posts are good student resources. Likely paid consulting rates.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Diane Tang</td>
<td>Google, Google Fellow (Stand Wissensstand; check current role); Global; practitioner</td>
<td>[https://experimentguide.com/](https://experimentguide.com/)</td>
<td>Co-author of Trustworthy Online Controlled Experiments; lead author of 'Overlapping Experiment Infrastructure: More, Better, Faster Experimentation' (KDD 2010), which describes Google's layered experiment system.</td>
<td>Recorded interview or remote Q&A on experiment infrastructure at scale. English. Hard to book.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Ya Xu</td>
<td>Formerly VP Engineering and Head of Data, LinkedIn (check current role); Global; practitioner</td>
<td>[https://experimentguide.com/](https://experimentguide.com/)</td>
<td>Co-author of Trustworthy Online Controlled Experiments; built LinkedIn's XLNT experimentation platform; papers on network effects and A/B testing in social networks (KDD 2015).</td>
<td>Remote talk on experimentation culture and network interference. English. Current role not verified.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Lukas Vermeer</td>
<td>Vista, Senior Director of Experimentation (Stand Suchergebnis); formerly 8 years responsible for A/B testing at Booking.com; advisor to ABsmartly; Global; practitioner / communicator</td>
<td>[https://www.lukasvermeer.nl/speaking/mediakit/](https://www.lukasvermeer.nl/speaking/mediakit/)</td>
<td>Leading European voice on scaling experimentation (Booking.com culture, empowered teams, SRM checks). Has a speaker media kit and speaks frequently at conferences and on podcasts.</td>
<td>Very good remote guest lecture (Netherlands, English); open to speaking requests via media kit. A Booking.com case plus a live talk work well together.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Stefan Thomke</td>
<td>Harvard Business School, Professor of Business Administration (check current title); German-born; Global (DACH roots); academic</td>
<td>[https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6875](https://www.hbs.edu/faculty/Pages/profile.aspx?facId=6875)</td>
<td>Author of Experimentation Works: The Surprising Power of Business Experiments (HBR Press 2020) and, with Kohavi, 'The Surprising Power of Online Experiments' (HBR 2017). HBS cases on Booking.com experimentation.</td>
<td>Book chapters and HBS cases for the managerial side; a remote talk is unlikely but a recorded HBR interview works. English, possibly German. Profile URL constructed.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Georgi Georgiev</td>
<td>Analytics-Toolkit.com, founder; Bulgaria; Global; practitioner / communicator</td>
<td>[https://www.analytics-toolkit.com/](https://www.analytics-toolkit.com/)</td>
<td>Author of Statistical Methods in Online A/B Testing (2019); writes on sequential testing (AGILE), power, minimum detectable effect and common statistical errors in CRO. Calculators can be used in class.</td>
<td>Remote guest session on test statistics and planning (English, European time zone). His blog and tools are good for labs.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Sean J. Taylor</td>
<td>Formerly Facebook Core Data Science and Lyft (head of rideshare labs); co-founder Motif Analytics (Stand Wissensstand; check current role); Global; practitioner / communicator</td>
<td>[https://seanjtaylor.com/](https://seanjtaylor.com/)</td>
<td>Prophet co-author; talks and threads on experimentation at Facebook and Lyft, marketplace experiments and switchback designs; field experiments on social influence (with Aral, Muchnik).</td>
<td>Remote talk or podcast clip on experimentation in two-sided marketplaces. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Dean Eckles</td>
<td>MIT Sloan School of Management, Associate Professor of Marketing (check current title); Global; academic</td>
<td>[https://deaneckles.com/](https://deaneckles.com/)</td>
<td>Formerly at Facebook; large-scale field experiments on peer effects and advertising, design of experiments under network interference, bootstrap for dependent data in online experiments.</td>
<td>Remote research talk for advanced students on interference and social advertising experiments. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Duncan J. Watts</td>
<td>University of Pennsylvania (Annenberg, Wharton, Engineering), Stevens University Professor; Global; academic</td>
<td>[https://css.seas.upenn.edu/](https://css.seas.upenn.edu/)</td>
<td>MusicLab experiment on social influence and success (Salganik, Dodds, Watts, Science 2006), a classic online experiment on social proof; also work on ad effectiveness at Yahoo and Microsoft Research.</td>
<td>Use MusicLab as a teaching example; a remote talk is unlikely. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Eytan Bakshy</td>
<td>Meta, leads Adaptive Experimentation group (Stand Wissensstand; check current role); Global; practitioner / academic</td>
<td>[https://eytan.github.io/](https://eytan.github.io/)</td>
<td>Creator of PlanOut (KDD 2014) and the open-source Ax / BoTorch platform for adaptive experiments and Bayesian optimisation; social advertising field experiments on Facebook (Bakshy et al. 2012).</td>
<td>Remote technical talk on adaptive experimentation and bandits; Ax tutorials for advanced labs. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Susan Athey</td>
<td>Stanford Graduate School of Business, Economics of Technology Professor; Global; academic</td>
<td>[https://athey.people.stanford.edu/](https://athey.people.stanford.edu/)</td>
<td>Causal machine learning (causal forests, heterogeneous treatment effects), contextual bandits and adaptive experiments; former chief economist at Microsoft and Bing experimentation background.</td>
<td>Recorded lectures (e.g. her ML and causal inference videos) instead of a live talk. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Garrett A. Johnson</td>
<td>Boston University Questrom School of Business, Associate Professor of Marketing (check title); Global; academic</td>
<td>[https://www.bu.edu/questrom/profile/garrett-johnson/](https://www.bu.edu/questrom/profile/garrett-johnson/)</td>
<td>Developed ghost ads for measuring ad effectiveness in field experiments (Johnson, Lewis, Nubbemeyer, JMR 2017); work on GDPR effects and on large-scale ad experiment meta-analyses.</td>
<td>Remote talk on ad-lift experiments and ghost ads; the ghost-ads paper is a core reading. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Brett R. Gordon</td>
<td>Kellogg School of Management, Northwestern University, Professor of Marketing; Global; academic</td>
<td>[https://www.kellogg.northwestern.edu/faculty/directory/gordon_brett.aspx](https://www.kellogg.northwestern.edu/faculty/directory/gordon_brett.aspx)</td>
<td>Lead author of 'A Comparison of Approaches to Advertising Measurement: Evidence from Big Field Experiments at Facebook' (Marketing Science 2019) and follow-up on whether observational methods can replace RCTs (2023).</td>
<td>Reading plus remote Q&A on why observational ad measurement fails. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Florian Zettelmeyer</td>
<td>Kellogg School of Management, Northwestern University, Professor of Marketing; German; Global (DACH roots); academic</td>
<td>[https://www.kellogg.northwestern.edu/faculty/directory/zettelmeyer_florian.aspx](https://www.kellogg.northwestern.edu/faculty/directory/zettelmeyer_florian.aspx)</td>
<td>Co-author of the Facebook ad field experiments comparison (Marketing Science 2019); teaches analytics for managers with a focus on causal inference and experiments.</td>
<td>Remote talk for managers on experiments vs. observational data; German possible. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Elea McDonnell Feit</td>
<td>Drexel University LeBow College of Business, Associate Professor of Marketing; Global; academic</td>
<td>[https://eleafeit.com/](https://eleafeit.com/)</td>
<td>Test and Roll: profit-maximizing A/B tests (Feit and Berman, Marketing Science 2019); co-author of R for Marketing Research and Analytics; open A/B-testing workshop materials in R for marketers.</td>
<td>Very good teaching fit: her open workshop slides and R code can be used directly; remote guest session realistic. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Ron Berman</td>
<td>The Wharton School, University of Pennsylvania, Assistant/Associate Professor of Marketing (check title); Global; academic</td>
<td>[https://www.ronberman.com/](https://www.ronberman.com/)</td>
<td>Test and Roll (with Feit); 'p-Hacking and False Discovery in A/B Testing' (with Pekelis, Scott, Van den Bulte) using Optimizely data; work on attribution.</td>
<td>Reading on p-hacking in A/B tests; remote Q&A. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Anja Lambrecht</td>
<td>London Business School, Professor of Marketing; German; Global (DACH roots); academic</td>
<td>[https://www.london.edu/faculty-and-research/faculty-profiles/l/lambrecht-a](https://www.london.edu/faculty-and-research/faculty-profiles/l/lambrecht-a)</td>
<td>Field experiments in online advertising: retargeting (Lambrecht and Tucker, JMR 2013), algorithmic bias in STEM job ads (Management Science 2019); measurement of digital marketing.</td>
<td>Remote guest lecture from London; German or English. Retargeting paper suits a class discussion.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Catherine Tucker</td>
<td>MIT Sloan School of Management, Sloan Distinguished Professor of Management and Professor of Marketing; Global; academic</td>
<td>[https://mitsloan.mit.edu/faculty/directory/catherine-tucker](https://mitsloan.mit.edu/faculty/directory/catherine-tucker)</td>
<td>Many field experiments in digital advertising and privacy (e.g. Goldfarb and Tucker on privacy regulation and ad effectiveness, retargeting with Lambrecht); co-chairs research on digital economy.</td>
<td>Recorded talks and papers; a remote talk is possible but hard to book. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Navdeep S. Sahni</td>
<td>Stanford Graduate School of Business, Associate Professor of Marketing (check title); Global; academic</td>
<td>[https://www.gsb.stanford.edu/faculty-research/faculty/navdeep-s-sahni](https://www.gsb.stanford.edu/faculty-research/faculty/navdeep-s-sahni)</td>
<td>Field experiments on search advertising, ad signalling and subscriptions; co-author of 'Sophisticated Consumers with Inertia' (Miller, Sahni, Strulov-Shlain): auto-renewal contracts tested on over 1 million readers of a European newspaper lowered take-up by 35 percent.</td>
<td>Subscription field experiment as a retail and pricing case; remote Q&A. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Klaus M. Miller</td>
<td>HEC Paris, Assistant Professor of Marketing (check title); German; Global (DACH); academic</td>
<td>[https://www.hec.edu/en/faculty-research/faculty-directory/faculty-member/miller-klaus](https://www.hec.edu/en/faculty-research/faculty-directory/faculty-member/miller-klaus)</td>
<td>Lead author of the large newspaper subscription field experiment on auto-renewal (SSRN 4065098, AEA RCT registry); research on digital news pricing and privacy in online advertising.</td>
<td>Remote guest talk in German or English on running a million-user pricing experiment with a publisher; geographically close (Paris).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Steven Tadelis</td>
<td>UC Berkeley Haas School of Business, Professor of Economics, Business and Public Policy; Global; academic</td>
<td>[https://haas.berkeley.edu/faculty/tadelis-steven/](https://haas.berkeley.edu/faculty/tadelis-steven/)</td>
<td>eBay paid-search experiment showing brand-keyword ads had near-zero returns (Blake, Nosko, Tadelis, Econometrica 2015), a key case for why experiments beat attribution; former eBay and Amazon economist.</td>
<td>The eBay study as a lecture case; remote Q&A. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Ramesh Johari</td>
<td>Stanford University, Professor of Management Science and Engineering; Global; academic</td>
<td>[https://web.stanford.edu/\~rjohari/](https://web.stanford.edu/~rjohari/)</td>
<td>Always-valid p-values and sequential testing behind Optimizely's Stats Engine (Johari, Pekelis, Walsh, Koomen); marketplace experiment design and interference.</td>
<td>Reading on peeking problems; remote technical talk. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Aleksander Fabijan</td>
<td>Microsoft, Experimentation Platform (ExP), data scientist / product manager (Stand Wissensstand; check current role); Slovenian; Global; practitioner / academic</td>
<td>[https://www.linkedin.com/in/aleksanderfabijan/](https://www.linkedin.com/in/aleksanderfabijan/)</td>
<td>PhD on experimentation growth; 'Experimentation growth: Evolving trustworthy A/B testing capabilities in online software companies' (Journal of Software: Evolution and Process 2018) and the Experimentation Evolution Model; many ExP papers on pitfalls.</td>
<td>Remote talk on experimentation maturity models; European time zone. English.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Maximilian Kasy</td>
<td>University of Oxford, Professor of Economics; Global; academic</td>
<td>[https://maxkasy.github.io/home/](https://maxkasy.github.io/home/)</td>
<td>Adaptive experimental design: exploration sampling for policy choice (Kasy and Sautmann, Econometrica 2021), adaptive targeted field experiment for refugees in Jordan; bridges bandits and classic RCTs.</td>
<td>Remote advanced talk on adaptive experiments and bandits. English.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Chetan Sharma</td>
<td>Eppo, founder and CEO (Eppo acquired by Datadog in 2025, Stand Wissensstand; check current role); formerly Airbnb and Webflow data; Global; practitioner</td>
<td>[https://www.geteppo.com/](https://www.geteppo.com/)</td>
<td>Built Eppo, a warehouse-native experimentation platform with CUPED and sequential tests; frequent writer and podcast guest on experimentation culture.</td>
<td>Remote talk on modern experimentation tooling and the vendor market. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Vijaye Raji</td>
<td>Founder of Statsig; after acquisition by OpenAI in 2025 CTO of Applications at OpenAI (Stand Wissensstand; check); formerly Facebook; Global; practitioner</td>
<td>[https://www.statsig.com/](https://www.statsig.com/)</td>
<td>Statsig productised Facebook-style experimentation (feature gates, pulse metrics, CUPED) for startups; shows the industry practice of experimentation as a product.</td>
<td>Background example rather than a speaker; hard to book. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Graham McNicoll</td>
<td>GrowthBook, co-founder and CEO; Global; practitioner</td>
<td>[https://www.growthbook.io/](https://www.growthbook.io/)</td>
<td>GrowthBook is an open-source feature-flagging and A/B testing platform with Bayesian and frequentist engines; students can install it for free for projects.</td>
<td>Remote demo for a lab session, combined with the open-source tool. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Peep Laja</td>
<td>Founder of CXL (CXL Institute) and Wynter (message testing); Estonia; Global; practitioner / communicator</td>
<td>[https://www.linkedin.com/in/peeplaja/](https://www.linkedin.com/in/peeplaja/)</td>
<td>Popularised research-driven CRO and A/B testing (CXL blog, ResearchXL framework, CXL Live conference); now focuses on B2B message testing at Wynter.</td>
<td>Remote guest talk for practitioner CRO perspective; CXL articles as reading. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Chris Goward</td>
<td>Founder of WiderFunnel (later Conversion.com), author; Canada; Global; practitioner (check current role)</td>
<td>[https://www.linkedin.com/in/chrisgoward/](https://www.linkedin.com/in/chrisgoward/)</td>
<td>Author of You Should Test That! (Wiley 2013); LIFT model for conversion hypotheses, early agency-side experimentation programmes for large brands.</td>
<td>LIFT model as a framework for student test hypotheses; a recorded talk rather than a live guest. English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>André Morys</td>
<td>konversionsKRAFT (Germany), founder and CEO; Global (DACH); practitioner / communicator</td>
<td>[https://www.konversionskraft.de/](https://www.konversionskraft.de/)</td>
<td>One of the best-known German-language CRO and experimentation voices; author on digital growth strategy and psychology in conversion optimisation; frequent speaker at German CRO conferences.</td>
<td>Strong fit for a German-language remote or on-site guest talk on CRO programmes in German-speaking retail. German and English.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Tobias Aubele</td>
<td>Professor of E-Commerce (Germany) and web-controlling consultant; awarded Germany's best conversion optimizer 2018 and CRO Practitioner of the Year 2020; Global (DACH); academic / practitioner</td>
<td>[https://www.websiteboosting.com/magazin/31/4-analytics-konferenz-wien.html](https://www.websiteboosting.com/magazin/31/4-analytics-konferenz-wien.html)</td>
<td>Has already spoken in Vienna (Google Analytics conference Austria, 2015). Combines teaching and CRO practice; German-language CRO expert.</td>
<td>Good German-language guest lecture (on-site or remote) bridging academic teaching and CRO consulting. Check current university.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
