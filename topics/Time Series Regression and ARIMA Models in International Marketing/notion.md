## Quellen zu Time Series Regression and ARIMA Models in International Marketing (Agentensuche, 26. Oktober 2026)
Deep-Dive-Suche mit sieben parallelen Rechercheagenten (zwei Artikelblöcke: Methoden der Zeitreihenregression, ARIMA, Persistenzmodellierung, VAR/VECM, Intervention und Forecasting sowie internationale bzw. länderübergreifende Anwendungen; Bücher und Reports; Websites, Blogs und Video-Tutorials; Lehrfälle und Praxisbeispiele; Software, Daten und Methoden; People und Communities), Suche auf Englisch und Deutsch. 294 Fundstellen nach Dublettenbereinigung. Schwerpunkte: Box-Jenkins/ARIMA und SARIMA(X), Transfer-Funktionen und Interventionsanalyse, Unit-Root-Tests und Persistenzmodellierung (Dekimpe & Hanssens), VAR, Impulse-Response und Kointegration, Saisonbereinigung (X-13ARIMA-SEATS, JDemetra+), Forecast-Evaluation (M4/M5) sowie internationale Anwendungen: Werbe- und Preiselastizitäten über Länder, Konjunkturzyklen und Marketing, Wechselkurse und Exporte, internationale Diffusion, Tourismusnachfrage, Google-Trends-Nowcasting. Hinweise: Kaggle-, IMF- und einige Verlagsseiten blockieren automatische Abrufe (403/404), solche Zeilen behalten 'in Suchergebnis bestätigt' oder 'Link ungeprüft'; PyFlux und NeuralProphet sind kaum noch gepflegt (in der Notiz markiert); deutschsprachige Quellen sind vor allem Lehrbücher (Springer) und wenige Blogs/Videos; WU-Kurs von Michael Hauser stammt von 2019. Status: 'Link geprüft' = Seite abgerufen, 'in Suchergebnis bestätigt' = nur über Suchtreffer bestätigt, 'Link ungeprüft' = vor Verwendung prüfen. Maschinenlesbare Quelle: GitHub topics/Time Series Regression and ARIMA Models in International Marketing/rows.json.
### Bücher (22)
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
<td>Forecasting: Principles and Practice (3rd ed.)</td>
<td>Rob J Hyndman & George Athanasopoulos, OTexts, 3rd ed., 2021, book</td>
<td>[https://otexts.com/fpp3/](https://otexts.com/fpp3/)</td>
<td>Core course text. Ch. 2-3 graphics/decomposition (STL, X-11, SEATS), Ch. 5 toolbox (residual diagnostics, accuracy), Ch. 7 time series regression (trend, seasonal dummies, Fourier terms, intervention dummies), Ch. 9 ARIMA (stationarity, differencing, ACF/PACF, seasonal ARIMA), Ch. 10 dynamic regression (regression with ARIMA errors, lagged predictors, e.g. advertising-sales), Ch. 11 hierarchical/grouped forecasts (useful for country x product hierarchies). R code (fable/tsibble) and datasets in tsibbledata/fpp3 packages. Master level, non-technical.</td>
<td>Primary reading for sessions on regression and ARIMA; assign Ch. 7, 9, 10 plus exercises. Free online (print version paid).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Forecasting: Principles and Practice, the Pythonic Way</td>
<td>Rob J Hyndman, George Athanasopoulos, Azul Garza, Cristian Challu, Max Mergenthaler, Kin G Olivares, OTexts, online edition (continuously updated, 2025/2026), book</td>
<td>[https://otexts.com/fpppy/](https://otexts.com/fpppy/)</td>
<td>Python edition of FPP3 built on the Nixtla open-source stack (statsforecast, mlforecast etc.). Same chapter logic (regression, ARIMA, dynamic regression), so students can choose R or Python.</td>
<td>Offer as Python alternative to FPP3 for students who code in Python. Free online.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Time Series Analysis and Its Applications: With R Examples (5th ed.)</td>
<td>Robert H. Shumway & David S. Stoffer, Springer Texts in Statistics, 5th ed., 2025, book</td>
<td>[https://doi.org/10.1007/978-3-031-70584-7](https://doi.org/10.1007/978-3-031-70584-7)</td>
<td>More rigorous than FPP3. Ch. 1-3 characteristics of time series, regression and exploratory analysis, ARIMA models (estimation, forecasting, seasonal ARIMA, regression with autocorrelated errors); later chapters on spectral analysis and state space models. R code for every example (astsa package). 5th ed. adds changepoints and more structural models.</td>
<td>Reference for students wanting the statistical foundations; selected chapters for advanced sessions. Paid (\~EUR 140-160); WU-Lizenz prüfen (SpringerLink). Easier sibling: Time Series: A Data Analysis Approach Using R (CRC 2019).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Time Series Analysis: Forecasting and Control (5th ed.)</td>
<td>George E. P. Box, Gwilym M. Jenkins, Gregory C. Reinsel & Greta M. Ljung, Wiley, 5th ed., 2015, book</td>
<td>[https://www.wiley.com/en-us/Time+Series+Analysis%3A+Forecasting+and+Control%2C+5th+Edition-p-9781118675021](https://www.wiley.com/en-us/Time+Series+Analysis%3A+Forecasting+and+Control%2C+5th+Edition-p-9781118675021)</td>
<td>The classic origin of the Box-Jenkins ARIMA methodology: identification (ACF/PACF), estimation, diagnostic checking, seasonal models, transfer function and intervention models that underlie advertising-sales and promotion impact analysis.</td>
<td>Background reference; cite for the Box-Jenkins cycle and transfer-function/intervention analysis. Paid (\~EUR 120); check WU library.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Applied Econometric Time Series (4th ed.)</td>
<td>Walter Enders, Wiley, 4th ed., 2015, book</td>
<td>[https://www.wiley.com/en-us/Applied+Econometric+Time+Series%2C+4th+Edition-p-9781118808566](https://www.wiley.com/en-us/Applied+Econometric+Time+Series%2C+4th+Edition-p-9781118808566)</td>
<td>Applied econometrics view: Ch. 2 stationary ARMA models (Box-Jenkins, AIC/BIC), Ch. 4 trends and unit roots (Dickey-Fuller), Ch. 5 multiequation models (intervention, transfer functions, VAR, impulse responses), Ch. 6 cointegration. Bridges ARIMA to the VAR/persistence modeling used in marketing.</td>
<td>Recommended for sessions on unit roots, VAR and persistence modeling. Paid (\~EUR 90-120); check WU library. Data sets on author website.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introductory Econometrics: A Modern Approach (7th ed.)</td>
<td>Jeffrey M. Wooldridge, Cengage, 7th ed., 2020, book</td>
<td>[https://www.cengage.com/c/introductory-econometrics-a-modern-approach-7e-wooldridge/](https://www.cengage.com/c/introductory-econometrics-a-modern-approach-7e-wooldridge/)</td>
<td>Time series chapters: Ch. 10 basic regression with time series data (static and finite distributed lag models, trends, seasonality), Ch. 11 further issues (stationarity, weak dependence, unit roots), Ch. 12 serial correlation and heteroskedasticity (tests, Prais-Winsten, HAC SEs), Ch. 18 advanced topics (infinite distributed lags/Koyck, cointegration, forecasting). Well suited for distributed-lag advertising models.</td>
<td>Use Ch. 10-12 as bridge from OLS to time series regression. Paid; WU library copies prüfen. Data via wooldridge R/Python packages (free).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introduction to Time Series and Forecasting (3rd ed.)</td>
<td>Peter J. Brockwell & Richard A. Davis, Springer Texts in Statistics, 3rd ed., 2016, book</td>
<td>[https://doi.org/10.1007/978-3-319-29854-2](https://doi.org/10.1007/978-3-319-29854-2)</td>
<td>Concise, mathematically clean intro: stationary processes, ARMA models, modeling and forecasting with ARMA, nonstationary and seasonal ARIMA, multivariate series, state-space models.</td>
<td>Theory reference for stronger students. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Time Series Models for Business and Economic Forecasting (3rd ed.)</td>
<td>Philip Hans Franses, Dick van Dijk & Anne Opschoor, Cambridge University Press, 3rd ed., 2014, book</td>
<td>[https://doi.org/10.1017/CBO9781139019460](https://doi.org/10.1017/CBO9781139019460)</td>
<td>Business-oriented forecasting text by Erasmus econometricians (Franses also published widely on marketing time series): trends, seasonality, ARIMA, unit roots, multivariate models, with business examples and exercises.</td>
<td>Intermediate alternative to Enders with business focus. Paid; check Cambridge Core via WU. DOI to be verified.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Market Response Models: Econometric and Time Series Analysis (2nd ed.)</td>
<td>Dominique M. Hanssens, Leonard J. Parsons & Randall L. Schultz, Kluwer/Springer, International Series in Quantitative Marketing, 2nd ed., 2001, book</td>
<td>[https://doi.org/10.1007/b109775](https://doi.org/10.1007/b109775)</td>
<td>The key marketing reference: sales response functions, carryover/distributed lags (Koyck, Nerlove-Arrow), ARIMA and transfer-function models, Granger causality, VAR and persistence modeling of marketing effects, competitive reaction; empirical generalisations on advertising and price elasticities.</td>
<td>Core marketing-specific reading linking time series methods to marketing-mix decisions. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Modeling Markets: Analyzing Marketing Phenomena and Improving Marketing Decision Making</td>
<td>Peter S. H. Leeflang, Jaap E. Wieringa, Tammo H. A. Bijmolt & Koen H. Pauwels, Springer, International Series in Quantitative Marketing, 2015, book</td>
<td>[https://doi.org/10.1007/978-1-4939-2086-0](https://doi.org/10.1007/978-1-4939-2086-0)</td>
<td>Modern marketing-models textbook: specification of response models, dynamic effects (lag structures, carryover), estimation and validation of aggregate models with time series data; many marketing-mix examples. Master/PhD level.</td>
<td>Use dynamic-model and estimation chapters to show regression with lags in marketing-mix models. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Advanced Methods for Modeling Markets</td>
<td>Peter S. H. Leeflang, Jaap E. Wieringa, Tammo H. A. Bijmolt & Koen H. Pauwels (eds.), Springer, International Series in Quantitative Marketing, 2017, book</td>
<td>[https://doi.org/10.1007/978-3-319-53469-5](https://doi.org/10.1007/978-3-319-53469-5)</td>
<td>Companion to Modeling Markets. Chapter 'Traditional Time Series' (ARIMA, transfer functions, unit roots, VAR/VEC, impulse responses, persistence) and chapter 'State Space Models' are directly relevant; further chapters on diffusion, competition and structural models.</td>
<td>Key reading for VAR/persistence and state space models in marketing. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Long-Term Impact of Marketing: A Compendium</td>
<td>Dominique M. Hanssens (ed.), World Scientific, 2018, book</td>
<td>[https://doi.org/10.1142/10704](https://doi.org/10.1142/10704)</td>
<td>Four decades of Hanssens and coauthors' time-series marketing research: market response and competitive behaviour (Ch. 1), persistence modeling, long-run advertising and price effects, marketing and firm value (Ch. 12, Srinivasan & Hanssens). Applied VAR, unit-root and persistence models on real marketing data.</td>
<td>Source of exemplary applied papers for advanced sessions and student projects. Paid (\~USD 180); check WU library.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Bücher</td>
<td>Handbook of Marketing Decision Models (2nd ed.) - chapter Time-Series Models in Marketing</td>
<td>Berend Wierenga & Ralf van der Lans (eds.), Springer, 2017 (1st ed. 2008; chapter by Dekimpe, Franses, Hanssens & Naik), book</td>
<td>[https://doi.org/10.1007/978-3-319-56941-3](https://doi.org/10.1007/978-3-319-56941-3)</td>
<td>Chapter 'Time-Series Models in Marketing' (1st ed.: [https://doi.org/10.1007/978-0-387-78213-3_11](https://doi.org/10.1007/978-0-387-78213-3_11)) surveys unit roots, VAR, persistence and state space models with marketing examples. Concise overview ideal for master students.</td>
<td>Assign the time series chapter as overview reading. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Handbook of Market Research - chapter Modeling Marketing Dynamics Using Vector Autoregressive (VAR) Models</td>
<td>Shuba Srinivasan, in: C. Homburg, M. Klarmann & A. Vomberg (eds.), Handbook of Market Research, Springer, 2022, book chapter</td>
<td>[https://doi.org/10.1007/978-3-319-57413-4_10](https://doi.org/10.1007/978-3-319-57413-4_10)</td>
<td>Tutorial chapter on VAR modeling in marketing: unit-root testing, VAR/VEC specification, Granger causality, impulse response functions, forecast error variance decomposition, with application.</td>
<td>Hands-on reading for a VAR/persistence session. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Principles of Business Forecasting (2nd ed.)</td>
<td>Keith Ord, Robert Fildes & Nikolaos Kourentzes, Wessex Press, 2nd ed., 2017, book</td>
<td>[https://www.wessex.com/principles-of-business-forecasting-2nd-edition.html](https://www.wessex.com/principles-of-business-forecasting-2nd-edition.html)</td>
<td>Managerial forecasting textbook: exponential smoothing, ARIMA, regression for forecasting incl. promotions and causal variables, judgmental forecasting, forecasting in organisations; sales/marketing examples.</td>
<td>Complement for managerial framing (forecast process, accuracy). Paid (\~USD 100).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>It's Not the Size of the Data - It's How You Use It: Smarter Marketing with Analytics and Dashboards</td>
<td>Koen Pauwels, AMACOM, 2014, book</td>
<td>[https://www.harpercollinsleadership.com/9780814433683/its-not-the-size-of-the-data-its-how-you-use-it/](https://www.harpercollinsleadership.com/9780814433683/its-not-the-size-of-the-data-its-how-you-use-it/)</td>
<td>Practitioner book by a leading VAR-in-marketing researcher: marketing dashboards, leading indicators, using time series (VAR, Granger causality) to link marketing actions to sales; international company cases.</td>
<td>Non-technical motivation reading; good for cases and discussion. Paid (\~EUR 25).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Introduction to Modern Time Series Analysis (2nd ed.)</td>
<td>Gebhard Kirchgässner, Jürgen Wolters & Uwe Hassler, Springer Texts in Business and Economics, 2nd ed., 2013, book</td>
<td>[https://doi.org/10.1007/978-3-642-33436-8](https://doi.org/10.1007/978-3-642-33436-8)</td>
<td>Compact econometric intro: univariate ARMA/ARIMA, Granger causality, VAR, unit roots and cointegration, ARCH. English version of the German classic Einführung in die moderne Zeitreihenanalyse (Kirchgässner/Wolters, Vahlen 2006).</td>
<td>Short, rigorous companion for VAR/cointegration. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Zeitreihenanalyse in den Wirtschaftswissenschaften (3. Aufl.)</td>
<td>Klaus Neusser, Vieweg+Teubner/Springer, 3. Aufl., 2011, book (German)</td>
<td>[https://doi.org/10.1007/978-3-8348-8653-8](https://doi.org/10.1007/978-3-8348-8653-8)</td>
<td>Deutschsprachiges Lehrbuch: ARMA-Modelle, Schätzung und Prognose, Box-Jenkins, Einheitswurzeltests, VAR, Kointegration, Zustandsraummodelle. English version: Time Series Econometrics, Springer 2016 ([https://doi.org/10.1007/978-3-319-32862-1](https://doi.org/10.1007/978-3-319-32862-1)).</td>
<td>German-language reference. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Angewandte Zeitreihenanalyse mit R</td>
<td>Rainer Schlittgen & Cristina Sattarhoff, De Gruyter Oldenbourg, 4. Aufl., 2020 (1. Aufl. 2010/2012), book (German)</td>
<td>[https://openlibrary.org/works/OL21686644W](https://openlibrary.org/works/OL21686644W)</td>
<td>Anwendungsorientiertes deutsches Lehrbuch mit R: Trend- und Saisonbereinigung, ARMA/ARIMA, Regression mit Zeitreihen, Interventionsanalyse, Transferfunktionen, multivariate Modelle; viele Beispiele mit R-Code. Classic theory counterpart: Schlittgen & Streitberg, Zeitreihenanalyse ([https://doi.org/10.1524/9783486710960](https://doi.org/10.1524/9783486710960)).</td>
<td>German applied companion with R code. Paid (\~EUR 50); check WU library / De Gruyter licence; current edition details to be verified.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Modelle der Zeitreihenanalyse</td>
<td>Manfred Deistler & Wolfgang Scherrer, Birkhäuser/Springer, 2018, book (German)</td>
<td>[https://doi.org/10.1007/978-3-319-68664-6](https://doi.org/10.1007/978-3-319-68664-6)</td>
<td>Theoretical German text by TU Wien authors (Austrian link): stationary processes, ARMA and state space systems, prediction, estimation, multivariate models. Mathematically demanding.</td>
<td>For mathematically interested students only. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Multivariate Analysemethoden - Kapitel Zeitreihenanalyse</td>
<td>Klaus Backhaus, Bernd Erichson, Wulff Plinke & Rolf Weiber, Springer Gabler, 15. Aufl., 2018 (newer editions available), book chapter (German)</td>
<td>[https://doi.org/10.1007/978-3-662-56655-8_3](https://doi.org/10.1007/978-3-662-56655-8_3)</td>
<td>Standard German marketing-research methods book; chapter Zeitreihenanalyse introduces trend/seasonal regression, autocorrelation, ARIMA and forecasting with a sales example and SPSS. Very accessible.</td>
<td>Easy German entry chapter widely known among WU students; use the latest edition. WU-Lizenz prüfen (SpringerLink).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Empirical Generalizations about Marketing Impact (2nd ed.)</td>
<td>Dominique M. Hanssens (ed.), Marketing Science Institute, Relevant Knowledge Series, 2015, book</td>
<td>[https://www.msi.org/](https://www.msi.org/)</td>
<td>Compact compendium of benchmarks: advertising, price and promotion elasticities, short- vs. long-run effects, carryover, diffusion; largely derived from time series models across many countries and categories.</td>
<td>Benchmarks to compare students' estimated elasticities; discussion of cross-country generalisability. MSI publication (members/paid); exact URL to be verified.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Journal Articles (78)
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
<td>The Persistence of Marketing Effects on Sales</td>
<td>Dekimpe, M. G. & Hanssens, D. M., Marketing Science 14(1), 1-21, 1995, article</td>
<td>[https://doi.org/10.1287/mksc.14.1.1](https://doi.org/10.1287/mksc.14.1.1)</td>
<td>Foundational paper introducing unit-root testing and VAR/impulse-response persistence analysis to marketing; distinguishes temporary vs. permanent (long-run) advertising effects on sales. Clear decision flow (stationary vs. evolving series -\> VAR in levels vs. differences vs. VECM) that maps directly onto a lecture on stationarity.</td>
<td>Core reading (session on unit roots and persistence); paid journal, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Sustained Spending and Persistent Response: A New Look at Long-Term Marketing Profitability</td>
<td>Dekimpe, M. G. & Hanssens, D. M., Journal of Marketing Research 36(4), 397-412, 1999, article</td>
<td>[https://doi.org/10.2307/3151996](https://doi.org/10.2307/3151996)</td>
<td>Defines four strategic scenarios (business as usual, escalation, hysteresis, evolving business practice) from combinations of stationary/evolving sales and marketing spending; VECM-based. Useful 2x2 framework for discussing long-term profitability of marketing.</td>
<td>Core reading / discussion; paid, WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Time-series models in marketing: Past, present and future</td>
<td>Dekimpe, M. G. & Hanssens, D. M., International Journal of Research in Marketing 17(2-3), 183-193, 2000, article</td>
<td>[https://doi.org/10.1016/S0167-8116(00](https://doi.org/10.1016/S0167-8116(00)</td>
<td>Short review (11 pp.) of univariate ARIMA, transfer functions, VAR, unit roots and cointegration applications in marketing; good map of the method landscape. Dated in its future outlook but an ideal entry reading.</td>
<td>Background / first reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Modeling Marketing Dynamics by Time Series Econometrics</td>
<td>Pauwels, K., Currim, I., Dekimpe, M. G., Hanssens, D. M., Mizik, N., Ghysels, E. & Naik, P., Marketing Letters 15(4), 167-183, 2004, article</td>
<td>[https://doi.org/10.1007/s11002-005-0455-0](https://doi.org/10.1007/s11002-005-0455-0)</td>
<td>Choice-symposium overview: when to use VAR/VECM, persistence modelling, state-space and mixed-frequency approaches for marketing questions; discusses data requirements and managerial interpretation of impulse responses. Compact methods primer.</td>
<td>Core/background reading for VAR session; paid, WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Market Response, Competitive Behavior, and Time Series Analysis</td>
<td>Hanssens, D. M., Journal of Marketing Research 17(4), 470-485, 1980, article</td>
<td>[https://doi.org/10.2307/3150500](https://doi.org/10.2307/3150500)</td>
<td>Early classic applying Box-Jenkins/transfer-function identification and causality testing to sales response and competitive reactions across marketing-mix instruments. Historical anchor showing how ARIMA identification is used to specify response models.</td>
<td>Background / classic; paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Intervention Analysis with Applications to Economic and Environmental Problems</td>
<td>Box, G. E. P. & Tiao, G. C., Journal of the American Statistical Association 70(349), 70-79, 1975, article</td>
<td>[https://doi.org/10.1080/01621459.1975.10480264](https://doi.org/10.1080/01621459.1975.10480264)</td>
<td>Original intervention (pulse/step) analysis within ARIMA models; the template for evaluating discrete events such as a campaign launch, price change, regulation or market entry in a sales series.</td>
<td>Methods reference for intervention-analysis lab; paid (JSTOR/T&F), WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Investigating Causal Relations by Econometric Models and Cross-spectral Methods</td>
<td>Granger, C. W. J., Econometrica 37(3), 424-438, 1969, article</td>
<td>[https://doi.org/10.2307/1912791](https://doi.org/10.2307/1912791)</td>
<td>Original definition of Granger causality. Use alongside marketing applications to teach what temporal-precedence tests can and cannot claim (not true causality).</td>
<td>Methods background (Granger causality); paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Co-Integration and Error Correction: Representation, Estimation, and Testing</td>
<td>Engle, R. F. & Granger, C. W. J., Econometrica 55(2), 251-276, 1987, article</td>
<td>[https://doi.org/10.2307/1913236](https://doi.org/10.2307/1913236)</td>
<td>Defines cointegration and the two-step error-correction estimator; basis for long-run equilibrium models such as sales vs. advertising or brand vs. category sales. Technical; assign selected sections.</td>
<td>Methods reference (cointegration); paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian Vector Autoregressive Models</td>
<td>Johansen, S., Econometrica 59(6), 1551-1580, 1991, article</td>
<td>[https://doi.org/10.2307/2938278](https://doi.org/10.2307/2938278)</td>
<td>Johansen trace/max-eigenvalue cointegration tests used in most marketing VECM applications (e.g., Dekimpe & Hanssens 1999). Highly technical; reference for the test as implemented in R (urca) and Stata.</td>
<td>Methods reference only; paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Distribution of the Estimators for Autoregressive Time Series With a Unit Root</td>
<td>Dickey, D. A. & Fuller, W. A., Journal of the American Statistical Association 74(366), 427-431, 1979, article</td>
<td>[https://doi.org/10.2307/2286348](https://doi.org/10.2307/2286348)</td>
<td>Source of the (augmented) Dickey-Fuller unit-root test, the first diagnostic step in persistence modelling. Short (5 pp.) but mathematical.</td>
<td>Methods reference; paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Testing the null hypothesis of stationarity against the alternative of a unit root</td>
<td>Kwiatkowski, D., Phillips, P. C. B., Schmidt, P. & Shin, Y., Journal of Econometrics 54(1-3), 159-178, 1992, article</td>
<td>[https://doi.org/10.1016/0304-4076(92](https://doi.org/10.1016/0304-4076(92)</td>
<td>KPSS test with stationarity as the null; teach as a confirmatory complement to ADF (marketing studies often report both). Useful for showing conflicting test outcomes in a lab.</td>
<td>Methods reference for unit-root lab; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Seasonal integration and cointegration</td>
<td>Hylleberg, S., Engle, R. F., Granger, C. W. J. & Yoo, B. S., Journal of Econometrics 44(1-2), 215-238, 1990, article</td>
<td>[https://doi.org/10.1016/0304-4076(90](https://doi.org/10.1016/0304-4076(90)</td>
<td>HEGY test for seasonal unit roots; relevant when deciding between seasonal dummies and seasonal differencing (SARIMA) in quarterly or monthly sales data. Technical.</td>
<td>Methods reference (seasonality); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Generalized impulse response analysis in linear multivariate models</td>
<td>Pesaran, H. H. & Shin, Y., Economics Letters 58(1), 17-29, 1998, article</td>
<td>[https://doi.org/10.1016/S0165-1765(97](https://doi.org/10.1016/S0165-1765(97)</td>
<td>Generalized impulse response functions that do not depend on Cholesky variable ordering; standard choice in marketing VAR papers (e.g., Trusov et al. 2009). Short; explains the ordering problem students hit in labs.</td>
<td>Methods reference for IRF session; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Computation and analysis of multiple structural change models</td>
<td>Bai, J. & Perron, P., Journal of Applied Econometrics 18(1), 1-22, 2003, article</td>
<td>[https://doi.org/10.1002/jae.659](https://doi.org/10.1002/jae.659)</td>
<td>Practical algorithm and tests for multiple unknown structural breaks (implemented in R strucchange). Useful for detecting regime shifts in sales series, e.g., after market entry, crises or COVID. Crossref lists online year 2002, print issue 2003.</td>
<td>Methods reference (structural breaks lab); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Long-Term Effects of Price Promotions on Category Incidence, Brand Choice, and Purchase Quantity</td>
<td>Pauwels, K., Hanssens, D. M. & Siddarth, S., Journal of Marketing Research 39(4), 421-439, 2002, article</td>
<td>[https://doi.org/10.1509/jmkr.39.4.421.19114](https://doi.org/10.1509/jmkr.39.4.421.19114)</td>
<td>VAR/impulse-response decomposition of promotion effects into incidence, choice and quantity; promotion effects are mostly temporary and dissipate within weeks. Strong exemplar for reading IRF plots and short- vs. long-run elasticities.</td>
<td>Core application reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Category-Demand Effects of Price Promotions</td>
<td>Nijs, V. R., Dekimpe, M. G., Steenkamp, J.-B. E. M. & Hanssens, D. M., Marketing Science 20(1), 1-22, 2001, article</td>
<td>[https://doi.org/10.1287/mksc.20.1.1.10197](https://doi.org/10.1287/mksc.20.1.1.10197)</td>
<td>Persistence modelling across 560 categories over four years (Dutch market data); permanent category effects are rare. Classic empirical generalisation via unit-root tests plus VAR, with a second-stage regression of IRF-based elasticities on category traits.</td>
<td>Core application / empirical generalisation; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Competitive Reactions to Advertising and Promotion Attacks</td>
<td>Steenkamp, J.-B. E. M., Nijs, V. R., Hanssens, D. M. & Dekimpe, M. G., Marketing Science 24(1), 35-54, 2005, article</td>
<td>[https://doi.org/10.1287/mksc.1040.0069](https://doi.org/10.1287/mksc.1040.0069)</td>
<td>VAR-based analysis of competitive reactions in several hundred categories (Dutch data); passive reaction is the dominant response. Good for teaching cross-brand impulse responses and competitive dynamics.</td>
<td>Application reading / seminar presentation; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Do Promotions Benefit Manufacturers, Retailers, or Both?</td>
<td>Srinivasan, S., Pauwels, K., Hanssens, D. M. & Dekimpe, M. G., Management Science 50(5), 617-629, 2004, article</td>
<td>[https://doi.org/10.1287/mnsc.1040.0225](https://doi.org/10.1287/mnsc.1040.0225)</td>
<td>VAR models on revenue and margin series for manufacturers and the retailer (Dominick's Finer Foods scanner data). Shows how impulse responses translate into profitability outcomes; the Dominick's data are publicly available for replication.</td>
<td>Application / replication idea with Dominick's data; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Effects of Word-of-Mouth versus Traditional Marketing: Findings from an Internet Social Networking Site</td>
<td>Trusov, M., Bucklin, R. E. & Pauwels, K., Journal of Marketing 73(5), 90-102, 2009, article</td>
<td>[https://doi.org/10.1509/jmkg.73.5.90](https://doi.org/10.1509/jmkg.73.5.90)</td>
<td>Very teachable VAR: Granger causality tests, generalized IRFs and long-term elasticities of WOM referrals vs. media and events on sign-ups. Compact (13 pp.), clear elasticity tables; often used as a model paper for student projects.</td>
<td>Core reading + lab template (Granger, VAR, GIRF); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Creating lift versus building the base: Current trends in marketing dynamics</td>
<td>Leeflang, P. S. H., Bijmolt, T. H. A., van Doorn, J., Hanssens, D. M., van Heerde, H. J., Verhoef, P. C. & Wieringa, J. E., International Journal of Research in Marketing 26(1), 13-20, 2009, article</td>
<td>[https://doi.org/10.1016/j.ijresmar.2008.06.006](https://doi.org/10.1016/j.ijresmar.2008.06.006)</td>
<td>Short overview of dynamic marketing models (VAR, state-space, dynamic linear models, distributed lags), classifying short-term lift vs. long-term base effects. Good conceptual framing reading.</td>
<td>Background reading; paid, WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Econometric Measurement of the Duration of Advertising Effect on Sales</td>
<td>Clarke, D. G., Journal of Marketing Research 13(4), 345-357, 1976, article</td>
<td>[https://doi.org/10.2307/3151017](https://doi.org/10.2307/3151017)</td>
<td>Meta-analysis of advertising carryover (Koyck/distributed-lag) estimates showing that measured duration depends on the data interval (data-interval bias). Classic anchor for adstock and distributed-lag teaching.</td>
<td>Core reading (distributed lags/adstock); paid (JSTOR), WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Generalizing What Is Known About Temporal Aggregation and Advertising Carryover</td>
<td>Leone, R. P., Marketing Science 14(3_supplement), G141-G150, 1995, article</td>
<td>[https://doi.org/10.1287/mksc.14.3.G141](https://doi.org/10.1287/mksc.14.3.G141)</td>
<td>Empirical generalisation: after correcting for temporal aggregation, advertising effects last roughly 6-9 months. Short; pairs with Clarke (1976) for an adstock half-life discussion.</td>
<td>Background reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Optimal Data Interval for Estimating Advertising Response</td>
<td>Tellis, G. J. & Franses, P. H., Marketing Science 25(3), 217-229, 2006, article</td>
<td>[https://doi.org/10.1287/mksc.1050.0178](https://doi.org/10.1287/mksc.1050.0178)</td>
<td>Shows when temporally aggregated data bias carryover estimates and which data interval suffices (Koyck model). Directly relevant when students choose weekly vs. monthly vs. quarterly data across countries.</td>
<td>Methods reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How Well Does Advertising Work? Generalizations from Meta-Analysis of Brand Advertising Elasticities</td>
<td>Sethuraman, R., Tellis, G. J., Briesch, R. A., Journal of Marketing Research 48(3), 457-471, 2011, article</td>
<td>[https://doi.org/10.1509/jmkr.48.3.457](https://doi.org/10.1509/jmkr.48.3.457)</td>
<td>Meta-analysis of several hundred brand advertising elasticities: average short-term elasticity about 0.1, long-term about 0.2; moderators include region (Europe vs US), product life cycle stage, data interval and model specification. Benchmark for judging students' own estimates.</td>
<td>Core benchmark reading for the advertising elasticity session. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Empirical Generalizations About Market Evolution and Stationarity</td>
<td>Dekimpe, M. G. & Hanssens, D. M., Marketing Science 14(3_supplement), G109-G121, 1995, article</td>
<td>[https://doi.org/10.1287/mksc.14.3.G109](https://doi.org/10.1287/mksc.14.3.G109)</td>
<td>Meta-study of unit-root findings across published marketing series: market shares are mostly stationary while many sales series evolve. Supports discussion of why stationarity matters for model choice.</td>
<td>Background reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>On the Use of Econometric Models for Policy Simulation in Marketing</td>
<td>Franses, P. H., Journal of Marketing Research 42(1), 4-14, 2005, article</td>
<td>[https://doi.org/10.1509/jmkr.42.1.4.56891](https://doi.org/10.1509/jmkr.42.1.4.56891)</td>
<td>Argues that models for policy simulation must account for how marketing instruments themselves are set (endogeneity); illustrated with time-series sales models. Good critical reading on what time-series regressions can support for decisions.</td>
<td>Critical/methods reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Long-Term Effect of Marketing Strategy on Brand Sales</td>
<td>Ataman, M. B., van Heerde, H. J. & Mela, C. F., Journal of Marketing Research 47(5), 866-882, 2010, article</td>
<td>[https://doi.org/10.1509/jmkr.47.5.866](https://doi.org/10.1509/jmkr.47.5.866)</td>
<td>Bayesian dynamic linear (state-space) model of 70 brands in 25 categories over five years (France); long-term elasticities of distribution and line length exceed those of advertising and discounting. Shows a state-space alternative to VAR.</td>
<td>Application reading (state-space / time-varying parameters); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Discovering How Advertising Grows Sales and Builds Brands</td>
<td>Bruce, N. I., Peters, K. & Naik, P. A., Journal of Marketing Research 49(6), 793-806, 2012, article</td>
<td>[https://doi.org/10.1509/jmr.11.0060](https://doi.org/10.1509/jmr.11.0060)</td>
<td>Dynamic (Kalman-filter) model linking advertising to brand-building metrics and sales over time; illustrates latent-state time-series modelling and adstock-like carryover.</td>
<td>Advanced application reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Practice Prize Winner - Dynamic Marketing Budget Allocation Across Countries, Products, and Marketing Activities</td>
<td>Fischer, M., Albers, S., Wagner, N. & Frie, M., Marketing Science 30(4), 568-585, 2011, article</td>
<td>[https://doi.org/10.1287/mksc.1100.0627](https://doi.org/10.1287/mksc.1100.0627)</td>
<td>International: dynamic sales-response models with carryover feed a heuristic that allocates a pharma marketing budget across countries, products and activities (Bayer implementation). Shows how estimated time-series response is turned into multi-country budget decisions.</td>
<td>Core reading for the international angle / case discussion; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How Business Cycles Contribute to Private-Label Success: Evidence from the United States and Europe</td>
<td>Lamey, L., Deleersnyder, B., Dekimpe, M. G., Steenkamp, J.-B. E. M., Journal of Marketing 71(1), 1-15, 2007, article</td>
<td>[https://doi.org/10.1509/jmkg.71.1.001](https://doi.org/10.1509/jmkg.71.1.001)</td>
<td>Long time series of private-label share in the US and three European countries (Belgium, Germany, UK) related to the business cycle with asymmetric (contraction vs expansion) time series models. Key result: private labels gain more in contractions than they lose in expansions, so part of the gain is permanent (ratchet effect).</td>
<td>Core reading or case for the private-label/retail session; replicate the asymmetric-response idea with dummy-interacted regressions. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Role of National Culture in Advertising's Sensitivity to Business Cycles: An Investigation Across Continents</td>
<td>Deleersnyder, B., Dekimpe, M. G., Steenkamp, J.-B. E. M., Leeflang, P. S. H., Journal of Marketing Research 46(5), 623-636, 2009, article</td>
<td>[https://doi.org/10.1509/jmkr.46.5.623](https://doi.org/10.1509/jmkr.46.5.623)</td>
<td>Advertising expenditure series for 37 countries and four media (magazines, newspapers, radio, TV); extracts cyclical components and relates the cyclical sensitivity of ad spending to Hofstede dimensions, stock-market pressure and foreign MNC presence. Finding: advertising is far more cyclical than GDP; less cyclical in long-term-oriented and high power distance countries, more cyclical under high uncertainty avoidance.</td>
<td>Core reading; ideal for demonstrating business-cycle filtering of country series followed by a second-stage cross-country regression. Free version via UNC repository; JMR WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Weathering Tight Economic Times: The Sales Evolution of Consumer Durables Over the Business Cycle</td>
<td>Deleersnyder, B., Dekimpe, M. G., Sarvary, M., Parker, P. M., Quantitative Marketing and Economics 2(4), 347-383, 2004, article</td>
<td>[https://doi.org/10.1007/s11129-004-0137-x](https://doi.org/10.1007/s11129-004-0137-x)</td>
<td>Classic on the cyclical sensitivity of consumer durables sales relative to the general economy, using business-cycle filtering and asymmetry tests on long series. Durables are more cyclical than GDP. Caveat: mainly US series; the method transfers to country data.</td>
<td>Background/methods reading for business-cycle filtering. Working-paper version on KU Leuven Lirias; journal WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Price and Advertising Effectiveness over the Business Cycle</td>
<td>van Heerde, H. J., Gijsenberg, M. J., Dekimpe, M. G., Steenkamp, J.-B. E. M., Journal of Marketing Research 50(2), 177-193, 2013, article</td>
<td>[https://doi.org/10.1509/jmr.10.0414](https://doi.org/10.1509/jmr.10.0414)</td>
<td>Time-varying short- and long-term price and advertising elasticities for 150 brands in 36 CPG categories, 18 years of monthly UK data (1993-2010). Long-term price sensitivity falls in expansions and advertising effectiveness also varies with the economic tide: elasticities are not constant over time.</td>
<td>Core or advanced reading for the elasticity session; motivates time-varying coefficients beyond static ARIMAX. Open version via RUG repository; JMR WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Do display ads influence search? Attribution and dynamics in online advertising</td>
<td>Kireyev, P., Pauwels, K. & Gupta, S., International Journal of Research in Marketing 33(3), 475-490, 2016, article</td>
<td>[https://doi.org/10.1016/j.ijresmar.2015.09.007](https://doi.org/10.1016/j.ijresmar.2015.09.007)</td>
<td>Recent VAR application to digital advertising: display ads raise search activity with a lag (cross-channel dynamics and attribution). Persistence/IRF approach on online data; suits digital marketing analytics students.</td>
<td>Application reading (digital, attribution); paid, WU-Lizenz prüfen</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Brand Buzz in the Echoverse</td>
<td>Hewett, K., Rand, W., Rust, R. T. & van Heerde, H. J., Journal of Marketing 80(3), 1-24, 2016, article</td>
<td>[https://doi.org/10.1509/jm.15.0033](https://doi.org/10.1509/jm.15.0033)</td>
<td>VAR on brand communications, traditional media, earned social media (Twitter) and deposits for US banks; shows echo effects and feedback loops, with IRF figures suitable for class discussion.</td>
<td>Application reading (social media dynamics); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Improving Consumer Mindset Metrics and Shareholder Value through Social Media: The Different Roles of Owned and Earned Media</td>
<td>Colicev, A., Malshe, A., Pauwels, K. & O'Connor, P., Journal of Marketing 82(1), 37-56, 2018, article</td>
<td>[https://doi.org/10.1509/jm.16.0055](https://doi.org/10.1509/jm.16.0055)</td>
<td>Panel VAR of owned and earned social media, YouGov BrandIndex mindset metrics and shareholder value for multiple brands; demonstrates VAR with mindset metrics and long-term effects.</td>
<td>Application reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Consumer Attitude Metrics for Guiding Marketing Mix Decisions</td>
<td>Hanssens, D. M., Pauwels, K. H., Srinivasan, S., Vanhuele, M. & Yildirim, G., Marketing Science 33(4), 534-550, 2014, article</td>
<td>[https://doi.org/10.1287/mksc.2013.0841](https://doi.org/10.1287/mksc.2013.0841)</td>
<td>VAR-based comparison of sales response models with and without attitudinal metrics (awareness, consideration, liking) for brands in France; tests gains in explanatory and forecasting power. Links time-series regression to marketing-mix decisions.</td>
<td>Application / discussion reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Social Media's Impact on the Consumer Mindset: When to Use Which Sentiment Extraction Tool?</td>
<td>Kübler, R. V., Colicev, A. & Pauwels, K. H., Journal of Interactive Marketing 50(1), 136-155, 2020, article</td>
<td>[https://doi.org/10.1016/j.intmar.2019.08.001](https://doi.org/10.1016/j.intmar.2019.08.001)</td>
<td>Compares sentiment-extraction tools as inputs to VAR models of consumer mindset metrics; the choice of text metric changes explanatory and predictive power. Bridges text analytics and time-series modelling.</td>
<td>Advanced application reading; paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Losses Loom Longer than Gains: Modeling the Impact of Service Crises on Perceived Service Quality over Time</td>
<td>Gijsenberg, M. J., van Heerde, H. J. & Verhoef, P. C., Journal of Marketing Research 52(5), 642-656, 2015, article</td>
<td>[https://doi.org/10.1509/jmr.14.0140](https://doi.org/10.1509/jmr.14.0140)</td>
<td>Dynamic model of perceived service quality around service crises (Dutch railways); models asymmetric event effects and their decay, a modern take on intervention analysis.</td>
<td>Application reading (interventions/events); paid, WU-Lizenz prüfen</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Inferring causal impact using Bayesian structural time-series models</td>
<td>Brodersen, K. H., Gallusser, F., Koehler, J., Remy, N. & Scott, S. L., Annals of Applied Statistics 9(1), 247-274, 2015, article</td>
<td>[https://doi.org/10.1214/14-AOAS788](https://doi.org/10.1214/14-AOAS788)</td>
<td>CausalImpact method (Google): Bayesian structural time series with control series to estimate the effect of a campaign or intervention, illustrated with an online advertising example. The companion R package CausalImpact makes it ideal for a lab; preprint freely available (arXiv/Google Research).</td>
<td>Lab (campaign intervention effect) + reading; free preprint, journal version paid</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Another look at measures of forecast accuracy</td>
<td>Hyndman, R. J. & Koehler, A. B., International Journal of Forecasting 22(4), 679-688, 2006, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2006.03.001](https://doi.org/10.1016/j.ijforecast.2006.03.001)</td>
<td>Introduces MASE and critiques MAPE/sMAPE; standard reference for choosing accuracy measures when comparing ARIMA vs. regression forecasts across series of different scale (e.g., countries). Short (10 pp.); preprint on the author's website.</td>
<td>Core reading for forecast evaluation; free preprint on author site, journal paid</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Automatic Time Series Forecasting: The forecast Package for R</td>
<td>Hyndman, R. J. & Khandakar, Y., Journal of Statistical Software 27(3), 2008, article</td>
<td>[https://doi.org/10.18637/jss.v027.i03](https://doi.org/10.18637/jss.v027.i03)</td>
<td>Describes the auto.arima and ets algorithms (unit-root testing via KPSS, AICc model selection) underlying the R forecast package; the go-to explanation of automated Box-Jenkins identification for labs.</td>
<td>Lab companion (R); open access</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The M4 Competition: 100,000 time series and 61 forecasting methods</td>
<td>Makridakis, S., Spiliotis, E. & Assimakopoulos, V., International Journal of Forecasting 36(1), 54-74, 2020, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2019.04.014](https://doi.org/10.1016/j.ijforecast.2019.04.014)</td>
<td>Results of M4: combinations and hybrid statistical/ML methods perform best, pure ML methods underperform; benchmarks include ARIMA, ETS and Theta. Data and code are public on GitHub and usable for forecasting exercises.</td>
<td>Core reading on forecasting accuracy + lab data; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>M5 accuracy competition: Results, findings, and conclusions</td>
<td>Spyros Makridakis, Evangelos Spiliotis & Vassilios Assimakopoulos, International Journal of Forecasting 38(4), 2022, report</td>
<td>[https://doi.org/10.1016/j.ijforecast.2021.11.013](https://doi.org/10.1016/j.ijforecast.2021.11.013)</td>
<td>Results of the M5 competition on 42,840 Walmart unit-sales series (hierarchical: item, store, state; with prices, SNAP and calendar events). Compares statistical (ARIMA, ETS) with ML (LightGBM) methods; role of hierarchy and explanatory variables. Data free on Kaggle.</td>
<td>Case on retail sales forecasting with promotions; students benchmark ARIMA vs. ML on M5 data. Open access (Elsevier).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Retail forecasting: Research and practice</td>
<td>Fildes, R., Ma, S. & Kolassa, S., International Journal of Forecasting 38(4), 1283-1318, 2022, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2019.06.004](https://doi.org/10.1016/j.ijforecast.2019.06.004)</td>
<td>Review of retail demand forecasting at different hierarchy levels, including promotion effects, regression with ARIMA-type errors and machine learning; links practice and research. Good bridge from sales response modelling to forecasting.</td>
<td>Background reading; open access status to check, journal</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Forecasting: theory and practice</td>
<td>Petropoulos, F. et al. (80+ authors), International Journal of Forecasting 38(3), 705-871, 2022, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2021.11.001](https://doi.org/10.1016/j.ijforecast.2021.11.001)</td>
<td>Encyclopedic review with short self-contained sections (ARIMA, exponential smoothing, interventions, forecast combination, evaluation, marketing and retail applications). Instructors can assign individual 1-2 page sections.</td>
<td>Reference / selective reading; open access</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Marketing Budget Allocation Across Countries: The Role of International Business Cycles</td>
<td>Peers, Y., van Heerde, H. J., Dekimpe, M. G., Marketing Science 36(5), 792-809, 2017, article</td>
<td>[https://doi.org/10.1287/mksc.2017.1046](https://doi.org/10.1287/mksc.2017.1046)</td>
<td>Directly on topic: how to allocate a marketing budget across origin countries whose business cycles are not synchronised, illustrated with tourism marketing (tourists from several origin countries). Separates whether unit sales, marketing effectiveness and margins move pro- or countercyclically per country. Good bridge between time series regression with cyclical components and an international budgeting decision.</td>
<td>Core reading for the international session; case discussion on pro- vs countercyclical spending. Open-access version via EUR repository; publisher version WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Effect of Business-Cycle Fluctuations on Private-Label Share: What has Marketing Conduct Got to do with it?</td>
<td>Lamey, L., Deleersnyder, B., Steenkamp, J.-B. E. M., Dekimpe, M. G., Journal of Marketing 76(1), 1-19, 2012, article</td>
<td>[https://doi.org/10.1509/jm.09.0320](https://doi.org/10.1509/jm.09.0320)</td>
<td>Follow-up to Lamey et al. (2007): two decades of data on 106 US CPG categories with seven marketing-mix instruments. Private-label share is countercyclical and partly permanently boosted; national brands' procyclical cuts in advertising, promotions and new product introductions amplify this. Caveat: US only, so pair it with the 2007 multi-country paper.</td>
<td>Supplementary reading; good for discussing marketing conduct as a mediator in time series. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Business cycle research in marketing: a review and research agenda</td>
<td>Dekimpe, M. G., Deleersnyder, B., Journal of the Academy of Marketing Science 46(1), 31-58, 2018, article</td>
<td>[https://doi.org/10.1007/s11747-017-0542-9](https://doi.org/10.1007/s11747-017-0542-9)</td>
<td>Review of marketing research on business cycles: cyclical filtering methods, asymmetric effects and multi-country evidence (advertising, private labels, durables, marketing effectiveness). Useful map of the Dekimpe/Steenkamp/Deleersnyder research stream for students.</td>
<td>Background reading at the start of the international/macro session. Open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Impact of Economic Contractions on the Effectiveness of R&D and Advertising: Evidence from U.S. Companies Spanning Three Decades</td>
<td>Steenkamp, J.-B. E. M., Fang, E., Marketing Science 30(4), 628-645, 2011, article</td>
<td>[https://doi.org/10.1287/mksc.1110.0641](https://doi.org/10.1287/mksc.1110.0641)</td>
<td>Firm panel over three decades showing that advertising and R&D investments pay off more (profit, market share) during contractions. US-only, but a standard reference in the countercyclical-spending debate; useful contrast to Deleersnyder et al. (2009).</td>
<td>Background reading / discussion input for the business-cycle debate. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The International Takeoff of New Products: The Role of Economics, Culture, and Country Innovativeness</td>
<td>Tellis, G. J., Stremersch, S., Yin, E., Marketing Science 22(2), 188-208, 2003, article</td>
<td>[https://doi.org/10.1287/mksc.22.2.188.16041](https://doi.org/10.1287/mksc.22.2.188.16041)</td>
<td>Sales time series of ten consumer durables across 16 European countries; identifies takeoff from the sales curve and models time to takeoff with a hazard model. Takeoff timing differs strongly across countries (Scandinavian fast, Mediterranean slower) and relates to culture and economics; discusses waterfall vs sprinkler entry.</td>
<td>Core reading for international diffusion; exercise: identify takeoff points in country sales series. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Understanding and managing international growth of new products</td>
<td>Stremersch, S., Tellis, G. J., International Journal of Research in Marketing 21(4), 421-438, 2004, article</td>
<td>[https://doi.org/10.1016/j.ijresmar.2004.07.001](https://doi.org/10.1016/j.ijresmar.2004.07.001)</td>
<td>Companion to the takeoff paper: studies the growth stage (duration and growth rate after takeoff) of new products across European countries; economic factors explain cross-country growth differences better than culture.</td>
<td>Supplementary reading alongside Tellis et al. (2003). Paid, WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Global Takeoff of New Products: Culture, Wealth, or Vanishing Differences?</td>
<td>Chandrasekaran, D., Tellis, G. J., Marketing Science 27(5), 844-860, 2008, article</td>
<td>[https://doi.org/10.1287/mksc.1070.0329](https://doi.org/10.1287/mksc.1070.0329)</td>
<td>16 products in 31 developed and developing countries (430 categories), parametric hazard model of time to takeoff with 12 drivers. Fastest takeoff in Japan and Norway; culture and wealth matter; time to takeoff shortens over calendar time and converges across countries.</td>
<td>Core reading for emerging vs developed market diffusion; good class debate on convergence. SSRN version free; journal WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Modeling Global Spillover of New Product Takeoff</td>
<td>van Everdingen, Y., Fok, D., Stremersch, S., Journal of Marketing Research 46(5), 637-652, 2009, article</td>
<td>[https://doi.org/10.1509/jmkr.46.5.637](https://doi.org/10.1509/jmkr.46.5.637)</td>
<td>Penetration data for eight high-tech products across 55 countries; foreign takeoffs (not mere introductions) accelerate a focal country's takeoff. Large, wealthy, export-heavy countries have more clout; poorer, tourist-receiving, densely populated countries are more susceptible; spillovers are stronger between geographically and economically close countries.</td>
<td>Core or supplementary reading on cross-country dependence in time series. SSRN version free; JMR WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Global Diffusion of Technological Innovations: A Coupled-Hazard Approach</td>
<td>Dekimpe, M. G., Parker, P. M., Sarvary, M., Journal of Marketing Research 37(1), 47-59, 2000, article</td>
<td>[https://doi.org/10.1509/jmkr.37.1.47.18722](https://doi.org/10.1509/jmkr.37.1.47.18722)</td>
<td>Classic on global diffusion of cellular telephony across a very large set of countries, modelling country-level adoption timing and diffusion with a coupled-hazard model and country covariates. Shows how international diffusion data are structured and why country heterogeneity matters.</td>
<td>Background classic for the diffusion block. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Investigating New Product Diffusion Across Products and Countries</td>
<td>Talukdar, D., Sudhir, K., Ainslie, A., Marketing Science 21(1), 97-114, 2002, article</td>
<td>[https://doi.org/10.1287/mksc.21.1.97.161](https://doi.org/10.1287/mksc.21.1.97.161)</td>
<td>Hierarchical Bayesian Bass model for several products across developed and developing countries; developing countries show lower penetration potential and slower diffusion; pooling across countries improves early forecasts.</td>
<td>Core reading for forecasting diffusion in emerging markets; lab: fit Bass curves per country. Open access per OpenAlex; otherwise WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Social Contagion and Income Heterogeneity in New Product Diffusion: A Meta-Analytic Test</td>
<td>Van den Bulte, C., Stremersch, S., Marketing Science 23(4), 530-544, 2004, article</td>
<td>[https://doi.org/10.1287/mksc.1040.0054](https://doi.org/10.1287/mksc.1040.0054)</td>
<td>Meta-analysis of Bass model parameters (q/p ratio) from many studies across countries; relates cross-country differences to income inequality and Hofstede culture dimensions. Useful for interpreting Bass parameters in international comparisons.</td>
<td>Supplementary reading for diffusion; source of benchmark parameters. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Innovation diffusion and new product growth models: A critical review and research directions</td>
<td>Peres, R., Muller, E., Mahajan, V., International Journal of Research in Marketing 27(2), 91-106, 2010, article</td>
<td>[https://doi.org/10.1016/j.ijresmar.2009.12.012](https://doi.org/10.1016/j.ijresmar.2009.12.012)</td>
<td>Review of diffusion and growth models including cross-country diffusion, international spillovers, takeoff and saddles. Good overview before the empirical takeoff papers.</td>
<td>Background reading for the diffusion block. Paid, WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Functional Regression: A New Model for Predicting Market Penetration of New Products</td>
<td>Sood, A., James, G. M., Tellis, G. J., Marketing Science 28(1), 36-51, 2009, article</td>
<td>[https://doi.org/10.1287/mksc.1080.0382](https://doi.org/10.1287/mksc.1080.0382)</td>
<td>Penetration curves of 760 categories (21 products x 70 countries); compares functional regression with Classic Bass, Meta-Bass and naive benchmarks for predicting eight aspects of penetration. Augmented functional regression forecasts best; product effects matter more than country effects. Strong example of global demand forecasting with out-of-sample evaluation.</td>
<td>Advanced reading / forecasting benchmark discussion. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Marketing mix and brand sales in global markets: Examining the contingent role of country-market characteristics</td>
<td>Bahadir, S. C., Bharadwaj, S. G., Srivastava, R. K., Journal of International Business Studies 46(5), 596-619, 2015, article</td>
<td>[https://doi.org/10.1057/jibs.2014.69](https://doi.org/10.1057/jibs.2014.69)</td>
<td>Estimates marketing-mix elasticities for brands across many country markets from longitudinal sales data and explains how elasticities vary with country-market characteristics (e.g. economic development, culture). Relevant for emerging vs developed market comparisons. Check details of instruments and country sample before assigning.</td>
<td>Core reading for cross-country elasticity comparisons. Paid, WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Winning hearts, minds and sales: How marketing communication enters the purchase process in emerging and mature markets</td>
<td>Pauwels, K., Erguncu, S., Yildirim, G., International Journal of Research in Marketing 30(1), 57-68, 2013, article</td>
<td>[https://doi.org/10.1016/j.ijresmar.2012.09.006](https://doi.org/10.1016/j.ijresmar.2012.09.006)</td>
<td>Vector autoregressive (VAR) modelling of marketing communication, consumer mindset metrics and sales, contrasting an emerging and a mature market; impulse responses show how communication moves through awareness, consideration and liking to sales differently across market types.</td>
<td>Core reading for the VAR/impulse-response lab with an international angle. SSRN version free; journal WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>New Empirical Generalizations on the Determinants of Price Elasticity</td>
<td>Bijmolt, T. H. A., van Heerde, H. J., Pieters, R. G. M., Journal of Marketing Research 42(2), 141-156, 2005, article</td>
<td>[https://doi.org/10.1509/jmkr.42.2.141.62296](https://doi.org/10.1509/jmkr.42.2.141.62296)</td>
<td>Meta-analysis of about 1,850 price elasticities (mean about -2.6) with moderators including country/region, time period, data aggregation and estimation method; documents that price elasticities changed over time.</td>
<td>Benchmark reading for price elasticity labs. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>How cannibalistic is the Internet channel? A study of the newspaper industry in the United Kingdom and the Netherlands</td>
<td>Deleersnyder, B., Geyskens, I., Gielens, K., Dekimpe, M. G., International Journal of Research in Marketing 19(4), 337-348, 2002, article</td>
<td>[https://doi.org/10.1016/S0167-8116(02](https://doi.org/10.1016/S0167-8116(02)</td>
<td>Intervention/structural-break time series analysis of newspaper circulation and advertising around the launch of online editions in the UK and the Netherlands; cannibalisation was rarer than feared. Clean two-country example of intervention analysis.</td>
<td>Lab example for intervention analysis and structural breaks. Open access per OpenAlex.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Exchange rate pass-through for strategic pricing and advertising</td>
<td>Kadiyali, V., Journal of International Economics 43(3-4), 437-461, 1997, article</td>
<td>[https://doi.org/10.1016/s0022-1996(97](https://doi.org/10.1016/s0022-1996(97)</td>
<td>Marketing-relevant exchange-rate pass-through study (US photographic film market, Kodak vs Fuji): estimates pass-through into both price and advertising in a structural NEIO model; incomplete pass-through depends on demand, cost and competitive conduct.</td>
<td>Background reading on exchange rates and international pricing/advertising. Open access per OpenAlex.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Currency Choice and Exchange Rate Pass-Through</td>
<td>Gopinath, G., Itskhoki, O., Rigobon, R., American Economic Review 100(1), 304-336, 2010, article</td>
<td>[https://doi.org/10.1257/aer.100.1.304](https://doi.org/10.1257/aer.100.1.304)</td>
<td>Micro data on US import prices show that pass-through depends strongly on invoicing currency (dollar vs non-dollar priced goods), in the short and the long run. Explains why export prices and sales react differently across markets after exchange-rate shocks.</td>
<td>Background reading for export pricing; economics-heavy, assign selected sections. Open access per OpenAlex.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Pricing-to-Market: Evidence From Plant-Level Prices</td>
<td>Fitzgerald, D., Haller, S., Review of Economic Studies 81(2), 761-786, 2014, article</td>
<td>[https://doi.org/10.1093/restud/rdt045](https://doi.org/10.1093/restud/rdt045)</td>
<td>Monthly plant-level prices of Irish producers selling the same product in Ireland and the UK. With local-currency invoicing, the relative markup moves one-for-one with exchange-rate changes: direct evidence of pricing-to-market. Intuitive case for international price-setting over time.</td>
<td>Case discussion on export pricing and exchange rates. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Tourism demand modelling and forecasting - A review of recent research</td>
<td>Song, H., Li, G., Tourism Management 29(2), 203-220, 2008, article</td>
<td>[https://doi.org/10.1016/j.tourman.2007.07.016](https://doi.org/10.1016/j.tourman.2007.07.016)</td>
<td>Review of international tourism demand forecasting (ARIMA, exponential smoothing, ADL/ECM, VAR, time-varying parameter models) with accuracy comparisons; no single method dominates across origin-destination pairs.</td>
<td>Background reading for the tourism forecasting lab. Paid, WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A review of research on tourism demand forecasting: Launching the Annals of Tourism Research Curated Collection on tourism demand forecasting</td>
<td>Song, H., Qiu, R. T. R., Park, J., Annals of Tourism Research 75, 338-362, 2019, article</td>
<td>[https://doi.org/10.1016/j.annals.2018.12.001](https://doi.org/10.1016/j.annals.2018.12.001)</td>
<td>Updated review of more than 200 tourism demand forecasting studies: time series (ARIMA/SARIMA, ETS), econometric and AI models, forecast combination and search-engine data, plus accuracy measures and research design.</td>
<td>Background reading. Open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The tourism forecasting competition</td>
<td>Athanasopoulos, G., Hyndman, R. J., Song, H., Wu, D. C., International Journal of Forecasting 27(3), 822-844, 2011, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2010.04.009](https://doi.org/10.1016/j.ijforecast.2010.04.009)</td>
<td>Forecasting competition on 1,311 monthly, quarterly and annual tourism series: compares ARIMA, ETS, damped trend, naive and econometric models. Naive forecasts are hard to beat for annual data; automated ETS/ARIMA do well for monthly and quarterly data. Competition data are public (R package Tcomp).</td>
<td>Core reading plus lab: reuse the competition data to benchmark ARIMA vs ETS. Paid, WU-Lizenz prüfen; data free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Time series forecasts of international travel demand for Australia</td>
<td>Lim, C., McAleer, M., Tourism Management 23(4), 389-396, 2002, article</td>
<td>[https://doi.org/10.1016/S0261-5177(01](https://doi.org/10.1016/S0261-5177(01)</td>
<td>Short classic applying Box-Jenkins ARIMA/seasonal ARIMA to quarterly tourist arrivals to Australia from Hong Kong, Malaysia and Singapore, with unit-root testing and accuracy comparison. Easy to replicate step by step.</td>
<td>Lab template for a seasonal ARIMA exercise. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Forecasting tourism demand with Google trends: Accuracy comparison of countries versus cities</td>
<td>Önder, I., International Journal of Tourism Research 19(6), 648-660, 2017, article</td>
<td>[https://doi.org/10.1002/jtr.2137](https://doi.org/10.1002/jtr.2137)</td>
<td>Compares autoregressive baselines with models adding Google Trends web and image search indices for Vienna, Barcelona, Austria and Belgium; search indices help most for Vienna. Direct local relevance for a WU audience.</td>
<td>Lab idea: replicate with Google Trends data for Austria/Vienna and Statistik Austria arrivals. Paid, WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Can Google data improve the forecasting performance of tourist arrivals? Mixed-data sampling approach</td>
<td>Bangwayo-Skeete, P. F., Skeete, R. W., Tourism Management 46, 454-464, 2015, article</td>
<td>[https://doi.org/10.1016/j.tourman.2014.07.014](https://doi.org/10.1016/j.tourman.2014.07.014)</td>
<td>Uses weekly Google search data in MIDAS models to forecast monthly tourist arrivals to Caribbean destinations from major origin markets, against SARIMA and AR benchmarks; Google-augmented MIDAS improves accuracy in most cases.</td>
<td>Supplementary reading for mixed-frequency nowcasting. Paid, WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Predicting the Present with Google Trends</td>
<td>Choi, H., Varian, H., Economic Record 88(s1), 2-9, 2012, article</td>
<td>[https://doi.org/10.1111/j.1475-4932.2012.00809.x](https://doi.org/10.1111/j.1475-4932.2012.00809.x)</td>
<td>Short foundational paper: adds Google Trends query indices to simple seasonal AR models to nowcast retail sales, car sales, unemployment claims, travel (visitor arrivals to Hong Kong by origin country) and consumer confidence. Very accessible ARIMAX-type example.</td>
<td>Core short reading and lab starter for Google Trends nowcasting. Journal paid (WU-Lizenz prüfen); earlier Google preprint version freely circulated.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Forecasting GDP growth rates in the United States and Brazil using Google Trends</td>
<td>Bantis, E., Clements, M. P., Urquhart, A., International Journal of Forecasting 39(4), 1909-1924, 2023, article</td>
<td>[https://doi.org/10.1016/j.ijforecast.2022.10.003](https://doi.org/10.1016/j.ijforecast.2022.10.003)</td>
<td>Dynamic factor models with Google Trends categories to nowcast GDP in a developed (US) and an emerging (Brazil) economy, handling the ragged-edge problem. Gains are broadly similar in both countries; more disaggregated queries do not help. Useful for cross-country nowcasting design choices.</td>
<td>Advanced reading on nowcasting across countries. Open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Forecasting tourism recovery amid COVID-19</td>
<td>Zhang, H., Song, H., Wen, L., Liu, C., Annals of Tourism Research 87, 103149, 2021, article</td>
<td>[https://doi.org/10.1016/j.annals.2021.103149](https://doi.org/10.1016/j.annals.2021.103149)</td>
<td>Forecasts the recovery of inbound tourism to Hong Kong from major source markets after the COVID-19 shock, combining econometric/time series forecasts with scenario analysis and expert judgmental adjustment. Shows how to forecast when a structural break invalidates history.</td>
<td>Case discussion: forecasting under shocks and structural breaks. Open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Visitor arrivals forecasts amid COVID-19: A perspective from the Europe team</td>
<td>Liu, A., Vici, L., Ramos, V., Giannoni, S., Blake, A., Annals of Tourism Research 88, 103182, 2021, article</td>
<td>[https://doi.org/10.1016/j.annals.2021.103182](https://doi.org/10.1016/j.annals.2021.103182)</td>
<td>Contribution to an international forecasting challenge on COVID-19 recovery: forecasts visitor arrivals to European destinations with time series/econometric models combined with scenario-based judgment.</td>
<td>Supplementary case for European international arrivals under shocks. Preprint free on HAL.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Back to Trend: COVID Effects on E-commerce in 47 Countries</td>
<td>Alcedo, J., Cavallo, A., Dwyer, B., Mishra, P., Spilimbergo, A., NBER Working Paper 29729, 2022, working paper</td>
<td>[https://doi.org/10.3386/w29729](https://doi.org/10.3386/w29729)</td>
<td>Mastercard transaction data for 47 economies and 26 industries before, during and after COVID-19. Online shares surged with lockdowns and fiscal transfers, then returned to pre-pandemic trends in almost all countries: little evidence of permanent structural change. Ideal multi-country example of temporary vs permanent shocks (link to persistence modelling).</td>
<td>Case discussion / intervention analysis exercise. Free (NBER).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Estimation of Panel Vector Autoregression in Stata</td>
<td>Abrigo, M. R. M., Love, I., Stata Journal 16(3), 778-804, 2016, article</td>
<td>[https://doi.org/10.1177/1536867X1601600314](https://doi.org/10.1177/1536867X1601600314)</td>
<td>Practical guide to panel VAR estimation (GMM), lag selection, Granger causality, impulse responses and variance decomposition with the pvar package. Directly usable for multi-country panel time series of marketing or trade data.</td>
<td>Lab/methods reading for panel VAR with country panels. Open access per OpenAlex.</td>
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
<td>The M6 forecasting competition: Bridging the gap between forecasting and investment decisions</td>
<td>Spyros Makridakis, Evangelos Spiliotis, Ross Hollyman, Fotios Petropoulos, Norman Swanson & Anil Gaba, International Journal of Forecasting 41(4), 2025, report</td>
<td>[https://pure.unic.ac.cy/en/publications/the-m6-forecasting-competition-bridging-the-gap-between-forecasti/](https://pure.unic.ac.cy/en/publications/the-m6-forecasting-competition-bridging-the-gap-between-forecasti/)</td>
<td>Live competition (Feb 2022-Feb 2023, 100 assets): hard to beat the market; weak link between forecasts and decisions; value of information sharing. Data and submissions on GitHub.</td>
<td>Optional reading on limits of forecastability and the forecast-decision link; less marketing-specific than M5. Check journal for OA status.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>X-13ARIMA-SEATS Seasonal Adjustment Program (software, reference manual, utilities)</td>
<td>U.S. Census Bureau, page revised July 2025, report/manual</td>
<td>[https://www.census.gov/data/software/x13as.html](https://www.census.gov/data/software/x13as.html)</td>
<td>Official home of X-13ARIMA-SEATS: regARIMA (regression with ARIMA errors), X-11 and SEATS adjustment, trading-day and moving-holiday regressors (Win Genhol for user-defined holidays such as Chinese New Year), diagnostics, batch processing. Usable from R via the seasonal package.</td>
<td>Explain how official statistics adjust monthly sales series and how holiday effects differ across countries. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>ESS Guidelines on Seasonal Adjustment - 2024 edition</td>
<td>Eurostat, Manuals and Guidelines KS-GQ-24-012, 2024, report</td>
<td>[https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/w/ks-gq-24-012](https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/w/ks-gq-24-012)</td>
<td>European standard for seasonal and calendar adjustment (doi 10.2785/705102): pre-treatment (outliers, national calendar effects), X-13 vs TRAMO-SEATS, revisions; new sections on high-frequency data, shocks (COVID) and long series. Recommends JDemetra+.</td>
<td>Selected sections when discussing seasonality and calendar effects in cross-country EU data. Free PDF.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Seasonal adjustment - Trusted Smart Statistics: JDemetra+ and RJDemetra (2024 training)</td>
<td>Eurostat CROS portal (JDemetra+ developed by National Bank of Belgium with Deutsche Bundesbank and Eurostat), 2024, report/training material</td>
<td>[https://cros.ec.europa.eu/book-page/seasonal-adjustment-trusted-smart-statistics-jdemetra-and-rjdemetra-2024](https://cros.ec.europa.eu/book-page/seasonal-adjustment-trusted-smart-statistics-jdemetra-and-rjdemetra-2024)</td>
<td>Training material for JDemetra+ (ESS-recommended since 2015, free, open source, EUPL) and its R interface RJDemetra: X-13 and TRAMO-SEATS in practice.</td>
<td>Shows the tool chain of European statistical offices (ESS members incl. Statistik Austria). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Saisonbereinigung der Konjunkturstatistiken mit X-12-ARIMA und mit X13 in JDemetra+</td>
<td>Stefan Linz, Claudia Fries & Julia Völker, Statistisches Bundesamt (Destatis), WISTA 4/2018, S. 59-80, report (German)</td>
<td>[https://www.destatis.de/DE/Methoden/WISTA-Wirtschaft-und-Statistik/2018/04/saisonbereinigung-konjunkturstatistiken-042018.pdf](https://www.destatis.de/DE/Methoden/WISTA-Wirtschaft-und-Statistik/2018/04/saisonbereinigung-konjunkturstatistiken-042018.pdf)</td>
<td>Deutschsprachige Methodenbeschreibung: Vergleich X-12-ARIMA vs. X13 in JDemetra+, Kalenderbereinigung, Ausreißer, Revisionen. No Statistik Austria methodology document surfaced in this search; check statistik.at directly.</td>
<td>German-language reading on seasonal adjustment in official statistics. Free PDF.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Reports</td>
<td>Quarterly National Accounts Manual (2017 ed.) - Chapter 7 Seasonal Adjustment</td>
<td>International Monetary Fund, 2018, report</td>
<td>[https://www.imf.org/external/pubs/ft/qna/](https://www.imf.org/external/pubs/ft/qna/)</td>
<td>IMF manual chapter on seasonal adjustment and trend-cycle estimation (X-13ARIMA-SEATS, TRAMO-SEATS), calendar effects across countries, revision policy.</td>
<td>Optional reading on cross-country comparability of adjusted data. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Forecasting at Scale (Prophet)</td>
<td>Sean J. Taylor & Benjamin Letham (Facebook), The American Statistician 72(1), 37-45, 2018 (PeerJ Preprint 2017), white paper</td>
<td>[https://doi.org/10.1080/00031305.2017.1380080](https://doi.org/10.1080/00031305.2017.1380080)</td>
<td>Prophet: decomposable regression model with piecewise trend, Fourier seasonality and country-specific holiday effects, designed for business forecasting at scale. Contrast to ARIMA (curve-fitting regression vs. stochastic model).</td>
<td>Industry alternative to ARIMA; students compare Prophet vs. ARIMA on a marketing series. Preprint free (PeerJ); journal version WU-Lizenz prüfen.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Bayesian Methods for Media Mix Modeling with Carryover and Shape Effects</td>
<td>Yuxue Jin, Yueqing Wang, Yunting Sun, David Chan & Jim Koehler, Google Inc., 2017, white paper</td>
<td>[https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/](https://research.google/pubs/bayesian-methods-for-media-mix-modeling-with-carryover-and-shape-effects/)</td>
<td>Google white paper formalising adstock (carryover) and saturation in regression-based media mix models; foundation for LightweightMMM and Google Meridian (github.com/google/meridian). Links distributed-lag regression to current MMM practice; compare Meta Robyn (github.com/facebookexperimental/Robyn, uses Prophet for trend/seasonality).</td>
<td>Read when moving from distributed-lag regression to modern MMM. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>The Long and the Short of It: Balancing Short and Long-Term Marketing Strategies</td>
<td>Les Binet & Peter Field, Institute of Practitioners in Advertising (IPA), 2013, report</td>
<td>[https://ipa.co.uk/knowledge/publications-reports/the-long-and-the-short-of-it-balancing-short-and-long-term-marketing-strategies/](https://ipa.co.uk/knowledge/publications-reports/the-long-and-the-short-of-it-balancing-short-and-long-term-marketing-strategies/)</td>
<td>Analysis of the IPA Databank (effectiveness cases from many countries): short-term activation vs. long-term brand building, 60:40 heuristic. Not econometrics itself, but motivates long-term effect measurement addressed by persistence/VAR models.</td>
<td>Discussion reading on short- vs. long-run effects; contrast with econometric evidence (Hanssens). Paid for non-members (IPA shop).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>The Multiplier Effect (and Ebiquity/WARC: The long-term impact of advertising)</td>
<td>WARC with Analytic Partners, BERA.ai, Prophet & System1, 2025; Ebiquity study on WARC 2018, report</td>
<td>[https://page.warc.com/the-multiplier-effect-report](https://page.warc.com/the-multiplier-effect-report)</td>
<td>Industry evidence that brand equity multiplies short-term returns; Ebiquity study of 504 campaigns/29 advertisers estimated long-term multipliers by medium (TV about 2.4). Based on econometric MMM across markets.</td>
<td>Practitioner evidence for long-term effects; use critically (limited method transparency). Registration required; full WARC content needs subscription (check WU access).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>MSI Research Priorities 2024-2026</td>
<td>Marketing Science Institute, 2024, report</td>
<td>[https://www.msi.org/](https://www.msi.org/)</td>
<td>Research agenda of the Marketing Science Institute incl. measuring marketing effectiveness, long-term effects, AI and analytics. Shows academic relevance and thesis topics.</td>
<td>Short reading to motivate thesis topics. Free (registration may be needed). Old priorities URL returned 404; exact page to be verified.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Websites (14)
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
<td>Forecasting: Principles and Practice (3rd ed), Chapter 10 Dynamic regression models</td>
<td>Rob J Hyndman & George Athanasopoulos, OTexts, 2021 (online edition), open textbook website, English</td>
<td>[https://otexts.com/fpp3/dynamic.html](https://otexts.com/fpp3/dynamic.html)</td>
<td>Regression with ARIMA errors in R (fable): estimation, forecasting, stochastic vs deterministic trends, dynamic harmonic regression, lagged predictors. Section 10.6 models monthly insurance quotations on TV advertising with lags up to 3 months - a ready-made advertising-carryover example; 10.2 US consumption vs income; 10.5 Australian eating-out turnover. Chapter 9 (ARIMA) precedes it. Master level, exercises included; embedded videos in many sections.</td>
<td>Core reading/lab companion for the R track; assign 10.6 as the advertising-lag case. Free, open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>statsmodels SARIMAX API reference and 'SARIMAX: Introduction' notebook</td>
<td>statsmodels developers, statsmodels.org, v0.15 docs, documentation website, English</td>
<td>[https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)</td>
<td>Authoritative reference for order, seasonal_order, exog and trend arguments. Companion notebook ([https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_sarimax_stata.html](https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_sarimax_stata.html)) replicates Stata examples: US WPI ARIMA, airline seasonal model, and an ARMAX with money supply m2 as regressor of consumption - directly shows exog handling and dynamic forecasting. Caveat: statsmodels SARIMAX exog is regression with ARMA errors, worth contrasting with Hyndman's ARIMAX note.</td>
<td>Python lab reference; students copy the ARMAX example and swap in ad spend/price. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Statistical forecasting: notes on regression and time series analysis</td>
<td>Robert Nau, Duke University Fuqua School of Business, ongoing, course website, English</td>
<td>[https://people.duke.edu/\~rnau/411home.htm](https://people.duke.edu/~rnau/411home.htm)</td>
<td>Business-school oriented, very readable notes: stationarity/differencing, log transforms, random walk, smoothing, multiple regression (interpretation, assumption tests), ARIMA identification rules, seasonal ARIMA and ARIMA with regressors, model selection and ethics in forecasting. Rules-of-thumb pages on identifying ARIMA orders are classroom gold. Software-neutral (some Statgraphics/Excel examples).</td>
<td>Pre-reading for students without econometrics background; ARIMA identification rules as handout. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>NIST/SEMATECH e-Handbook of Statistical Methods, 6.4.4 Univariate Time Series Models (Box-Jenkins)</td>
<td>NIST, itl.nist.gov, e-handbook (updated 2012), reference website, English</td>
<td>[https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44.htm](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44.htm)</td>
<td>Concise reference on stationarity, seasonality, Box-Jenkins identification, estimation, validation, with worked univariate and seasonal examples and sample data sets. Good for the classical Box-Jenkins workflow; no marketing data, no exog regressors.</td>
<td>Short reference reading for the identification-estimation-diagnosis cycle. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>STAT 510 Applied Time Series Analysis</td>
<td>Penn State Department of Statistics, online.stat.psu.edu, open course notes, English</td>
<td>[https://online.stat.psu.edu/stat510/](https://online.stat.psu.edu/stat510/)</td>
<td>14 lessons with R code: ARIMA identification/forecasting, seasonal models, Lesson 8 regression with ARIMA errors and cross-correlation between two series, Lesson 9 prewhitening and intervention analysis (useful for campaign/launch effects), VAR. Rigorous but approachable.</td>
<td>Lab companion; Lessons 8-9 for ad-sales cross-correlation and intervention (promotion/launch) analysis. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>StatsForecast documentation (Nixtla) incl. 'Exogenous Regressors' guide</td>
<td>Nixtla, nixtlaverse.nixtla.io, current docs, documentation website, English</td>
<td>[https://nixtlaverse.nixtla.io/statsforecast/index.html](https://nixtlaverse.nixtla.io/statsforecast/index.html)</td>
<td>Fast Python AutoARIMA/ETS/Theta for many series at once (panel of countries/SKUs), supports exogenous variables; how-to guide ([https://nixtlaverse.nixtla.io/statsforecast/docs/how-to-guides/Exogenous](https://nixtlaverse.nixtla.io/statsforecast/docs/how-to-guides/Exogenous)) adds future regressors to AutoARIMA and compares with/without. Ideal for forecasting many international markets in one call.</td>
<td>Python lab for multi-market (country-level) forecasting; scale-up after statsmodels. Free, open source.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Nixtla use case: What-If Forecasting - Price Effects in Retail</td>
<td>Nixtla, nixtla.io docs, use-case tutorial, English</td>
<td>[https://www.nixtla.io/docs/use_cases/what_if_forecasting_price_effects_in_retail](https://www.nixtla.io/docs/use_cases/what_if_forecasting_price_effects_in_retail)</td>
<td>Uses M5 Walmart data (FOODS_1_129, 10 stores) with sell_price as exogenous variable; reruns forecast with prices +/-5% for scenario comparison. Explicitly warns that differences are associations, not causal price effects - excellent discussion trigger. Uses TimeGPT (API key needed; free tier).</td>
<td>In-class discussion: scenario forecasting vs causal price elasticity; can be replicated with SARIMAX. Free docs; TimeGPT needs login/API key.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Prophet docs: Seasonality, Holiday Effects, and Regressors</td>
<td>Meta (Facebook) Prophet team, facebook.github.io/prophet, documentation website, English</td>
<td>[https://facebook.github.io/prophet/docs/seasonality,_holiday_effects,_and_regressors.html](https://facebook.github.io/prophet/docs/seasonality,_holiday_effects,_and_regressors.html)</td>
<td>Holidays dataframe with windows, built-in country holidays (add_country_holidays) - directly relevant for international marketing calendars - subdivision holidays, add_regressor for extra regressors (future values must be known). Python and R.</td>
<td>Lab: compare country-holiday handling across markets with SARIMAX dummies. Free. Note: Prophet is in maintenance mode.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Forecasting with sktime (tutorial notebook)</td>
<td>sktime developers, sktime.net, v1.x docs, documentation/tutorial, English</td>
<td>[https://www.sktime.net/en/stable/examples/01_forecasting.html](https://www.sktime.net/en/stable/examples/01_forecasting.html)</td>
<td>Unified scikit-learn-style forecasting API: horizons, ARIMA/AutoARIMA/SARIMAX wrappers, exogenous X, backtesting, pipelines with deseasonalising, tuning, probabilistic forecasts. Exogenous example uses dummy data, not ARIMA.</td>
<td>Optional advanced lab for model comparison/backtesting in Python. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>CRAN Task View: Time Series Analysis</td>
<td>Rob J Hyndman & Rebecca Killick (maintainers), CRAN, updated 2026-09-30, reference website, English</td>
<td>[https://cran.r-project.org/web/views/TimeSeries.html](https://cran.r-project.org/web/views/TimeSeries.html)</td>
<td>Curated, current map of R packages (forecast, fable, tsibble, seasonal/X-13, dynlm, vars, etc.). Saves time choosing packages for regression with ARIMA errors, seasonal adjustment, intervention models.</td>
<td>Instructor reference and student orientation for the R track. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>forecast R package website (auto.arima)</td>
<td>Rob J Hyndman et al., pkg.robjhyndman.com, package documentation, English</td>
<td>[https://pkg.robjhyndman.com/forecast/](https://pkg.robjhyndman.com/forecast/)</td>
<td>Docs for auto.arima (with xreg for regression with ARIMA errors), ETS, STL, TBATS; describes fable as complementary tidyverse package. Many older textbooks/tutorials use forecast, so useful bridge.</td>
<td>Reference for students following older R tutorials. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>JDemetra+ documentation</td>
<td>Eurostat / National Bank of Belgium / JDemetra+ team, Quarto online book, documentation website, English</td>
<td>[https://jdemetra-new-documentation.netlify.app/](https://jdemetra-new-documentation.netlify.app/)</td>
<td>Official software for seasonal adjustment used by European statistical offices (incl. Statistik Austria): X-13ARIMA and TRAMO-SEATS, calendar correction (working days, national holidays), outlier detection, external regressors; GUI plus R (rjdverse). Relevant when students use official seasonally adjusted retail/consumption data across EU countries.</td>
<td>Background reference for working with Eurostat/Statistik Austria data and calendar effects. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Michael Hauser course pages: Dynamische Systeme und Zeitreihenanalyse, Ökonometrie I/II (WU Wien)</td>
<td>Michael Hauser, WU Vienna Institute for Statistics and Mathematics, page dated 2019, course website, German/English</td>
<td>[https://statmath.wu.ac.at/\~hauser/](https://statmath.wu.ac.at/~hauser/)</td>
<td>Austrian/WU source: slides, data and R/EViews scripts for time series analysis and econometrics (incl. MgtSci 'Dynamische Systeme und Zeitreihenanalyse'). German-language local material aligned with WU students' prior courses. Some links may be outdated (2019).</td>
<td>Instructor reference; German-language background slides for students; check prior WU knowledge. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>PyMC-Marketing: Media Mix Modeling (MMM) in Python - End-to-End Example</td>
<td>PyMC Labs / PyMC-Marketing developers, pymc-marketing.io, docs notebook, English</td>
<td>[https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html](https://www.pymc-marketing.io/en/stable/notebooks/mmm/mmm_example.html)</td>
<td>Bayesian time series regression of weekly sales on two media channels with geometric adstock (l_max=8), logistic saturation, linear trend and Fourier yearly seasonality, event dummies; simulated data (179 weeks) for parameter recovery. Shows how time series regression extends to MMM.</td>
<td>Bridge session: from regression with ARIMA errors to MMM; advanced lab. Free, open source.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Blogs (15)
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
<td>The ARIMAX model muddle</td>
<td>Rob J Hyndman, Hyndsight blog, 2010, blog post, English</td>
<td>[https://robjhyndman.com/hyndsight/arimax/](https://robjhyndman.com/hyndsight/arimax/)</td>
<td>Explains why ARMAX coefficients are hard to interpret and why regression with ARMA errors keeps the usual 'effect of x on y' meaning; notes all are transfer function special cases; difference non-stationary variables to avoid spurious regression. Short and precise - exactly the conceptual issue marketing students get wrong with ad-spend effects.</td>
<td>Required short reading before the SARIMAX lab. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Hyndsight (blog of Rob J Hyndman)</td>
<td>Rob J Hyndman, robjhyndman.com, ongoing (latest posts Oct 2026), blog, English</td>
<td>[https://robjhyndman.com/hyndsight/](https://robjhyndman.com/hyndsight/)</td>
<td>Ongoing posts on forecasting practice, e.g. 'Monthly, quarterly and annual growth rates' (Jul 2026) and 'Evaluating time series foundation model claims' (Aug 2026) - useful for current debates (foundation models vs ARIMA) in class.</td>
<td>Instructor reading; pick 1-2 posts for discussion. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Forecasting at Uber: An Introduction</td>
<td>Slawek Smyl, Franziska Bell; Uber Engineering Blog, 6 Sep 2018, company blog</td>
<td>[https://www.uber.com/blog/forecasting-introduction/](https://www.uber.com/blog/forecasting-introduction/)</td>
<td>How Uber forecasts marketplace demand and supply by city, capacity and marketing. It covers ARIMA, Holt-Winters and Theta, ML and deep learning, chronological backtesting (sliding versus expanding window), naive benchmarks and prediction intervals (Omphalos framework).</td>
<td>Reading for the backtesting and prediction-interval session; students mirror the expanding-window backtest in their own ARIMA lab. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Prophet: forecasting at scale</td>
<td>Sean J. Taylor & Ben Letham, Meta/Facebook Research blog, 2017, company blog post, English</td>
<td>[https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/](https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/)</td>
<td>Rationale for an additive regression model (piecewise trend, Fourier yearly + weekly seasonality, holidays) for business series; framed as 'analyst-in-the-loop'. Useful to contrast decomposable regression with ARIMA.</td>
<td>Discussion reading: when is a regression/decomposition model preferable to ARIMA? Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>You're probably modeling seasonality the wrong way</td>
<td>Tom Vladeck, Recast blog, 2022, vendor blog post, English</td>
<td>[https://getrecast.com/seasonality/](https://getrecast.com/seasonality/)</td>
<td>Argues that treating seasonality as an additive control under-credits media in peak seasons; proposes time-varying ROI. Vendor perspective (promotes Recast) but provocative for discussing seasonality dummies/Fourier terms in sales-advertising regressions.</td>
<td>Debate prompt in the MMM/time series regression session. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Business Case: TV Impact - profitability of TV advertising via time series decomposition</td>
<td>Steffen Wagner, INWT Statistics blog (Berlin), 2016, company blog post, English (German site available)</td>
<td>[https://www.inwt-statistics.com/blog/tv-advertising](https://www.inwt-statistics.com/blog/tv-advertising)</td>
<td>German-region consultancy case: forecast an unbiased online traffic baseline per channel, attribute deviation to TV spots, handle overlapping spot windows; R2 \~0.7-0.8. Concrete marketing application of baseline forecasting/intervention logic.</td>
<td>Mini-case for intervention/baseline thinking; replicate idea with synthetic data. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Who's best in class? Comparing forecasting models with a Predictive Analytics Cube (PAC)</td>
<td>INWT Statistics blog, company blog post, English</td>
<td>[https://www.inwt-statistics.com/read-blog/predictive-analytics-cube-mvp-en.html](https://www.inwt-statistics.com/read-blog/predictive-analytics-cube-mvp-en.html)</td>
<td>Benchmarks auto.arima and Prophet against an ETS baseline with rolling-origin time series cross-validation; plans exogenous variables. Practical example of model comparison workflow.</td>
<td>Supplementary reading for evaluation session. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>What the MAPE is FALSELY blamed for, its TRUE weaknesses and BETTER alternatives</td>
<td>statworx team (Frankfurt), statworx content hub, 2019, company blog post, English</td>
<td>[https://www.statworx.com/en/content-hub/blog/what-the-mape-is-falsely-blamed-for-its-true-weaknesses-and-better-alternatives](https://www.statworx.com/en/content-hub/blog/what-the-mape-is-falsely-blamed-for-its-true-weaknesses-and-better-alternatives)</td>
<td>Clear discussion of MAPE problems (zeros, small actuals, cross-series comparison), relative MAE, MASE; recommends multiple metrics plus plots. Directly useful when students compare forecast accuracy across countries with different sales levels.</td>
<td>Reading for forecast-accuracy session. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Time Series Forecasting With Random Forest</td>
<td>statworx content hub (DACH consultancy), blog post, English</td>
<td>[https://www.statworx.com/en/content-hub/blog/time-series-forecasting-with-random-forest](https://www.statworx.com/en/content-hub/blog/time-series-forecasting-with-random-forest)</td>
<td>R walkthrough on German wage/income tax revenue: log + differencing, time-delay embedding (lag matrix), direct multi-step strategy, seasonal naive benchmark. Good bridge from lag-regression to ML; follow-up post on tuning with time-ordered CV.</td>
<td>Optional extension: ML vs ARIMA on the same series. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Time Series Forecasting: Regression oder ARIMA Models?</td>
<td>Novustat Statistik-Blog, 2023, blog post, German</td>
<td>[https://novustat.com/statistik-blog/time-series-forecasting-regression-oder-arima-models.html](https://novustat.com/statistik-blog/time-series-forecasting-regression-oder-arima-models.html)</td>
<td>German-language comparison of regression (explanatory drivers) vs ARIMA (own past), including sales/cost examples. Introductory level; partly promotional for consulting services. Sister post 'ARIMA Model: So gelingen Vorhersagen'.</td>
<td>German pre-reading for students who prefer German. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Automated Time Series Feature Engineering with MLforecast</td>
<td>Nixtla blog, 2025, company blog post, English</td>
<td>[https://www.nixtla.io/blog/automated-time-series-feature-engineering-with-mlforecast](https://www.nixtla.io/blog/automated-time-series-feature-engineering-with-mlforecast)</td>
<td>Synthetic daily e-commerce sales (3 products, trend + weekly cycle); automates lags, rolling stats, date features, differencing, time-ordered cross-validation with LightGBM. Shows 'time series regression with lag features' at scale. Efficiency claim (80%) not measured.</td>
<td>Optional lab extension after manual lag regression. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>What COVID did to our forecasting models (and what we built to handle the next shock)</td>
<td>Harrison Katz; Airbnb Tech Blog (airbnb.tech), about 2026, company blog</td>
<td>[https://airbnb.tech/?p=745](https://airbnb.tech/?p=745)</td>
<td>Splits bookings into volume and lead-time composition; uses Bayesian Dirichlet ARMA and an intervention model for structural breaks. International guests showed sharper booking-horizon compression and slower recovery than domestic guests. The text quotes inconsistent error-reduction figures (31% vs 24%).</td>
<td>COVID demand-shock discussion: intervention dummies versus smooth transition, and domestic versus international markets. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>Applied Methods from Mathematical Optimization and Machine Learning in E-commerce (GOR workshop)</td>
<td>Zalando Engineering Blog, 2023, company blog post, English</td>
<td>[https://engineering.zalando.com/posts/2023/02/gor-workshop.html](https://engineering.zalando.com/posts/2023/02/gor-workshop.html)</td>
<td>European e-commerce view: article-level demand forecasting per market with probabilistic deep RNN forecasts, pricing context. Shows what multi-country retail forecasting looks like in practice beyond ARIMA.</td>
<td>Background reading on industrial multi-market forecasting. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>How to Create an ARIMA Model for Time Series Forecasting in Python</td>
<td>Jason Brownlee, Machine Learning Mastery, blog tutorial, English</td>
<td>[https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/)</td>
<td>Step-by-step statsmodels ARIMA on a small monthly sales dataset (shampoo sales, per memory), train/test split and rolling (walk-forward) forecasts. Simple entry point; caveat: check code against current statsmodels API (old ARIMA class removed).</td>
<td>Optional self-study for Python beginners. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Blogs</td>
<td>SQL to SARIMAX: How I navigate the first time-series analysis personal project for my portfolio</td>
<td>Towards Data Science, blog post, English</td>
<td>[https://towardsdatascience.com/sql-to-sarimax-how-i-navigate-the-first-time-series-analysis-personal-project-for-my-portfolio-1ed24cba2c52/](https://towardsdatascience.com/sql-to-sarimax-how-i-navigate-the-first-time-series-analysis-personal-project-for-my-portfolio-1ed24cba2c52/)</td>
<td>Student-style project analysing promotion effects on sales across products and cities, then SARIMAX; good model for a student term project workflow (SQL extraction -\> EDA -\> SARIMAX). Quality of modelling not verified.</td>
<td>Example of a student project write-up. Free (TDS may show paywall prompts).</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### (Video-) Tutorials (14)
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
<td>Time Series Talk: ARIMA Model (and series: Seasonal ARIMA, Coding SARIMA, AIC & BIC)</td>
<td>ritvikmath, YouTube, \~2019, video series, English</td>
<td>[https://www.youtube.com/watch?v=3UmyHed0iYE](https://www.youtube.com/watch?v=3UmyHed0iYE)</td>
<td>ARIMA intro \~9:26 min with whiteboard intuition for AR, I, MA. Companions: Seasonal ARIMA ([https://www.youtube.com/watch?v=WjeGUs6mzXg](https://www.youtube.com/watch?v=WjeGUs6mzXg)), Coding the SARIMA Model ([https://www.youtube.com/watch?v=Al8m6K_stfA](https://www.youtube.com/watch?v=Al8m6K_stfA)), Model Selection AIC & BIC ([https://www.youtube.com/watch?v=McEN54l3EPU](https://www.youtube.com/watch?v=McEN54l3EPU)). Short, intuitive; older code uses deprecated statsmodels ARIMA class.</td>
<td>Pre-class flipped videos (total under 1 hour). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Forecasting: Principles & Practice 3rd ed - video playlist</td>
<td>Rob J Hyndman & George Athanasopoulos, YouTube (linked from Hyndsight), video playlist, English</td>
<td>[https://www.youtube.com/playlist?list=PLyCNZ_xXGzpm7W9jLqbIyBAiSO5jDwJeE](https://www.youtube.com/playlist?list=PLyCNZ_xXGzpm7W9jLqbIyBAiSO5jDwJeE)</td>
<td>Short videos embedded in most fpp3 sections, covering what the authors use in their own courses; overview page [https://robjhyndman.com/hyndsight/fpp3_videos.html](https://robjhyndman.com/hyndsight/fpp3_videos.html). Exact ARIMA/dynamic regression video titles not verified - check playlist for chapters 9-10.</td>
<td>Pre-class videos matched to fpp3 readings (R track). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>posit::conf(2023) Workshop: Tidy time series and forecasting in R</td>
<td>Rob J Hyndman, posit, YouTube, 2023, workshop recording, English</td>
<td>[https://www.youtube.com/watch?v=Fo8aFDWchcY](https://www.youtube.com/watch?v=Fo8aFDWchcY)</td>
<td>Recording of Hyndman's tsibble/fable workshop (two-day course for tidyverse users). Length not verified (likely multi-hour); use ARIMA and dynamic regression segments.</td>
<td>Instructor prep / optional deep dive for R students. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Aileen Nielsen - Time Series Analysis - PyCon 2017</td>
<td>Aileen Nielsen, PyCon US, YouTube, 2017, tutorial recording, English</td>
<td>[https://www.youtube.com/watch?v=zmfe2RaX-14](https://www.youtube.com/watch?v=zmfe2RaX-14)</td>
<td>Hands-on Python tutorial (PyCon tutorials typically \~3 h; length not verified) in four parts: handling timestamped data in pandas, common time series problems, prediction and classification exercises. Strong on pandas resampling/windows; older library versions. Related playlist: [https://www.youtube.com/playlist?list=PLRRxOfxVBikdM1SbWQlCd8ENfN8ZuJ_js](https://www.youtube.com/playlist?list=PLRRxOfxVBikdM1SbWQlCd8ENfN8ZuJ_js).</td>
<td>Python data-prep self-study before ARIMA labs; first hour most relevant. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Practical Time Series Analysis</td>
<td>Tural Sadigov & William Thistleton, State University of New York, Coursera, MOOC, English (R)</td>
<td>[https://www.coursera.org/learn/practical-time-series-analysis](https://www.coursera.org/learn/practical-time-series-analysis)</td>
<td>6 modules (\~26 h): basic stats, visualisation, stationarity, MA/AR, Yule-Walker/PACF, AIC and ARIMA (week 5), seasonality/SARIMA and forecasting (week 6). R-based, rated 4.6, \~99k learners. Weeks 5-6 are the key ARIMA content; no exogenous regressors.</td>
<td>Self-study for students needing ARIMA foundations; assign weeks 3-6. Free to browse/audit options vary; certificate paid (Coursera Plus).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>ARIMA Models in Python</td>
<td>James Fulton, DataCamp, course, English (German UI available)</td>
<td>[https://www.datacamp.com/courses/arima-models-in-python](https://www.datacamp.com/courses/arima-models-in-python)</td>
<td>\~4 h, 4 chapters: ARMA/stationarity, fitting AR/MA/ARMA/ARMAX/ARIMA in statsmodels, order selection via ACF/PACF, AIC/BIC and diagnostics, SARIMA + global forecast challenge. Interactive exercises; ARMAX chapter relevant for ad-spend regressors.</td>
<td>Assignable homework (DataCamp Classrooms free for instructors). Otherwise paid subscription (\~USD 25-40/month).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>ARIMA Models in R</td>
<td>David Stoffer, DataCamp, course, English</td>
<td>[https://www.datacamp.com/courses/arima-models-in-r](https://www.datacamp.com/courses/arima-models-in-r)</td>
<td>\~4 h, 13 videos/45 exercises with astsa: ARMA on simulated data, ARIMA on real data, validation, forecasting, seasonal ARIMA. Taught by co-author of Shumway & Stoffer textbook.</td>
<td>R-track homework; free via DataCamp Classrooms, else paid subscription.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Python for Time Series Forecasting</td>
<td>Jesus Lopez, LinkedIn Learning, 2025, video course, English</td>
<td>[https://www.linkedin.com/learning/python-for-time-series-forecasting](https://www.linkedin.com/learning/python-for-time-series-forecasting)</td>
<td>4 h 19 min, intermediate: data from FRED/Excel, Plotly, decomposition, baselines, ARIMA (ch. 7), SARIMA (ch. 8), stationarity, exponential smoothing, Prophet with holidays, train/test and walk-forward validation (ch. 15), template notebooks in Codespaces.</td>
<td>Self-study for Python track; chapters 6-9 and 13-15 most relevant. Login; check if WU provides LinkedIn Learning, else paid (\~EUR 30/month).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Kaggle Learn: Time Series</td>
<td>Ryan Holbrook, Kaggle Learn, free micro-course, English (Python)</td>
<td>[https://www.kaggle.com/learn/time-series](https://www.kaggle.com/learn/time-series)</td>
<td>Lessons: Linear Regression With Time Series (time-step and lag features), Trend, Seasonality (Fourier/dummies), Time Series as Features, Hybrid Models, Forecasting With ML; runnable notebooks (dataset believed to be Kaggle Store Sales, not verified). Excellent for 'time series regression' framing; no ARIMA.</td>
<td>Hands-on homework before ARIMA session. Free, Kaggle login.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Forecasting Economic Time Series in Python using SARIMAX</td>
<td>YouTube, video tutorial, English</td>
<td>[https://www.youtube.com/watch?v=tr8PF2v9Wgo](https://www.youtube.com/watch?v=tr8PF2v9Wgo)</td>
<td>Walkthrough of statsmodels SARIMAX on vehicle sales data - close to a marketing sales example. Channel, length and quality not verified.</td>
<td>Optional coding video for lab prep. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>ARIMAX Model for Sales Forecasting</td>
<td>YouTube, video tutorial, English</td>
<td>[https://www.youtube.com/watch?v=RdmtJNdYqyU](https://www.youtube.com/watch?v=RdmtJNdYqyU)</td>
<td>ARIMAX on sales with promotion and discount variables as regressors - the typical marketing exog use case. Channel, length and quality not verified; preview before assigning.</td>
<td>Optional demo of promotion regressors. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Dax/Aktien vorhersagen mit ARIMA Modellen in R (\~6 Minuten)</td>
<td>YouTube, video tutorial, German</td>
<td>[https://www.youtube.com/watch?v=fodtuaQmZPs](https://www.youtube.com/watch?v=fodtuaQmZPs)</td>
<td>About 6-minute German-language demo of auto.arima in R on DAX series. Short German entry point; finance not marketing data, channel not verified.</td>
<td>Optional German pre-class video. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Gretl Tutorium (deutsch): ADF-Test und KPSS-Test auf Stationarität von Zeitreihen</td>
<td>YouTube, \~2020, video tutorials, German</td>
<td>[https://www.youtube.com/watch?v=7LctYlWmbUY](https://www.youtube.com/watch?v=7LctYlWmbUY)</td>
<td>German explanations of unit root testing (ADF; KPSS: [https://www.youtube.com/watch?v=vqCvyqJjhAA](https://www.youtube.com/watch?v=vqCvyqJjhAA)) in Gretl. Concepts transfer to Python/R; Gretl GUI may differ now. Length not verified.</td>
<td>German self-study for stationarity concepts. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Forecasting time series using R (Melbourne R Users)</td>
<td>Rob J Hyndman, Melbourne R Users, YouTube, talk recording, English</td>
<td>[https://www.youtube.com/watch?v=1Lh1HlBUf8k](https://www.youtube.com/watch?v=1Lh1HlBUf8k)</td>
<td>Hyndman talk on forecasting with R (forecast package era: ETS, auto.arima). Length/date not verified; older API but clear conceptual overview.</td>
<td>Optional background video. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Cases for Teaching (17)
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
<td>Harmonizing Demand Forecasting and Supply at Mahindra & Mahindra Ltd.</td>
<td>Alok Yadav, Sunil Ashra; Ivey Publishing, product no. W13569, 2014 (orig. 2013), teaching case, 6 pp.</td>
<td>[https://store.hbr.org/product/harmonizing-demand-forecasting-and-supply-at-mahindra-mahindra-ltd/W13569](https://store.hbr.org/product/harmonizing-demand-forecasting-and-supply-at-mahindra-mahindra-ltd/W13569)</td>
<td>India's leading tractor maker; sales offices produce rolling 3-month demand forecasts and dealers complain about irregular supply. Monthly historical tractor sales with seasonal and irregular demand; Ivey positions it for sales forecasting and econometrics courses. Student spreadsheet with data (7B13D019, .xls) is available; a teaching note is usual for Ivey but is not shown on the HBR store page, so check it at Ivey or HBP.</td>
<td>Lab case: students fit seasonal decomposition, exponential smoothing and SARIMA or time series regression with seasonal dummies to the tractor data and compare holdout errors. Then discuss how the forecasts feed supply decisions in an emerging market. Paid: about USD 11.95 per student (HBP educator discount up to 50%).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>A-CAT Corp.: Forecasting</td>
<td>Jitendra R. Sharma; Ivey Publishing, product no. W13377, 2013, teaching case, 4 pp.</td>
<td>[https://store.hbr.org/product/a-cat-corp-forecasting/W13377](https://store.hbr.org/product/a-cat-corp-forecasting/W13377)</td>
<td>Indian maker of voltage regulators for price-sensitive rural buyers; sales drop and component shortages arise. The operations manager must collect data, apply several forecasting methods, back-test them and recommend one. Short and data-driven; often used in graduate quantitative methods courses. The store page lists no teaching note or spreadsheet, so check at Ivey.</td>
<td>Warm-up or homework case on back-testing (moving average, exponential smoothing, trend regression) before ARIMA is introduced. Paid: about USD 11.95 per copy.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Toffee Inc.: Demand Planning for Chocolate Bars</td>
<td>Jitendra R. Sharma (IMT); Ivey Publishing, product no. W15155, 2015, teaching case, 5 pp.</td>
<td>[https://store.hbr.org/product/toffee-inc-demand-planning-for-chocolate-bars/W15155](https://store.hbr.org/product/toffee-inc-demand-planning-for-chocolate-bars/W15155)</td>
<td>Confectionery maker with seasonal demand data (about 2006-2010 per secondary sources). Students forecast with seasonal factors and a linear trend, then link the forecasts to EOQ and safety stock. The store page lists no supplements or teaching note.</td>
<td>Introductory lab on classical decomposition and trend-plus-seasonal regression; extend it with an ARIMA comparison. Paid: about USD 11.95.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Markdown Optimization for an Indian Apparel Retailer</td>
<td>Deepak George, Karthik Kuram, Ramalakshmi Subramanian, Sumad Singh, Dinesh Kumar Unnikrishnan; IIM Bangalore via HBP, product no. IMB561, 2016, teaching case, 16 pp.</td>
<td>[https://store.hbr.org/product/markdown-optimization-for-an-indian-apparel-retailer/IMB561](https://store.hbr.org/product/markdown-optimization-for-an-indian-apparel-retailer/IMB561)</td>
<td>WE SELL STYLE, an Indian fashion chain with over 200 stores. Seasonal, hard-to-forecast demand drives end-of-season markdown decisions based on sales rate, sell-through and remaining stock. HBP search snippets say it uses time series forecasting with regression. Available in many languages, including German.</td>
<td>Case discussion linking sales-response regression over time (price, markdown, season) to pricing decisions in an emerging market. Paid: about USD 11.95.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Sport Obermeyer Ltd.</td>
<td>Janice H. Hammond, Ananth Raman; Harvard Business School, product no. 695022, 1994, teaching case, 20 pp.</td>
<td>[https://store.hbr.org/product/sport-obermeyer-ltd/695022](https://store.hbr.org/product/sport-obermeyer-ltd/695022)</td>
<td>Classic case on demand forecasting for fashion skiwear with short life cycles. It contrasts judgmental committee forecasts and the dispersion of forecasts with sourcing in Hong Kong and China. A simplified planning data set is included in the exhibits. A teaching note is available to registered HBP educators (check there). It is not an ARIMA case.</td>
<td>Contrast session: when time series models fail (new products, no history) and judgmental or expert forecasts take over. Paid: about USD 11.95.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Forecasting Beer Demand at Anadolu Efes</td>
<td>Murat Köksalan, Selin Özpeynirci, Haldun Süral; INFORMS Transactions on Education 10(3), 2010, case article plus student case (DOI 10.1287/ited.1100.0048cs)</td>
<td>[https://pubsonline.informs.org/doi/10.1287/ited.1100.0048cs](https://pubsonline.informs.org/doi/10.1287/ited.1100.0048cs)</td>
<td>Students build a multiple regression model of monthly beer demand in Turkey using price, tourism and seasonality variables. They test the regression assumptions, validate the model and apply transformations. The student case is marked Free Access in the search result. The teaching note (0048tn) is restricted to instructors via the INFORMS Instructor Materials page.</td>
<td>Core lab for time series regression: seasonal dummies, tourism as a driver, autocorrelated residuals, then a SARIMAX comparison. Free (student case); the teaching note needs instructor registration.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Forecasting at FoodMart: A Case on Cultural Diversity in Supply Chain Management</td>
<td>Amy David (Purdue); INFORMS Transactions on Education 25(3), 2025, case plus case article (DOI 10.1287/ited.2023.0037cs)</td>
<td>[https://pubsonline.informs.org/doi/10.1287/ited.2023.0037cs](https://pubsonline.informs.org/doi/10.1287/ited.2023.0037cs)</td>
<td>A grocery planner finds that Mexican Coke sales spike in spring, but in a different week each year (a moving holiday), so standard seasonal factors misfire. Five years of weekly sales for four products are provided. It teaches that forecasting needs cultural knowledge, such as moving religious holidays across markets.</td>
<td>Excellent international-marketing hook: model moving holidays (Easter, Ramadan) with event dummies in regression or ARIMAX versus fixed seasonal factors. Access via INFORMS (WU-Lizenz prüfen); the teaching note is for instructors.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Canyon Bicycles: Judgmental Demand Forecasting in Direct Sales</td>
<td>Christoph Diermann, Arnd Huchzermeier (WHU); INFORMS Transactions on Education 17(2), 2017, case article (DOI 10.1287/ited.2016.0165ca) and student case (0165cs)</td>
<td>[https://pubsonline.informs.org/doi/10.1287/ited.2016.0165cs](https://pubsonline.informs.org/doi/10.1287/ited.2016.0165cs)</td>
<td>A German premium direct-to-consumer bicycle brand; the CEO and experts forecast the whole season's demand in a two-day meeting. Topics: team composition, debiasing, demand distributions and forecast quality. A detailed teaching note and debrief slides are restricted to instructors. Related research reports that ML forecasts on Canyon data cut errors by about 24% versus judgment.</td>
<td>Case discussion on judgment versus statistical forecasts in a DACH firm; pair it with an ARIMA lab to discuss forecast combination. Access via INFORMS (WU-Lizenz prüfen).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Quality Kitchen Meat Loaf Mix (A) and (B)</td>
<td>Charles Bonini; Stanford GSB, case no. DS84A (A) and (B), 1989, teaching case</td>
<td>[https://www.gsb.stanford.edu/faculty-research/case-studies/quality-kitchen-meat-loaf-mix](https://www.gsb.stanford.edu/faculty-research/case-studies/quality-kitchen-meat-loaf-mix)</td>
<td>A new brand manager must write a marketing plan using historical sales, advertising, promotion and economic data. Preliminary regression results are given; case (B) presents more detailed regressions to interpret. A classic sales-response-over-time case. Free download only for Stanford GSB members; others contact businesscases@stanford.edu.</td>
<td>Discussion of advertising elasticities and carry-over in a time series sales-response regression; good bridge from regression to distributed lags. Access: request from Stanford (price not shown).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Marriott Rooms Forecasting</td>
<td>Samuel E. Bodily, Larry Weatherford; Darden Business Publishing, product no. QA-0389, 1989, teaching case, 6 pp.</td>
<td>[https://store.darden.virginia.edu/marriott-rooms-forecasting](https://store.darden.virginia.edu/marriott-rooms-forecasting)</td>
<td>A hotel manager must decide whether to accept 60 extra reservations by forecasting no-shows from historical data. Darden recommends it for teaching seasonality and exponential smoothing. The store page shows no teaching note or supplement.</td>
<td>Short in-class exercise on day-of-week seasonality and smoothing in hospitality demand; extend it to ARIMA. Paid (Darden or HBP; price shown only in the cart).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Time Series Forecasting (technical note)</td>
<td>Samuel E. Bodily; Darden Business Publishing, product no. QA-0438 (HBP UV0678), 1993, technical note, 17 pp.</td>
<td>[https://store.darden.virginia.edu/time-series-forecasting](https://store.darden.virginia.edu/time-series-forecasting)</td>
<td>Covers approaches to forecasting, moving averages, exponential smoothing, seasonality, trend, implementation, and Holt and Winters models. Companion notes: QA-0407 Seasonality in Time Series Forecasting (Bodily and Weatherford, 6 pp.) and QA-0695 Time Series (Pfeifer, 2006, 17 pp.).</td>
<td>Pre-reading before ARIMA sessions; pairs with the Marriott case. Paid, low price (Darden or HBP).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Forecasting Using the Linear Regression Model (technical note)</td>
<td>Phillip E. Pfeifer; Darden Business Publishing, product no. QA-0327, 1985, technical note, 5 pp.</td>
<td>[https://store.darden.virginia.edu/forecasting-using-the-linear-regression-model](https://store.darden.virginia.edu/forecasting-using-the-linear-regression-model)</td>
<td>Shows how a regression produces a point forecast and a forecast interval for an uncertain dependent variable. A short conceptual bridge to time series regression forecasting.</td>
<td>Pre-reading on prediction intervals before students forecast with regression plus ARIMA errors. Paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Multiple Regression and Marketing-Mix Models (technical note)</td>
<td>Rajkumar Venkatesan, Shea Gibbs; Darden Business Publishing, product no. UV6764, 2013, technical note, 10 pp.</td>
<td>[https://store.hbr.org/product/multiple-regression-and-marketing-mix-models/UV6764](https://store.hbr.org/product/multiple-regression-and-marketing-mix-models/UV6764)</td>
<td>Introduces multiple regression for marketing-mix models, omitted-variable bias, and economic versus statistical significance. Used in Darden's Big Data in Marketing elective.</td>
<td>Marketing-specific pre-reading before a lab on lagged advertising effects (adstock) in time series regression. Paid: USD 8.95.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>JMP020 Direct Mail (JMP Case Study Library)</td>
<td>JMP Statistical Discovery (SAS), JMP Case Study Library, case JMP020, teaching case with data, 9 pp.</td>
<td>[https://www.jmp.com/content/dam/jmp/documents/en/academic/case-study-library/case-study-library-12/jmp020-direct-mail.pdf](https://www.jmp.com/content/dam/jmp/documents/en/academic/case-study-library/case-study-library-12/jmp020-direct-mail.pdf)</td>
<td>A free case on lagged effects of direct-mail spending on weekly sales. It shows that lagging a time series variable means shifting it down one row; the model estimates about a USD 53 rise in next week's sales per mail dollar (per the search snippet). Data and exercises included; solutions on request for instructors. The PDF was fetched, but its text could not be read.</td>
<td>Free warm-up lab on distributed lags and carry-over in sales response; can be redone in R or Python instead of JMP. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Wilkins, a Zurn Company: Demand Forecasting</td>
<td>The Case Centre listing (publisher and number to verify on the product page), teaching case</td>
<td>[https://www.thecasecentre.org/students/products/view?id=70486](https://www.thecasecentre.org/students/products/view?id=70486)</td>
<td>Students compare executive opinion, linear regression and time series methods on demand data with seasonality, trend and random fluctuations. The Case Centre page returned 403, so details come from the search snippet only.</td>
<td>Method-comparison case (judgment versus regression versus smoothing or ARIMA). Paid via The Case Centre (WU-Lizenz prüfen).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Operations Management Reading: Forecasting</td>
<td>Steven C. Wheelwright, Winslow; Harvard Business Publishing, reference 8043 (teaching-note software supplement 8045), revised 2024, reading</td>
<td>[https://www.thecasecentre.org/products/view?id=125085](https://www.thecasecentre.org/products/view?id=125085)</td>
<td>A short summary of judgmental methods and a longer quantitative section (smoothing, decomposition, regression). Listed with a teaching note, exhibit slides and a software supplement. Case Centre page not fetchable (403).</td>
<td>Background reading for students without a forecasting background. Paid (HBP or Case Centre).</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Time Series Analysis and Forecasting (reading)</td>
<td>Business Expert Press chapter via Harvard Business Publishing, product no. BEP505, 2019, reading, 43 pp.</td>
<td>[https://hbsp.harvard.edu/product/BEP505-PDF-ENG](https://hbsp.harvard.edu/product/BEP505-PDF-ENG)</td>
<td>A 43-page operations-management reading on moving averages, weighted moving averages, exponential smoothing and regression-based predictive analytics. The HBSP page renders via JavaScript, so details come from the search snippet.</td>
<td>Optional pre-reading. Paid (HBP).</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Praxisbeispiele (21)
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
<td>Rossmann Store Sales (Kaggle competition)</td>
<td>Rossmann (Germany) / Kaggle, competition, 2015</td>
<td>[https://www.kaggle.com/c/rossmann-store-sales](https://www.kaggle.com/c/rossmann-store-sales)</td>
<td>Daily sales for 1,115 German drugstores, Jan 2013 to Jul 2015; forecast 6 weeks. Promotions, state and school holidays, competitor distance and closures are included. Top teams added Google Trends, weather and macro data. Metric: RMSPE.</td>
<td>Replicate: per-store SARIMA or regression with promotion and holiday dummies versus pooled gradient boosting; discuss promotion lift over time. Free (Kaggle login for download).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Corporación Favorita Grocery Sales Forecasting and Store Sales - Time Series Forecasting (Kaggle)</td>
<td>Corporación Favorita (Ecuador) / Kaggle, research competition 2017-2018 plus ongoing getting-started competition</td>
<td>[https://www.kaggle.com/competitions/store-sales-time-series-forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)</td>
<td>Ecuadorian grocer, 54 stores, 2013-2017. Files include sales, promotions, transactions, store info, oil prices (Ecuador is oil-dependent) and national, regional and local holidays, plus the 2016 earthquake shock. The original competition is at kaggle.com/c/favorita-grocery-sales-forecasting.</td>
<td>Very good international lab: ARIMAX with oil price as a macro driver, holiday calendars by region, and an intervention dummy for the earthquake. Free (Kaggle login).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>M5 Forecasting - Accuracy (Walmart, Kaggle) and IJF results papers</td>
<td>Makridakis, Spiliotis, Assimakopoulos / University of Nicosia, Walmart, Kaggle, 2020; results in International Journal of Forecasting 38(4), 2022</td>
<td>[https://www.kaggle.com/competitions/m5-forecasting-accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy)</td>
<td>42,840 hierarchical daily unit-sales series (3 US states, 10 stores, 3,049 products) with prices, SNAP days and events. The papers document that LightGBM-style ML beat statistical benchmarks, while exponential smoothing and ARIMA remain strong baselines. A sister Uncertainty competition covers quantile forecasts.</td>
<td>Replicate baselines (naive, ETS, ARIMA) on a subset and compare with the winners; discuss hierarchy and price effects. Free (Kaggle login); papers via ScienceDirect (WU-Lizenz prüfen).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Walmart Recruiting - Store Sales Forecasting (Kaggle)</td>
<td>Walmart / Kaggle, recruiting competition, 2014</td>
<td>[https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)</td>
<td>Weekly department sales for 45 Walmart stores with markdown (promotion) data and major holidays (Super Bowl, Labor Day, Thanksgiving, Christmas) weighted more heavily in scoring. Small and tidy, so it suits classroom labs.</td>
<td>Lab: regression with holiday and markdown effects plus ARIMA errors on store-level weekly sales. Free (Kaggle login).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Web Traffic Time Series Forecasting (Wikipedia, Kaggle)</td>
<td>Google / Kaggle, competition, 2017</td>
<td>[https://www.kaggle.com/c/web-traffic-time-series-forecasting](https://www.kaggle.com/c/web-traffic-time-series-forecasting)</td>
<td>Daily views of about 145,000 Wikipedia articles (Jul 2015 to Sep 2017) in seven language editions (EN, DE, FR, ES, RU, JA, ZH), by access and agent type. Weekly patterns differ by language (strong for Spanish). Metric: SMAPE.</td>
<td>International angle: compare seasonality and ARIMA fits for the same brand or topic page across language markets, as a proxy for cross-country interest. Free (Kaggle login).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Predict Future Sales (1C Company, Russia, Kaggle)</td>
<td>1C Company / Kaggle / HSE Coursera course, ongoing competition</td>
<td>[https://www.kaggle.com/c/competitive-data-science-predict-future-sales](https://www.kaggle.com/c/competitive-data-science-predict-future-sales)</td>
<td>Daily sales of software and media items across Russian shops, Jan 2013 to Oct 2015; forecast monthly totals for Nov 2015. The shop and item lists change over time and labels are in Russian, which is realistic for an emerging-market retailer.</td>
<td>Homework on aggregating daily to monthly series and fitting ARIMA per category. Free (Kaggle login).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Recruit Restaurant Visitor Forecasting (Japan, Kaggle)</td>
<td>Recruit Holdings / Kaggle, competition, 2017-2018</td>
<td>[https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting](https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting)</td>
<td>Daily visitors for about 800 Japanese restaurants (Jan 2016 to Apr 2017) from the AirREGI POS and reservation systems, with Japanese holidays and Golden Week. Strong year-end and New Year seasonality.</td>
<td>Lab on holiday effects in a non-Western calendar (Golden Week) using regression with ARIMA errors. Free (Kaggle login).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>The Tourism Forecasting Competition (data in R package Tcomp)</td>
<td>Athanasopoulos, Hyndman, Song, Wu; International Journal of Forecasting 27(3), 2011; data in CRAN package Tcomp (P. Ellis)</td>
<td>[https://cran.r-project.org/package=Tcomp](https://cran.r-project.org/package=Tcomp)</td>
<td>1,311 monthly, quarterly and yearly tourism series from tourism bodies worldwide, with train and test splits. The paper compares ARIMA, exponential smoothing and econometric models; Tcomp reproduces its tables.</td>
<td>Replicate: students fit auto.arima and ETS to the tourism series and reproduce the paper's MAPE/MASE tables. Free (R).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Forecasting Tourism Demand with Google Trends for a Major European City Destination (Vienna)</td>
<td>Irem Önder, Ulrich Gunter (MODUL University Vienna); Tourism Analysis 21(2-3), 2016, journal article</td>
<td>[https://research.modul.ac.at/en/publications/forecasting-tourism-demand-with-google-trends-for-a-major-europea/](https://research.modul.ac.at/en/publications/forecasting-tourism-demand-with-google-trends-for-a-major-europea/)</td>
<td>Google Trends web and image search indices improve forecasts of Vienna arrivals by source market and horizon, beating AR, Holt-Winters and naive benchmarks. Native-language queries work better. Follow-ups compare Vienna, Barcelona, Austria and Belgium, and use Facebook likes for Graz, Innsbruck, Salzburg and Vienna.</td>
<td>Local replication: Vienna arrivals by origin country (Statistik Austria or Wien Tourismus) plus Google Trends in German, Italian etc., fitted as an ARIMAX. Guest-speaker potential (Vienna). Paper paid (WU-Lizenz prüfen).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Now- und Forecasting touristischer Nächtigungen, Umsätze und Wertschöpfung für Österreich</td>
<td>Oliver Fritz, Anna Burton, Philipp Piribauer; WIFO Studies 69823, 2022, commissioned by Österreich Werbung</td>
<td>[https://ideas.repec.org/b/wfo/wstudy/69823.html](https://ideas.repec.org/b/wfo/wstudy/69823.html)</td>
<td>WIFO compares several nowcasting and forecasting models for Austrian overnight stays, tourism revenue and value added; shrinkage models perform best. German with an English abstract; full text via wifo.ac.at.</td>
<td>Austrian real-world example of model competition and forecast evaluation; discuss it with an ARIMA lab on Austrian tourism data. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Statistik Austria: Ankünfte und Nächtigungen (monthly tourism statistics, e.g. December 2025 release)</td>
<td>Statistik Austria, press release and monthly tourism statistics, 2026</td>
<td>[https://www.statistik.at/fileadmin/announcement/2026/01/20260130AnkuenfteNaechtigungenDezember2025.pdf](https://www.statistik.at/fileadmin/announcement/2026/01/20260130AnkuenfteNaechtigungenDezember2025.pdf)</td>
<td>Monthly arrivals and overnight stays by federal state and origin country. Vienna passed 20 million nights in 2025 (+6.5%), and about 74% of all nights were foreign guests (Germany, Netherlands, Switzerland). Long series are available in STATcube.</td>
<td>Data source for a SARIMA lab on Vienna nights by origin market, including the COVID intervention (2020-2021). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Forecasting the Evolving Composition of Inbound Tourism Demand: A Bayesian Compositional Time Series Approach Using Platform Booking Data</td>
<td>Harrison Katz (Airbnb); arXiv 2602.18358, 2026, preprint</td>
<td>[https://arxiv.org/abs/2602.18358](https://arxiv.org/abs/2602.18358)</td>
<td>Forecasts guest-origin-market shares for four destination regions with BDARMA on Airbnb data from 2017 to 2025. Benchmarks are naive, ETS and SARIMA on log-ratios. It shows pandemic breaks with uneven recovery by market; about 27% lower error than naive for EMEA. Proprietary data.</td>
<td>Advanced example of forecasting country-of-origin mix, a core international-marketing question; students replicate the idea with Statistik Austria nights by origin. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Deep Learning based Forecasting: a case study from the online fashion industry (Zalando)</td>
<td>Manuel Kunz, Stefan Birr, Tim Januschowski et al. (Zalando); arXiv 2305.14406, 2023, preprint</td>
<td>[https://arxiv.org/abs/2305.14406](https://arxiv.org/abs/2305.14406)</td>
<td>Zalando's global, transformer-based demand forecasting for a fashion catalogue with high turnover. It stresses price-demand control under a fixed-inventory assumption. Zalando operates in about 25 European markets. Related 2026 paper: transformer for regular weeks, LightGBM for sales events.</td>
<td>Discussion: why European e-commerce leaders move from per-series ARIMA to global models, and what ARIMA still offers (interpretability, baselines). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>SPAR Österreich: KI-Prognose für Obst und Gemüse gegen Lebensmittelverschwendung</td>
<td>Trending Topics (news), 25 Aug 2022; SPAR Österreich with Microsoft</td>
<td>[https://www.trendingtopics.eu/spar-will-lebensmittelverschwendung-mit-ki-bekaempfen/](https://www.trendingtopics.eu/spar-will-lebensmittelverschwendung-mit-ki-bekaempfen/)</td>
<td>SPAR forecasts per-store order quantities for over 1,500 stores using sales, weather, promotions, marketing campaigns and seasonality. It claims over 90% accuracy (company figure, unverified). It builds on SPAR's long-running automatic ordering system.</td>
<td>Austrian warm-up example for regressors in demand forecasts (weather, promotions); possible guest speaker from SPAR ICS. Free (German).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Coca-Cola Europacific Partners: Predicting the weather's impact on demand</td>
<td>Smith Institute, case study (consultancy), ongoing since 2018</td>
<td>[https://www.smithinst.co.uk/case-studies/predicting-the-weathers-impact-on-demand/](https://www.smithinst.co.uk/case-studies/predicting-the-weathers-impact-on-demand/)</td>
<td>For CCEP across 31 countries in Europe, Oceania and Southeast Asia, ML models separate weather and public-holiday effects from underlying sales. Weekly weather-based forecasts are used to time marketing and promotions. No quantified results are given (placeholders on the page).</td>
<td>Example of regression with weather and holiday covariates across countries; students build temperature-adjusted beverage sales models. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Unilever demand sensing with Terra Technology (vendor case study)</td>
<td>IoT ONE case-study listing, based on Terra Technology (now E2open) material, vendor case</td>
<td>[https://iotone.com/case-study/unilever-s-demand-sensing-and-inventory-optimisation-with-terra-technology/c17876](https://iotone.com/case-study/unilever-s-demand-sensing-and-inventory-optimisation-with-terra-technology/c17876)</td>
<td>Reports that 7-day MAPE improved by 22% and European inventory fell by 35% with short-term demand sensing. P&G reported over 50% lower short-horizon error with the same vendor. These are vendor claims without baselines, so treat them critically.</td>
<td>Critical-reading exercise: what counts as forecast improvement (horizon, baseline, metric)? Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Predicting the Present with Google Trends</td>
<td>Hyunyoung Choi, Hal Varian; Google Research blog 2009; Economic Record 88 (special issue), 2012</td>
<td>[https://www.research.google/blog/predicting-the-present-with-google-trends/](https://www.research.google/blog/predicting-the-present-with-google-trends/)</td>
<td>Seasonal AR models of auto sales, home sales, retail sales and travel (Hong Kong visitor arrivals by origin country) improve when Google Trends categories are added. A replication by Coupé (Economics E-Journal 2018) exists.</td>
<td>Replicate: an AR(1) plus Google Trends nowcast for car registrations or retail sales in Austria or another country; compare out-of-sample MAE. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>OECD Weekly Tracker of Economic Activity (Google Trends nowcast, 46 countries)</td>
<td>Nicolas Woloszko, OECD Economics Department Working Paper No. 1634 (2020), OECD data tool</td>
<td>[https://search.oecd.org/economy/weekly-tracker-of-gdp-growth](https://search.oecd.org/economy/weekly-tracker-of-gdp-growth)</td>
<td>A machine-learning nowcast of weekly GDP growth for 46 OECD and G20 countries from Google Trends (consumption, labour, housing, trade, uncertainty), designed for rapid shocks such as COVID. Publication is currently paused for revision.</td>
<td>Cross-country example of search-data nowcasting; discuss comparability of Google Trends across languages. Free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Google COVID-19 Community Mobility Reports (via Our World in Data)</td>
<td>Google (2020-2022), processed by Our World in Data, data visualisation and download</td>
<td>[https://ourworldindata.org/grapher/change-visitors-retail-recreation](https://ourworldindata.org/grapher/change-visitors-retail-recreation)</td>
<td>Daily percentage change in visits to retail and recreation, grocery and other places versus a Jan-Feb 2020 baseline, by country. CSV, API and R/Python/Stata code are offered. Google stopped updating in October 2022.</td>
<td>Use as an exogenous COVID-shock regressor in a country-level retail or tourism ARIMAX (for example Austria vs Italy vs Sweden). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>IMF World Economic Outlook Oct 2015, Ch. 3: Exchange Rates and Trade Flows: Disconnected?</td>
<td>IMF Research Department (lead Daniel Leigh), World Economic Outlook chapter, 2015</td>
<td>[https://www.tralac.org/images/docs/8182/weo2015-chapter-3-exchange-rates-and-trade-flows-october-2015.pdf](https://www.tralac.org/images/docs/8182/weo2015-chapter-3-exchange-rates-and-trade-flows-october-2015.pdf)</td>
<td>Over 50 economies across about three decades: a 10% real effective depreciation raises net exports by about 1.5% of GDP on average, mostly within a year. Global value chains weaken the effect only for intermediates. This is a third-party copy; the original is on imf.org.</td>
<td>Example of distributed-lag time series regression; students estimate the lagged effect of EUR/USD on Austrian exports to the US (Statistik Austria, ECB data). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>The Role of National Culture in Advertising's Sensitivity to Business Cycles: An Investigation Across Continents</td>
<td>Barbara Deleersnyder, Marnik Dekimpe, Jan-Benedict Steenkamp, Peter Leeflang; Journal of Marketing Research 46(5), 2009; ERIM working paper ERS-2007-095-MKT</td>
<td>[https://repub.eur.nl/pub/10890](https://repub.eur.nl/pub/10890)</td>
<td>Ad spending in 37 countries across four media over up to 25 years. It is more volatile than GDP (co-movement elasticity about 1.4) and more cyclical where uncertainty avoidance is high and long-term orientation low. It uses time series filtering of ad spending.</td>
<td>International marketing discussion: replicate a simple version with ad-spend and GDP series for a few countries (filter, then regress cyclical components). Working paper free; JMR via WU-Lizenz.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Software (27)
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
<td>statsmodels (tsa: ARIMA, SARIMAX, VAR, VECM, UnobservedComponents)</td>
<td>statsmodels developers, PyPI/GitHub, v0.15.0, BSD-3-Clause, 2026, package</td>
<td>[https://www.statsmodels.org/stable/tsa.html](https://www.statsmodels.org/stable/tsa.html)</td>
<td>Core Python library for the course: SARIMAX (ARIMAX with exogenous regressors such as advertising or price), adfuller/kpss unit-root tests, VAR with irf() and fevd(), VECM with Johansen select_coint_rank, UnobservedComponents (structural time series), ETSModel, grangercausalitytests, STL/MSTL. Many example notebooks in the docs.</td>
<td>Main Python lab tool (pip install statsmodels, no friction in Colab/Anaconda). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pmdarima (auto_arima)</td>
<td>alkaline-ml, PyPI, v2.1.1, MIT, 2025, package</td>
<td>[https://alkaline-ml.com/pmdarima/](https://alkaline-ml.com/pmdarima/)</td>
<td>Python port of R auto.arima: stepwise order selection, seasonal differencing tests (OCSB/CH), pipelines with Fourier and Box-Cox transformers. Wraps statsmodels SARIMAX.</td>
<td>Quick demo of automatic order selection vs. manual Box-Jenkins identification. Check wheel availability for the newest Python/numpy before the semester. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>StatsForecast (Nixtla)</td>
<td>Nixtla, PyPI/GitHub, v2.1.1, Apache-2.0, 2025, package</td>
<td>[https://nixtlaverse.nixtla.io/statsforecast/](https://nixtlaverse.nixtla.io/statsforecast/)</td>
<td>Very fast AutoARIMA, AutoETS, AutoTheta, MSTL, CrostonOptimized for thousands of series (numba). Long-format data (unique_id, ds, y) suits multi-country or multi-SKU panels; integrates with M4/M5 loaders (datasetsforecast).</td>
<td>Lab on forecasting many country-level series at once and benchmarking vs. naive/seasonal naive. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>sktime</td>
<td>sktime community, PyPI/GitHub, v1.2.0, BSD-3-Clause, 2026, package</td>
<td>[https://www.sktime.net/](https://www.sktime.net/)</td>
<td>Unified scikit-learn-style interface to ARIMA/AutoARIMA, ETS, Theta, Prophet, VAR, reduction to ML; temporal cross-validation (ExpandingWindowSplitter) and forecast evaluation metrics.</td>
<td>Good for teaching proper rolling-origin evaluation and model comparison pipelines. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Darts</td>
<td>Unit8, PyPI/GitHub, v0.48.1, Apache-2.0, 2026, package</td>
<td>[https://unit8co.github.io/darts/](https://unit8co.github.io/darts/)</td>
<td>TimeSeries object with ARIMA, VARIMA, ETS, Prophet, plus regression and deep models (N-BEATS, TFT) with past/future covariates; backtesting utilities and built-in toy datasets (AirPassengers etc.).</td>
<td>Optional advanced lab: classical vs. ML forecasting with marketing covariates. Torch dependency makes the full install heavy; use the lighter u8darts install without torch in class. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Prophet (Python and R)</td>
<td>Meta (Facebook) Core Data Science, PyPI v1.5.0 / CRAN v1.1.7, MIT, 2026, package</td>
<td>[https://facebook.github.io/prophet/](https://facebook.github.io/prophet/)</td>
<td>Additive trend + seasonality + holiday model with extra regressors; country holiday calendars (add_country_holidays) useful for international retail/tourism series.</td>
<td>Contrast with SARIMAX in a lab; discuss its weak accuracy in forecasting benchmarks. cmdstan backend can cause install trouble on Windows; current pip wheels are usually fine. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>NeuralProphet</td>
<td>NeuralProphet team, PyPI, v0.9.0, MIT, 2024, package</td>
<td>[https://neuralprophet.com/](https://neuralprophet.com/)</td>
<td>PyTorch-based Prophet successor with autoregression (AR-Net), lagged and future regressors, events.</td>
<td>Optional demo only; project activity has slowed and Torch install adds friction. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>arch</td>
<td>Kevin Sheppard, PyPI, v8.0.0, NCSA, 2026, package</td>
<td>[https://arch.readthedocs.io/](https://arch.readthedocs.io/)</td>
<td>Unit-root tests (ADF, DF-GLS, Phillips-Perron, KPSS, Zivot-Andrews with structural break), cointegration tests (Engle-Granger, Phillips-Ouliaris), GARCH volatility models, bootstrap.</td>
<td>More complete unit-root and break-robust testing than statsmodels; GARCH for FX/price volatility in international marketing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>linearmodels</td>
<td>Kevin Sheppard, PyPI, v7.1, NCSA, 2025, package</td>
<td>[https://bashtage.github.io/linearmodels/](https://bashtage.github.io/linearmodels/)</td>
<td>Panel regression (fixed/random effects, clustered SEs), IV/2SLS, system estimation. Complements time-series tools for country-by-time panels (e.g. ad spend and sales across markets).</td>
<td>Lab on panel time-series regression across countries; IV for endogenous marketing spend. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>tfcausalimpact (Python CausalImpact port)</td>
<td>Willian Fuks, PyPI/GitHub, v0.0.19, Apache-2.0, package</td>
<td>[https://github.com/WillianFuks/tfcausalimpact](https://github.com/WillianFuks/tfcausalimpact)</td>
<td>Python port of Google CausalImpact using TensorFlow Probability structural time series; pre/post period intervention effect with control series.</td>
<td>Lab: effect of a campaign launch or market entry on sales or search interest. TensorFlow dependency is heavy; pin versions. pycausalimpact (v0.1.1) is an older unmaintained alternative. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>CausalPy</td>
<td>PyMC Labs, PyPI/GitHub, v0.9.0, Apache-2.0, 2026, package</td>
<td>[https://github.com/pymc-labs/CausalPy](https://github.com/pymc-labs/CausalPy)</td>
<td>Bayesian quasi-experimental methods (interrupted time series, synthetic control, difference-in-differences) built on PyMC (v6.3.2). Bridge from intervention analysis to causal inference.</td>
<td>Advanced project option for campaign evaluation with uncertainty. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>PyFlux</td>
<td>Ross Taylor, PyPI, v0.4.15, BSD, 2018, package</td>
<td>[https://pypi.org/project/pyflux/](https://pypi.org/project/pyflux/)</td>
<td>Historic Python library for ARIMA, ARIMAX, GAS and Bayesian time-series models.</td>
<td>Not recommended: unmaintained since 2018 and does not install on current Python; mention only to steer students to statsmodels/PyMC. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>forecast (R)</td>
<td>Rob J Hyndman et al., CRAN, v9.0.2, GPL-3, 2026, package</td>
<td>[https://cran.r-project.org/web/packages/forecast/index.html](https://cran.r-project.org/web/packages/forecast/index.html)</td>
<td>auto.arima, Arima with xreg (regression with ARIMA errors), ets, tbats, checkresiduals, Fourier terms. Reference: Hyndman and Khandakar (2008, JSS).</td>
<td>Classic R lab tool still widely used in theses; fable is the successor for new teaching but forecast is simplest for ts objects. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>fable / feasts / tsibble / fpp3 (tidyverts)</td>
<td>Mitchell O'Hara-Wild, Rob J Hyndman et al., CRAN, fable 0.5.0, feasts 0.5.0, tsibble 1.2.0, fpp3 1.0.3, GPL-3, 2026, package suite</td>
<td>[https://cran.r-project.org/web/packages/fpp3/index.html](https://cran.r-project.org/web/packages/fpp3/index.html)</td>
<td>Tidy time-series workflow: ARIMA(), ETS(), TSLM(), VAR(), dynamic regression with ARIMA errors, unitroot_kpss/ndiffs features, STL decomposition, accuracy(). fpp3 meta-package loads datasets (tourism, aus_retail, global_economy).</td>
<td>Recommended R stack for the course; matches the free textbook Forecasting: Principles and Practice, 3rd ed. install.packages('fpp3'). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>vars (R)</td>
<td>Bernhard Pfaff, CRAN, v1.6-1, GPL-2/3, 2024, package</td>
<td>[https://cran.r-project.org/web/packages/vars/index.html](https://cran.r-project.org/web/packages/vars/index.html)</td>
<td>VAR/SVAR estimation, VARselect lag choice, irf() incl. orthogonalised IRFs, fevd, causality() Granger tests, serial.test; vec2var converts a VECM.</td>
<td>Core lab for persistence modelling of the marketing mix (Dekimpe-Hanssens style IRFs). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>urca (R)</td>
<td>Bernhard Pfaff, CRAN, v1.3-4, GPL-2/3, 2024, package</td>
<td>[https://cran.r-project.org/web/packages/urca/index.html](https://cran.r-project.org/web/packages/urca/index.html)</td>
<td>ur.df, ur.kpss, ur.pp, ur.za (Zivot-Andrews break), ca.jo Johansen cointegration and cajorls VECM.</td>
<td>Unit-root and cointegration lab; pairs with vars. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>tseries (R)</td>
<td>Adrian Trapletti, Kurt Hornik, CRAN, v0.10-63, GPL-2/3, 2026, package</td>
<td>[https://cran.r-project.org/web/packages/tseries/index.html](https://cran.r-project.org/web/packages/tseries/index.html)</td>
<td>adf.test, kpss.test, pp.test, po.test, jarque.bera.test, garch.</td>
<td>Lightweight alternative test functions; easy for students. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>CausalImpact and bsts (R)</td>
<td>Google (Brodersen et al.) / Steven L. Scott, CRAN, CausalImpact 1.4.1 (Apache-2.0, 2025), bsts 0.9.11 (LGPL-2.1, 2025), package</td>
<td>[https://github.com/google/CausalImpact](https://github.com/google/CausalImpact)</td>
<td>Bayesian structural time-series counterfactual for campaign/intervention evaluation with control series; bsts adds spike-and-slab regressor selection and nowcasting with Google Trends.</td>
<td>Lab on measuring campaign or market-entry impact; pair with Google Trends data. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>seasonal (R interface to X-13ARIMA-SEATS)</td>
<td>Christoph Sax, CRAN, v1.11.0, GPL-3, 2026, package; X-13 binary by US Census Bureau (x13binary)</td>
<td>[https://cran.r-project.org/web/packages/seasonal/index.html](https://cran.r-project.org/web/packages/seasonal/index.html)</td>
<td>seas() runs X-13ARIMA-SEATS with automatic outlier, trading-day and Easter detection; view() Shiny interface. Python access via statsmodels x13_arima_analysis (needs the X-13 binary from census.gov).</td>
<td>Seasonal adjustment demo for retail/tourism series; explain why official statistics use X-13/TRAMO-SEATS. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>JDemetra+ 3.x (with RJDemetra / rjd3 R packages)</td>
<td>Eurostat / National Bank of Belgium, GitHub, v3.9.0, EUPL-1.2, 2026, app + R packages (RJDemetra 0.2.8, rjd3x13 3.9.0)</td>
<td>[https://github.com/jdemetra/jdplus-main/releases](https://github.com/jdemetra/jdplus-main/releases)</td>
<td>Official ESS-recommended seasonal adjustment software (X-13 and TRAMO-SEATS) with national calendar regressors; used by Eurostat and national statistical offices. Docs: [https://jdemetra-new-documentation.netlify.app/](https://jdemetra-new-documentation.netlify.app/)</td>
<td>Show how official statistics seasonally adjust the data students download. Requires Java 17+; rjd3 R packages need rJava. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>gretl</td>
<td>Allin Cottrell, Riccardo Lucchetti, SourceForge, 2026c, GPL, 2026, app</td>
<td>[https://gretl.sourceforge.net/](https://gretl.sourceforge.net/)</td>
<td>Free GUI econometrics: ARIMA/ARMAX, unit-root tests, VAR/VECM with IRFs, Johansen, Chow/QLR break tests, X-13/TRAMO plugins; German localisation and many textbook datasets.</td>
<td>Low-friction GUI option for students without coding background; good for replicating textbook examples. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>EViews</td>
<td>S&P Global, EViews 14, proprietary, app</td>
<td>[https://www.eviews.com/home.html](https://www.eviews.com/home.html)</td>
<td>Menu-driven time-series econometrics: ARIMA, VAR/VECM, SVAR, unit-root and break tests, X-13, state space. Common in applied marketing/economics papers.</td>
<td>Optional; full student version is paid (a limited Student Lite version exists). WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Stata time-series suite (tsset, arima, var, vec, dfuller)</td>
<td>StataCorp, Stata 19, proprietary, 2025, app</td>
<td>[https://www.stata.com/features/time-series/](https://www.stata.com/features/time-series/)</td>
<td>tsset, arima with covariates, var/svar, irf, vec/vecrank, dfuller/dfgls, estat sbsingle structural breaks, forecast commands.</td>
<td>Use if students already know Stata. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>IBM SPSS Statistics Forecasting module</td>
<td>IBM, proprietary, app</td>
<td>[https://www.ibm.com/products/spss-statistics](https://www.ibm.com/products/spss-statistics)</td>
<td>Expert Modeler (automatic ARIMA/exponential smoothing), ARIMA with predictors and transfer functions, intervention outliers, seasonal decomposition.</td>
<td>Familiar to many marketing students; menu-based ARIMA demo. Forecasting is an add-on module. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Microsoft Excel (FORECAST.ETS, Forecast Sheet, Analysis ToolPak)</td>
<td>Microsoft, Microsoft 365, proprietary, app</td>
<td>[https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41](https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41)</td>
<td>FORECAST.ETS implements AAA exponential smoothing with seasonality detection; ToolPak regression for lagged-advertising models. No ARIMA.</td>
<td>Warm-up session: practitioners' forecasting baseline before ARIMA, and its limits. Via Microsoft 365; WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>modeltime (R)</td>
<td>Matt Dancho, CRAN, v1.3.5, MIT, 2026, package</td>
<td>[https://cran.r-project.org/web/packages/modeltime/index.html](https://cran.r-project.org/web/packages/modeltime/index.html)</td>
<td>tidymodels-style framework: arima_reg, prophet_reg, exp_smoothing and ML models with calibration and refit workflows.</td>
<td>Optional alternative to fable for students using tidymodels. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>strucchange and dynlm (R)</td>
<td>Zeileis et al., CRAN, strucchange 1.6-0 (2026), dynlm 0.3-6 (2019), GPL-2/3, package</td>
<td>[https://cran.r-project.org/web/packages/strucchange/index.html](https://cran.r-project.org/web/packages/strucchange/index.html)</td>
<td>strucchange: Chow, CUSUM/MOSUM, Bai-Perron breakpoints(); dynlm: time-series regression with L() lags and d() differences, e.g. Koyck/distributed-lag advertising models.</td>
<td>Lab on structural breaks (e.g. COVID, regulatory change) and distributed-lag ad-response models. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Data (26)
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
<td>Eurostat database (incl. R package eurostat)</td>
<td>Eurostat (European Commission), portal, open data (reuse with attribution), continuously updated; R package eurostat v4.1.1 (BSD-2)</td>
<td>[https://ec.europa.eu/eurostat/web/main/data/database](https://ec.europa.eu/eurostat/web/main/data/database)</td>
<td>EU-27 + EFTA + candidate countries; monthly/quarterly series. Key tables: retail trade volume (sts_trtu_m), HICP (prc_hicp_midx), tourism nights (tour_occ_nim), international trade (Comext), consumer confidence (ei_bsco_m). SDMX API; Python via the eurostat or sdmx1 packages.</td>
<td>Main project data source for cross-country ARIMA/VAR work. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat Short-term business statistics: retail trade</td>
<td>Eurostat, dataset collection, open data, monthly</td>
<td>[https://ec.europa.eu/eurostat/web/short-term-business-statistics/database](https://ec.europa.eu/eurostat/web/short-term-business-statistics/database)</td>
<td>Monthly retail trade turnover/volume indices by NACE (food, non-food, mail order and internet) for EU countries, mostly from 2000; unadjusted, calendar-adjusted and seasonally adjusted versions.</td>
<td>Ideal lab series: SARIMA on unadjusted vs. adjusted data, cross-country comparison of e-commerce growth. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat Tourism database</td>
<td>Eurostat, dataset collection, open data, monthly/annual</td>
<td>[https://ec.europa.eu/eurostat/web/tourism/database](https://ec.europa.eu/eurostat/web/tourism/database)</td>
<td>Nights spent and arrivals at tourist accommodation by country of residence, monthly, also NUTS regions; strong seasonality and COVID-19 intervention.</td>
<td>Intervention analysis (COVID-19) and seasonal ARIMA lab for international tourism marketing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat HICP database</td>
<td>Eurostat, dataset collection, open data, monthly</td>
<td>[https://ec.europa.eu/eurostat/web/hicp/database](https://ec.europa.eu/eurostat/web/hicp/database)</td>
<td>Harmonised consumer price indices by COICOP category and country since 1996.</td>
<td>Price series for deflating sales and for VAR models of price and demand. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>OECD Data Explorer (MEI, consumer and business confidence, CPI, trade)</td>
<td>OECD, portal (SDMX API), CC BY 4.0, continuously updated</td>
<td>[https://data-explorer.oecd.org/](https://data-explorer.oecd.org/)</td>
<td>38 OECD members + partners; monthly Main Economic Indicators, consumer confidence indicator (CCI), business confidence, retail trade, CPI, composite leading indicators. OECD.Stat was replaced in 2024; the R package OECD (0.2.5, 2021) targets the old API, use rsdmx or readsdmx instead.</td>
<td>Exogenous regressors (consumer confidence) in ARIMAX models of country sales. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>World Bank World Development Indicators</td>
<td>World Bank, DataBank portal + API, CC BY 4.0, annual; R package WDI v2.8.0</td>
<td>[https://databank.worldbank.org/source/world-development-indicators](https://databank.worldbank.org/source/world-development-indicators)</td>
<td>About 1,400 indicators for over 200 economies, annual from 1960 (GDP, internet use, trade share, tourism receipts). A subset is in fpp3 as global_economy.</td>
<td>Annual macro controls for international market-selection or diffusion projects; short annual series limit ARIMA use. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>IMF Data (IFS, Direction of Trade Statistics)</td>
<td>International Monetary Fund, portal + SDMX API, free (IMF terms), monthly/quarterly/annual</td>
<td>[https://data.imf.org/](https://data.imf.org/)</td>
<td>International Financial Statistics (exchange rates, prices, interest rates) and DOTS bilateral merchandise trade for about 190 countries. The portal was relaunched in 2025 and dataset URLs changed; the page refused automated access here.</td>
<td>Exchange-rate and bilateral export series for VAR/cointegration labs (e.g. exchange-rate pass-through to exports). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>UN Comtrade (Comtrade Plus)</td>
<td>United Nations Statistics Division, portal + API, free tier with registration, monthly/annual; R package comtradr v1.0.6</td>
<td>[https://comtradeplus.un.org/](https://comtradeplus.un.org/)</td>
<td>Bilateral trade by HS product code for about 200 reporters, annual since 1962 and monthly since 2010. Free API key needed; call limits apply.</td>
<td>Product-level export series for international marketing projects (e.g. Austrian wine exports by destination). Free with login.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>FRED (Federal Reserve Economic Data)</td>
<td>Federal Reserve Bank of St. Louis, portal + API, free (some series copyrighted by original sources), daily to annual; R fredr v2.1.0, Python fredapi / pandas-datareader</td>
<td>[https://fred.stlouisfed.org/](https://fred.stlouisfed.org/)</td>
<td>Over 800,000 US and international series, incl. US retail sales (RSXFS), consumer sentiment, exchange rates and OECD MEI mirrors.</td>
<td>Easiest API for first labs; quick retail sales downloads for SARIMA. Free (API key). Page timed out during check.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>STATcube (Statistik Austria)</td>
<td>Statistik Austria, portal, free basic access (registration for full features), monthly/annual; R package STATcubeR v1.0.1 (2026)</td>
<td>[https://www.statistik.at/datenbanken/statcube-statistische-datenbank](https://www.statistik.at/datenbanken/statcube-statistische-datenbank)</td>
<td>Austrian official statistics: tourism overnight stays by country of origin and municipality (monthly), foreign trade, retail trade, CPI. Open-data subset via data.statistik.gv.at; interface in German and English.</td>
<td>Local Austrian project data (e.g. Vienna overnight stays by source market) for SARIMA and intervention models. Free / login.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>WIFO data</td>
<td>Österreichisches Institut für Wirtschaftsforschung (WIFO), portal, partly free, partly members/licence</td>
<td>[https://www.wifo.ac.at/daten/](https://www.wifo.ac.at/daten/)</td>
<td>Austrian business-cycle indicators (WIFO-Konjunkturtest), forecasts and macro time series; information on access to register data via the Austrian Micro Data Center.</td>
<td>Background macro series for Austrian projects; check which series are free. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Google Trends</td>
<td>Google, web tool, free, weekly/monthly (daily for short windows), normalised 0-100; R gtrendsR v1.5.2, Python pytrends (unofficial)</td>
<td>[https://trends.google.com/trends/](https://trends.google.com/trends/)</td>
<td>Search interest by country and region since 2004; proxy for brand/category interest across markets. Values are sampled and rescaled per query, so downloads differ between pulls; unofficial APIs are rate-limited.</td>
<td>Lab: nowcasting sales with search data, CausalImpact on campaign launches, cross-country brand interest. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>UN Tourism (UNWTO) Tourism Data Dashboard</td>
<td>UN Tourism (formerly UNWTO), dashboard, free (detailed statistics partly paid via e-library), monthly/annual</td>
<td>[https://www.unwto.org/tourism-data/global-and-regional-tourism-performance](https://www.unwto.org/tourism-data/global-and-regional-tourism-performance)</td>
<td>International tourist arrivals and receipts by region and country, post-COVID recovery tracker.</td>
<td>Context data and annual series for international tourism marketing; monthly country detail is limited. Free / paid.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>M4 Competition dataset</td>
<td>Makridakis, Spiliotis, Assimakopoulos, GitHub, open, 2018, dataset (100,000 series)</td>
<td>[https://github.com/Mcompetitions/M4-methods](https://github.com/Mcompetitions/M4-methods)</td>
<td>100,000 yearly to hourly series (micro, macro, industry, finance, demographic) with benchmark forecasts. Paper: [https://doi.org/10.1016/j.ijforecast.2019.04.014](https://doi.org/10.1016/j.ijforecast.2019.04.014). Loaders in datasetsforecast (Python).</td>
<td>Benchmark exercise: students compare their ARIMA against published M4 benchmarks. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>M5 Forecasting (Walmart hierarchical sales)</td>
<td>University of Nicosia / Walmart, Kaggle, competition data, 2020, dataset</td>
<td>[https://www.kaggle.com/competitions/m5-forecasting-accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy)</td>
<td>42,840 daily hierarchical unit-sales series (3,049 products, 10 stores, 3 US states) with prices, SNAP days and event calendar, 2011-2016. Paper: [https://doi.org/10.1016/j.ijforecast.2021.11.013](https://doi.org/10.1016/j.ijforecast.2021.11.013).</td>
<td>Project data for price/promotion regressors and hierarchical forecasting; large download. Free with Kaggle login, competition rules apply.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Tourism Forecasting Competition data (Tcomp)</td>
<td>Athanasopoulos, Hyndman, Song, Wu; Kaggle / CRAN Tcomp v1.0.1, GPL-3, 2011, dataset</td>
<td>[https://www.kaggle.com/competitions/tourism1](https://www.kaggle.com/competitions/tourism1)</td>
<td>1,311 monthly, quarterly and annual tourism series (arrivals, nights) from many countries; paper [https://doi.org/10.1016/j.ijforecast.2010.04.009](https://doi.org/10.1016/j.ijforecast.2010.04.009). Easiest access: install.packages('Tcomp').</td>
<td>Ready-made international tourism series for SARIMA vs. ETS benchmarking. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>fpp3 / tsibbledata datasets (tourism, aus_retail, global_economy, aus_arrivals)</td>
<td>Hyndman et al., CRAN tsibbledata v0.4.1 / fpp3 v1.0.3, GPL-3, dataset</td>
<td>[https://cran.r-project.org/web/packages/tsibbledata/index.html](https://cran.r-project.org/web/packages/tsibbledata/index.html)</td>
<td>tourism: quarterly Australian domestic overnight trips by region and purpose (304 series); aus_retail: monthly retail turnover by state and industry (152 series); global_economy: annual data for about 260 countries; aus_arrivals: quarterly arrivals from Japan, NZ, UK, US. Textbook: [https://otexts.com/fpp3/](https://otexts.com/fpp3/)</td>
<td>Zero-friction lab data matching textbook exercises; Python users can export to CSV. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Rossmann Store Sales</td>
<td>Rossmann (Germany), Kaggle competition data, 2015, dataset</td>
<td>[https://www.kaggle.com/c/rossmann-store-sales](https://www.kaggle.com/c/rossmann-store-sales)</td>
<td>Daily sales for 1,115 German Rossmann stores 2013-2015 with promotion, school/state holiday and competitor-distance variables.</td>
<td>German retail case for ARIMAX with promotion dummies and holiday effects. Free with Kaggle login; competition rules apply.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Walmart Recruiting Store Sales Forecasting</td>
<td>Walmart, Kaggle competition data, 2014, dataset</td>
<td>[https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)</td>
<td>Weekly sales for 45 stores by department 2010-2012 with markdowns (promotions), CPI, fuel price, unemployment and holiday weeks.</td>
<td>Small, tidy dataset for regression with ARIMA errors and markdown effects. Free with Kaggle login.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Corporación Favorita Grocery Sales Forecasting</td>
<td>Corporación Favorita (Ecuador), Kaggle competition data, 2017, dataset</td>
<td>[https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting)</td>
<td>Daily unit sales for about 4,000 items in 54 stores 2013-2017 with promotions, oil price and holidays; very large (over 100 million rows). Smaller sibling: Kaggle 'Store Sales - Time Series Forecasting'.</td>
<td>Emerging-market retail case; aggregate to store/family level for class use. Free with Kaggle login.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Online Retail II (UCI)</td>
<td>Daqing Chen, UCI Machine Learning Repository, CC BY 4.0, 2019, dataset</td>
<td>[https://archive.ics.uci.edu/dataset/502/online+retail+ii](https://archive.ics.uci.edu/dataset/502/online+retail+ii)</td>
<td>About 1.07 million transactions of a UK online gift retailer 2009-2011 with customer country (about 40 countries).</td>
<td>Aggregate to daily/weekly sales by country for an international e-commerce SARIMA lab. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Dominick's Finer Foods dataset</td>
<td>James M. Kilts Center, University of Chicago Booth, free for academic research, 1989-1997, dataset</td>
<td>[https://www.chicagobooth.edu/research/kilts/research-data/dominicks](https://www.chicagobooth.edu/research/kilts/research-data/dominicks)</td>
<td>Weekly store-level scanner data for about 100 Chicago stores and over 25 categories with prices, deals and store traffic. Classic data for price-promotion time-series studies.</td>
<td>Free classic marketing data for VAR/persistence modelling of promotions. Free download after accepting terms.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>NielsenIQ Retail Scanner and Consumer Panel (Kilts Center)</td>
<td>Kilts Center, Chicago Booth, institutional subscription, 2006-present, dataset</td>
<td>[https://www.chicagobooth.edu/research/kilts/research-data/nielseniq](https://www.chicagobooth.edu/research/kilts/research-data/nielseniq)</td>
<td>Weekly UPC-by-store data for tens of thousands of US stores and a large household panel; Nielsen Ad Intel advertising data also available.</td>
<td>Thesis/research option only; requires institutional subscription. WU-Lizenz prüfen (probably not licensed).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>IRI Marketing Data Set (now Circana)</td>
<td>Bronnenberg, Kruger, Mela (2008), Marketing Science database paper; IRI now Circana, dataset</td>
<td>[https://doi.org/10.1287/mksc.1080.0450](https://doi.org/10.1287/mksc.1080.0450)</td>
<td>Weekly store and household panel data for 30 categories in 47 US markets from 2001, distributed to academics under licence.</td>
<td>Research-grade scanner data for persistence/VAR projects; access by application and fee. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Data</td>
<td>Statista</td>
<td>Statista GmbH, portal, commercial</td>
<td>[https://www.statista.com/](https://www.statista.com/)</td>
<td>Market data, consumer surveys, advertising spend and e-commerce statistics by country; many series are annual and from secondary sources.</td>
<td>Quick context figures; check original sources before modelling. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>WU Bibliothek Datenbanken (e.g. Euromonitor Passport, LSEG, Statista)</td>
<td>WU Vienna University Library, database portal</td>
<td>[https://www.wu.ac.at/bibliothek/recherche/datenbanken](https://www.wu.ac.at/bibliothek/recherche/datenbanken)</td>
<td>Entry point to WU-licensed databases with market and macro time series (e.g. country-by-category sales, financial and macro data where licensed).</td>
<td>Check which licensed databases contain category sales by country for student projects. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Statistische Methoden (12)
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
<td>ARIMA / SARIMA and automatic order selection</td>
<td>Hyndman and Khandakar (2008), Journal of Statistical Software 27(3), method</td>
<td>[https://doi.org/10.18637/jss.v027.i03](https://doi.org/10.18637/jss.v027.i03)</td>
<td>Box-Jenkins identification, estimation and diagnostics; auto.arima algorithm. Pair with Box, Jenkins, Reinsel, Ljung (2015), Time Series Analysis, 5th ed., Wiley.</td>
<td>Lecture plus lab: manual ACF/PACF identification vs. auto.arima/pmdarima on a retail series. Open access.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Unit-root tests (ADF) and stationarity tests (KPSS)</td>
<td>Dickey and Fuller (1979), JASA 74(366); Kwiatkowski, Phillips, Schmidt, Shin (1992), Journal of Econometrics 54, method</td>
<td>[https://doi.org/10.1080/01621459.1979.10482531](https://doi.org/10.1080/01621459.1979.10482531)</td>
<td>ADF tests the unit-root null, KPSS the stationarity null; use both to decide on differencing and on evolving vs. stationary sales (KPSS: [https://doi.org/10.1016/0304-4076(92](https://doi.org/10.1016/0304-4076(92))90104-Y).</td>
<td>Lab on whether brand sales are evolving or stationary across countries. Paywalled; WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Intervention analysis</td>
<td>Box and Tiao (1975), JASA 70(349), method</td>
<td>[https://doi.org/10.1080/01621459.1975.10480264](https://doi.org/10.1080/01621459.1975.10480264)</td>
<td>Pulse, step and ramp interventions in ARIMA models; basis for evaluating campaigns, regulation or COVID shocks.</td>
<td>Lab: Austrian tourism nights with COVID step/pulse dummies. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Bayesian structural time series / CausalImpact</td>
<td>Brodersen, Gallusser, Koehler, Remy, Scott (2015), Annals of Applied Statistics 9(1), method</td>
<td>[https://doi.org/10.1214/14-AOAS788](https://doi.org/10.1214/14-AOAS788)</td>
<td>Counterfactual prediction from control series to estimate the causal effect of a marketing intervention; implemented in CausalImpact (R) and tfcausalimpact (Python).</td>
<td>Lab on campaign evaluation with Google Trends controls. Free preprint on arXiv.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>VAR models and impulse response functions</td>
<td>Sims (1980), Econometrica 48(1); Pesaran and Shin (1998), generalized IRF, Economics Letters 58, method</td>
<td>[https://doi.org/10.2307/1912017](https://doi.org/10.2307/1912017)</td>
<td>VAR treats marketing mix and sales as jointly endogenous; generalized IRFs ([https://doi.org/10.1016/S0165-1765(97](https://doi.org/10.1016/S0165-1765(97))00214-0) avoid the ordering dependence and are standard in marketing persistence studies.</td>
<td>Lab with vars/statsmodels: IRF of sales to an advertising shock. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Cointegration and VECM</td>
<td>Engle and Granger (1987), Econometrica 55(2); Johansen (1988), Journal of Economic Dynamics and Control 12, method</td>
<td>[https://doi.org/10.2307/1913236](https://doi.org/10.2307/1913236)</td>
<td>Long-run equilibrium between evolving series (e.g. exports and exchange rates, sales and distribution); Johansen trace test: [https://doi.org/10.1016/0165-1889(88](https://doi.org/10.1016/0165-1889(88))90041-3.</td>
<td>Lab with urca::ca.jo or statsmodels VECM. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Granger causality</td>
<td>Granger (1969), Econometrica 37(3), method</td>
<td>[https://doi.org/10.2307/1912791](https://doi.org/10.2307/1912791)</td>
<td>Predictive causality tests in VARs; use the Toda-Yamamoto version with non-stationary data.</td>
<td>Discussion of what Granger causality does and does not show for advertising-sales relationships. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Persistence modelling in marketing</td>
<td>Dekimpe and Hanssens (1995), Marketing Science 14(1); Dekimpe and Hanssens (2000), IJRM 17(2-3), method</td>
<td>[https://doi.org/10.1287/mksc.14.1.1](https://doi.org/10.1287/mksc.14.1.1)</td>
<td>Unit roots plus VAR/VECM IRFs to separate short-run from permanent marketing effects; the 2000 review ([https://doi.org/10.1016/S0167-8116(00](https://doi.org/10.1016/S0167-8116(00))00014-8) is the best teaching overview.</td>
<td>Core marketing reading for the VAR session. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Distributed lags / Koyck advertising carryover</td>
<td>Clarke (1976), Journal of Marketing Research 13(4), method</td>
<td>[https://doi.org/10.2307/3151017](https://doi.org/10.2307/3151017)</td>
<td>Meta-analysis of advertising duration from Koyck geometric-lag models; data-interval bias in carryover estimates. Koyck (1954) is the original model.</td>
<td>Lab: estimate a Koyck/adstock model with dynlm or statsmodels and derive the long-run effect. WU-Lizenz prüfen.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>ETS / exponential smoothing in state-space form</td>
<td>Hyndman, Koehler, Snyder, Grose (2002), International Journal of Forecasting 18(3), method</td>
<td>[https://doi.org/10.1016/S0169-2070(01](https://doi.org/10.1016/S0169-2070(01)</td>
<td>Innovations state-space framework behind ETS(), AutoETS and Excel FORECAST.ETS; links to Kalman filtering and structural time series.</td>
<td>Benchmark model against ARIMA in forecasting labs. WU-Lizenz prüfen; fpp3 chapter 8 is free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Structural break tests</td>
<td>Bai and Perron (2003), Journal of Applied Econometrics 18(1), method</td>
<td>[https://doi.org/10.1002/jae.659](https://doi.org/10.1002/jae.659)</td>
<td>Multiple unknown breakpoints in regression; implemented in strucchange::breakpoints; Zivot-Andrews unit-root test with a break in arch/urca.</td>
<td>Lab: detect breaks in brand sales after a market entry or crisis. WU-Lizenz prüfen.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Statistische Methoden</td>
<td>Forecast evaluation with competition benchmarks</td>
<td>Makridakis, Spiliotis, Assimakopoulos (2020), International Journal of Forecasting 36(1) (M4), method</td>
<td>[https://doi.org/10.1016/j.ijforecast.2019.04.014](https://doi.org/10.1016/j.ijforecast.2019.04.014)</td>
<td>Shows simple statistical methods and combinations remain hard to beat; defines sMAPE/MASE/OWA metrics used in labs.</td>
<td>Reading for the forecast-evaluation session. Open access.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Communities & Events (13)
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
<td>International Institute of Forecasters (IIF)</td>
<td>Non-profit professional society founded 1982; Global</td>
<td>[https://forecasters.org/](https://forecasters.org/)</td>
<td>Publishes International Journal of Forecasting and Foresight; runs the ISF, webinars and awards incl. student awards.</td>
<td>Students can join as members via the Join the IIF page; follow webinars and blog.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>International Symposium on Forecasting (ISF) 2027</td>
<td>IIF annual conference, 20-23 June 2027, Paphos, Cyprus; Global</td>
<td>[https://forecasters.org/events/symposium-on-forecasting](https://forecasters.org/events/symposium-on-forecasting)</td>
<td>Leading forecasting conference with academic and practitioner tracks (retail, marketing, ML vs. statistical models) and tool workshops.</td>
<td>Thesis students can submit or attend; recorded keynotes for class.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Foresight: The International Journal of Applied Forecasting</td>
<td>IIF practitioner journal; Global</td>
<td>[https://forecasters.org/foresight/](https://forecasters.org/foresight/)</td>
<td>Short practitioner articles on demand forecasting, forecast accuracy and S&OP.</td>
<td>Assign selected articles as practitioner readings; access via IIF membership or library.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>ISMS Marketing Science Conference 2027</td>
<td>INFORMS Society for Marketing Science, 24-26 June 2027, Seattle (doctoral consortium 23 June); Global</td>
<td>[https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2027-ISMS-Marketing-Science-Conference](https://www.informs.org/Meetings-Conferences/INFORMS-Conference-Calendar/2027-ISMS-Marketing-Science-Conference)</td>
<td>Main venue for quantitative marketing incl. time-series marketing-mix and persistence models.</td>
<td>Advanced students can attend; programme useful to find current research and speakers.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>EMAC - European Marketing Academy</td>
<td>European marketing academic society; annual conference (2026 Bath) plus fall conference (2026 Bremen); Europe</td>
<td>[https://emac-online.org/](https://emac-online.org/)</td>
<td>Marketing modeling and international marketing tracks; publishes IJRM.</td>
<td>Student and doctoral membership; proceedings as source of European time-series marketing papers.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna Workshop on Economic Forecasting (IHS)</td>
<td>Institute for Advanced Studies, Vienna; 3rd edition June 2025; Wien</td>
<td>[https://www.ihs.ac.at/events/conference-series/forecasting-workshop/vienna-workshop-on-economic-forecasting-2025](https://www.ihs.ac.at/events/conference-series/forecasting-workshop/vienna-workshop-on-economic-forecasting-2025)</td>
<td>Academic workshop on time-series forecasting, ML and forecast evaluation; IHS also hosts the Vienna Workshop on High-Dimensional Time Series (May 2026).</td>
<td>Watch for the next edition; local networking with Austrian forecasters (IHS, WIFO).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna Data Science Group (VDSG)</td>
<td>Volunteer non-profit data science community since 2015; Wien</td>
<td>[https://www.vdsg.at/](https://www.vdsg.at/)</td>
<td>5,000+ Meetup members and 130+ public events on ML, analytics and applied AI; source of local practitioner speakers.</td>
<td>Students join free via Meetup or become members; can propose talks.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Vienna R User Group (Vienna\<-R) and R-Ladies Vienna</td>
<td>Local R communities; Wien</td>
<td>[https://www.r-bloggers.com/2022/09/financial-industry-supports-robust-vienna-r-community/](https://www.r-bloggers.com/2022/09/financial-industry-supports-robust-vienna-r-community/)</td>
<td>R meetups (founded 2011, hosted at Uni Wien and TU Wien) relevant for fable/forecast/strucchange users; R-Ladies Vienna on Meetup (rladies-vienna).</td>
<td>Students join via Meetup; current activity level should be checked.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Nixtla Community Slack</td>
<td>Open-source time-series community around StatsForecast (AutoARIMA), NeuralForecast and TimeGPT; Global</td>
<td>[https://pypi.org/project/statsforecast/](https://pypi.org/project/statsforecast/)</td>
<td>Python AutoARIMA/ETS at scale; developers answer questions in Slack.</td>
<td>Join via the Slack invite in the Nixtla docs or StatsForecast README (invite links may expire).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Lancaster Centre for Marketing Analytics and Forecasting (CMAF)</td>
<td>Lancaster University research centre; UK/Global</td>
<td>[https://www.lancaster.ac.uk/centre-for-marketing-analytics-and-forecasting/](https://www.lancaster.ac.uk/centre-for-marketing-analytics-and-forecasting/)</td>
<td>Free practitioner workshops and webinars (e.g. retail demand forecasting, hierarchical forecasting for manufacturing).</td>
<td>Students register for free online events.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Forecasting Impact Podcast</td>
<td>Podcast on forecasting practice; Global</td>
<td>[https://forecastingimpact.buzzsprout.com/](https://forecastingimpact.buzzsprout.com/)</td>
<td>Episodes with Kolassa, Athanasopoulos and other forecasters.</td>
<td>Free listening assignments.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>Marketing Science Institute (MSI)</td>
<td>Academic-industry marketing research network; Global</td>
<td>[https://www.msi.org/](https://www.msi.org/)</td>
<td>Webinars (e.g. with Pauwels) and research priorities on marketing measurement and MMM; expert directory.</td>
<td>Free webinars; some content member-only.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Communities & Events</td>
<td>WU Institute for Retailing and Data Science - Praxisdialog</td>
<td>WU Wien event series with retail practitioners; Wien</td>
<td>[https://www.wu.ac.at/fileadmin/wu/d/i/retail/PDF_Dokumente/Praxisdialog/Ank%C3%BCndigungen/Praxisdialog_WS_25_26.pdf](https://www.wu.ac.at/fileadmin/wu/d/i/retail/PDF_Dokumente/Praxisdialog/Ank%C3%BCndigungen/Praxisdialog_WS_25_26.pdf)</td>
<td>Talks by retail managers (e.g. Amazon Austria, Oct 2025); pipeline for Austrian retail and forecasting guest speakers.</td>
<td>Open to WU students; check the semester programme.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### People (24)
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
<td>Marnik Dekimpe</td>
<td>Tilburg University, Research Professor of Marketing; academic; Global</td>
<td>[https://www.tilburguniversity.edu/webwijs/show/m.g.dekimpe.htm](https://www.tilburguniversity.edu/webwijs/show/m.g.dekimpe.htm)</td>
<td>Co-founder of persistence modeling in marketing (unit-root tests, VAR/VECM, impulse responses for long-run marketing effects; Dekimpe and Hanssens 1995/1999). Work on international retailing, emerging markets and business cycles.</td>
<td>Ideal remote guest lecture (EN) on whether marketing effects persist, linking ARIMA/unit roots to managerial questions; strong fit for the international angle.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Dominique Hanssens</td>
<td>UCLA Anderson, Distinguished Research Professor of Marketing; academic; Global</td>
<td>[https://www.anderson.ucla.edu/faculty-and-research/marketing/faculty/hanssens](https://www.anderson.ucla.edu/faculty-and-research/marketing/faculty/hanssens)</td>
<td>Co-author of Market Response Models (Hanssens, Parsons and Schultz), the classic text on time-series marketing models; Long Term Impact of Marketing; Empirical Generalizations about Marketing Impact; Handbook of Marketing Analytics (2nd ed. 2026); former MSI executive director.</td>
<td>Recorded interview or remote Q&A (EN) on long-term marketing ROI and market response modeling; books as reading backbone.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Koen Pauwels</td>
<td>Northeastern University D'Amore-McKim, Distinguished Professor of Marketing (2026 CV: Associate Dean of Research, IJRM Editor-in-Chief 2024-2027); academic/consultant; Global</td>
<td>[https://damore-mckim.northeastern.edu/people/koen-pauwels/](https://damore-mckim.northeastern.edu/people/koen-pauwels/)</td>
<td>VAR/persistence modeling of marketing actions, KPI and dashboard research, co-editor of Advanced Methods for Modeling Markets (Springer); consults on combining attribution with MMM. Previously built Ozyegin University Istanbul (cross-country cases).</td>
<td>Strong guest-speaker fit (EN, remote; frequent speaker at MMA and MSI webinars) on VAR models for brand KPIs and MMM in practice.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Jan-Benedict Steenkamp</td>
<td>UNC Kenan-Flagler, Knox Massey Distinguished Professor of Marketing; academic; Global</td>
<td>[https://www.kenan-flagler.unc.edu/faculty/directory/jan-benedict-steenkamp/](https://www.kenan-flagler.unc.edu/faculty/directory/jan-benedict-steenkamp/)</td>
<td>Global marketing and branding scholar (Global Brand Strategy, 2017); co-author of time-series studies on competitive reactions and private labels across countries; executive chairman of AiMark (international panel data).</td>
<td>Remote lecture (EN) on international brand dynamics; supports the international framing of time-series cases.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Harald van Heerde</td>
<td>UNSW Sydney Business School, SHARP Research Professor of Marketing; academic; Global</td>
<td>[https://www.unsw.edu.au/staff/harald-van-heerde](https://www.unsw.edu.au/staff/harald-van-heerde)</td>
<td>Econometric marketing-mix models incl. dynamic models, time-varying parameters and time series; price wars, product-harm crises, economic cycles; Marketing Science Hub at AiMark.</td>
<td>Remote guest lecture (EN) on dynamic sales-response models; time-zone constraint (Sydney).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Barbara Deleersnyder</td>
<td>Tilburg University, Professor of Marketing; academic; Global</td>
<td>[https://research.tilburguniversity.edu/en/persons/barbara-deleersnyder](https://research.tilburguniversity.edu/en/persons/barbara-deleersnyder)</td>
<td>Time-series work on business cycles and marketing (advertising cyclicality across countries, private labels over the cycle), multi-country studies with Dekimpe and Steenkamp; co-supervises PhD on business cycles and price sensitivity.</td>
<td>Remote session (EN) on international business-cycle effects on marketing spending; multi-country time-series case material.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Shuba Srinivasan</td>
<td>Boston University Questrom, Barron Professor of Marketing; academic; Global</td>
<td>[https://www.bu.edu/questrom/profile/shuba-srinivasan](https://www.bu.edu/questrom/profile/shuba-srinivasan)</td>
<td>Applies time-series econometrics (VAR, persistence) to marketing and firm value; co-author of Marketing and Firm Value (with Hanssens, 2022).</td>
<td>Remote lecture (EN) on the marketing-finance interface with time-series models.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Gerard Tellis</td>
<td>USC Marshall, Neely Chaired Professor of American Enterprise; academic; Global</td>
<td>[https://www.marshall.usc.edu/personnel/gerard-tellis](https://www.marshall.usc.edu/personnel/gerard-tellis)</td>
<td>Advertising effectiveness and new-product growth across countries (global innovation, international takeoff), time-series models of advertising carryover; Distinguished Professor at Erasmus Rotterdam.</td>
<td>Remote talk (EN) on international diffusion and advertising dynamics.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Peter Leeflang</td>
<td>University of Groningen, Professor Emeritus of Marketing; academic; Global</td>
<td>[https://www.rug.nl/staff/p.s.h.leeflang/](https://www.rug.nl/staff/p.s.h.leeflang/)</td>
<td>Co-author/editor of Building Models for Marketing Decisions, Modeling Markets and Advanced Methods for Modeling Markets (Springer, with Wieringa, Bijmolt, Pauwels), standard references for time-series marketing models.</td>
<td>Reading reference; recorded interview possible (EN); emeritus, availability uncertain.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Jaap Wieringa</td>
<td>University of Groningen, Full Professor of Research Methods in Business, chair of Marketing department; academic; Global</td>
<td>[https://www.rug.nl/staff/j.e.wieringa/?lang=en](https://www.rug.nl/staff/j.e.wieringa/?lang=en)</td>
<td>Time series analysis, state space modelling, Kalman filtering and diffusion modelling for marketing; co-editor of Advanced Methods for Modeling Markets; multiple best-teacher awards.</td>
<td>Teaching-oriented remote guest (EN) for the methods part (ARIMA vs. state space).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Rob J Hyndman</td>
<td>Monash University, Vice-Chancellor's Distinguished Professor of Statistics; academic; Global</td>
<td>[https://robjhyndman.com/](https://robjhyndman.com/)</td>
<td>Author of the free textbook Forecasting: Principles and Practice (fpp3 in R, Python edition fpppy); forecast/fable R packages incl. auto.arima; blog Hyndsight.</td>
<td>Core reading (fpp3 chapters on ARIMA and dynamic regression); recorded talks online; live guest unlikely (time zone).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>George Athanasopoulos</td>
<td>Monash University, Professor and Head of Department of Econometrics and Business Statistics; academic; Global</td>
<td>[https://research.monash.edu/en/persons/george-athanasopoulos/](https://research.monash.edu/en/persons/george-athanasopoulos/)</td>
<td>Co-author of Forecasting: Principles and Practice; hierarchical forecasting and tourism demand forecasting (international arrivals); IIF President 2020-2024.</td>
<td>Tourism-demand cases fit international marketing; Forecasting Impact podcast episode usable as listening assignment.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Spyros Makridakis</td>
<td>University of Nicosia, Director of the Institute for the Future / Makridakis Open Forecasting Center; academic; Global</td>
<td>[https://unic.ac.cy/makridakis-spyridon](https://unic.ac.cy/makridakis-spyridon)</td>
<td>Organizer of the M-competitions (M4; M5 with Walmart retail sales; M6); founding editor of Journal of Forecasting and International Journal of Forecasting.</td>
<td>Use M4/M5 findings as discussion case on ARIMA vs. ML; recorded keynotes available.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Fotios Petropoulos</td>
<td>University of Bath School of Management, Professor of Management Science; academic; Global</td>
<td>[https://fpetropoulos.eu/](https://fpetropoulos.eu/)</td>
<td>Lead editor of Forecasting: theory and practice (International Journal of Forecasting 2022, open encyclopedic review); judgmental forecasting and model selection.</td>
<td>Remote guest (EN) on forecasting practice and model selection; active in the IIF community.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>People</td>
<td>Nikolaos Kourentzes</td>
<td>University of Skövde, Skövde AI Lab, Professor of Predictive Analytics; academic; Global</td>
<td>[https://kourentzes.com/forecasting/](https://kourentzes.com/forecasting/)</td>
<td>Business and promotional demand forecasting, temporal hierarchies; author of R packages (e.g. tsutils, thief, nnfor) and a widely read forecasting blog.</td>
<td>Remote guest (EN) on retail and promotional demand forecasting; blog posts as readings.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Sven F. Crone</td>
<td>Lancaster University (Centre for Marketing Analytics and Forecasting) and founder of iqast; academic/practitioner; Global (German native)</td>
<td>[https://www.lancaster.ac.uk/lums/people/sven-crone](https://www.lancaster.ac.uk/lums/people/sven-crone)</td>
<td>Neural network vs. statistical forecasting for business demand; industry projects with AB InBev, Beiersdorf and Hapag-Lloyd; executive education in demand planning.</td>
<td>German-speaking guest (DE/EN, remote) bridging ARIMA benchmarks and ML in FMCG demand planning.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Stephan Kolassa</td>
<td>SAP Switzerland, Data Science Expert; IIF Fellow; practitioner; DACH</td>
<td>[https://forecasters.org/blog/2023/07/03/iif-fellow-and-distinguished-researcher-stephan-kolassa/](https://forecasters.org/blog/2023/07/03/iif-fellow-and-distinguished-researcher-stephan-kolassa/)</td>
<td>Designs retail forecasting and replenishment algorithms at SAP; co-author of Demand Forecasting for Managers (with Siemsen); long-time Foresight author and editor.</td>
<td>Excellent DACH practitioner guest (DE/EN, remote or on site) on retail forecasting at scale and accuracy metrics.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>People</td>
<td>Robert M. Kunst</td>
<td>Institute for Advanced Studies (IHS) Vienna, Fellow; Univ.-Prof. at Universität Wien until retirement 2022; academic; Wien</td>
<td>[https://www.ihs.ac.at/people/robert-kunst/](https://www.ihs.ac.at/people/robert-kunst/)</td>
<td>Time series econometrics: seasonality, seasonal unit roots, cointegration, forecasting and model selection; co-organizer of the Vienna Workshop on Economic Forecasting; coordinating editor of Empirical Economics.</td>
<td>On-site guest in Wien (DE/EN) on seasonal ARIMA and unit roots; lecture-style format.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Michael Hauser</td>
<td>WU Wien, Institute for Statistics and Mathematics, ao. Univ.-Prof. (retired); academic; Wien</td>
<td>[https://statmath.wu.ac.at/\~hauser/](https://statmath.wu.ac.at/~hauser/)</td>
<td>Time series analysis and forecasting incl. sales forecasting (Umsatzprognose) and staff planning, ARFIMA models, diffusion models, price indices.</td>
<td>Possible WU-internal guest (DE) on applied sales forecasting; retired, availability to check.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Sylvia Frühwirth-Schnatter</td>
<td>WU Wien, Professor of Applied Statistics and Econometrics; academic; Wien</td>
<td>[https://statmath.wu.ac.at/\~fruehwirth](https://statmath.wu.ac.at/~fruehwirth)</td>
<td>Bayesian time series: state space, Markov switching and finite mixture models (Springer monograph); member of the Austrian Academy of Sciences, former ISBA president.</td>
<td>WU-internal guest (DE/EN) for an advanced extension: regime switching and state space as alternatives to ARIMA.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Achim Zeileis</td>
<td>Universität Innsbruck, Department of Statistics, Professor; academic; Österreich</td>
<td>[https://www.zeileis.org/](https://www.zeileis.org/)</td>
<td>Co-author of Applied Econometrics with R (AER); R packages zoo, strucchange (structural breaks) and sandwich (HAC standard errors for time-series regression).</td>
<td>Remote or on-site guest (DE/EN) on structural breaks and robust inference in time-series regression; R-centric.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Thomas Reutterer</td>
<td>WU Wien, Head of Institute for Marketing and Customer Analytics; academic; Wien</td>
<td>[https://www.wu.ac.at/en/mca/institute/meet-our-team/thomas-reutterer](https://www.wu.ac.at/en/mca/institute/meet-our-team/thomas-reutterer)</td>
<td>Modeling and forecasting customer behavior (customer base analysis, CLV, RNN/LSTM vs. RFM; IJRM 2022 best-article finalist). Topic fit: customer-level forecasting rather than ARIMA.</td>
<td>WU colleague, easy on-site guest (DE/EN) contrasting aggregate time series with customer-level forecasting.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Nils Wlömert</td>
<td>WU Wien, Institute for Retailing and Data Science, Professor of Marketing; academic; Wien</td>
<td>[https://sites.google.com/view/nilswloemert/home](https://sites.google.com/view/nilswloemert/home)</td>
<td>Quantitative marketing with longitudinal data: Spotify market entry and music revenues across countries (IJRM 2016), playlist effects (JM 2025, with van Heerde), social media boycotts (JMR 2026).</td>
<td>WU colleague (DE/EN) for a session on international streaming data and dynamic effects.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>People</td>
<td>Christof Bitschnau and Resul Akay (Quantics)</td>
<td>Quantics, Vienna AI demand-forecasting start-up (CEO / Chief Data Scientist); practitioner; Wien</td>
<td>[https://www.trendingtopics.eu/quantics-neues-wiener-startup-prognostiziert-absatzzahlen-mit-hilfe-von-ki/](https://www.trendingtopics.eu/quantics-neues-wiener-startup-prognostiziert-absatzzahlen-mit-hilfe-von-ki/)</td>
<td>Founded 2020 in Vienna; hierarchical demand forecasting for retail, food and manufacturing incl. effects of discounts, loyalty cards and weather; aws seed funding; presented hierarchical forecasting at Lancaster CMAF.</td>
<td>Local practitioner guest (DE/EN, on site in Wien) showing how promotions and drivers enter forecasting models in industry.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
