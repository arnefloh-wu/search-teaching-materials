## Quellen zu Regressionsanalyse mit Python (Agentensuche, 5. Oktober 2026)
Zwei parallele Rechercheagenten (Software, Websites, Videos, Daten, Praxisbeispiele; Bücher, Artikel, Reports, Lehrfälle). 137 Fundstellen zu linearer Regression, nicht-linearen Effekten, Moderation, Mediation, Dummy-Kodierung, Annahmen und Diagnostik sowie Zeitreihenregression. Importiert aus der Notion-Seite Regression vom 5. Oktober 2026.
### Bücher (15)
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
<td>An Introduction to Statistical Learning, with Applications in Python (ISLP)</td>
<td>James, Witten, Hastie, Tibshirani and Taylor, Springer, 2023, book (free PDF on the book website)</td>
<td>[https://www.statlearning.com/](https://www.statlearning.com/)</td>
<td>Chapter 3 (linear regression) uses the Advertising data (sales on TV, radio, newspaper), covers qualitative predictors, the TV x radio interaction, polynomial terms and residual diagnostics; Chapter 7 covers polynomials, step functions and splines. The Ch03-linreg-lab.ipynb notebook is maintained and uses statsmodels. The cleanest marketing-flavoured, free, Python-native regression text available.</td>
<td>Session 1 (Ch. 3 as core reading and lab warm-up), Session 2 (Ch. 7 sections on non-linear fits as background to saturation curves); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Python for Marketing Research and Analytics</td>
<td>Jason S. Schwarz, Chris Chapman and Elea McDonnell Feit, Springer, 2020, book (283 pp.)</td>
<td>[https://doi.org/10.1007/978-3-030-49720-0](https://doi.org/10.1007/978-3-030-49720-0)</td>
<td>The only Python regression text written for marketers. Chapter 7 "Identifying Drivers of Outcomes: Linear Models" (doi 10.1007/978-3-030-49720-0_7) runs a satisfaction-drivers regression with statsmodels formulas, standardisation, factor (dummy) coding, interactions and a short marketing-mix example; Chapter 8 "Additional Linear Modeling Topics" covers collinearity/VIF, logistic regression and hierarchical models. All examples are Colab notebooks with simulated marketing data.</td>
<td>Session 1 (Ch. 7 as reading; notebooks as lab), Session 2 (Ch. 8 on collinearity); paid (Springer, often free via WU SpringerLink licence).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Regression and Other Stories</td>
<td>Andrew Gelman, Jennifer Hill and Aki Vehtari, Cambridge University Press, 2020 (corrected online version), book; free PDF for personal use</td>
<td>[https://users.aalto.fi/\~ave/ROS.pdf](https://users.aalto.fi/~ave/ROS.pdf)</td>
<td>The best modern teaching text on interpreting regression. Ch. 10 (multiple predictors, indicator variables, interactions), Ch. 11 (assumptions, diagnostics, model evaluation, with a clear ranking of which assumptions matter most), Ch. 12 (log transformations and elasticity-style interpretation, standardising) and Chs. 18 to 21 (causal inference with regression) map directly onto Session 1. Simulation-first style suits AI-assisted coding.</td>
<td>Session 1 (Chs. 10 and 12 as reading), Session 2 (Ch. 11 on diagnostics); free PDF; examples are R/rstanarm, Python port partial.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introduction to Mediation, Moderation, and Conditional Process Analysis (3rd ed.)</td>
<td>Andrew F. Hayes, Guilford Press, January 2022, book (732 pp.)</td>
<td>[https://www.routledge.com/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis-Third-Edition-A-Regression-Based-Approach/Hayes/p/book/9781462549030](https://www.routledge.com/Introduction-to-Mediation-Moderation-and-Conditional-Process-Analysis-Third-Edition-A-Regression-Based-Approach/Hayes/p/book/9781462549030)</td>
<td>The PROCESS reference used by almost every consumer-behaviour paper students will read. Parts on mediation, moderation (simple slopes, Johnson-Neyman, multicategorical moderators) and conditional process (moderated mediation) are all OLS-based; the 3rd edition adds PROCESS for R next to SPSS and SAS. Use it to give students the vocabulary, then reproduce the models in statsmodels.</td>
<td>background (instructor reference for moderation in Session 1 and any student project with survey data); paid (about EUR 80).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Coding for Economists</td>
<td>Arthur Turrell, 2021 to present, free online book (Python, Quarto/Jupyter)</td>
<td>[https://aeturrell.github.io/coding-for-economists](https://aeturrell.github.io/coding-for-economists)</td>
<td>Python-only, current and practical. The econmt-regression chapter shows statsmodels and pyfixest with formulas, fixed effects, robust and clustered standard errors and regression tables; econmt-diagnostics covers residual and influence diagnostics; time-series covers lags and autocorrelation. Closest in spirit to the course stack.</td>
<td>Session 1 and Session 3 (regression and fixed-effects chapters as lab reference), Session 4 (time-series chapter); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introductory Econometrics: A Modern Approach (8th ed.) with Using Python for Introductory Econometrics (2nd ed.)</td>
<td>Jeffrey M. Wooldridge, Cengage, January 2025, book; Florian Heiss and Daniel Brunner, 2024, free open-access Python companion</td>
<td>[https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161/](https://www.cengage.com/c/introductory-econometrics-a-modern-approach-8e-wooldridge/9780357900161/)</td>
<td>The standard applied econometrics text: Ch. 6 (logs, quadratics, interactions), Ch. 7 (dummy variables, interactions with dummies, Chow tests), Ch. 8 (heteroskedasticity-robust inference), Chs. 10 to 12 (time-series regression, trends, seasonality, serial correlation, HAC errors). Heiss and Brunner reproduce every example in Python with statsmodels and the wooldridge data package, chapter for chapter.</td>
<td>Session 1 (Chs. 6 to 7), Session 4 (Chs. 10 to 12); Wooldridge paid (about EUR 70 to 90), UPfIE free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Forecasting: Principles and Practice, the Pythonic Way</td>
<td>Rob J. Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler and Kin G. Olivares, OTexts, 2025 (print May 2026), free online book</td>
<td>[https://otexts.com/fpppy/](https://otexts.com/fpppy/)</td>
<td>Python (Nixtla) edition of fpp3. The time-series regression chapter (trend, seasonal dummies, Fourier terms, lagged predictors, residual autocorrelation checks) and the dynamic regression chapter (regression with ARIMA errors, distributed lags) are the clearest free treatment of forecasting as regression. First 13 chapters follow fpp3 numbering (Ch. 7 time-series regression, Ch. 10 dynamic regression, unverified for the Python edition).</td>
<td>Session 4 (core reading for forecasting as regression), Session 2 (seasonality controls); free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>The Effect: An Introduction to Research Design and Causality (2nd ed.)</td>
<td>Nick Huntington-Klein, Chapman and Hall/CRC (Routledge), July 2025, book; free online edition</td>
<td>[https://theeffectbook.net/](https://theeffectbook.net/)</td>
<td>Ch. 13 "Regression" explains controls, polynomial terms, logs, interactions, robust and clustered standard errors with R, Stata and Python code side by side; the causal-diagram chapters explain why "controlling for" a mediator distorts a marketing effect. Written for students with no maths background.</td>
<td>Session 1 (Ch. 13), Session 4 (difference-in-differences and synthetic control chapters); free online, print about EUR 60.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Causal Inference for the Brave and True</td>
<td>Matheus Facure, 2020 to present, free online book (Python)</td>
<td>[https://matheusfacure.github.io/python-causality-handbook/landing-page.html](https://matheusfacure.github.io/python-causality-handbook/landing-page.html)</td>
<td>Short, humorous Python chapters on regression as a causal tool, omitted-variable bias, good and bad controls, dummy-variable regression, fixed effects and difference-in-differences, all in statsmodels. A good bridge from Session 1 elasticities to Session 4 experiments.</td>
<td>Session 1 and Session 4 (optional readings); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introduction to Econometrics (4th ed.)</td>
<td>James H. Stock and Mark W. Watson, Pearson, 2019 (Global Edition ISBN 9781292264455), book</td>
<td>[https://www.pearson.com/en-gb/subject-catalog/p/introduction-to-econometrics-global-edition/P200000005500/9781292740652](https://www.pearson.com/en-gb/subject-catalog/p/introduction-to-econometrics-global-edition/P200000005500/9781292740652)</td>
<td>The "nonlinear regression functions" chapter (polynomials, logs, interactions between binary and continuous regressors) is the best textbook chapter on log-log versus log-linear interpretation; the time-series chapters cover distributed lags and HAC standard errors. Clear, intuitive, widely available in European libraries.</td>
<td>background (Session 1 for log specifications, Session 4 for dynamic causal effects); paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Principles of Econometrics (5th ed.)</td>
<td>R. Carter Hill, William E. Griffiths and Guay C. Lim, Wiley, 2018, book (912 pp.)</td>
<td>[https://www.wiley.com/en-us/Principles+of+Econometrics,+5th+Edition-p-9781119320944](https://www.wiley.com/en-us/Principles+of+Econometrics,+5th+Edition-p-9781119320944)</td>
<td>More gentle and example-heavy than Wooldridge, with chapters on indicator variables, heteroskedasticity and time-series regression (lags, serial correlation, HAC errors). Data sets are downloadable in several formats, which makes it easy to port examples to Python.</td>
<td>background (alternative textbook for students needing more worked examples); paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Multivariate Data Analysis (8th ed.)</td>
<td>Joseph F. Hair, William C. Black, Barry J. Babin and Rolph E. Anderson, Cengage, 2019, book (832 pp.)</td>
<td>[https://www.cengageasia.com/TitleDetails/isbn/9781473756540](https://www.cengageasia.com/TitleDetails/isbn/9781473756540)</td>
<td>The marketing-research classic; Ch. 5 "Multiple Regression" walks through design, assumptions, VIF thresholds, dummy coding and validation in the step-by-step style business students and reviewers expect. Software-neutral (no Python), and some rules of thumb (VIF cut-offs) are more conservative than current practice.</td>
<td>background (Ch. 5 as a checklist for the project report); paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Discovering Statistics Using IBM SPSS Statistics (6th ed.)</td>
<td>Andy Field, SAGE, February 2024, book (1,144 pp.)</td>
<td>[https://uk.sagepub.com/en-gb/eur/discovering-statistics-using-ibm-spss-statistics/book285130](https://uk.sagepub.com/en-gb/eur/discovering-statistics-using-ibm-spss-statistics/book285130)</td>
<td>Ch. 11 (moderation and mediation with PROCESS, including a two-mediator example new in this edition) and Ch. 12 (categorical predictors and dummy coding) are the friendliest explanations for students with no maths background. SPSS-based, so use for concepts only.</td>
<td>background (students who need an intuitive explanation of interactions or dummy coding); paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Statistical Rethinking (2nd ed.) with the PyMC port</td>
<td>Richard McElreath, CRC Press, 2020, book; PyMC port by the PyMC developers</td>
<td>[https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2](https://github.com/pymc-devs/pymc-resources/tree/main/Rethinking_2)</td>
<td>Ch. 4 (linear regression, polynomials, splines), Ch. 5 (multiple regression, categorical variables, spurious association), Ch. 6 (causal diagrams, post-treatment bias) and Ch. 8 (interactions) give the Bayesian view students need before PyMC-Marketing in Session 3. The PyMC notebooks reproduce the code in Python.</td>
<td>Session 3 (background for Bayesian and hierarchical regression); book paid, notebooks free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Applied Regression Analysis and Generalized Linear Models (3rd ed.)</td>
<td>John Fox, SAGE, 2016 (published 2015), book</td>
<td>[https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254](https://us.sagepub.com/en-us/nam/applied-regression-analysis-and-generalized-linear-models/book237254)</td>
<td>The reference for diagnostics: dummy-variable regression (Ch. 7), unusual and influential data (Ch. 11), non-normality, non-constant variance and non-linearity (Ch. 12), collinearity (Ch. 13). Graduate level; use for instructor preparation and for answering "is this outlier a problem?" questions.</td>
<td>background (Session 2 diagnostics); paid.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Journal Articles (35)
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
<td>A Tutorial on Teaching Data Analytics with Generative AI</td>
<td>Robert L. Bray, INFORMS Journal on Applied Analytics 55(4), 319-343, 2025, article</td>
<td>[https://doi.org/10.1287/inte.2023.0053](https://doi.org/10.1287/inte.2023.0053)</td>
<td>A Kellogg MBA analytics course rebuilt around ChatGPT: custom GPTs that tutor students through linear, Poisson, logistic and ordered-logit regressions, students teaching each other the regression they learned from their GPT, and chat logs submitted as homework. The most concrete published model for AI-assisted regression teaching to business students.</td>
<td>background (instructor reading for course design; ideas for Session 1 lab and AI-assistant rules).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A New Era of Learning: Considerations for ChatGPT as a Tool to Enhance Statistics and Data Science Education</td>
<td>Amanda R. Ellis and Emily Slade, Journal of Statistics and Data Science Education 31(2), 128-133, 2023, article</td>
<td>[https://doi.org/10.1080/26939169.2023.2223609](https://doi.org/10.1080/26939169.2023.2223609)</td>
<td>Short, practical piece on using ChatGPT to generate code, explain output and create practice data, with concrete prompts and warnings about plausible but wrong statistical answers. JSDSE has since opened a generative-AI collection (2025) worth monitoring.</td>
<td>background (instructor reading; supports the Session 1 "what AI assistants get wrong" segment).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Generative AI and Marketing Education: What the Future Holds</td>
<td>Abhijit Guha, Dhruv Grewal and Stephen Atlas, Journal of Marketing Education 46(1), 6-17, 2024 (online December 2023), article</td>
<td>[https://doi.org/10.1177/02734753231215436](https://doi.org/10.1177/02734753231215436)</td>
<td>Survey of marketing educators, students and managers on how generative AI changes marketing teaching, including analytics tasks; useful for justifying an AI-assisted coding course design to a programme committee.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Elasticity benchmarks: price (Bijmolt, van Heerde and Pieters 2005) and advertising (Sethuraman, Tellis and Briesch 2011)</td>
<td>Bijmolt, van Heerde and Pieters, Journal of Marketing Research 42(2), 141-156, 2005; Sethuraman, Tellis and Briesch, Journal of Marketing Research 48(3), 457-471, 2011, articles (meta-analyses)</td>
<td>[https://doi.org/10.1509/jmkr.42.2.141.62296](https://doi.org/10.1509/jmkr.42.2.141.62296)</td>
<td>Mean price elasticity about -2.6 across 1,851 estimates; mean short-term advertising elasticity 0.12 and long-term 0.24, with moderators (country, product type, life-cycle stage, data interval). These are the benchmarks students should compare their log-log coefficients against, and both papers are themselves regressions with moderators.</td>
<td>Session 1 (benchmark slide for the Alpenglow elasticities; reading for interpreting log-log coefficients), Session 2 (advertising elasticity plausibility check).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Thinking about U: Theorizing and testing U- and inverted U-shaped relationships in strategy research</td>
<td>Richard F. J. Haans, Constant Pieters and Zi-Lin He, Strategic Management Journal 37(7), 1177-1195, 2016, article</td>
<td>[https://doi.org/10.1002/smj.2399](https://doi.org/10.1002/smj.2399)</td>
<td>The standard guide to quadratic terms: how to theorise them, the three-step test (sign, turning point inside the data range, slopes on both sides), and how moderators shift or flatten a U. Directly applicable to advertising wear-out and price-quality curves.</td>
<td>Session 2 (reading before saturation curves); paywalled, author copies circulate.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Two Lines: A Valid Alternative to the Invalid Testing of U-Shaped Relationships With Quadratic Regressions</td>
<td>Uri Simonsohn, Advances in Methods and Practices in Psychological Science 1(4), 538-555, 2018, article (open access)</td>
<td>[https://doi.org/10.1177/2515245918805755](https://doi.org/10.1177/2515245918805755)</td>
<td>Shows that a significant quadratic term can appear when the true curve is merely concave (saturating), which is exactly the saturation-versus-wear-out confusion in MMM. Proposes the interrupted "two lines" test as a functional-form-free alternative.</td>
<td>Session 2 (short reading; good discussion point on why Hill curves and quadratics tell different stories).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Shape of Advertising Response Functions Revisited: A Model of Dynamic Probabilistic Thresholds</td>
<td>Demetrios Vakratsas, Fred M. Feinberg, Frank M. Bass and Gurumurthy Kalyanaram, Marketing Science 23(1), 109-119, 2004, article</td>
<td>[https://doi.org/10.1287/mksc.1030.0035](https://doi.org/10.1287/mksc.1030.0035)</td>
<td>Marketing-science treatment of concave versus S-shaped advertising response, with thresholds. Gives theoretical grounding for the Session 2/3 Hill curve and the course's "shape uncertainty" lesson.</td>
<td>Session 2 (background reading for the instructor; excerpt for students).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Your MMM is Broken: Identification of Nonlinear and Time-varying Effects in Marketing Mix Models</td>
<td>Ryan Dew, Nicolas Padilla and Anya Shchetkina, 2024, working paper (arXiv 2408.07678); authors (unverified)</td>
<td>[https://ideas.repec.org/p/arx/papers/2408.07678.html](https://ideas.repec.org/p/arx/papers/2408.07678.html)</td>
<td>Shows that saturation and time-varying effects in MMM are hard to tell apart with typical weekly data, so different non-linear specifications fit equally well but imply different ROAS. Matches the course's own finding that saturation shape is weakly identified with 156 weeks.</td>
<td>Session 2 or 3 (advanced optional reading; supports caveat 2 in the course design).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Multiple Regression: Testing and Interpreting Interactions</td>
<td>Leona S. Aiken and Stephen G. West, SAGE, 1991, book (classic methods monograph)</td>
<td>[https://us.sagepub.com/en-us/nam/multiple-regression/book3045](https://us.sagepub.com/en-us/nam/multiple-regression/book3045)</td>
<td>Origin of the simple-slopes approach, centring advice and the plots of slopes at plus and minus one standard deviation that most published moderation analyses still follow. Cite as the classic, teach the modern refinements below.</td>
<td>background.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Understanding Interaction Models: Improving Empirical Analyses</td>
<td>Thomas Brambor, William Roberts Clark and Matt Golder, Political Analysis 14(1), 63-82, 2006, article</td>
<td>[https://doi.org/10.1093/pan/mpi014](https://doi.org/10.1093/pan/mpi014)</td>
<td>The four-rule checklist: include all constitutive terms, do not read main-effect coefficients as unconditional effects, compute marginal effects with standard errors across the moderator, and plot them. Short and readable; the right text for "price elasticity depends on GDP per capita" models.</td>
<td>Session 1 (core reading for country-level moderation with Hofstede/GDP).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Spotlights, Floodlights, and the Magic Number Zero: Simple Effects Tests in Moderated Regression</td>
<td>Stephen A. Spiller, Gavan J. Fitzsimons, John G. Lynch and Gary H. McClelland, Journal of Marketing Research 50(2), 277-288, 2013, article</td>
<td>[https://doi.org/10.1509/jmr.12.0420](https://doi.org/10.1509/jmr.12.0420)</td>
<td>Marketing's reference for probing interactions: spotlight tests at meaningful moderator values, floodlight (Johnson-Neyman) regions otherwise, and why median splits are wrong. Simonsohn's working paper "GAMify Spotlight & Floodlight" ([https://urisohn.com/sohn_files/papers/gamify.pdf](https://urisohn.com/sohn_files/papers/gamify.pdf)) extends it to non-linear moderation.</td>
<td>Session 1 (reading; floodlight plot of the price effect across GDP or Hofstede scores as a lab extension, computable with marginaleffects or by hand in statsmodels).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How Much Should We Trust Estimates from Multiplicative Interaction Models? Simple Tools to Improve Empirical Practice</td>
<td>Jens Hainmueller, Jonathan Mummolo and Yiqing Xu, Political Analysis 27(2), 163-192, 2019, article</td>
<td>[https://doi.org/10.1017/pan.2018.46](https://doi.org/10.1017/pan.2018.46)</td>
<td>Replicates 46 published interactions and finds many rest on a linear-interaction assumption or on moderator values with no data. Proposes binning and kernel estimators (interflex package, R/Stata). Essential when the moderator is a country characteristic with only six countries, as in Alpenglow.</td>
<td>Session 1 (reading; caution that six countries cannot support a continuous moderator claim).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Misleading Heuristics and Moderated Multiple Regression Models</td>
<td>Julie R. Irwin and Gary H. McClelland, Journal of Marketing Research 38(1), 100-109, 2001, article</td>
<td>[https://doi.org/10.1509/jmkr.38.1.100.18835](https://doi.org/10.1509/jmkr.38.1.100.18835)</td>
<td>Explains which simple-regression habits fail once an interaction is added (reading lower-order coefficients as main effects, standardised coefficients, R-squared change logic). Marketing examples.</td>
<td>Session 1 (instructor background; one-slide summary for students).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The mean-centring debate: Echambadi and Hess (2007); Iacobucci et al. (2016); McClelland et al. (2017)</td>
<td>Echambadi and Hess, Marketing Science 26(3), 438-445, 2007; Iacobucci, Schneider, Popovich and Bakamitsos, Behavior Research Methods 48(4), 1308-1317, 2016; McClelland, Irwin, Disatnik and Sivan, Behavior Research Methods 49, 394-402, 2017, articles</td>
<td>[https://doi.org/10.1287/mksc.1060.0263](https://doi.org/10.1287/mksc.1060.0263)</td>
<td>Echambadi and Hess prove that centring changes neither precision nor fit in a moderated regression; Iacobucci et al. distinguish "micro" (helped by centring) from "macro" multicollinearity; McClelland et al. reply that multicollinearity is a red herring for moderators. Together they settle a question AI assistants routinely get wrong ("centre to fix the VIF").</td>
<td>Session 1 (multicollinearity segment; short reading or instructor background).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Difference Between "Significant" and "Not Significant" is not Itself Statistically Significant</td>
<td>Andrew Gelman and Hal Stern, The American Statistician 60(4), 328-331, 2006, article</td>
<td>[https://doi.org/10.1198/000313006X152649](https://doi.org/10.1198/000313006X152649)</td>
<td>Four pages that prevent the commonest cross-country error: "the elasticity is significant in Italy but not in Austria, so the markets differ". Motivates testing the interaction directly.</td>
<td>Session 1 (short reading tied to the country comparison exercise).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Reconsidering Baron and Kenny: Myths and Truths about Mediation Analysis</td>
<td>Xinshu Zhao, John G. Lynch and Qimei Chen, Journal of Consumer Research 37(2), 197-206, 2010, article</td>
<td>[https://doi.org/10.1086/651257](https://doi.org/10.1086/651257)</td>
<td>The marketing reference that replaced the causal-steps logic: only the indirect effect a x b matters, no total effect is required, and a decision tree classifies complementary, competitive and indirect-only mediation. Non-technical.</td>
<td>background (optional Session 1 extension, e.g. price affects sales via perceived quality or brand attitude).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Moderator-Mediator Variable Distinction in Social Psychological Research</td>
<td>Reuben M. Baron and David A. Kenny, Journal of Personality and Social Psychology 51(6), 1173-1182, 1986, article</td>
<td>[https://doi.org/10.1037/0022-3514.51.6.1173](https://doi.org/10.1037/0022-3514.51.6.1173)</td>
<td>One of the most cited papers in social science and still the source of the moderator/mediator definitions; its causal-steps test is now discouraged (see Zhao et al., Hayes). Read for the definitions, not the procedure.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models</td>
<td>Kristopher J. Preacher and Andrew F. Hayes, Behavior Research Methods 40(3), 879-891, 2008, article</td>
<td>[https://doi.org/10.3758/BRM.40.3.879](https://doi.org/10.3758/BRM.40.3.879)</td>
<td>Established bootstrap confidence intervals for indirect effects and contrasts between mediators; the logic is easy to code in Python with a resampling loop over two statsmodels regressions.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>An Index and Test of Linear Moderated Mediation</td>
<td>Andrew F. Hayes, Multivariate Behavioral Research 50(1), 1-22, 2015, article</td>
<td>[https://doi.org/10.1080/00273171.2014.962683](https://doi.org/10.1080/00273171.2014.962683)</td>
<td>Defines the index of moderated mediation, the single test for whether an indirect effect differs across a moderator (for example, across countries or cultural clusters). The standard citation in conditional process papers.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A General Approach to Causal Mediation Analysis</td>
<td>Kosuke Imai, Luke Keele and Dustin Tingley, Psychological Methods 15(4), 309-334, 2010, article</td>
<td>[https://doi.org/10.1037/a0020761](https://doi.org/10.1037/a0020761)</td>
<td>Potential-outcomes definition of mediation (ACME, ADE), the sequential ignorability assumption and sensitivity analysis. Implemented in Python as statsmodels.stats.mediation.Mediation ([https://www.statsmodels.org/stable/generated/statsmodels.stats.mediation.Mediation.html](https://www.statsmodels.org/stable/generated/statsmodels.stats.mediation.Mediation.html), confirmed via listing), so students can run it without R.</td>
<td>background (instructor reference for any project with a mediator).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Meaningful Mediation Analysis: Plausible Causal Inference and Informative Communication</td>
<td>Rik Pieters, Journal of Consumer Research 44(3), 692-716, 2017, article</td>
<td>[https://doi.org/10.1093/jcr/ucx081](https://doi.org/10.1093/jcr/ucx081)</td>
<td>Reviews 166 JCR mediation analyses and asks for effect decomposition, effect sizes, difference tests and data sharing; also discusses when a mediation claim is causally plausible. The best bridge between PROCESS practice and causal thinking for marketers.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>That's a Lot to Process! Pitfalls of Popular Path Models</td>
<td>Julia M. Rohrer, Paul Hünermund, Ruben C. Arslan and Malte Elson, Advances in Methods and Practices in Psychological Science 5(2), 2022, article (open access)</td>
<td>[https://doi.org/10.1177/25152459221095827](https://doi.org/10.1177/25152459221095827)</td>
<td>Shows with causal diagrams how PROCESS-style mediation and moderated mediation can be badly biased by mediator-outcome confounding; argues for explicit assumptions. Co-author Hünermund (CBS) is a good European name for a causal-inference guest slot.</td>
<td>background (instructor reading; critique to pair with Hayes).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Theorizing, testing, and concluding for mediation in SCM research: Tutorial and procedural recommendations</td>
<td>Manus Rungtusanatham, Jason W. Miller and Kenneth K. Boyer, Journal of Operations Management 32(3), 99-113, 2014, article (note: JOM, not Journal of Supply Chain Management)</td>
<td>[https://doi.org/10.1016/j.jom.2014.01.002](https://doi.org/10.1016/j.jom.2014.01.002)</td>
<td>Business-school tutorial with eight procedural recommendations, from theorising the mechanism to reporting bootstrapped indirect effects. Useful template for student projects outside consumer psychology.</td>
<td>background.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Negative Consequences of Dichotomizing Continuous Predictor Variables</td>
<td>Julie R. Irwin and Gary H. McClelland, Journal of Marketing Research 40(3), 366-371, 2003, article</td>
<td>[https://doi.org/10.1509/jmkr.40.3.366.19237](https://doi.org/10.1509/jmkr.40.3.366.19237)</td>
<td>The dichotomising paper (often confused with their 2001 paper): median splits lose power and can create spurious effects. Students turning GDP or Hofstede scores into "high/low" dummies need this.</td>
<td>Session 1 (short reading or one slide).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Tutorial on Testing, Visualizing, and Probing an Interaction Involving a Multicategorical Variable in Linear Regression Analysis</td>
<td>Andrew F. Hayes and Amanda K. Montoya, Communication Methods and Measures 11(1), 1-30, 2017, article</td>
<td>[https://doi.org/10.1080/19312458.2016.1271116](https://doi.org/10.1080/19312458.2016.1271116)</td>
<td>Explains indicator, sequential and Helmert coding of a multi-level factor and how coding choice changes what each interaction coefficient means. Directly relevant to "country (six levels) x price" models; translate to patsy C(country, Treatment('AT')) or Sum coding.</td>
<td>Session 1 (instructor background; lab note on coding choices).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How to capitalize on a priori contrasts in linear (mixed) models: A tutorial</td>
<td>Daniel J. Schad, Shravan Vasishth, Sven Hohenstein and Reinhold Kliegl, Journal of Memory and Language 110, 104038, 2020, article (open access)</td>
<td>[https://doi.org/10.1016/j.jml.2019.104038](https://doi.org/10.1016/j.jml.2019.104038)</td>
<td>The clearest modern tutorial on treatment, sum (effect), sliding-difference and Helmert contrasts, with the hypothesis matrix behind each. Written for R, but the contrast logic is identical in patsy and formulaic.</td>
<td>background (instructor reference for effect coding of countries).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Collinearity, Power, and Interpretation of Multiple Regression Analysis</td>
<td>Charlotte H. Mason and William D. Perreault, Journal of Marketing Research 28(3), 268-280, 1991, article</td>
<td>[https://doi.org/10.2307/3172863](https://doi.org/10.2307/3172863)</td>
<td>Marketing simulation showing that fears about collinearity are often exaggerated and that sample size, R-squared and effect size matter as much as VIF. A healthy counterweight to mechanical VIF cut-offs in MMM.</td>
<td>Session 1 (multicollinearity), Session 2 (VIF in MMM diagnostics).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Some heteroskedasticity-consistent covariance matrix estimators with improved finite sample properties</td>
<td>James G. MacKinnon and Halbert White, Journal of Econometrics 29(3), 305-325, 1985, article</td>
<td>[https://doi.org/10.1016/0304-4076(8590158-7](https://doi.org/10.1016/0304-4076(8590158-7)</td>
<td>Source of HC1, HC2 and HC3; shows HC3 performs best in small samples. Explains the cov_type="HC3" option in statsmodels and why it is a sensible default for small weekly datasets.</td>
<td>Session 2 (background for robust SEs in the lab).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How Robust Standard Errors Expose Methodological Problems They Do Not Fix, and What to Do About It</td>
<td>Gary King and Margaret E. Roberts, Political Analysis 23(2), 159-179, 2015, article</td>
<td>[https://doi.org/10.1093/pan/mpu015](https://doi.org/10.1093/pan/mpu015)</td>
<td>If classical and robust standard errors differ a lot, the model is misspecified and the coefficients may be wrong too; robust errors are a diagnostic, not a cure. A crucial correction to "always add robust SEs" advice from AI assistants.</td>
<td>Session 2 (reading; compare classical and HC3 SEs as a diagnostic step).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Clustered standard errors: Cameron and Miller (2015) and Abadie, Athey, Imbens and Wooldridge (2023)</td>
<td>A. Colin Cameron and Douglas L. Miller, Journal of Human Resources 50(2), 317-372, 2015; Alberto Abadie, Susan Athey, Guido W. Imbens and Jeffrey M. Wooldridge, Quarterly Journal of Economics 138(1), 1-35, 2023, articles</td>
<td>[https://doi.org/10.3368/jhr.50.2.317](https://doi.org/10.3368/jhr.50.2.317)</td>
<td>Cameron and Miller is the practitioner guide (when to cluster, few-cluster problems, wild bootstrap); Abadie et al. explain that clustering is a design question (sampling or assignment), not a reflex. With six countries the few-clusters warning is directly relevant.</td>
<td>Session 3 (background for panel OLS with country fixed effects; why not to cluster on six countries naively).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix</td>
<td>Whitney K. Newey and Kenneth D. West, Econometrica 55(3), 703-708, 1987, article</td>
<td>[https://doi.org/10.2307/1913610](https://doi.org/10.2307/1913610)</td>
<td>The HAC (Newey-West) estimator behind cov_type="HAC" in statsmodels; the correct fix for autocorrelated residuals in weekly sales regressions when the model is otherwise sound.</td>
<td>Session 2 and Session 4 (background; one slide on HAC errors with maxlags).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Persistence of Marketing Effects on Sales, and the 2024 update on persistence modelling</td>
<td>Marnik G. Dekimpe and Dominique M. Hanssens, Marketing Science 14(1), 1-21, 1995; and "Persistence Modeling in Marketing: Descriptive, Predictive, and Normative Uses", Australasian Marketing Journal, 2024, articles</td>
<td>[https://doi.org/10.1287/mksc.14.1.1](https://doi.org/10.1287/mksc.14.1.1)</td>
<td>The founding paper of persistence modelling (unit roots, VAR, impulse responses) using advertising for a home-improvement chain, plus the authors' own 30-year retrospective. Explains why short-run regression coefficients understate long-run marketing effects.</td>
<td>Session 2 (background on carryover), Session 4 (reading on long-term effects).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Modeling Marketing Dynamics by Time Series Econometrics</td>
<td>Koen Pauwels, Imran Currim, Marnik G. Dekimpe, Eric Ghysels, Dominique M. Hanssens, Natalie Mizik and Prasad Naik, Marketing Letters 15(4), 167-183, 2004, article</td>
<td>[https://doi.org/10.1007/s11002-005-0455-0](https://doi.org/10.1007/s11002-005-0455-0)</td>
<td>Short overview of the time-series toolkit for marketing (unit-root tests, VAR/VECM, impulse response, state-space models) by the leading names, with guidance on which tool answers which managerial question.</td>
<td>Session 4 (reading).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Dynamic Models for Dynamic Theories: The Ins and Outs of Lagged Dependent Variables</td>
<td>Luke Keele and Nathan J. Kelly, Political Analysis 14(2), 186-205, 2006, article</td>
<td>[https://www.cambridge.org/core/journals/political-analysis/article/abs/dynamic-models-for-dynamic-theories-the-ins-and-outs-of-lagged-dependent-variables/F4AB52C3E9964515825D1E6F20C9EA42](https://www.cambridge.org/core/journals/political-analysis/article/abs/dynamic-models-for-dynamic-theories-the-ins-and-outs-of-lagged-dependent-variables/F4AB52C3E9964515825D1E6F20C9EA42)</td>
<td>When a lagged dependent variable is appropriate (dynamic theory, Koyck-style carryover) and when it biases estimates (autocorrelated errors). Koyck lags are the regression form of geometric adstock, so this links Session 2 to Session 4.</td>
<td>Session 4 (background reading).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Lagged Outcomes, Lagged Predictors, and Lagged Errors: A Clarification on Common Factors</td>
<td>Scott J. Cook and Clayton Webb, Political Analysis 29(4), 561-569, 2021, article</td>
<td>[https://doi.org/10.1017/pan.2020.53](https://doi.org/10.1017/pan.2020.53)</td>
<td>Recent clarification of the lagged-dependent-variable debate: a model with lagged outcome, lagged predictors and autocorrelated errors (common-factor restriction) and what each specification assumes. No "Kelly 2020" paper on lagged dependent variables could be found; this is the closest recent paper and probably the intended one, alongside Keele and Kelly 2006.</td>
<td>background (instructor reference for Session 4 specification choices).</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Reports (6)
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
<td>What's in a p? Reassessing best practices for conducting and reporting hypothesis-testing research</td>
<td>Klaus E. Meyer, Arjen van Witteloostuijn and Sjoerd Beugelsdijk, Journal of International Business Studies 48, 535-551, 2017, editorial (methods guidelines)</td>
<td>[https://doi.org/10.1057/s41267-017-0078-8](https://doi.org/10.1057/s41267-017-0078-8)</td>
<td>JIBS's own reporting standard for regression-based IB research: drop significance stars, report exact p-values, confidence intervals and effect sizes, show robustness and discuss economic significance. The right reporting norm for an international marketing course.</td>
<td>Session 5 (reporting checklist for project pitches and reports); Session 1 (how to report an elasticity).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Hypothesis-testing research in international business: progress, pitfalls, and a way forward</td>
<td>Jelena Cerar, B. Sebastian Reiche and Phillip C. Nell, Journal of International Business Studies 57(7), 1115-1129, 2026, article (open access; follow-up audit of the 2017 guidelines)</td>
<td>[https://link.springer.com/article/10.1057/s41267-026-00859-6](https://link.springer.com/article/10.1057/s41267-026-00859-6)</td>
<td>Audits all significance-testing articles in JIBS and JWB from 2012 to 2024: rigour has improved, but reporting of standard errors, confidence intervals, effect sizes and outlier treatment still lags, with signs of p-hacking. Co-author Nell is at WU Vienna, which makes him an obvious local guest for a reporting-standards slot.</td>
<td>Session 5 (reading); guest-talk angle (WU colleague).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>The ASA Statement on p-Values (2016) and "Moving to a World Beyond p \< 0.05" (2019)</td>
<td>Ronald L. Wasserstein and Nicole A. Lazar, The American Statistician 70(2), 129-133, 2016; Wasserstein, Allen L. Schirm and Lazar, The American Statistician 73(sup1), 1-19, 2019, official statement and editorial</td>
<td>[https://doi.org/10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108)</td>
<td>Six principles on what a p-value does and does not mean, followed by the "ATOM" advice (accept uncertainty, be thoughtful, open, modest). Short enough for students; underpins how the course reports regression output.</td>
<td>Session 1 (two-page reading on interpreting coefficients and p-values).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Journal Article Reporting Standards for Quantitative Research (JARS-Quant)</td>
<td>Mark Appelbaum, Harris Cooper, Rex B. Kline, Evan Mayo-Wilson, Arthur M. Nezu and Stephen M. Rao, American Psychologist 73(1), 3-25, 2018, APA task force report</td>
<td>[https://doi.org/10.1037/amp0000191](https://doi.org/10.1037/amp0000191)</td>
<td>The APA reporting checklist used by consumer-behaviour journals: report estimates with confidence intervals, effect sizes, assumption checks, handling of outliers and missing data, and full model specifications, including for mediation and moderation models.</td>
<td>Session 5 (checklist for the written project report).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>NIST/SEMATECH e-Handbook of Statistical Methods, Chapter 4: Process Modeling</td>
<td>National Institute of Standards and Technology, online handbook (maintained since 2003, updated 2012), government report</td>
<td>[https://www.itl.nist.gov/div898/handbook/pmd/pmd.htm](https://www.itl.nist.gov/div898/handbook/pmd/pmd.htm)</td>
<td>Free, authoritative and plain-language chapter on linear, non-linear and weighted least squares, model validation with residual plots, and lack-of-fit testing. Engineering examples, but the residual-diagnostics pages are the best free visual reference.</td>
<td>Session 2 (diagnostics reference); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Google media mix modelling technical reports: Jin et al. (2017) and Chan and Perry (2017)</td>
<td>Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan and Jim Koehler, "Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects"; David Chan and Michael Perry, "Challenges and Opportunities in Media Mix Modeling", Google Inc., 2017, technical reports</td>
<td>[https://research.google.com/pubs/archive/46001.pdf](https://research.google.com/pubs/archive/46001.pdf)</td>
<td>Jin et al. define the adstock and Hill-saturation regression that PyMC-Marketing and Meridian build on; Chan and Perry explain, in regression language, why MMM struggles (collinear channels, endogenous budgets, limited data). Together they turn the regression topics of Session 1 into the MMM of Sessions 2 and 3.</td>
<td>Session 2 (Jin et al. as core reading), Session 3 (Chan and Perry as discussion reading); free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Websites (16)
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
<td>ISLP Chapter 3 lab: Linear Regression (Python)</td>
<td>James, Witten, Hastie, Tibshirani and Taylor, 2023, website (book lab notebook).</td>
<td>[https://intro-stat-learning.github.io/ISLP/labs/Ch03-linreg-lab.html](https://intro-stat-learning.github.io/ISLP/labs/Ch03-linreg-lab.html)</td>
<td>Short, rigorous statsmodels walk-through: simple and multiple regression, interaction terms, polynomial terms, qualitative predictors (Carseats ShelveLoc dummies), leverage and residual plots. Chapter 3 of the free book uses the Advertising data (TV x radio synergy) to explain interactions.</td>
<td>session 1 pre-reading and lab template. Free (book PDF free at [http://statlearning.com](http://statlearning.com)).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Model to Meaning: Interactions and polynomials chapter ([http://marginaleffects.com](http://marginaleffects.com))</td>
<td>Vincent Arel-Bundock, 2026, book website (CRC Press, free HTML).</td>
<td>[https://marginaleffects.com/chapters/interactions.html](https://marginaleffects.com/chapters/interactions.html)</td>
<td>Explains interactions, polynomial terms and conditional slopes with side-by-side R and Python code, and why raw coefficients on product terms mislead. The best current source for "how do I interpret this moderation model" with Python.</td>
<td>session 1 reading (moderation) and session 2 (non-linear slopes). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>statsmodels example notebooks (regression diagnostics, interactions, contrasts, HAC, ARDL)</td>
<td>statsmodels developers, ongoing, documentation (Jupyter notebooks).</td>
<td>[https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks](https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks)</td>
<td>Ready-made notebooks: regression_diagnostics, linear_regression_diagnostics_plots, regression_plots (influence, partial regression, CCPR), contrasts (treatment, sum, Helmert coding), interactions_anova, categorical_interaction_plot, wls, gls, robust_models_\*, autoregressive_distributed_lag, statespace_sarimax_\*.</td>
<td>sessions 1, 2 and 4 lab seeds; give students the diagnostic notebook as a checklist. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Coding for Economists: Regression, Regression diagnostics and visualisation chapters</td>
<td>Arthur Turrell (economist, formerly Bank of England), 2021 to 2026, online book (v1.0.0 archived on Zenodo, January 2024).</td>
<td>[https://aeturrell.github.io/coding-for-economists/econmt-regression.html](https://aeturrell.github.io/coding-for-economists/econmt-regression.html)</td>
<td>Practical, current Python regression chapters built on pyfixest and statsmodels: fixed effects, robust and clustered errors, transformations, interaction terms, multiple-model tables, plus chapters on diagnostics, generalised models and Bayesian regression with Bambi. Written for economists coming from Stata, which suits business students.</td>
<td>sessions 1 and 3 reading; template for regression tables. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Causal Inference for the Brave and True (chapters 5 to 7)</td>
<td>Matheus Facure, 2020 to 2022, online book.</td>
<td>[https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html](https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html)</td>
<td>"The Unreasonable Effectiveness of Linear Regression", "Grouped and Dummy Regression" and "Beyond Confounders" explain regression as adjustment, Frisch-Waugh-Lovell, dummy variables and good vs bad controls (including why controlling for a mediator biases the total effect), all in statsmodels with business examples.</td>
<td>session 1 reading; session 4 background on causal interpretation. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>The Effect, Chapter 13 Regression</td>
<td>Nick Huntington-Klein, 2021 (online), CRC Press 2022, book website.</td>
<td>[https://theeffectbook.net/ch-StatisticalAdjustment.html](https://theeffectbook.net/ch-StatisticalAdjustment.html)</td>
<td>Covers polynomials, logs, interaction terms (including why interactions are noisy and need much larger samples), heteroscedasticity-robust and clustered errors, with code in R, Stata and Python (statsmodels formulas with I()).</td>
<td>session 1 reading for interactions and transformations. Free online.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Marginalia: a guide to marginal effects (Andrew Heiss)</td>
<td>Andrew Heiss (Georgia State University), 20 May 2022, blog post.</td>
<td>[https://www.andrewheiss.com/blog/2022/05/20/marginalia/](https://www.andrewheiss.com/blog/2022/05/20/marginalia/)</td>
<td>Builds up marginal effects from slopes and partial derivatives, then distinguishes average marginal effects, marginal effects at the mean and conditional effects, with a summary table. R code, but concepts map one to one onto marginaleffects for Python.</td>
<td>background for the instructor; optional reading for session 1 interactions. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>UCLA OARC: Contrast coding systems for categorical variables and PROCESS seminar</td>
<td>UCLA Office of Advanced Research Computing, Statistical Methods and Data Analytics, undated (maintained), website.</td>
<td>[https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/](https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/)</td>
<td>The classic reference table of dummy, simple, deviation (effect), Helmert, difference and polynomial coding with what each coefficient means; the statsmodels/patsy contrasts page is a direct Python translation of it. The PROCESS seminar explains simple mediation and bootstrap indirect effects step by step.</td>
<td>session 1 (dummy vs effect coding for countries); background for mediation. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>QuantEcon: Linear Regression in Python</td>
<td>Thomas J. Sargent and John Stachurski, QuantEcon, ongoing (PDF version dated 2020), lecture.</td>
<td>[https://python.quantecon.org/ols.html](https://python.quantecon.org/ols.html)</td>
<td>Cross-country regression (institutions and GDP, replicating Acemoglu, Johnson and Robinson) with statsmodels and linearmodels, covering multivariate OLS, omitted variable bias, endogeneity and 2SLS. A good international example that is not marketing.</td>
<td>background; session 1 optional reading on cross-country regression and endogeneity. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Forecasting: Principles and Practice, the Pythonic Way, Chapter 7 Time series regression models</td>
<td>Rob J Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler and Kin G. Olivares, 2025, online book (OTexts).</td>
<td>[https://otexts.com/fpppy/07-regression.html](https://otexts.com/fpppy/07-regression.html)</td>
<td>Trend, seasonal dummies, Fourier terms, lagged predictors, intervention dummies and residual diagnostics for time-series regression, in Python with Nixtla's statsforecast and mlforecast. Chapter 10 (dynamic regression, ARIMA errors) is the bridge to ARIMAX.</td>
<td>session 4 core reading. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Real Python: Linear Regression in Python</td>
<td>Mirko Stojiljković, Real Python, website tutorial (originally 2019, updated; date unverified).</td>
<td>[https://realpython.com/linear-regression-in-python/](https://realpython.com/linear-regression-in-python/)</td>
<td>Gentle introduction for non-programmers: simple, multiple and polynomial regression with scikit-learn and statsmodels, reading summary() output, under- and overfitting.</td>
<td>pre-course self-study before session 1. Free (some Real Python content needs a subscription).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Python Data Science Handbook: In Depth, Linear Regression</td>
<td>Jake VanderPlas, 2016 (2nd edition O'Reilly 2022), online book chapter.</td>
<td>[https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html](https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html)</td>
<td>Basis-function regression (polynomial and Gaussian bases) shows that "linear" means linear in coefficients, then ridge and lasso; ends with a bicycle-traffic time-series example with day-of-week and weather regressors.</td>
<td>session 2 background on non-linear effects and regularisation. Free online.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Bambi interpret notebooks: Plot Predictions and Plot Comparisons</td>
<td>Bambi developers, 2023 to 2026, documentation.</td>
<td>[https://bambinos.github.io/bambi/notebooks/plot_comparisons.html](https://bambinos.github.io/bambi/notebooks/plot_comparisons.html)</td>
<td>Worked examples of conditional predictions and comparisons for models with interactions, which double as a visual explanation of moderation (and of Bayesian uncertainty around it).</td>
<td>session 3 background. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>You need 16 times the sample size to estimate an interaction (Gelman)</td>
<td>Andrew Gelman, Statistical Modeling, Causal Inference, and Social Science, 15 March 2018, blog post.</td>
<td>[https://statmodeling.stat.columbia.edu/2018/03/15/need16/](https://statmodeling.stat.columbia.edu/2018/03/15/need16/)</td>
<td>The standard error of an interaction is about twice that of a main effect, and plausible interactions are smaller than main effects, so power collapses. A crucial caution before students claim that culture "moderates" an elasticity estimated on six countries.</td>
<td>session 1 or 3 discussion point. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Websites</td>
<td>Regression and Other Stories, Python ports</td>
<td>Pablo Insente (ROS-python) and Farhan Reynaldo (Bambi version), 2020 to 2023, GitHub/website; book by Gelman, Hill and Vehtari (Cambridge, 2020).</td>
<td>[https://github.com/pabloinsente/ROS-python](https://github.com/pabloinsente/ROS-python)</td>
<td>Python versions of the book's examples on transformations, interactions, centring, log models and prediction; Gelman's own blog announced the port in August 2020.</td>
<td>background for the instructor. Free (book itself paid, PDF free on the authors' site, unverified).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Seeing Theory: Regression Analysis, and R Psychologist interactive visualisations</td>
<td>Daniel Kunin et al., Brown University, 2017, interactive website; Kristoffer Magnusson, [http://rpsychologist.com](http://rpsychologist.com), interactive website.</td>
<td>[https://seeing-theory.brown.edu/regression-analysis/index.html](https://seeing-theory.brown.edu/regression-analysis/index.html)</td>
<td>Drag points on Anscombe's quartet and watch the OLS line and R² react (Seeing Theory); Magnusson's correlation and r² visualisations show how outliers and restriction of range change estimates. No regression-specific moderation visual was found on rpsychologist.</td>
<td>session 1 lecture warm-up (influential points, R²). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### (Video-) Tutorials (12)
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
<td>StatQuest: Linear Regression, Clearly Explained; Multiple Regression; Using Linear Models for t-tests and ANOVA</td>
<td>Josh Starmer, StatQuest, YouTube videos (about 27 minutes for the linear regression video), beginner.</td>
<td>[https://www.youtube.com/watch?v=7ArmBVF2dCs](https://www.youtube.com/watch?v=7ArmBVF2dCs)</td>
<td>Least squares, R², why adding variables never lowers R², F-test p-values; the linear-models video shows that t-tests and ANOVA are regressions on dummy variables, the clearest intuition for dummy coding.</td>
<td>pre-session 1 viewing. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Statistical Learning with Python (Stanford, edX / YouTube)</td>
<td>Trevor Hastie, Robert Tibshirani and Jonathan Taylor, Stanford Online, 2023, video course; introductory to intermediate.</td>
<td>[https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python](https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python)</td>
<td>Chapter 3 lectures cover simple and multiple regression, interactions (Advertising TV x radio), qualitative predictors and the statsmodels lab; later chapters cover splines and GAMs. Lectures track the free ISLP book.</td>
<td>session 1 and 2 optional viewing. Free to audit; certificate about USD 186.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Brandon Foltz: Statistics 101, Multiple Linear Regression playlist</td>
<td>Brandon Foltz, YouTube, playlist of 17 videos averaging about 20 minutes, beginner.</td>
<td>[https://www.youtube.com/watch?v=fTfMdCQJz4s](https://www.youtube.com/watch?v=fTfMdCQJz4s)</td>
<td>Slow, business-oriented explanations of multiple regression, dummy variables, two categorical predictors, multicollinearity and model building, with no programming, ideal for students without a statistics background.</td>
<td>pre-session 1 remedial viewing. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Ben Lambert: A full course in econometrics, undergraduate level</td>
<td>Ben Lambert, YouTube playlist (hundreds of short videos), undergraduate.</td>
<td>[https://www.youtube.com/playlist?list=PLcZcY_ZXuygxO0CSE0lMa5WadbPpNix7v](https://www.youtube.com/playlist?list=PLcZcY_ZXuygxO0CSE0lMa5WadbPpNix7v)</td>
<td>Intuition-first coverage of Gauss-Markov assumptions, heteroscedasticity (Breusch-Pagan, White, Goldfeld-Quandt), serial correlation (Durbin-Watson, Breusch-Godfrey), functional form and omitted variable bias.</td>
<td>sessions 1 and 2 reference clips on assumptions and diagnostics. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Andrew Hayes: Modern Integration of Mediation and Moderation Analysis</td>
<td>Andrew F. Hayes, YouTube talk (length unverified), intermediate.</td>
<td>[https://www.youtube.com/watch?v=Lb8M-eQzL60](https://www.youtube.com/watch?v=Lb8M-eQzL60)</td>
<td>The author of PROCESS on conditional process analysis: why moderation and mediation belong in one model, the index of moderated mediation, and bootstrap inference.</td>
<td>background; optional viewing for students using mediation in projects. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Hayes / CCRAM: Mediation, Moderation, and Conditional Process Analysis (on demand and online course)</td>
<td>Andrew F. Hayes, Canadian Centre for Research Analysis and Methods (Haskayne, University of Calgary), paid workshop; online run 9 September 2026 to 9 March 2027 (per search listing).</td>
<td>[https://haskayne.ucalgary.ca/CCRAM/mediation-moderation-and-conditional-process-analysis-on-demand](https://haskayne.ucalgary.ca/CCRAM/mediation-moderation-and-conditional-process-analysis-on-demand)</td>
<td>The canonical training in PROCESS-style analysis (SPSS, SAS, R), based on Hayes's 3rd edition (2022).</td>
<td>background for the instructor; paid (fee unverified).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>DataCamp: Introduction to Regression with statsmodels in Python, and Intermediate Regression with statsmodels in Python</td>
<td>DataCamp, interactive courses, about 4 hours each, beginner and intermediate.</td>
<td>[https://www.datacamp.com/courses/introduction-to-regression-with-statsmodels-in-python](https://www.datacamp.com/courses/introduction-to-regression-with-statsmodels-in-python)</td>
<td>Browser-based exercises on ols() formulas, categorical predictors, transformations, prediction and diagnostics, then parallel slopes, interactions and Simpson's paradox. Suits students with no programming background.</td>
<td>pre-course or between sessions 1 and 2. Subscription (free via DataCamp Classrooms for teaching, unverified).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Coursera: Fitting Statistical Models to Data with Python (University of Michigan)</td>
<td>Brenda Gunderson, Brady T. West and Kerby Shedden, University of Michigan, Coursera, course 3 of "Statistics with Python", intermediate, about 20 hours.</td>
<td>[https://www.coursera.org/learn/fitting-statistical-models-data-python/](https://www.coursera.org/learn/fitting-statistical-models-data-python/)</td>
<td>Linear and logistic regression, multilevel and marginal models in statsmodels and seaborn on real data, taught by a statsmodels core developer (Shedden).</td>
<td>optional self-study. Free to audit; certificate via Coursera subscription.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Mostly Harmless Fixed Effects Regression in Python with PyFixest (PyCon DE and PyData Berlin 2024)</td>
<td>Alexander Fischer (trivago), conference talk, 24 April 2024, about 30 minutes (unverified), intermediate.</td>
<td>[https://www.youtube.com/watch?v=kSQxGGA7Rr4](https://www.youtube.com/watch?v=kSQxGGA7Rr4)</td>
<td>Fixed effects via Frisch-Waugh-Lovell, cluster-robust inference and wild bootstrap, A/B test analysis and staggered event studies in pyfixest, presented by a European industry economist.</td>
<td>session 3 background; Fischer is a plausible guest speaker (industry econometrics, Germany). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Mixtape Sessions: Causal Inference I</td>
<td>Scott Cunningham and guest instructors, Mixtape Sessions, multi-day live workshops, intermediate; code in R and Stata (Python not confirmed).</td>
<td>[https://github.com/Mixtape-Sessions/Causal-Inference-1](https://github.com/Mixtape-Sessions/Causal-Inference-1)</td>
<td>Regression as adjustment, potential outcomes, DAGs, IV and RDD with open slides and problem sets on GitHub; the companion book \*Causal Inference: The Mixtape\* includes Python code (unverified for every chapter).</td>
<td>background for session 4 (experiments, DiD). Paid live workshops (sliding-scale fee, unverified); materials free on GitHub.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>freeCodeCamp: regression analysis course for beginners</td>
<td>Ayush Singh for [http://freeCodeCamp.org](http://freeCodeCamp.org), YouTube, about 10 hours, beginner.</td>
<td>[https://www.freecodecamp.org/news/master-regression-analysis-for-machine-learning/](https://www.freecodecamp.org/news/master-regression-analysis-for-machine-learning/)</td>
<td>Linear, multiple and polynomial regression, feature engineering and model evaluation in Python. Machine-learning framing (prediction rather than inference), so weaker on standard errors, moderation and mediation.</td>
<td>optional self-study only. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>3Blue1Brown: Essence of Linear Algebra</td>
<td>Grant Sanderson, YouTube series, beginner to intermediate.</td>
<td>[https://www.youtube.com/c/3blue1brown](https://www.youtube.com/c/3blue1brown)</td>
<td>No dedicated regression video was found; the linear-algebra series (projections, column space) is the best visual background for why OLS is a projection and why perfect multicollinearity breaks it.</td>
<td>background only. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
</table>
### Cases for Teaching (11)
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
<td>ISLP Chapter 3 lab and Stanford Online "Statistical Learning with Python"</td>
<td>Hastie, Tibshirani and Taylor (Stanford), 2023 onwards, course (edX, 11 weeks) with Jupyter labs</td>
<td>[https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python](https://online.stanford.edu/courses/sohs-ystatslearningp-statistical-learning-python)</td>
<td>The Advertising data set (sales vs TV, radio, newspaper budgets) is the canonical classroom example of a marketing regression with an interaction (TV x radio synergy) and diminishing returns; the lab is maintained Python (statsmodels, ISLP helpers) and the lecture videos are free to audit.</td>
<td>Session 1 (warm-up lab before the Alpenglow panel; videos as optional preparation); free to audit.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Pilgrim Bank (A): Customer Profitability</td>
<td>Frances X. Frei and Dennis Campbell, Harvard Business School, 2001 (revised later), case with data spreadsheet</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=28546](https://www.hbs.edu/faculty/Pages/item.aspx?num=28546)</td>
<td>Classic data case: about 30,000 customers, does online banking raise profitability? Students move from a naive comparison to multiple regression with age, income, tenure and district dummies and see the online effect shrink. Teaches confounding, dummy coding and low R-squared interpretation in a decision setting. Pilgrim Bank (B) adds retention (logistic regression).</td>
<td>Session 1 (case discussion; data easily loaded in Python); paid (HBP academic price, about USD 5 to 10 per student).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Store24 (A): Managing Employee Retention</td>
<td>Frances X. Frei and Dennis Campbell, Harvard Business School case 602-096, 2001 (revised October 2017), case with store-level data</td>
<td>[https://hbsp.harvard.edu/product/602096-PDF-ENG](https://hbsp.harvard.edu/product/602096-PDF-ENG)</td>
<td>Store-level profit regressed on manager and crew tenure, competition, population and visibility; the natural extension is a non-linear (diminishing) tenure effect and a tenure x location interaction. Five pages, quick to teach.</td>
<td>Session 1 (alternative or second case on interpretation and non-linear terms); paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Multiple Regression and Marketing-Mix Models (Darden technical note)</td>
<td>Darden Business Publishing, University of Virginia, technical note (used in the Darden elective "Big Data in Marketing"); authors and product number (unverified)</td>
<td>[https://store.darden.virginia.edu/multiple-regression-and-marketing-mix-models](https://store.darden.virginia.edu/multiple-regression-and-marketing-mix-models)</td>
<td>A business-school note that moves from simple regression to multiple regression for marketing-mix models, with particular attention to omitted-variable bias in marketing coefficients. Matches the course's own "Session 1 elasticities are attenuated because media are omitted" lesson.</td>
<td>Session 1 to 2 (pre-reading bridging regression foundations and MMM); paid.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Python for Marketing Research and Analytics notebooks</td>
<td>Schwarz, Chapman and Feit, 2020 onwards, GitHub repository of Colab notebooks and data</td>
<td>[https://github.com/python-marketing-research/python-marketing-research-1ed](https://github.com/python-marketing-research/python-marketing-research-1ed)</td>
<td>Ready-made, marketing-specific Python labs: Chapter 7 amusement-park satisfaction drivers (OLS, standardised coefficients, factor coding, interactions), Chapter 8 collinearity and logistic regression. Simulated data, so no licensing issues; can be ported to Quarto in Positron.</td>
<td>Session 1 (backup lab or homework); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Linear Regression in Python (QuantEcon)</td>
<td>Thomas J. Sargent and John Stachurski (QuantEcon), lecture in "Intermediate Quantitative Economics with Python", continuously updated, course page</td>
<td>[https://python.quantecon.org/ols.html](https://python.quantecon.org/ols.html)</td>
<td>Clear, polished walk-through of OLS in statsmodels and IV with linearmodels (Acemoglu-Johnson-Robinson institutions data, with continent dummies), including the matrix algebra for those who want it. Good model of a Jupyter Book/MyST lecture format similar to Quarto.</td>
<td>Session 1 (optional reading on omitted-variable bias and endogeneity); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Data 100: Principles and Techniques of Data Science (UC Berkeley)</td>
<td>UC Berkeley Data 100 teaching team, every semester (Fall 2026 site live), course notes and labs</td>
<td>[https://ds100.org/](https://ds100.org/)</td>
<td>Python-first lectures and labs on OLS, feature engineering (one-hot encoding, polynomial features), bias-variance and inference for regression using pandas, statsmodels and scikit-learn. Shows how a large course teaches dummy encoding and non-linear features to non-statisticians.</td>
<td>background (instructor template for labs and auto-checked exercises); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Statistical forecasting: notes on regression and time series analysis (Duke Decision 411)</td>
<td>Robert Nau, Fuqua School of Business, Duke University, course notes (online since the 2000s, last major revision about 2019)</td>
<td>[https://people.duke.edu/\~rnau/411home.htm](https://people.duke.edu/~rnau/411home.htm)</td>
<td>MBA-level notes that remain among the best plain-language explanations of regression for forecasting: transformations, dummy variables for seasons and events, residual autocorrelation, lags and ARIMA, with a weekly beer-sales example across 2,000 stores. Software is Statgraphics, so concepts only.</td>
<td>Session 4 (reading on regression for forecasting, seasonal dummies and lags); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>COMET: Dummy Variables and Interactions notebooks (UBC Economics)</td>
<td>UBC Vancouver School of Economics, COMET project, 2022 onwards, open notebooks</td>
<td>[https://comet.arts.ubc.ca/docs/5_Research/econ490-r/12_Dummy.html](https://comet.arts.ubc.ca/docs/5_Research/econ490-r/12_Dummy.html)</td>
<td>Open, well-paced notebooks on creating dummies from multi-category variables, interpreting their coefficients and interacting dummies with continuous variables, plus a "good regression practices" notebook. Mainly R and Stata; Python coverage could not be confirmed.</td>
<td>background (template for a short dummy-coding notebook in Python); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Regression and Other Stories in Python (Bambi port)</td>
<td>Bambi developers (Ravin Kumar, Tomás Capretto, Osvaldo Martin and contributors), 2020 onwards, GitHub notebooks</td>
<td>[https://github.com/bambinos/Bambi_resources/tree/master/ROS](https://github.com/bambinos/Bambi_resources/tree/master/ROS)</td>
<td>Python versions of ROS examples (Earnings, KidIQ, ElectionsEconomy, Residuals, Rsquared and others) with Bambi formulas, which use the same syntax as statsmodels and lead naturally into PyMC. Coverage is partial (18 example folders).</td>
<td>Session 1 (worked examples on interpretation), Session 3 (bridge to Bayesian regression); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>A Note on the Marketing Analytics Course at Darden</td>
<td>Darden Business Publishing, University of Virginia, technical note describing a second-year MBA elective; authors and year (unverified)</td>
<td>[https://www.thecasecentre.org/programmeAdmin/products/view?id=88638](https://www.thecasecentre.org/programmeAdmin/products/view?id=88638)</td>
<td>Describes a three-module marketing analytics elective (product analytics, customer analytics, measuring return on marketing) built on regression and experiments with large marketing databases. Useful benchmark for the course's own structure.</td>
<td>background (course-design benchmark); paid.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Praxisbeispiele (9)
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
<td>Cross-national differences in market response (Datta, van Heerde, Dekimpe and Steenkamp 2022)</td>
<td>Hannes Datta, Harald J. van Heerde, Marnik G. Dekimpe and Jan-Benedict E. M. Steenkamp, \*Journal of Marketing Research\* 59(2), 2022, article.</td>
<td>[https://doi.org/10.1177/00222437211058102](https://doi.org/10.1177/00222437211058102)</td>
<td>1,600+ brands, 14 categories, 14 Indo-Pacific Rim countries over 10+ years: average price elasticity -0.42, line-length 0.46, distribution 0.37, with elasticities explained by brand, category and country factors; high power distance (Hofstede) and income inequality lower price and distribution elasticities. A direct model for the course's "elasticity moderated by culture" exercise.</td>
<td>session 1 case (second-stage regression of elasticities on Hofstede and GDP) and session 3. Paywalled; check WU library access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>CUPED: regression adjustment in A/B tests at Microsoft and [http://Booking.com](http://Booking.com)</td>
<td>Alex Deng, Ya Xu, Ron Kohavi and Toby Walker, WSDM 2013, paper (Microsoft); Simon Jackson, [http://Booking.com](http://Booking.com), 2018, engineering blog.</td>
<td>[https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf](https://exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf)</td>
<td>Adding the pre-period metric as a covariate (essentially regression adjustment) cuts variance and required sample size; [http://Booking.com](http://Booking.com) explains why tiny conversion effects across 1.5 million room nights a day need it. Shows students that "controls" in regression matter even in randomised experiments.</td>
<td>session 4 (experiments and geo-lift). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>DoorDash CUPAC and Glovo covariate adjustment</td>
<td>DoorDash Engineering, 2020 (date unverified), blog; Glovo Engineering (Barcelona), Medium blog (date unverified).</td>
<td>[https://careersatdoordash.com/blog/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/](https://careersatdoordash.com/blog/improving-experimental-power-through-control-using-predictions-as-covariate-cupac/)</td>
<td>Extends CUPED by using a machine-learned prediction of the outcome as the regression covariate (CUPAC); Glovo, a European delivery platform, compares covariate-adjustment estimators in practice.</td>
<td>session 4 extension reading; Glovo is a possible European guest-speaker lead. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Uber Labs: mediation modelling and causal inference</td>
<td>Uber Engineering blog (Uber Labs: Totte Harinen, Bonnie Li and colleagues), 2019, engineering blog posts.</td>
<td>[https://www.uber.com/us/en/blog/causal-inference-at-uber/](https://www.uber.com/us/en/blog/causal-inference-at-uber/)</td>
<td>Uses mediation analysis to explain why a product change moved an outcome (for example, how delivery delays affect future Uber Eats engagement) and to promote a proven mediator to a short-term KPI. A business example of mediation beyond survey research, with the causal caveats spelled out.</td>
<td>session 1 or 4 example of mediation (marketing action to intermediate metric to sales). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Google geo experiments: geo-based and time-based regression</td>
<td>Jon Vaver and Jim Koehler, Google, 2011, white paper; Jouni Kerman, Peng Wang and Jon Vaver, Google, 2017, white paper.</td>
<td>[https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)</td>
<td>Ad effectiveness (iROAS) estimated by weighted regression of post-period response on pre-period response across geos (GBR), and by a time-series regression of treated on control markets (TBR). Exactly the bridge from regression to the geo-lift test in session 4.</td>
<td>session 4 reading and lab rationale for geolift_germany.csv. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Facebook advertising RCTs vs observational regression (Gordon, Zettelmeyer, Bhargava and Chapsky 2019)</td>
<td>Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava and Dan Chapsky, \*Marketing Science\* 38(2), 2019, article.</td>
<td>[https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf](https://www.kellogg.northwestern.edu/faculty/gordon_b/files/fb_comparison.pdf)</td>
<td>15 Facebook campaigns run as RCTs (500 million user-experiment observations): matching and regression-based observational methods often overstated lift, sometimes by a factor of three or more. The strongest evidence for why regression coefficients on ad exposure are not automatically causal.</td>
<td>session 4 case (experiments vs models). Free working-paper PDF.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Walmart and the M5 forecasting competition</td>
<td>Spyros Makridakis, Evangelos Spiliotis and Vassilios Assimakopoulos, \*International Journal of Forecasting\*, 2022, article; Walmart forecasting team (Brian Seaman and colleagues; authorship unverified), "Applicability of the M5 to Forecasting at Walmart", IJF 2022, commentary.</td>
<td>[https://www.sciencedirect.com/science/article/pii/S0169207021001874](https://www.sciencedirect.com/science/article/pii/S0169207021001874)</td>
<td>Forecasting Walmart unit sales showed that pure extrapolation fails without price, promotion, holiday and event regressors; Walmart's own commentary explains what transfers to production forecasting.</td>
<td>session 4 reading (forecasting as regression with promotion covariates). Results paper open access (unverified); commentary paywalled.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Meta Robyn: ridge regression MMM in production</td>
<td>Meta Marketing Science (facebookexperimental), 2021 to 2026, open-source software and documentation (R stable; Python version in beta).</td>
<td>[https://github.com/facebookexperimental/Robyn](https://github.com/facebookexperimental/Robyn)</td>
<td>A widely used industry MMM that is, at its core, a ridge regression on adstocked and saturated media variables with trend and seasonality decomposed by Prophet: the clearest real-world proof that MMM is time-series regression with transformed regressors.</td>
<td>session 2 (link OLS MMM to industry practice). Free, MIT.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>statworx: Food for Regression, price elasticity from sales data</td>
<td>statworx (Frankfurt data-science consultancy), blog post (date unverified).</td>
<td>[https://www.statworx.com/en/content-hub/blog/food-for-regression-using-sales-data-to-identify-price-elasticity](https://www.statworx.com/en/content-hub/blog/food-for-regression-using-sales-data-to-identify-price-elasticity)</td>
<td>A German consultancy's worked example of estimating price elasticity with log-log regression on retail sales, including the pitfalls (promotions, endogeneity, too little price variation). statworx is a realistic DACH guest-speaker lead.</td>
<td>session 1 reading alongside the "Is our price too high in Poland?" exercise. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Software (18)
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
<td>statsmodels (formula API, OLS/WLS/GLS, robust covariance, diagnostics)</td>
<td>statsmodels developers (Josef Perktold, Kevin Sheppard and others), 2009 to 2026, software. Version 0.15.0, released 27 August 2026, BSD-3-Clause, Python 3.10 or later.</td>
<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
<td>The reference for teaching regression in Python: smf.ols("np.log(sales) \~ np.log(price) + C(country) + promo:C(country)", df).fit(cov_type="HC3") gives R-style output, cov_type="cluster" and "HAC" (Newey-West), variance_inflation_factor, het_breuschpagan, acorr_breusch_godfrey, OLSInfluence (Cook's distance, leverage), plot_regress_exog, and statsmodels.stats.mediation.Mediation. Release 0.15 abstracts the formula engine so either patsy or formulaic can be the backend and accepts polars DataFrames directly.</td>
<td>sessions 1 to 4 lab workhorse (elasticity models, MMM OLS, diagnostics, HAC errors); pin 0.15 in requirements.txt. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>statsmodels.tsa (SARIMAX, ARDL, distributed lags)</td>
<td>statsmodels developers, part of statsmodels 0.15.0 (27 August 2026), software.</td>
<td>[https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks](https://github.com/statsmodels/statsmodels/tree/main/examples/notebooks)</td>
<td>SARIMAX(endog, exog=...) is regression with ARIMA errors (ARIMAX), ARDL and UECM estimate distributed-lag models of advertising carry-over, seasonal_decompose/STL and acf/pacf plots diagnose residual autocorrelation; 0.15 adds Diebold-Mariano and Pesaran-Timmermann forecast tests.</td>
<td>session 2 (residual autocorrelation in the MMM, distributed lags as a bridge to adstock) and session 4 lab (forecast baseline). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyFixest</td>
<td>Alexander Fischer, Styfen Schär and the py-econometrics team, 2023 to 2026, software. Version 0.60.0, 11 June 2026, MIT.</td>
<td>[https://pypi.org/project/pyfixest/](https://pypi.org/project/pyfixest/)</td>
<td>Port of R's fixest: pf.feols("log_sales \~ log_price \| country + week", data=df, vcov=\{"CRV1": "country"\}) with fast high-dimensional fixed effects, IV and Poisson, wild cluster bootstrap (important with only 6 to 8 countries), randomisation inference, DiD and event-study estimators, multiple-estimation syntax, and etable() regression tables rendered with Great Tables. Integrates with marginaleffects.</td>
<td>session 3 (country and week fixed effects), session 4 (DiD on the geo-lift data). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>marginaleffects (Python)</td>
<td>Vincent Arel-Bundock and contributors, 2023 to 2026, software. Version 0.6.1, 5 July 2026, GPL-3.0-or-later, Python 3.12 or later. The Python package now lives in the joint R/Python repository (the old pymarginaleffects repo was archived on 15 August 2026).</td>
<td>[https://pypi.org/project/marginaleffects/](https://pypi.org/project/marginaleffects/)</td>
<td>One consistent grammar (predictions, comparisons, slopes, hypotheses, plot_slopes) for interpreting interactions and non-linear terms: conditional slopes of price at each level of a cultural moderator, average marginal effects, contrasts between countries, delta-method or bootstrap intervals. Works on statsmodels formula models and pyfixest. The companion book \*Model to Meaning\* (CRC Press, 2026) is free online.</td>
<td>session 1 (interpreting an interaction with a Hofstede moderator), session 2 (slopes of non-linear response curves). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>linearmodels</td>
<td>Kevin Sheppard, 2017 to 2025, software. Version 7.0, 21 October 2025, NCSA licence.</td>
<td>[https://pypi.org/project/linearmodels/](https://pypi.org/project/linearmodels/)</td>
<td>PanelOLS with entity and time effects and clustered covariance, RandomEffects, BetweenOLS, FirstDifferenceOLS, IV2SLS/IVGMM (price endogeneity), and a compare() table. Needs a (entity, time) MultiIndex, which is a useful lesson in panel data structure.</td>
<td>session 3 lab (panel OLS with country fixed effects, as named in the course design). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>formulaic and patsy (formulas, dummy and effect coding)</td>
<td>formulaic: Matthew Wardrop, version 1.2.2, 2 June 2026, MIT. patsy: Nathaniel Smith, now maintained by Wardrop and Tomás Capretto, version 1.0.3, 29 August 2026, BSD-2.</td>
<td>[https://pypi.org/project/formulaic/](https://pypi.org/project/formulaic/)</td>
<td>These build the design matrix behind every formula: C(country, Treatment(reference="DE")), C(region, Sum) for effect (deviation) coding, Helmert, polynomial contrasts, bs()/cr() splines and I(price\*\*2). The patsy README says it is no longer actively developed and recommends migrating to formulaic, which statsmodels 0.15 now supports as a backend.</td>
<td>session 1 (dummy vs effect coding of countries and seasons); background for the formula syntax students and AI assistants generate. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>scikit-learn (linear models, splines, pipelines)</td>
<td>scikit-learn developers (Inria and community), 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
<td>[https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)</td>
<td>LinearRegression, Ridge (the estimator inside Meta's Robyn MMM), HuberRegressor, SplineTransformer and PolynomialFeatures for non-linear effects, OneHotEncoder(drop="first") for dummies, Pipeline, TimeSeriesSplit for rolling-origin evaluation. No p-values or standard errors, which is a teachable contrast with statsmodels (prediction vs inference).</td>
<td>session 1 (out-of-sample fit), session 2 (ridge, holdout), session 4 (time-series cross-validation). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pingouin</td>
<td>Raphael Vallat, 2018 to 2026, software. Version 0.7.0, 26 September 2026, GPL-3.0, Python 3.11 or later.</td>
<td>[https://pypi.org/project/pingouin/](https://pypi.org/project/pingouin/)</td>
<td>pg.mediation_analysis(data, x, m, y, covar, n_boot, seed) returns a tidy table of a, b, total, direct and indirect paths with bias-corrected bootstrap intervals and supports parallel mediators; pg.linear_regression gives tidy OLS output with relative importance. No dedicated moderation function: moderation is a product term in linear_regression or statsmodels.</td>
<td>session 1 or background (simple mediation demo, e.g. advertising to brand attitude to sales). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>PyProcessMacro (Python PROCESS)</td>
<td>Quentin André, 2017 to 2026, software. Version 2.2.0, 29 September 2026, MIT (distributed with Andrew Hayes's permission, not endorsed by him), Python 3.11 or later. Revived in September 2026 after years without releases.</td>
<td>[https://pypi.org/project/pyprocessmacro/](https://pypi.org/project/pyprocessmacro/)</td>
<td>Reimplements all PROCESS models 1 to 76 (moderation, mediation, moderated mediation, serial mediation with model 6), tested against PROCESS 2.16 and, for the 42 models still defined, PROCESS for R 5.0; 2.2 adds multicategorical X and moderators (indicator, Helmert, effect coding), percentile spotlight values as in PROCESS 3+, negative binomial outcomes, tidy()/glance() outputs and to_statsmodels(). Note that its defaults follow PROCESS 2; percent=True, spotlight="percentiles" reproduces PROCESS 3 to 5.</td>
<td>background and optional lab for students who know PROCESS from SPSS courses; useful when a thesis supervisor expects PROCESS model numbers. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pyGAM</td>
<td>Daniel Servén Marín, Charlie Brummitt and contributors, 2018 to 2025, software. Version 0.12.0, 18 December 2025, Apache-2.0.</td>
<td>[https://pypi.org/project/pygam/](https://pypi.org/project/pygam/)</td>
<td>Generalised additive models (LinearGAM(s(0) + f(1) + te(2, 3))) with penalised splines, factor terms, tensor interactions, monotonic and concave constraints and partial-dependence plots: a data-driven way to show students what a saturating spend-response curve looks like before imposing Hill or logistic forms.</td>
<td>session 2 (exploring the shape of the response curve). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Bambi</td>
<td>Tomás Capretto, Ravin Kumar, Osvaldo Martin and contributors (PyMC ecosystem), 2020 to 2026, software. Version 0.21.0, 10 September 2026, MIT, Python 3.12 or later.</td>
<td>[https://pypi.org/project/bambi/](https://pypi.org/project/bambi/)</td>
<td>Bayesian regression with R-style formulas, including hierarchical terms (1 + log_price \| country); its interpret module (plot_predictions, plot_comparisons, plot_slopes) is modelled on marginaleffects. A gentle step from OLS to the partial pooling used in PyMC-Marketing.</td>
<td>session 3 (partial pooling of elasticities across countries before PyMC-Marketing). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>DoWhy and CausalML (causal mediation)</td>
<td>DoWhy: PyWhy (originally Microsoft Research), version 0.14, 8 November 2025, MIT. CausalML: Uber, version 0.17.0, 4 July 2026, Apache-2.0.</td>
<td>[https://github.com/py-why/dowhy](https://github.com/py-why/dowhy)</td>
<td>DoWhy estimates natural direct and natural indirect effects from an explicit causal graph (and its GCM module quantifies causal influence), which shows students that mediation needs causal assumptions, not just a product of coefficients. CausalML focuses on uplift and heterogeneous treatment effects for marketing campaigns.</td>
<td>background; session 4 discussion of experiments vs observational estimates. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>semopy</td>
<td>Georgy Meshcheryakov and Anastasia Igolkina, 2019 to 2024, software. Version 2.3.11, 4 January 2024, licence not stated on PyPI.</td>
<td>[https://pypi.org/project/semopy/](https://pypi.org/project/semopy/)</td>
<td>lavaan-style SEM syntax in Python (attitude \~ a\*ad; sales \~ b\*attitude + c\*ad; ind := a\*b), so mediation with latent constructs (brand attitude measured by several items) can be estimated. No release since January 2024, so treat as stable but low-maintenance.</td>
<td>background only (thesis students with survey data). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>StatsForecast and sktime (time-series regression and forecasting)</td>
<td>StatsForecast: Nixtla, version 2.1.1, 16 July 2026, Apache-2.0. sktime: sktime community, version 1.2.0, 22 September 2026, BSD-3-Clause. pmdarima 2.1.1 (17 November 2025, MIT) as an older auto-ARIMA option.</td>
<td>[https://pypi.org/project/statsforecast/](https://pypi.org/project/statsforecast/)</td>
<td>StatsForecast fits AutoARIMA (with exogenous regressors, i.e. ARIMAX), ETS and seasonal baselines quickly across many series (one per country) and is the engine used in the Python edition of \*Forecasting: Principles and Practice\*; sktime offers a scikit-learn-like interface with reduction (regression on lags) and pipelines.</td>
<td>session 4 lab (country-level forecasts, rolling-origin evaluation). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Regression tables: summary_col, PyFixest etable, stargazer and Great Tables</td>
<td>statsmodels summary_col (0.15.0); PyFixest etable (0.60.0); stargazer (Pietro Battiston and Matthew Burke), version 0.0.7, 4 April 2024, GPLv2; Great Tables (Posit), version 1.0.0, 25 September 2026, MIT.</td>
<td>[https://github.com/StatsReporting/stargazer](https://github.com/StatsReporting/stargazer)</td>
<td>Side-by-side model tables (coefficients, standard errors, stars, R², N) for comparing pooled, fixed-effects and interaction models. etable already outputs Great Tables objects that render in Quarto HTML; stargazer mimics R's stargazer for statsmodels OLS but is barely maintained.</td>
<td>sessions 1 and 3 (model comparison table in the project repo milestone). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>seaborn and Yellowbrick (diagnostic plots)</td>
<td>seaborn (Michael Waskom), version 0.13.2, 25 January 2024, BSD; Yellowbrick (District Data Labs), version 1.5, 21 August 2022, Apache-2.0.</td>
<td>[https://pypi.org/project/seaborn/](https://pypi.org/project/seaborn/)</td>
<td>sns.regplot(order=2 / logx=True / lowess=True), sns.residplot and sns.lmplot(hue="country") make linearity, heteroscedasticity and group-specific slopes (moderation) visible in one line; Yellowbrick adds ResidualsPlot, PredictionError and CooksDistance for scikit-learn models. Yellowbrick has had no release since 2022.</td>
<td>sessions 1 and 2 (diagnostic plots in the lab). Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Software</td>
<td>ISLP (package)</td>
<td>James, Witten, Hastie, Tibshirani and Taylor, 2023 to 2026, software. Version 0.4.1, 3 February 2026, BSD-style licence.</td>
<td>[https://pypi.org/project/ISLP/](https://pypi.org/project/ISLP/)</td>
<td>Ships the textbook datasets (Carseats, OJ, Bikeshare, Credit, Wage and others) via load_data() plus ModelSpec, poly(), bs(), ns() helpers that make interaction and spline design matrices explicit; the companion Chapter 3 lab is a complete statsmodels regression walk-through.</td>
<td>session 1 warm-up data and exercises. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Reference points outside Python: R lm/fixest/marginaleffects and SPSS/R PROCESS</td>
<td>R Core (lm), Laurent Bergé (fixest), Arel-Bundock (marginaleffects for R), Jacob Long (interactions, Johnson-Neyman plots); Andrew F. Hayes, PROCESS macro for SPSS, SAS and R (current major release 5).</td>
<td>[http://processmacro.org/](http://processmacro.org/)</td>
<td>R remains the reference for regression teaching material, and most Python packages above are ports (pyfixest of fixest, marginaleffects, bambi of brms, pyprocessmacro of PROCESS). PROCESS is the de facto standard in marketing and consumer research for moderation and mediation, so students will meet "Model 4" and "Model 7" language in papers; pyprocessmacro lets them reproduce it without an SPSS licence.</td>
<td>background; one slide mapping SPSS PROCESS and R syntax to the Python equivalents.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
### Data (15)
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
<td>Advertising.csv (ISLR/ISLP)</td>
<td>James, Witten, Hastie and Tibshirani, \*An Introduction to Statistical Learning\*, dataset; 200 markets x 4 variables (TV, radio, newspaper spend in USD thousands; sales in thousand units).</td>
<td>[https://www.statlearning.com/s/Advertising.csv](https://www.statlearning.com/s/Advertising.csv)</td>
<td>The canonical teaching set for multiple regression, the TV x radio interaction (synergy), diminishing returns (log or square-root TV) and the "newspaper is significant alone but not jointly" lesson in omitted variables.</td>
<td>session 1 warm-up and session 2 bridge to response curves. Free for teaching (book data).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Carseats (ISLP)</td>
<td>ISLP package, simulated data, 400 stores x 11 variables (Sales, Price, CompPrice, Advertising, Income, ShelveLoc Bad/Medium/Good, Urban, US).</td>
<td>[https://islp.readthedocs.io/en/latest/datasets/Carseats.html](https://islp.readthedocs.io/en/latest/datasets/Carseats.html)</td>
<td>Ideal for dummy coding (three-level ShelveLoc and changing the reference level), price x advertising and price x US interactions, and effect coding comparisons.</td>
<td>session 1 lab exercise. Free (BSD-style).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>OJ and Bikeshare (ISLP)</td>
<td>ISLP package. OJ: 1,070 orange juice purchases (Citrus Hill vs Minute Maid) with prices, discounts, specials, brand loyalty and store, from Stine, Foster and Waterman, \*Business Analysis Using Regression\* (1998). Bikeshare: hourly and daily Capital Bikeshare counts 2011 to 2012 with season, holiday, weather.</td>
<td>[https://github.com/intro-stat-learning/ISLP/tree/main/docs/source/datasets](https://github.com/intro-stat-learning/ISLP/tree/main/docs/source/datasets)</td>
<td>OJ is a compact price-and-promotion dataset (price differences, discounts, loyalty as a moderator); Bikeshare teaches seasonal dummies, hour-of-day effects and count outcomes.</td>
<td>sessions 1 (OJ, promotions) and 4 (Bikeshare, seasonality and time-series regression). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>dunnhumby Source Files: Breakfast at the Frat</td>
<td>dunnhumby, dataset; 156 weeks of unit sales, spend, base and shelf price, feature (sale tag) and display for products in four categories (mouthwash, pretzels, frozen pizza, boxed cereal) across stores.</td>
<td>[https://www.dunnhumby.com/source-files/](https://www.dunnhumby.com/source-files/)</td>
<td>Real retail scanner data for log-log price elasticities, promotion dummies, feature x display interactions and store fixed effects, at a manageable size.</td>
<td>session 1 extension exercise or a project alternative. Free with registration; dunnhumby terms restrict redistribution (do not commit raw files to the course repo).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>dunnhumby: The Complete Journey (completejourney-py)</td>
<td>dunnhumby; Python port of the R completejourney package, version 0.1.0, MIT (data under dunnhumby terms); about 2,500 households, one year of transactions, campaigns, coupons and demographics.</td>
<td>[https://pypi.org/project/completejourney-py/](https://pypi.org/project/completejourney-py/)</td>
<td>Household-level data for regression of spend on campaign exposure with demographic moderators (income, household size), and for discussing selection into campaigns.</td>
<td>background or project alternative. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Dominick's Finer Foods (Kilts Center, Chicago Booth)</td>
<td>Kilts Center for Marketing, University of Chicago Booth; about 9 years (1989 to 1997) of weekly store-level scanner data for roughly 100 Chicago stores and 3,500+ UPCs in 25+ categories, including randomised pricing experiments.</td>
<td>[https://www.chicagobooth.edu/research/kilts/research-data/dominicks](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)</td>
<td>The classic dataset behind decades of price-elasticity and promotion research; good for log-log demand models with store and week fixed effects and for showing elasticity differences across store demographics.</td>
<td>background or advanced project data. Free for academic research only, acknowledgement required; files are large SAS/Stata zips.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Rossmann Store Sales (Kaggle)</td>
<td>Rossmann (German drugstore chain), Kaggle competition, 2015; daily sales for 1,115 German stores 2013 to 2015 with Promo, Promo2, school and state holidays, competitor distance and store type.</td>
<td>[https://www.kaggle.com/datasets/pratyushakar/rossmann-store-sales](https://www.kaggle.com/datasets/pratyushakar/rossmann-store-sales)</td>
<td>A European, marketing-relevant time series: promotion dummies, day-of-week and holiday effects, trend, lagged effects and store heterogeneity (promotion x store type moderation).</td>
<td>session 4 (time-series regression with promotions) or session 1 promo-elasticity demo. Free with Kaggle login; competition rules govern use (check before redistributing).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Walmart store sales and M5 (Kaggle)</td>
<td>Walmart Recruiting Store Sales Forecasting (Kaggle, 2014): weekly sales for 45 stores by department 2010 to 2012 with holiday flags and markdowns MarkDown1 to 5. M5 (Kaggle, 2020): 3,049 products in 10 US stores over 1,941 days with prices, SNAP days and events.</td>
<td>[https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data)</td>
<td>Holiday dummies, promotion (markdown) effects, seasonality and hierarchical structure; M5 adds daily prices for elasticity estimation.</td>
<td>session 4 forecasting exercise or project extension. Free with Kaggle login; competition terms apply.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Hofstede dimension data matrix</td>
<td>Geert Hofstede / Hofstede Insights, dataset (version 2015-12-08): six dimensions (PDI, IDV, MAS, UAI, LTO, IVR) for roughly 100 countries and regions (count unverified); .csv, .xls, .sav.</td>
<td>[https://geerthofstede.com/research-and-vsm/dimension-data-matrix/](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/)</td>
<td>The standard country-level moderator: merge with country elasticities and regress elasticity on power distance or uncertainty avoidance (as in Datta et al. 2022), or interact log price with a dimension in a pooled model.</td>
<td>session 1 (already planned via country_meta.csv) and session 3. Free for research use; contact the owners for commercial use.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>World Bank WDI via wbgapi</td>
<td>World Bank, World Development Indicators; wbgapi Python client version 1.0.14, 27 February 2026.</td>
<td>[https://pypi.org/project/wbgapi/](https://pypi.org/project/wbgapi/)</td>
<td>GDP per capita, inflation, internet penetration, Gini and population for cross-country regressions and as moderators of marketing elasticities (income inequality in Datta et al. 2022). Data are CC BY 4.0.</td>
<td>sessions 1 and 3 (country covariates). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat via the eurostat package</td>
<td>Eurostat; eurostat Python package version 1.1.1, 13 June 2024.</td>
<td>[https://pypi.org/project/eurostat/](https://pypi.org/project/eurostat/)</td>
<td>Harmonised EU retail trade volumes, HICP prices, household consumption and digital economy indicators by country and month: good for time-series regressions with seasonality and for EU cross-country panels.</td>
<td>session 4 (monthly retail trade series) or projects. Free (Eurostat reuse policy, attribution).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Our World in Data and Gapminder</td>
<td>Our World in Data (owid-catalog 1.2.7, 5 October 2026) and the gapminder Python package (0.1, 2018, copy of the R teaching data: 142 countries, 1952 to 2007, life expectancy, population, GDP per capita).</td>
<td>[https://pypi.org/project/owid-catalog/](https://pypi.org/project/owid-catalog/)</td>
<td>Gapminder is the cleanest dataset for teaching log transformations (log GDP), continent dummies and continent x GDP interactions; OWID adds hundreds of current indicators, CC BY.</td>
<td>session 1 warm-up (logs and interactions with a non-marketing example). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>statsmodels built-in datasets and Rdatasets</td>
<td>statsmodels sm.datasets (e.g. macrodata, longley, grunfeld) and sm.datasets.get_rdataset() access to Rdatasets (e.g. Duncan from carData, Guerry from HistData).</td>
<td>[https://github.com/statsmodels/statsmodels/tree/main/statsmodels/datasets](https://github.com/statsmodels/statsmodels/tree/main/statsmodels/datasets)</td>
<td>One-line loading; Duncan is the textbook case for influential observations (ministers, conductors), Guerry for cross-regional regression, macrodata for quarterly time-series regression with HAC errors.</td>
<td>session 1 and 2 diagnostics exercises. Free (get_rdataset needs internet).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Housing datasets: caveats (Boston, California)</td>
<td>Boston housing (Harrison and Rubinfeld 1978) in ISLP; California housing (sklearn.datasets.fetch_california_housing, 20,640 block groups).</td>
<td>[https://github.com/intro-stat-learning/ISLP](https://github.com/intro-stat-learning/ISLP)</td>
<td>Boston was removed from scikit-learn (1.2) because of its racially constructed B variable and data issues; avoid it or use it only to discuss data ethics. California housing is fine for non-linear effects but is not marketing.</td>
<td>avoid in labs; mention as a caveat when students find these in AI-generated code. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Kaggle: Customer Personality Analysis (marketing campaign)</td>
<td>Kaggle community upload (originally an iFood-style case dataset), about 2,240 customers x 29 variables: demographics, spend by category, campaign responses, web and store purchases (size from search listings, unverified).</td>
<td>[https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)</td>
<td>Easy cross-sectional marketing data for regression of spend on income with education and marital-status dummies, and moderation (income x kids at home).</td>
<td>optional practice data. Free with login; licence stated as CC0 on Kaggle (unverified).</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
