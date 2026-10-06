## Quellen zu Python, polars, plotnine, Great Tables und Quarto (Agentensuche, 5. Oktober 2026)
Zwei parallele Rechercheagenten (Software, Websites, Videos, Daten, Praxisbeispiele; Bücher, Artikel, Reports, Lehrfälle). 129 Fundstellen. Versionsstand laut PyPI am 5. Oktober 2026: polars 1.44.2 (2.0 als Release Candidate mit Breaking Changes), plotnine 0.15.8, great-tables 1.0.0, Quarto 1.10.18. Importiert aus der Notion-Seite Python and Packages vom 5. Oktober 2026.
### Bücher (14)
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
<td>Python Polars: The Definitive Guide</td>
<td>Jeroen Janssens and Thijs Nieuwdorp, O'Reilly, April 2025, book (501 pages)</td>
<td>[https://www.oreilly.com/library/view/python-polars-the/9781098156077/](https://www.oreilly.com/library/view/python-polars-the/9781098156077/)</td>
<td>The reference text for the course stack. Janssens (Posit) and Nieuwdorp cover expressions, eager and lazy APIs, data types, joins and reshaping, and, unusually, a full part on visualising Polars data with Altair, hvPlot, plotnine and Great Tables, plus pandas interoperability. The only book that treats the polars plus plotnine plus Great Tables combination as one workflow.</td>
<td>sessions 1-3 (chapters on expressions, reading data and visualisation as background reading for labs); paid (about EUR 60 print, or via an institutional O'Reilly Learning subscription if WU has one).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Modern Polars</td>
<td>Kevin Heavey, 2022-2024 (rolling), free online book (GitHub, built with Quarto)</td>
<td>[https://kevinheavey.github.io/modern-polars/](https://kevinheavey.github.io/modern-polars/)</td>
<td>Side-by-side pandas and polars code for the same tasks (indexing, method chaining, tidy data, time series, scaling), modelled on Tom Augspurger's "Modern Pandas". The fastest way for a student or an AI assistant that already "thinks in pandas" to see the polars idiom.</td>
<td>session 1-2 (reading, a pandas-to-polars migration reference for students who arrive with pandas snippets from ChatGPT); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Effective Polars: Optimized Data Manipulation for Polars 1.0</td>
<td>Matt Harrison (with Anique Khawar and Thomas M. Ahern), self-published (Treading on Python series), March 2024, updated edition for Polars 1.0 July 2024, book (368 pages)</td>
<td>[https://github.com/mattharrison/effective_polars_book](https://github.com/mattharrison/effective_polars_book)</td>
<td>Opinionated, chain-first style from the author of Effective Pandas; short chapters on columns, joins, strings, dates, group-by and lazy evaluation with real datasets, and a clear argument for why method chaining produces readable, debuggable analysis code. Harrison also runs corporate training, so the examples are built for people who learn by doing.</td>
<td>session 2 (lab reference for group-by and reshaping); paid (about EUR 40 print or PDF).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Polars Cookbook</td>
<td>Yuki Kakegawa, Packt, August 2024, book (394 pages, over 60 recipes for Polars 1.x)</td>
<td>[https://www.packtpub.com/en-us/product/polars-cookbook-9781805125150](https://www.packtpub.com/en-us/product/polars-cookbook-9781805125150)</td>
<td>Recipe format (reading CSV, Parquet and databases; aggregations, window functions, string handling, missing values, pivots and joins, time series, pandas and PyArrow interop). Good when a student needs "how do I do X" rather than a narrative; weaker on visualisation and reporting.</td>
<td>background (lab troubleshooting reference); paid (about EUR 45, Packt subscription or O'Reilly Learning).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Python for Data Analysis, 3rd edition</td>
<td>Wes McKinney, O'Reilly, 2022, book, free online (open-access HTML of the full text)</td>
<td>[https://wesmckinney.com/book/](https://wesmckinney.com/book/)</td>
<td>The pandas author's own textbook, free online with notebooks. Still the clearest introduction to the dataframe mental model (tidy columns, group-by, joins, reshaping, time series) that polars inherits and tightens. Use it to explain the concepts, then show the polars equivalent.</td>
<td>session 1-2 (background reading, chapters 5, 8 and 10); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Python Data Science Handbook, 2nd edition</td>
<td>Jake VanderPlas, O'Reilly, 2022 (2e), book, free online as Jupyter notebooks</td>
<td>[https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)</td>
<td>Free, notebook-based coverage of NumPy, pandas, matplotlib and scikit-learn with Colab and Binder launch buttons. The matplotlib chapters are the best short explanation of why a grammar of graphics (plotnine) is easier for beginners than imperative plotting.</td>
<td>background (students who want the matplotlib and scikit-learn layer under plotnine and statsmodels); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Effective Pandas 2: Opinionated Patterns for Data Manipulation</td>
<td>Matt Harrison, self-published (Treading on Python), January 2024, book (580 pages)</td>
<td>[https://www.amazon.co.uk/Effective-Pandas-Opinionated-Patterns-Manipulation/dp/B0CSRGH8R3](https://www.amazon.co.uk/Effective-Pandas-Opinionated-Patterns-Manipulation/dp/B0CSRGH8R3)</td>
<td>Updated for pandas 2 (PyArrow-backed dtypes, copy-on-write). Its chaining style is the pandas counterpart of the polars idiom, so it is the right pandas book to recommend if a student must read legacy pandas code or a dataset only ships with pandas examples.</td>
<td>background (optional for students who meet pandas in internships); paid (about EUR 45).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Fundamentals of Data Visualization</td>
<td>Claus O. Wilke, O'Reilly, 2019, book, free online (CC BY-NC-ND)</td>
<td>[https://clauswilke.com/dataviz/](https://clauswilke.com/dataviz/)</td>
<td>Tool-agnostic principles (which chart for which question, colour, redundancy, uncertainty, "ugly, bad and wrong" figures) written by a ggplot2 power user; the figures are built with the grammar-of-graphics logic plotnine implements. The best text for grading student charts.</td>
<td>session 2-3 (reading before the visualisation lab; chapters 1-5 and 29 "Telling a story"); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>ggplot2: Elegant Graphics for Data Analysis, 3rd edition</td>
<td>Hadley Wickham, Danielle Navarro and Thomas Lin Pedersen, Springer, 3e online 2023-2024, book, free online</td>
<td>[https://ggplot2-book.org/](https://ggplot2-book.org/)</td>
<td>plotnine is a near one-to-one port of ggplot2, so this is effectively the plotnine theory book: layers, aesthetics, scales, facets, themes, "the grammar" chapter. Students translate aes(), geom_\*, facet_wrap and theme almost unchanged.</td>
<td>session 2 (background reading; part II "The grammar"); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Python for Marketing Research and Analytics</td>
<td>Jason S. Schwarz, Chris Chapman and Elea McDonnell Feit, Springer, 2020, book (283 pages)</td>
<td>[https://doi.org/10.1007/978-3-030-49720-0](https://doi.org/10.1007/978-3-030-49720-0)</td>
<td>Python port of the well-known R for Marketing Research and Analytics: segmentation, choice, satisfaction drivers, marketing-mix style regressions, all on simulated marketing datasets, written for readers "with little programming background". pandas and seaborn based, so students need to translate to polars and plotnine, which is itself a useful exercise.</td>
<td>sessions 3-4 (case data and worked examples; the GitHub notebooks are Apache 2.0); book paid (Springer, about EUR 60; often free via university SpringerLink access).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Applied Marketing Analytics Using Python</td>
<td>Gokhan Yildirim (Imperial College Business School) and Raoul V. Kübler (ESSEC), SAGE, July 2025, textbook (384 pages)</td>
<td>[https://uk.sagepub.com/en-gb/eur/applied-marketing-analytics-using-python/book288563](https://uk.sagepub.com/en-gb/eur/applied-marketing-analytics-using-python/book288563)</td>
<td>The first marketing-analytics textbook written for Python by European marketing academics: segmentation, marketing mix modelling, attribution, user-generated content and text mining, churn prediction, demand forecasting, image analytics, plus a chapter on data project management. Comes with datasets, code, slides, teaching guide and test bank.</td>
<td>sessions 3-5 (MMM and attribution chapters as reading; datasets for cases); paid (about GBP 45 paperback; instructor resources via SAGE).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Quarto: The Practical Guide</td>
<td>Mine Çetinkaya-Rundel and Charlotte Wickham, in progress 2025-2026 (print edition planned), book, free online</td>
<td>[https://quarto-tdg.org/](https://quarto-tdg.org/)</td>
<td>A concept-first Quarto guide (getting started, computation, documents, websites, slides, extensions) by the two people who teach Quarto most, and language-neutral with Python and R examples. Fills the gap between the reference docs and a course handout. Nick Tierney's "Quarto for Scientists" ([https://qmd4sci.njtierney.com/](https://qmd4sci.njtierney.com/), R-leaning) is the shorter alternative.</td>
<td>session 1 (reading before the first Quarto report) and session 5 (slides and websites); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Coding for Economists and Python for Data Science (python4DS)</td>
<td>Arthur Turrell (Bank of England), 2020-2026 (rolling), two free online books built with Quarto</td>
<td>[https://aeturrell.github.io/coding-for-economists](https://aeturrell.github.io/coding-for-economists)</td>
<td>python4DS is a chapter-by-chapter Python port of R for Data Science; Coding for Economists adds reproducible workflows, Quarto, uv, plotnine and lets-plot, regression and text. Both are written for social-science students without a programming background and are maintained with uv and GitHub Actions, so they model the exact tooling the course uses.</td>
<td>sessions 1-3 (reading, especially the Quarto, data tidying and visualisation chapters); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Bücher</td>
<td>Think Python, 3rd edition</td>
<td>Allen B. Downey, O'Reilly / Green Tea Press, 2024, book, free online (HTML and Jupyter notebooks)</td>
<td>[https://allendowney.github.io/ThinkPython/](https://allendowney.github.io/ThinkPython/)</td>
<td>The gentlest full Python introduction, rewritten for the 3rd edition around notebooks and with a chapter on using AI assistants to learn programming. For students who need the language basics (functions, lists, dictionaries) under the dataframe layer.</td>
<td>background (pre-course self-study for students with zero coding); free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Journal Articles (20)
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
<td>A layered grammar of graphics</td>
<td>Hadley Wickham, 2010, article, Journal of Computational and Graphical Statistics 19(1), 3-28</td>
<td>[https://doi.org/10.1198/jcgs.2009.07098](https://doi.org/10.1198/jcgs.2009.07098)</td>
<td>The paper that defines the layer, aesthetic, geom, stat, scale and facet model plotnine implements. Twelve readable pages; the worked examples translate directly into plotnine code.</td>
<td>session 2 (short reading before the visualisation lab); open preprint.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The Grammar of Graphics, 2nd edition</td>
<td>Leland Wilkinson, Springer, 2005, book (the original reference)</td>
<td>[https://doi.org/10.1007/0-387-28695-0](https://doi.org/10.1007/0-387-28695-0)</td>
<td>The source of the idea; Wickham 2010 and plotnine are its practical descendants. Dense, so cite rather than assign; the introduction chapter (10.1007/0-387-28695-0_1) is enough for students.</td>
<td>background; paywalled (SpringerLink, usually available via WU library).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Tidy data</td>
<td>Hadley Wickham, 2014, article, Journal of Statistical Software 59(10)</td>
<td>[https://doi.org/10.18637/jss.v059.i10](https://doi.org/10.18637/jss.v059.i10)</td>
<td>Defines the "one variable per column, one observation per row" convention that polars unpivot and pivot, plotnine aesthetics and Great Tables all assume. The cleanest explanation of why reshaping matters before plotting.</td>
<td>session 2 (reading, 10 pages); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Literate programming</td>
<td>Donald E. Knuth, 1984, article, The Computer Journal 27(2), 97-111</td>
<td>[https://doi.org/10.1093/comjnl/27.2.97](https://doi.org/10.1093/comjnl/27.2.97)</td>
<td>The origin of "code and prose in one document" that runs through Sweave, knitr, R Markdown, Jupyter and Quarto. Two pages of the introduction are enough to show students that Quarto is not a gimmick but a 40-year-old idea.</td>
<td>session 1 (one-paragraph excerpt in the Quarto lecture); paywalled, widely available copies.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Reproducible research in computational science</td>
<td>Roger D. Peng, 2011, article, Science 334(6060), 1226-1227</td>
<td>[https://doi.org/10.1126/science.1213847](https://doi.org/10.1126/science.1213847)</td>
<td>The standard two-page statement of the reproducibility spectrum (publication only, to code and data, to linked executable code and data). Gives the course a vocabulary for why a Quarto report with embedded polars code is the deliverable rather than a PowerPoint.</td>
<td>session 1 (reading); paywalled (Science), author version circulates widely.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>R Markdown: integrating a reproducible analysis tool into introductory statistics</td>
<td>Ben Baumer, Mine Çetinkaya-Rundel, Andrew Bray, Linda Loi and Nicholas J. Horton, 2014, article, Technology Innovations in Statistics Education 8(1)</td>
<td>[https://doi.org/10.5070/T581020118](https://doi.org/10.5070/T581020118)</td>
<td>The first classroom study of literate documents with beginners: students who hand in rendered reports make fewer copy-paste errors and understand the analysis better. Everything it says about R Markdown applies to Quarto with Python.</td>
<td>background (justifies the "every assignment is a rendered .qmd" rule); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Tools and recommendations for reproducible teaching</td>
<td>Mine Dogucu and Mine Çetinkaya-Rundel, 2022, article, Journal of Statistics and Data Science Education 30(3), 251-260 (special issue on teaching reproducibility)</td>
<td>[https://doi.org/10.1080/26939169.2022.2138645](https://doi.org/10.1080/26939169.2022.2138645)</td>
<td>Practical guidance on building course materials reproducibly (version control, literate documents, GitHub Classroom, a public course website); the companion paper Çetinkaya-Rundel and Rundel 2018, "Infrastructure and tools for teaching computing throughout the statistical curriculum", The American Statistician 72(1), [https://doi.org/10.1080/00031305.2017.1397549](https://doi.org/10.1080/00031305.2017.1397549), covers the infrastructure side.</td>
<td>background (instructor reading for course design); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Reproducibility in the classroom</td>
<td>Mine Dogucu, 2025, review article, Annual Review of Statistics and Its Application 12, 89-105</td>
<td>[https://doi.org/10.1146/annurev-statistics-112723-034436](https://doi.org/10.1146/annurev-statistics-112723-034436)</td>
<td>The most recent synthesis of what teaching reproducibility means in statistics and data science courses (tools, assessment, Quarto and notebooks, open materials). A good single citation for the syllabus.</td>
<td>background; paywalled (Annual Reviews), preprint on ResearchGate.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A fresh look at introductory data science</td>
<td>Mine Çetinkaya-Rundel and Victoria Ellison, 2021, article, Journal of Statistics and Data Science Education 29(S1), S16-S26</td>
<td>[https://doi.org/10.1080/10691898.2020.1804497](https://doi.org/10.1080/10691898.2020.1804497)</td>
<td>Describes the Duke STA 199 design (data first, modelling late, GitHub from week one, literate reports throughout) that most modern Python-and-Quarto courses copy. Useful for the sequencing of a five-session course.</td>
<td>background (course design); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Innovative and interactive statistics teaching using Quarto</td>
<td>Evans, 2026, article, Teaching Statistics (Wiley), early view</td>
<td>[https://doi.org/10.1111/test.12409](https://doi.org/10.1111/test.12409)</td>
<td>The first journal article specifically about Quarto in the classroom (interactive documents, slides and exercises). Recent enough to reflect Quarto 1.6 and later.</td>
<td>background; paywalled (Wiley), check WU access.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Jupyter Notebooks: a publishing format for reproducible computational workflows</td>
<td>Thomas Kluyver, Benjamin Ragan-Kelley, Fernando Pérez et al., 2016, conference paper, Positioning and Power in Academic Publishing (ELPUB 2016), 87-90</td>
<td>[https://doi.org/10.3233/978-1-61499-649-1-87](https://doi.org/10.3233/978-1-61499-649-1-87)</td>
<td>The canonical citation for the notebook format Quarto renders with Python (Quarto executes .qmd files through Jupyter kernels). Four pages, explains kernels, cells and nbconvert, which demystifies what Positron does when it renders.</td>
<td>session 1 (citation in the Quarto lecture); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Exploration and explanation in computational notebooks, and Ten simple rules for Jupyter notebooks</td>
<td>Adam Rule, Aurélien Tabard and James D. Hollan, 2018, CHI 2018 paper; Adam Rule, Amanda Birmingham et al., 2019, article, PLOS Computational Biology 15(7)</td>
<td>[https://doi.org/10.1145/3173574.3173606](https://doi.org/10.1145/3173574.3173606)</td>
<td>The 2018 study of a million GitHub notebooks shows how messy exploratory notebooks become (one in four has no prose); the 2019 "ten rules" paper is the fix (tell a story, document the process, modularise, record dependencies, share). Together they explain why the course asks for Quarto reports rather than raw notebooks.</td>
<td>session 1 and 5 (the ten rules as a grading checklist); CHI paywalled, PLOS open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Towards scalable dataframe systems</td>
<td>Devin Petersohn, Stephen Macke, Doris Xin, William Ma, Doris Lee, Xiangxi Mo, Joseph E. Gonzalez, Joseph M. Hellerstein, Anthony D. Joseph and Aditya Parameswaran, 2020, article, Proceedings of the VLDB Endowment 13(12), 2033-2046</td>
<td>[https://doi.org/10.14778/3407790.3407807](https://doi.org/10.14778/3407790.3407807)</td>
<td>The first formal dataframe algebra and a critique of pandas (ordered rows, mixed types, eager execution) that reads like a design brief for polars (lazy plans, strict schemas, query optimisation). Sections 1-3 are accessible to non-engineers.</td>
<td>background (instructor reading; one slide on why polars is lazy); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Evaluation of dataframe libraries for data preparation on a single machine</td>
<td>Angelo Mozzillo, Luca Zecchini, Luca Gagliardelli, Adeel Aslam, Sonia Bergamaschi and Giovanni Simonini, 2025, conference article, EDBT 2025 (preprint 2023)</td>
<td>[https://openproceedings.org/2025/conf/edbt/paper-96.pdf](https://openproceedings.org/2025/conf/edbt/paper-96.pdf)</td>
<td>Independent benchmark of pandas, Polars, Modin, Dask, Vaex, cuDF and PySpark on data-preparation tasks; conclusion is that pandas has the richest API for tiny data, polars is the default when data fits in RAM, Spark only beyond that. Gives the course an evidence-based answer to "why polars and not pandas".</td>
<td>session 1 (one figure in the tooling lecture); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The composable data management system manifesto</td>
<td>Pedro Pedreira, Orri Erling, Konstantinos Karanasos, Scott Schneider, Wes McKinney, Satya R. Valluri, Mohamed Zait and Jacques Nadeau, 2023, article, Proceedings of the VLDB Endowment 16(10), 2679-2685</td>
<td>[https://doi.org/10.14778/3603581.3603604](https://doi.org/10.14778/3603581.3603604)</td>
<td>Co-written by the pandas and Arrow creator; explains Apache Arrow as the shared columnar memory layer that lets polars, pandas 2, DuckDB and Parquet exchange data without copying. The background to why pl.from_pandas and .to_pandas() are cheap and why narwhals exists.</td>
<td>background; open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Ten guidelines for better tables</td>
<td>Jonathan A. Schwabish, 2020, article, Journal of Benefit-Cost Analysis 11(2), 151-178</td>
<td>[https://doi.org/10.1017/bca.2020.11](https://doi.org/10.1017/bca.2020.11)</td>
<td>The practical rulebook for presentation tables (right-align numbers, remove gridlines, group and highlight, put units in headers). Great Tables' design philosophy post ([https://posit-dev.github.io/great-tables/blog/design-philosophy/](https://posit-dev.github.io/great-tables/blog/design-philosophy/), Iannone and Chow, April 2024) explicitly builds on this tradition, and each guideline maps to a GT method.</td>
<td>session 3 (reading before the Great Tables lab, with the design-philosophy post); paywalled (Cambridge), free summaries widely available.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>A new era of learning: considerations for ChatGPT as a tool to enhance statistics and data science education</td>
<td>Amanda R. Ellis and Emily Slade, 2023, article, Journal of Statistics and Data Science Education 31(2), 128-133</td>
<td>[https://doi.org/10.1080/26939169.2023.2223609](https://doi.org/10.1080/26939169.2023.2223609)</td>
<td>Early, balanced discussion of generative AI in data-analysis courses (calculator analogy, assessment design, where the tools fail). Short and open access; sets the tone for a course that is explicitly AI-assisted.</td>
<td>session 1 (reading alongside the course AI policy); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>The use of generative AI in statistical data analysis and its impact on teaching statistics at universities of applied sciences</td>
<td>Schwarz, 2025, article, Teaching Statistics (Wiley)</td>
<td>[https://doi.org/10.1111/test.12398](https://doi.org/10.1111/test.12398)</td>
<td>A European (German-speaking) applied-university perspective on students using LLMs to write analysis code: what they get right, where they stop checking, and how to redesign tasks. Close to the CEMS setting.</td>
<td>background (instructor reading on assessment design); open access status not confirmed.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Is GPT-4 a good data analyst?</td>
<td>Liying Cheng, Xingxuan Li and Lidong Bing, 2023, conference article, Findings of EMNLP 2023, 9496-9514</td>
<td>[https://doi.org/10.18653/v1/2023.findings-emnlp.637](https://doi.org/10.18653/v1/2023.findings-emnlp.637)</td>
<td>Benchmarks GPT-4 against professional analysts on question-to-SQL-to-chart-to-insight tasks and finds comparable performance with characteristic errors (plausible but wrong aggregations, over-confident narratives). Good evidence for the "verify the dataframe, not the prose" habit. For the current state of LLM data-science agents see the 2025 survey at [https://doi.org/10.48550/arXiv.2510.04023](https://doi.org/10.48550/arXiv.2510.04023).</td>
<td>session 1 or 4 (discussion reading on AI-assisted analysis); open access.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Journal Articles</td>
<td>Teaching Python for data science: collaborative development of a modular and interactive curriculum</td>
<td>Multiple authors (author list on the JOSE page), 2021, article, Journal of Open Source Education 4(37), 138</td>
<td>[https://doi.org/10.21105/jose.00138](https://doi.org/10.21105/jose.00138)</td>
<td>Describes an open, modular Python data-science curriculum (notebooks, autograded exercises, Binder) and the lessons from running it with beginners. Useful for borrowing exercise design patterns; also worth reading next to the business-school pieces in the Journal of Information Systems Education, for example "A foundation course in business analytics: design and implementation at two universities" (2020, [https://eric.ed.gov/?id=EJ1281524](https://eric.ed.gov/?id=EJ1281524)).</td>
<td>background (course design); open access.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Reports (7)
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
<td>Python Developers Survey 2024 (JetBrains and Python Software Foundation)</td>
<td>JetBrains and PSF, December 2024 (eighth edition, over 30,000 respondents), report</td>
<td>[https://lp.jetbrains.com/python-developers-survey-2024/](https://lp.jetbrains.com/python-developers-survey-2024/)</td>
<td>The best yearly census of Python tooling. 51 percent of respondents do data exploration; among them pandas 80 percent, NumPy 75 percent, Spark 16 percent, Polars 15 percent, Dask 7 percent; uv, Ruff and Polars are singled out as the Rust-based tooling wave. Gives students a realistic picture: polars is growing fast but pandas is what they will meet in most firms.</td>
<td>session 1 (one slide on the tooling landscape); free. Check for the 2025 edition, due late 2025 or early 2026 (not found in search).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Stack Overflow Developer Survey 2025</td>
<td>Stack Overflow, July 2025 (about 49,000 respondents), report</td>
<td>[https://survey.stackoverflow.co/2025/](https://survey.stackoverflow.co/2025/)</td>
<td>Python usage rose seven percentage points year on year, the largest jump of any major language, driven by AI and data work; the AI section documents how many developers use assistants daily and how much they trust them. Useful for the "why Python" and "why AI-assisted" framing.</td>
<td>session 1 (background slide); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Polars adoption statistics: GitHub and PyPI</td>
<td>pola-rs/polars repository (GitHub) and PyPI download trackers ([http://pypistats.org](http://pypistats.org), ClickPy, [http://pepy.tech](http://pepy.tech)), live, websites</td>
<td>[https://github.com/pola-rs/polars](https://github.com/pola-rs/polars)</td>
<td>Hard numbers for the "is this mainstream" question. Search listings cite about 24 million PyPI downloads a month and over 250 million total in September 2025, and over 675 million total by 2026 (figures from Wikipedia and blog listings, unverified). Also note the Polars 2.0 line: check that course material and the AI assistants' snippets match the version installed.</td>
<td>session 1 (tooling slide); free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Posit 2024 Year in Review and Public Benefit Corporation report</td>
<td>Posit PBC, December 2024 and 2025, company reports (both written in Quarto)</td>
<td>[https://posit.co/blog/2024-posit-year-in-review](https://posit.co/blog/2024-posit-year-in-review)</td>
<td>The only official statements on Quarto's scale: about five full-time engineers on Quarto, three releases in 2024, Quarto Live, and the Python-side investments (Positron, Great Tables, plotnine, pointblank) that make the stack coherent. Posit does not publish Quarto download counts, so adoption claims elsewhere are anecdotal.</td>
<td>background; free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>NumFOCUS annual and impact reports</td>
<td>NumFOCUS, 2023-2025, non-profit reports</td>
<td>[https://numfocus.org/community/mission/annual-reports](https://numfocus.org/community/mission/annual-reports)</td>
<td>Lists the sponsored and affiliated projects behind the stack (pandas, NumPy, Jupyter, Arrow, matplotlib and others; 62 sponsored and 93 affiliated projects in 2024) and the small development grants that keep them alive. A reminder that the open-source stack has an institutional home, which matters when students ask "who maintains this".</td>
<td>background; free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Kaggle State of Data Science and Machine Learning 2022</td>
<td>Kaggle (Google), 2022 (sixth and last edition, 23,997 responses), report with full raw data</td>
<td>[https://www.kaggle.com/kaggle-survey-2022](https://www.kaggle.com/kaggle-survey-2022)</td>
<td>Python and SQL as the dominant skills, VS Code overtaking Jupyter as the IDE, scikit-learn as the standard modelling library. Out of date on polars (not yet asked about) but the raw survey data is an excellent teaching dataset: students can replicate the report's charts in polars and plotnine.</td>
<td>session 2 (lab dataset for group-by and faceted charts); free (Kaggle account needed).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Reports</td>
<td>Anaconda State of Data Science 2024 and 2025</td>
<td>Anaconda, 2024 (seventh edition) and 2025 (eighth edition), vendor reports</td>
<td>[https://www.anaconda.com/resources/report/state-of-data-science-report-2024](https://www.anaconda.com/resources/report/state-of-data-science-report-2024)</td>
<td>Practitioner survey on AI adoption in data work: 87 percent increasing AI use, 59 percent of work done on local laptops, and in 2025 only 22 percent of organisations calling their AI deployment strategic. Vendor-funded, so read as marketing-adjacent, but useful for the AI-assisted analysis framing.</td>
<td>background; free (registration wall).</td>
<td>neu; Link ungeprüft</td>
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
<td>Polars user guide, including "Coming from pandas"</td>
<td>Polars team, 2023 to 2026, website (official documentation).</td>
<td>[https://docs.pola.rs/user-guide/](https://docs.pola.rs/user-guide/)</td>
<td>The migration page is the clearest short statement of the mental model (expressions instead of index and lambdas, lazy by default, with_columns versus assignment) and maps pandas idioms to polars.</td>
<td>session 1 pre-reading (concepts, expressions, lazy API chapters). Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Modern Polars (Kevin Heavey)</td>
<td>Kevin Heavey, 2023, website (online book, side-by-side polars and pandas, modelled on Modern Pandas).</td>
<td>[https://kevinheavey.github.io/modern-polars/](https://kevinheavey.github.io/modern-polars/)</td>
<td>Each chapter (indexing, method chaining, tidy data, time series, performance) shows the same task in pandas and polars with commentary; ideal for students whose AI assistant keeps producing pandas.</td>
<td>session 1 and 4 reading; the tidy-data chapter pairs with plotnine. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Python Polars: The Definitive Guide (companion site)</td>
<td>Jeroen Janssens and Thijs Nieuwdorp, O'Reilly, February 2025, book with free companion website; foreword by Ritchie Vink.</td>
<td>[https://polarsguide.com/](https://polarsguide.com/)</td>
<td>The reference text for polars 1.x; chapter 16 covers visualisation including plotnine, and the authors use polars with Quarto. Posit announced it on its blog.</td>
<td>background and recommended purchase (about EUR 50; O'Reilly subscription). Free site, paid book.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Polars Cookbook (Yuki Kakegawa) and Effective Polars (Matt Harrison)</td>
<td>Yuki Kakegawa, Packt, August 2024, book (394 pages, 60+ recipes for polars 1.x); Matt Harrison, self-published, July 2024 edition for polars 1.0, book.</td>
<td>[https://www.packtpub.com/en-us/product/polars-cookbook-9781805121152](https://www.packtpub.com/en-us/product/polars-cookbook-9781805121152)</td>
<td>Recipe-style alternatives to the Definitive Guide: the Cookbook is task oriented (joins, reshaping, time series, I/O), Effective Polars is opinionated and exercise driven. Both are intermediate.</td>
<td>background; lab solution sources. Paid (roughly EUR 35 to 45).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>[http://plotnine.org](http://plotnine.org) documentation and gallery</td>
<td>Hassan Kibirige, 2024 to 2026, website (reference, guide, gallery rebuilt in Quarto in 2024).</td>
<td>[https://plotnine.org/](https://plotnine.org/)</td>
<td>Gallery entries are executable notebooks (including winners of the 2024 Plotnine Contest), the reference mirrors ggplot2 naming, and the "Three major updates to the Plotnine website" post (Posit blog) explains the layout.</td>
<td>session 2 lab reference. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Announcing Plotnine 0.15.0 (Posit blog)</td>
<td>Hassan Kibirige, Posit blog, 2025, article.</td>
<td>[https://posit.co/blog/plotnine-0-15-0](https://posit.co/blog/plotnine-0-15-0)</td>
<td>Introduces plot composition (\|, /), text alignment and facet improvements with examples; the best short "what is new" for anyone with ggplot2 habits.</td>
<td>session 2 optional reading. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Jeroen Janssens: Plotnine cheatsheet and "Plotnine: Grammar of Graphics for Python"</td>
<td>Jeroen Janssens (Posit), October 2025 (cheatsheet) and 2024 update of a 2019 post, website.</td>
<td>[https://jeroenjanssens.com/plotnine-cheatsheet/](https://jeroenjanssens.com/plotnine-cheatsheet/)</td>
<td>The post rebuilds a classic ggplot2 walkthrough with polars 1.0 and plotnine 0.13, exactly the course pairing; the cheatsheet is a printable one-page summary.</td>
<td>session 2 handout. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Great Tables documentation, Get Started and Examples</td>
<td>Posit (Iannone and Chow), 2024 to 2026, website.</td>
<td>[https://posit-dev.github.io/great-tables/](https://posit-dev.github.io/great-tables/)</td>
<td>Get Started walks the component model (header, stub, spanners, formatting, styling, nanoplots); the examples page shows finished tables built from the bundled datasets, several with a business flavour (gtcars, sp500, pizzaplace).</td>
<td>session 3 lab reference. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>The Design Philosophy of Great Tables</td>
<td>Rich Iannone and Michael Chow, Great Tables blog, 4 April 2024, article.</td>
<td>[https://posit-dev.github.io/great-tables/blog/design-philosophy/](https://posit-dev.github.io/great-tables/blog/design-philosophy/)</td>
<td>Argues from 5,000 years of table history why structure (stub, spanners, notes) matters and why computational tables should expose it; a readable "why tables deserve design" piece for business students.</td>
<td>session 3 pre-reading. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Great Tables blog: polars posts</td>
<td>Michael Chow and Rich Iannone, Great Tables blog, 2024 to 2025, articles: "Great Tables: the Polars DataFrame styler of your dreams" (January 2024), "Great Tables is now BYODF" (April 2024), "Nanoplots and more, v0.4.0" (March 2024), "Becoming the Polars .style property" (April 2025), "Generating LaTeX output for PDF".</td>
<td>[https://posit-dev.github.io/great-tables/blog/](https://posit-dev.github.io/great-tables/blog/)</td>
<td>Shows polars expressions driving conditional formatting (tab_style(locations=loc.body(rows=pl.col("x") \> 0))), which is the course's main table idiom, plus honest notes on PDF limitations.</td>
<td>session 3 reading. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Posit blog: Level Up Your Python Tables and What we did with publication-quality tables in 2024</td>
<td>Posit, 2024 to 2025, articles with a companion video series.</td>
<td>[https://posit.co/blog/level-up-great-tables](https://posit.co/blog/level-up-great-tables)</td>
<td>Structure, style and clarity walkthroughs with videos; the year-in-review post lists gt and Great Tables features side by side, useful for R-trained colleagues.</td>
<td>session 3 background. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Quarto guide: Using Python, Presentations, Dashboards, Manuscripts</td>
<td>Posit, 2022 to 2026, website (official guide).</td>
<td>[https://quarto.org/docs/computations/python.html](https://quarto.org/docs/computations/python.html)</td>
<td>The guide pages are the canonical reference for the Jupyter engine, cell options (#\| echo: false, #\| fig-cap), revealjs and pptx output, dashboards and parameterised reports; the Quarto blog moved to [http://opensource.posit.co](http://opensource.posit.co) in 2025 ([https://opensource.posit.co/blog/q/quarto/](https://opensource.posit.co/blog/q/quarto/)).</td>
<td>sessions 3 and 5 reference. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Quarto Live documentation</td>
<td>George Stagg, Posit, 2024 to 2026, website.</td>
<td>[https://r-wasm.github.io/quarto-live/](https://r-wasm.github.io/quarto-live/)</td>
<td>Setup, \{pyodide\} cells, exercises with grading and OJS integration; the Tidyverse blog post "WebAssembly roundup part 3: Quarto Live 0.1.1" (October 2024) is the readable introduction.</td>
<td>background for building self-study pages. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Real Python: Python Polars tutorial and Using ggplot in Python with plotnine</td>
<td>Real Python, 2023 to 2025, website tutorials (with optional video course "Working With Python Polars").</td>
<td>[https://realpython.com/polars-python/](https://realpython.com/polars-python/)</td>
<td>Beginner-paced, well edited, with runnable code on GitHub ([https://github.com/realpython/materials/tree/master/python-polars](https://github.com/realpython/materials/tree/master/python-polars)); the plotnine tutorial starts from the grammar itself. Real Python Podcast episode 260 (August 2025) interviews the Definitive Guide authors.</td>
<td>session 1 and 2 self-study. Articles free; video courses by subscription.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Polars Academy and PyData talk pages on [http://pola.rs](http://pola.rs)</td>
<td>Polars (company), 2023 to 2026, website (learning hub plus posts summarising conference talks with slides and video links).</td>
<td>[https://pola.rs/academy/](https://pola.rs/academy/)</td>
<td>Official short courses (expressions, lazy API, plugins) and the canonical index of Ritchie Vink's PyData talks (Amsterdam, NYC, Eindhoven 2023).</td>
<td>background. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>awesome-polars and awesome-quarto</td>
<td>Damien Dotta (awesome-polars) and Mickaël Canouil (awesome-quarto), 2022 to 2026, GitHub lists.</td>
<td>[https://github.com/ddotta/awesome-polars](https://github.com/ddotta/awesome-polars)</td>
<td>Curated, actively updated indexes of talks, books, plugins, courses and example sites (awesome-quarto lists Python-specific items such as "Quarto for the Python user" by Jumping Rivers and Charlotte Wickham's parameterised-report talks).</td>
<td>background for the instructor. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Coding for Economists and Python for Data Science (Arthur Turrell)</td>
<td>Arthur Turrell, 2021 to 2026, website (two free Quarto-style online books).</td>
<td>[https://aeturrell.github.io/coding-for-economists/vis-plotnine.html](https://aeturrell.github.io/coding-for-economists/vis-plotnine.html)</td>
<td>Coding for Economists has a full chapter "Data visualisation using the grammar of graphics with plotnine" and discusses polars; python4DS mirrors R for Data Science in Python and ends with Quarto reporting. Written for beginners with no programming background.</td>
<td>session 2 reading (plotnine chapter), background for the rest. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Websites</td>
<td>Calmcode: Python Polars vs. pandas</td>
<td>Vincent Warmerdam, Calmcode, 2022 to 2024, website with short videos.</td>
<td>[https://calmcode.io/course/polars/introduction](https://calmcode.io/course/polars/introduction)</td>
<td>Eight videos of two to five minutes each (introduction, read_csv, with_columns, pipe, sort and filter, sessionise, over expressions, eager versus lazy) using a clickstream-style dataset; calm, beginner friendly.</td>
<td>session 1 pre-lab viewing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### (Video-) Tutorials (15)
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
<td>Ritchie Vink: Polars, DataFrames in the multi-core era (PyData NYC 2023) and Polars and a peek into the expression engine (PyData Amsterdam 2023)</td>
<td>Ritchie Vink (Polars creator), PyData, 2023, conference talks (about 35 to 40 minutes each, intermediate).</td>
<td>[https://www.youtube.com/watch?v=NJbBWDzZuWs](https://www.youtube.com/watch?v=NJbBWDzZuWs)</td>
<td>The creator explains why polars is built around expressions and a query optimiser; good for the "why not pandas" question without benchmark hype.</td>
<td>session 1 optional viewing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Marco Gorelli: Understanding Polars expressions when you are used to pandas; Polars and time series (PyCon DE and PyData Berlin 2024); How Narwhals brings Polars, DuckDB, PyArrow and pandas together (PyData London 2025)</td>
<td>Marco Gorelli (Quansight Labs, Narwhals author, pandas and Polars contributor), 2023 to 2025, conference talks, 29 to 36 minutes, beginner to intermediate.</td>
<td>[https://www.youtube.com/watch?v=qz-zAHBz6Ks](https://www.youtube.com/watch?v=qz-zAHBz6Ks)</td>
<td>The expressions talk is the single best bridge for pandas-trained viewers; the time-series talk covers date handling needed for weekly sales data.</td>
<td>session 1 (expressions) and session 4 (time series). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Hassan Kibirige: Grammar of Graphics in Python with Plotnine (posit::conf 2023)</td>
<td>Hassan Kibirige (plotnine creator), Posit, 2023, conference talk (about 20 minutes, beginner).</td>
<td>[https://www.youtube.com/watch?v=q816IZuqVNo](https://www.youtube.com/watch?v=q816IZuqVNo)</td>
<td>The author's own explanation of layers, aesthetics and facets with plotnine code; the Mode blog interview "Who's behind the numbers?" ([https://mode.com/blog/whos-behind-the-numbers-hassan-kibirige/](https://mode.com/blog/whos-behind-the-numbers-hassan-kibirige/)) adds background.</td>
<td>session 2 pre-viewing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Rich Iannone: Adequate Tables? No, We Want Great Tables (posit::conf 2024) and Making Things Nice in Python (posit::conf 2025)</td>
<td>Rich Iannone (Posit), 2024 and 2025, conference talks (about 20 minutes each, beginner).</td>
<td>[https://pyvideo.org/positconf-2024/adequate-tables-no-we-want-great-tables.html](https://pyvideo.org/positconf-2024/adequate-tables-no-we-want-great-tables.html)</td>
<td>Live-coded table building from a dataframe to a publication table, nanoplots included; the 2025 talk adds Pointblank for data validation.</td>
<td>session 3 pre-viewing. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Talk Python episode 492: Great Tables (Iannone and Chow)</td>
<td>Michael Kennedy with Rich Iannone and Michael Chow, Talk Python To Me, 2024, podcast with video (about 1 hour, beginner).</td>
<td>[https://www.youtube.com/watch?v=15ICWSJ0sGk](https://www.youtube.com/watch?v=15ICWSJ0sGk)</td>
<td>Conversational tour of the design, polars integration and Quarto rendering; good commute listening before the tables session.</td>
<td>session 3 optional. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Jeroen Janssens: Python Polars, the Definitive Crash Course (PyData Global 2025)</td>
<td>Jeroen Janssens (Posit), PyData Global, December 2025, tutorial recording (long form, beginner to intermediate).</td>
<td>[https://opensource.posit.co/resources/videos/2026-01-09_jeroen-janssens-python-polars-the-definitive-crash-course-pydata-global-2025/](https://opensource.posit.co/resources/videos/2026-01-09_jeroen-janssens-python-polars-the-definitive-crash-course-pydata-global-2025/)</td>
<td>Condenses the O'Reilly book into one session, with polars 1.x syntax and plotnine figures.</td>
<td>session 1 and 4 self-study. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Keith Galli: Quarto with Python Crash Course (Posit YouTube series)</td>
<td>Keith Galli for Posit, 2024 to 2025, video series (six videos; crash course 96 minutes, parameterised reports 26 minutes, plus slides, dashboards and portfolio site; beginner).</td>
<td>[https://www.youtube.com/playlist?list=PL9HYL-VRX0oQZPzhJR022G_bV4vynT4Ol](https://www.youtube.com/playlist?list=PL9HYL-VRX0oQZPzhJR022G_bV4vynT4Ol)</td>
<td>Python-only Quarto teaching from zero: reports, PDFs, revealjs slides, dashboards and "100s of custom reports in minutes" with parameters; the companion repo is a ready template.</td>
<td>session 3 pre-viewing (crash course), session 5 (parameterised reports). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Mine Çetinkaya-Rundel: Quarto Dashboards video series and Build-a-Dashboard workshop</td>
<td>Mine Çetinkaya-Rundel (Duke University and Posit), November 2024, three videos (first dashboard, components, theming; about 20 minutes each) with R and Python starter code; posit::conf(2024) full-day workshop materials.</td>
<td>[https://www.youtube.com/watch?v=KdsQgwaY950](https://www.youtube.com/watch?v=KdsQgwaY950)</td>
<td>Builds an Olympic medals dashboard in Python or R step by step; "Teaching (with) Quarto" ([https://mine-cetinkaya-rundel.github.io/teach-with-quarto/](https://mine-cetinkaya-rundel.github.io/teach-with-quarto/)) covers course websites and slides.</td>
<td>session 5 dashboards; background for the course site. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Albert Rapp: How to Automate Data Reports with Quarto (Beginner's Guide)</td>
<td>Albert Rapp (3 Minutes Wednesdays), 2024 to 2025, YouTube videos and newsletter (10 to 20 minutes, beginner; R-based code but Quarto features are language independent).</td>
<td>[https://www.youtube.com/watch?v=KCpuUF4vi5g](https://www.youtube.com/watch?v=KCpuUF4vi5g)</td>
<td>Short, polished explanations of parameterised reports, Typst PDFs and revealjs styling; translate the R cells to Python and the rest carries over.</td>
<td>session 5 optional. Free (newsletter free, paid tier exists).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Charlotte Wickham: From one notebook to many reports, automating with Quarto (SciPy 2025)</td>
<td>Charlotte Wickham (Posit, Quarto team), SciPy, 2025, conference talk (about 25 minutes, beginner to intermediate).</td>
<td>[https://github.com/mcanouil/awesome-quarto](https://github.com/mcanouil/awesome-quarto)</td>
<td>Parameterised Python notebooks rendered to many PDFs, exactly the "one report per country" pattern for an international marketing project.</td>
<td>session 5. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Udemy: Data Analysis with Polars (Liam Brannigan)</td>
<td>Liam Brannigan, Udemy, 2022 to 2025 (updated for polars 1.x), paid course (60 Jupyter notebooks, roughly 8 hours, beginner to intermediate; 4.7 rating, endorsed by Ritchie Vink).</td>
<td>[https://www.udemy.com/course/data-analysis-with-polars/](https://www.udemy.com/course/data-analysis-with-polars/)</td>
<td>The most complete structured polars course; the public GitHub repo gives free sample notebooks and datasets.</td>
<td>background; recommend to students who want depth. Paid (Udemy pricing, typically EUR 15 to 90 with frequent discounts).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>DataCamp: Introduction to Polars</td>
<td>DataCamp, updated May 2026, online course (3 hours, 12 videos, 42 exercises, beginner).</td>
<td>[https://www.datacamp.com/courses/introduction-to-polars](https://www.datacamp.com/courses/introduction-to-polars)</td>
<td>Browser-based exercises on selecting, filtering, group-by, pivots; no setup needed, so it suits students who struggle with environments. DataCamp has no plotnine course; the only plotnine MOOC found is a 1.5-hour Coursera guided project "Data Visualization using Plotnine and ggplot" ([https://www.coursera.org/projects/data-visualization-using-plotnine](https://www.coursera.org/projects/data-visualization-using-plotnine)).</td>
<td>session 1 optional practice. First chapter free, rest by subscription (DataCamp Classroom is free for instructors and students).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Real Python video course: Working With Python Polars</td>
<td>Real Python, 2024, video course (about 1 hour, beginner).</td>
<td>[https://realpython.com/courses/working-with-python-polars/](https://realpython.com/courses/working-with-python-polars/)</td>
<td>Video version of the written tutorial: dataframes, expressions, reading data, group-by, lazy API.</td>
<td>session 1 optional. Subscription (free article alternative above).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Posit Academy and posit::conf(2023) Introduction to Data Science with Python</td>
<td>Posit, 2023 to 2026; Academy Apprenticeships are six-to-eight-week mentored cohorts for organisations (price on request); a free open library of courses, labs and workshops launched in 2025. The 2023 workshop (plotnine, pandas, functions, Quarto) has public materials.</td>
<td>[https://academy.posit.co/](https://academy.posit.co/)</td>
<td>The workshop repo is a tested beginner curriculum in the same stack (plotnine plus Quarto), easy to adapt to polars.</td>
<td>background; lab material source. Free materials; apprenticeships paid.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>(Video-) Tutorials</td>
<td>Polars Code Academy and martinbel Polars tutorials (YouTube)</td>
<td>Polars Code Academy channel (feature-by-feature short videos) and Martin Bel's playlist "Polars: the main alternative to pandas" (about 57 minutes total), 2023 to 2025, beginner.</td>
<td>[https://www.youtube.com/channel/UCFaPNTDJga0Ebwvftju9jMQ/about](https://www.youtube.com/channel/UCFaPNTDJga0Ebwvftju9jMQ/about)</td>
<td>Short topic videos that students can look up when stuck on one function.</td>
<td>background. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Cases for Teaching (12)
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
<td>From Jupyter notebooks to websites with Quarto (PyData workshop) and Teaching Quarto in introductory data science courses</td>
<td>Mine Çetinkaya-Rundel (Duke University and Posit), 2024, workshop site and conference talk</td>
<td>[https://mine.quarto.pub/quarto-pydata/](https://mine.quarto.pub/quarto-pydata/)</td>
<td>The Python-specific Quarto workshop from the person who designed the modern intro data science course: notebook to document to website to slides, with GitHub Pages publishing. The "teach with Quarto" talk explains how she structures lectures, labs and homework as Quarto projects in STA 199 (R, [https://mine.quarto.pub/sta-199/](https://mine.quarto.pub/sta-199/)), which is the template to port.</td>
<td>session 1 (adapt the workshop as the first lab) and session 5 (publishing the final project); free.</td>
<td>neu; in Suchergebnis bestätigt</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>LSE DS105 Data for Data Science (and the Quarto course-website template)</td>
<td>Jon Cardoso-Silva, LSE Data Science Institute, 2022-2026 (rolling), public course website and GitHub template</td>
<td>[https://lse-dsi.github.io/DS105/](https://lse-dsi.github.io/DS105/)</td>
<td>A full undergraduate Python course for coding beginners in a social-science school, built entirely in Quarto and GitHub Pages: pandas, lets-plot (grammar of graphics, a plotnine sibling), Jupyter and Quarto notebooks, Git and GitHub, weekly labs with public solutions. The template repository documents the Python environment set-up and is reused for DS101, DS202 and ME204.</td>
<td>sessions 1-2 (borrow lab structure; the week 2 and 3 labs on loading and reshaping data are the closest analogue); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Posit Academy: Foundations of Python for Data Science</td>
<td>Posit PBC, 2024-2026, mentor-led course with public project repositories</td>
<td>[https://academy.posit.co/](https://academy.posit.co/)</td>
<td>The closest commercial analogue to the course stack: Positron IDE, Quarto .qmd milestones, uv environments, pandas, plotnine, statsmodels and scikit-learn, organised around one real dataset per project with weekly mentor sessions. The public repos show how Posit scaffolds a beginner project (data folder, milestone files, environment file).</td>
<td>session 1-2 (copy the milestone structure for the group project); course paid (enterprise pricing), repos free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>UConn STAT 3255/5255 Introduction to Data Science (Python, Quarto)</td>
<td>Jun Yan and students, University of Connecticut Department of Statistics, Spring 2025 (editions back to 2022), open course notes</td>
<td>[https://statds.github.io/ids-s25/](https://statds.github.io/ids-s25/)</td>
<td>A Python data science course whose entire textbook is a Quarto book written and extended by the students themselves (each student contributes a chapter via pull request): Python basics, pandas, visualisation (a plotnine section exists in earlier editions), SQL, modelling, with a chapter on reproducible data science with Quarto. A worked example of Quarto plus GitHub as the course infrastructure.</td>
<td>background (model for the "students contribute to a shared Quarto site" assignment); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Data Science: A First Introduction (Python edition)</td>
<td>Tiffany Timbers, Trevor Campbell, Melissa Lee, Joel Ostblom and Lindsey Heagy, University of British Columbia, 2023-2025, open textbook (CC BY-NC-SA)</td>
<td>[https://python.datasciencebook.ca/](https://python.datasciencebook.ca/)</td>
<td>A full first-year data science textbook in Python with Jupyter, pandas and Altair, a direct port of the R edition (tidyverse, ggplot2). Chapters on wrangling, visualisation, classification, regression and clustering are each a lab with worksheets, and the book's "reading, wrangling, visualising, communicating" arc matches a five-session structure.</td>
<td>sessions 2-4 (lab readings; translate Altair to plotnine); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>BYU-Idaho CSE 250 Data Science Programming</td>
<td>J. Hathaway and colleagues, Brigham Young University-Idaho, 2021-2026 (rolling), public course site</td>
<td>[https://byuistats.github.io/CSE250-Course/](https://byuistats.github.io/CSE250-Course/)</td>
<td>A project-based Python course for non-computer-science students that teaches the grammar of graphics, pandas and Altair, and requires every project to be a rendered Quarto document; includes a Python port of R for Data Science and a baseball database project. Good source of small graded projects with public rubrics.</td>
<td>sessions 2-3 (project templates and rubrics); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Penn MUSA 550 Geospatial Data Science in Python: "From notebooks to the web: Quarto and GitHub Pages"</td>
<td>Nick Hand, University of Pennsylvania Weitzman School, Fall 2023, public course site and lecture</td>
<td>[https://musa-550-fall-2023.github.io/content/week-9/lecture-9A.html](https://musa-550-fall-2023.github.io/content/week-9/lecture-9A.html)</td>
<td>A single, well-structured lecture that takes a Python Jupyter workflow to a published Quarto website with interactive charts on GitHub Pages, exactly the publishing step students struggle with. The whole course is itself a Quarto site built from notebooks.</td>
<td>session 5 (lab on publishing the final report); free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Practical Data Science with Python (Duke MIDS IDS 720)</td>
<td>Nick Eubank, Duke University, 2019-2026 (rolling), public course site and textbook</td>
<td>[https://www.practicaldatascience.org/](https://www.practicaldatascience.org/)</td>
<td>Flipped, exercise-heavy course on wrangling messy real data with pandas, git and GitHub, written for students from social science and policy backgrounds; includes a "welcome non-Duke students" page that makes it usable as self-study. Its "defensive programming" and "what to do when you are stuck" pages are directly reusable for an AI-assisted course. Quarto use not confirmed.</td>
<td>sessions 1-2 (reading on data cleaning habits); free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Companion notebooks for Python for Marketing Research and Analytics, and SAGE resources for Applied Marketing Analytics Using Python</td>
<td>Schwarz, Chapman and Feit (GitHub, Apache 2.0, 2020-2024) and Yildirim and Kübler (SAGE instructor resources, 2025)</td>
<td>[https://github.com/python-marketing-research/python-marketing-research-1ed](https://github.com/python-marketing-research/python-marketing-research-1ed)</td>
<td>The two ready-made sets of marketing teaching cases in Python: segmentation, satisfaction drivers and choice (Schwarz et al.) and MMM, attribution, churn and forecasting (Yildirim and Kübler), each with datasets and notebooks. Both are pandas-based, so the natural assignment is "rewrite this analysis in polars and plotnine and present it as a Great Tables report".</td>
<td>sessions 3-4 (cases); GitHub free, SAGE resources require instructor registration.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Business-school cases with datasets: "Applying Data Science and Analytics at P&G" and the HBP cases-with-datasets collection</td>
<td>Harvard Business School (case) and Harvard Business Publishing Education (collection), 2020-2025, teaching cases</td>
<td>[https://www.hbs.edu/faculty/Pages/item.aspx?num=58380](https://www.hbs.edu/faculty/Pages/item.aspx?num=58380)</td>
<td>The P&G case covers how a consumer-goods marketer built dashboards and analytics teams, a good discussion frame for "what a report should do for a manager". The HBP collection filters cases that ship with a dataset, which is what a polars and Quarto lab needs; Ivey Publishing has an equivalent filter.</td>
<td>session 5 (discussion case on reporting and dashboards); paid (HBP, about USD 5 to 9 per student copy).</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>Quarto dashboards with Python (official guide) and a business-school example</td>
<td>Posit (Quarto documentation, 2023-2026) and Wake Forest School of Business ("Create your own data blog with Quarto and Python", class listing, 2024)</td>
<td>[https://quarto.org/docs/dashboards/](https://quarto.org/docs/dashboards/)</td>
<td>Quarto dashboards turn a .qmd with polars, plotnine or Plotly cells into a static dashboard (value boxes, tabsets, sidebars) deployable on GitHub Pages, so students can produce a manager-facing dashboard without Shiny or Tableau. The Wake Forest listing shows a business school already teaching Quarto with Python as a career skill.</td>
<td>session 5 (lab: convert the group report into a dashboard); free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Cases for Teaching</td>
<td>University of Edinburgh "Introduction to Data Analysis" course repositories</td>
<td>University of Edinburgh School of Mathematics (edinburgh-data-science GitHub organisation), 2016-2024, course repositories</td>
<td>[https://github.com/edinburgh-data-science](https://github.com/edinburgh-data-science)</td>
<td>Second-year undergraduate data analysis course built around McKinney's Python for Data Analysis, plus a first-year Foundations of Data Science course; useful mainly as an example of a mathematics department teaching Python data analysis from a free textbook. Little recent activity and no Quarto, so a weaker example than the others; the Carpentries at Edinburgh ([https://edcarp.github.io/](https://edcarp.github.io/)) run current Python workshops.</td>
<td>background; free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Praxisbeispiele (11)
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
<td>Polars at Decathlon: Ready to Play? (Spark to polars)</td>
<td>Arnaud Vennin (Decathlon Digital), Polars blog, 15 September 2025, case (also on Medium and covered by InfoQ, December 2025).</td>
<td>[https://pola.rs/posts/case-decathlon/](https://pola.rs/posts/case-decathlon/)</td>
<td>A European sports retailer replacing Spark jobs with single-machine polars to cut cost and complexity; a retail analytics story students recognise.</td>
<td>session 1 motivation slide. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>BMLL, Citizens, Double River, Vydia, Rabobank and La Mobilière case studies (Polars blog)</td>
<td>Polars, 2024 to 2026, cases: BMLL (1.5 TB of market data in under four minutes, 48x faster than pandas), Citizens bank (analyst empowerment), Double River Investments (plugins), Vydia (music CSV processing), Rabobank (window functions), La Mobilière (Swiss insurer).</td>
<td>[https://pola.rs/posts/case-bmll/](https://pola.rs/posts/case-bmll/)</td>
<td>Short, concrete production stories including two European financial firms (Rabobank, La Mobilière); the Citizens case is about analysts, not engineers, which matches the course audience.</td>
<td>background; one or two quoted in session 1. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>KS&R: hundreds of personalised PDF reports weekly with Quarto (Posit customer story)</td>
<td>Posit customer story, 2024 to 2025, case (KS&R Decision Sciences and Innovation team, a market research firm).</td>
<td>[https://posit.co/about/customer-stories](https://posit.co/about/customer-stories)</td>
<td>A market research company replacing a legacy reporting pipeline with parameterised Quarto reports; the closest documented match to what marketing analysts do.</td>
<td>session 5 case for parameterised reports. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Bay FC: weekly match reports with Quarto and Posit Connect</td>
<td>Posit customer story with Arielle Dror (Director of Data and Analytics, Bay FC, NWSL), 2025, case.</td>
<td>[https://posit.co/about/customer-stories](https://posit.co/about/customer-stories)</td>
<td>Sports marketing adjacent: automated weekly reports for coaches and recruitment, showing Quarto as the delivery layer rather than a notebook.</td>
<td>session 5 example. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>University of Connecticut, Introduction to Data Science (STAT 3255/5255) taught in Python with Quarto</td>
<td>Jun Yan, University of Connecticut, 2025, course website and book built with Quarto, Python throughout; chapter "Reproducible data science" explains Quarto for homework, notes and presentations.</td>
<td>[https://statds.github.io/ids-s25/quarto.html](https://statds.github.io/ids-s25/quarto.html)</td>
<td>A full university course where students submit Quarto documents via GitHub; a template for assessment workflow.</td>
<td>background for course design. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Teaching (with) Quarto (Mine Çetinkaya-Rundel, Duke)</td>
<td>Mine Çetinkaya-Rundel, 2023 to 2024, talk and website on building course sites, slides and assignments with Quarto, plus "Using Quarto to make and organise teaching materials" (Maria Tackett, JSM).</td>
<td>[https://mine-cetinkaya-rundel.github.io/teach-with-quarto/](https://mine-cetinkaya-rundel.github.io/teach-with-quarto/)</td>
<td>The reference pattern for a Quarto course website with GitHub Classroom; the author also leads the Python-inclusive dashboard workshop above.</td>
<td>background for course design. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Coding for Economists (Bank of England economist, plotnine chapter)</td>
<td>Arthur Turrell (economist, formerly Bank of England and ONS Data Science Campus), 2021 to 2026, free online book built with Jupyter Book.</td>
<td>[https://aeturrell.github.io/coding-for-economists/vis-plotnine.html](https://aeturrell.github.io/coding-for-economists/vis-plotnine.html)</td>
<td>A practising economist teaching plotnine to non-programmers with economic data; the closest documented analogue to a business-school plotnine course.</td>
<td>session 2 reading. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Great Tables for scientific publishing and Great Tables + marimo</td>
<td>Posit Great Tables blog, 2024 to 2025, articles ("Great Tables for scientific publishing"; Jerry Wu, "Great Tables + marimo = interactive tables").</td>
<td>[https://posit-dev.github.io/great-tables/blog/tables-for-scientific-publishing/](https://posit-dev.github.io/great-tables/blog/tables-for-scientific-publishing/)</td>
<td>Worked, real tables (not toy data) and a reactive-notebook integration that shows how far the HTML table model stretches.</td>
<td>session 3 background. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Why a University of Pittsburgh professor standardised his teaching on marimo</td>
<td>marimo blog, 2025, case (University of Pittsburgh "Writing Machines" course; also Utrecht University WASM apps and a Stanford course).</td>
<td>[https://marimo.io/blog/case-study-pitt](https://marimo.io/blog/case-study-pitt)</td>
<td>Documented classroom use of reactive Python notebooks with no-install WebAssembly delivery; relevant if the course wants in-browser exercises beyond Quarto Live.</td>
<td>background. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Plotnine Contest 2024 gallery and tashapiro's python-plotnine workshop</td>
<td>Posit (2024 Plotnine Contest entries now in the plotnine gallery) and Tanya Shapiro's workshop for R-Ladies Cologne and Paris and PyLadies Tunis and Munich, 2023 to 2024, examples.</td>
<td>[https://plotnine.org/gallery/index.html](https://plotnine.org/gallery/index.html)</td>
<td>The closest thing to data-journalism-grade plotnine work: polished, annotated charts with full code, including Economist-style themes that students can copy.</td>
<td>session 2 inspiration and theme templates. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Praxisbeispiele</td>
<td>Jeroen Janssens: Plotnine with Polars 1.0 (worked example)</td>
<td>Jeroen Janssens (Posit), 2024, blog post rebuilding a classic ggplot2 tutorial with polars and plotnine.</td>
<td>[https://jeroenjanssens.com/plotnine/](https://jeroenjanssens.com/plotnine/)</td>
<td>A documented end-to-end example in exactly the course stack, by the author of the polars reference book.</td>
<td>session 2 worked example. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Software (20)
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
<td>polars</td>
<td>Ritchie Vink and Polars contributors, 2020 to 2026, software (Python bindings to a Rust query engine). Version 1.44.2 on PyPI, released 9 September 2026; 2.0.0-rc.2 published 20 September 2026 (new Map dtype, streaming engine as default). MIT licence, Python 3.10 or later.</td>
<td>[https://pypi.org/project/polars/](https://pypi.org/project/polars/)</td>
<td>Eager DataFrame and lazy LazyFrame (pl.scan_csv(...).filter(...).group_by(...).agg(...).collect()), an expression API with no index, multi-threaded out of the box, to_pandas() via pyarrow for statsmodels and seaborn, .plot backed by Altair. Mature (1.x since July 2024) with a very large user base; the 2.0 release is imminent, so pin the major version in the course environment.</td>
<td>session 1 lab (reading CSV and parquet, select, filter, group_by, joins), session 4 (lazy pipelines on larger panel data). Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>plotnine</td>
<td>Hassan Kibirige (maintained with Posit support), 2017 to 2026, software. Version 0.15.8, 14 August 2026, MIT, Python 3.10 or later.</td>
<td>[https://pypi.org/project/plotnine/](https://pypi.org/project/plotnine/)</td>
<td>A faithful grammar-of-graphics port of ggplot2: ggplot(df, aes(...)) + geom_\*() + facet_wrap() + theme_\*(), with scales, stats, labels, built-in themes (theme_minimal, theme_bw, theme_538, theme_xkcd) and, since 0.15 (2025), plot composition with \| and /, HCL colour space and better facet strips. Accepts polars frames (converted to pandas internally). Renders through matplotlib, so PNG, SVG and PDF output work in Quarto.</td>
<td>session 2 lab and all later sessions for figures; ggplot2 tutorials transfer almost one to one. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Great Tables</td>
<td>Rich Iannone and Michael Chow, Posit, 2023 to 2026, software. Version 1.0.0, 25 September 2026, MIT, Python 3.10 or later.</td>
<td>[https://pypi.org/project/great-tables/](https://pypi.org/project/great-tables/)</td>
<td>Python port of R's gt: header, stub, spanners, fmt_number, fmt_currency, fmt_percent, tab_style, data_color, nanoplots (fmt_nanoplot, line and bar sparklines with hover values), polars selectors in columns=, [http://pl.DataFrame.style](http://pl.DataFrame.style) returning a GT, save() to PNG and native HTML rendering in Quarto; LaTeX output exists but nanoplots do not render to PDF yet. 1.0 added load_dataset(), fmt_url, tab_style_body and HTML escaping by default (breaking for anyone injecting raw HTML).</td>
<td>session 3 lab (summary tables for a market comparison), session 5 project reports. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Quarto CLI</td>
<td>Posit (J.J. Allaire, Carlos Scheidegger, Charlotte Wickham and others), 2022 to 2026, software. Stable v1.10.18, 24 July 2026 (also on PyPI as quarto-cli 1.10.18, so uv add quarto-cli installs it into the project); pre-release v1.11.5, 17 September 2026. MIT.</td>
<td>[https://github.com/quarto-dev/quarto-cli/releases](https://github.com/quarto-dev/quarto-cli/releases)</td>
<td>One .qmd (or .ipynb) renders to HTML, revealjs slides, pptx, docx, PDF (LaTeX or Typst), dashboards (format: dashboard with cards and value boxes) and manuscripts (type: manuscript project with notebook embedding). Python cells run through a Jupyter kernel (ipykernel), parameterised reports via the Jupyter engine, brand.yml theming since 1.6, accessibility checks in 1.8. Quarto 2, a Rust rewrite with a collaborative editor, was announced on 6 April 2026 for late 2026 and promises backward compatibility.</td>
<td>sessions 3 and 5 (reports, slides, GitHub Pages deployment); background for all labs since Positron edits and previews .qmd natively. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Quarto Live (r-wasm/quarto-live)</td>
<td>George Stagg, Posit, 2024 to 2026, software (Quarto extension), MIT; version not read (unverified).</td>
<td>[https://github.com/r-wasm/quarto-live](https://github.com/r-wasm/quarto-live)</td>
<td>Pyodide-powered \{pyodide\} code cells and graded exercises (hints, solutions, custom checks) that run in the student's browser on a static site; polars has a Pyodide build, so simple polars and plotnine exercises can be served from GitHub Pages without a server.</td>
<td>background; candidate for self-study pages in sessions 1 and 2. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pandas</td>
<td>pandas development team (NumFOCUS), 2008 to 2026, software. Version 3.0.6, 17 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
<td>[https://pypi.org/project/pandas/](https://pypi.org/project/pandas/)</td>
<td>Still the interchange format: plotnine, seaborn and statsmodels formulas consume pandas frames, and polars to_pandas() and pl.from_pandas() make the round trip cheap. pandas 3.0 (2026) changed defaults (copy-on-write, string dtype), which is why older tutorials sometimes warn.</td>
<td>background; teach to_pandas() in session 4 before statsmodels. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>narwhals</td>
<td>Marco Gorelli and contributors, 2024 to 2026, software. Version 2.26.0, 8 September 2026, MIT.</td>
<td>[https://pypi.org/project/narwhals/](https://pypi.org/project/narwhals/)</td>
<td>Thin compatibility layer that lets libraries (Altair, Plotly, marimo, scikit-lego and others) accept polars, pandas, DuckDB and pyarrow inputs without depending on any of them. Explains to students why polars "just works" in Altair and marimo.</td>
<td>background only. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pyarrow</td>
<td>Apache Arrow project, 2016 to 2026, software. Version 25.0.1, 10 August 2026, Apache-2.0.</td>
<td>[https://pypi.org/project/pyarrow/](https://pypi.org/project/pyarrow/)</td>
<td>Columnar memory format underneath polars, pandas 3 strings, DuckDB and parquet I/O; required for zero-copy to_pandas() and for reading parquet in the labs.</td>
<td>background dependency, mention in session 1. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>DuckDB</td>
<td>DuckDB Foundation, 2019 to 2026, software. Version 1.5.6, 28 September 2026, MIT.</td>
<td>[https://pypi.org/project/duckdb/](https://pypi.org/project/duckdb/)</td>
<td>In-process SQL engine that queries polars and pandas frames and parquet files directly (duckdb.sql("select ... from df").pl()); the natural bridge for students who already know SQL and for larger-than-memory panel data.</td>
<td>optional in session 4 for SQL-minded students. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Altair (Vega-Altair)</td>
<td>Jake VanderPlas and contributors, 2016 to 2026, software. Version 6.3.0, 15 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
<td>[https://pypi.org/project/altair/](https://pypi.org/project/altair/)</td>
<td>Declarative interactive charts; polars' built-in df.plot.\* uses Altair, and Altair accepts polars frames natively via narwhals. The interactive counterpart to plotnine for HTML dashboards.</td>
<td>session 5 dashboards; otherwise alternative to plotnine. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>matplotlib</td>
<td>matplotlib development team, 2003 to 2026, software. Version 3.11.2, 11 September 2026, PSF-style licence.</td>
<td>[https://pypi.org/project/matplotlib/](https://pypi.org/project/matplotlib/)</td>
<td>Rendering backend for plotnine (and for pandas .plot); needed to save figures at print resolution and to tweak the occasional detail plotnine does not expose.</td>
<td>background dependency. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>seaborn</td>
<td>Michael Waskom, 2012 to 2024, software. Version 0.13.2, 25 January 2024 (no release since), BSD-3-Clause.</td>
<td>[https://pypi.org/project/seaborn/](https://pypi.org/project/seaborn/)</td>
<td>Popular statistical plotting on pandas; the seaborn.objects interface is grammar-like. Stable but slow-moving and pandas-only, so it is the comparison point rather than the course tool; AI assistants often suggest it, which students should recognise.</td>
<td>background, "why not seaborn" note in session 2. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>marimo</td>
<td>marimo team (Akshay Agrawal, Myles Scolnick), 2023 to 2026, software. Version 0.25.1, 1 October 2026, Apache-2.0.</td>
<td>[https://pypi.org/project/marimo/](https://pypi.org/project/marimo/)</td>
<td>Reactive, git-friendly notebooks stored as .py, with built-in polars support and a documented Great Tables integration; runs as an app or in WebAssembly. Useful alternative to Jupyter for exploratory work, though Quarto remains the reporting layer.</td>
<td>background; possible demo in session 1. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>JupyterLab and ipykernel</td>
<td>Project Jupyter, 2015 to 2026, software. JupyterLab 4.6.4, 21 September 2026, BSD-3-Clause.</td>
<td>[https://pypi.org/project/jupyterlab/](https://pypi.org/project/jupyterlab/)</td>
<td>Quarto executes Python through a Jupyter kernel, so ipykernel (and optionally JupyterLab) must be in the project environment even when students never open a notebook; Positron handles kernels but the dependency is still required.</td>
<td>session 1 environment setup. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>uv</td>
<td>Astral, 2024 to 2026, software. Version 0.12.23, 3 October 2026, MIT or Apache-2.0.</td>
<td>[https://pypi.org/project/uv/](https://pypi.org/project/uv/)</td>
<td>Fast project and Python manager: uv init, uv add polars plotnine great-tables ipykernel quarto-cli, uv run quarto render, with a lock file committed to GitHub so every student reproduces the same environment.</td>
<td>session 1 setup and the course template repository. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>statsmodels</td>
<td>statsmodels developers, 2009 to 2026, software. Version 0.15.0, 27 August 2026, BSD-3-Clause.</td>
<td>[https://pypi.org/project/statsmodels/](https://pypi.org/project/statsmodels/)</td>
<td>Formula interface (smf.ols("sales \~ price + adstock", data=[http://df.to_pandas(](http://df.to_pandas())).fit().summary()) with the regression tables marketing students expect; pandas input only, which is the main reason to teach to_pandas().</td>
<td>session 4 regression and simple marketing-mix models. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>scikit-learn</td>
<td>scikit-learn developers, 2007 to 2026, software. Version 1.9.1, 10 September 2026, BSD-3-Clause, Python 3.11 or later.</td>
<td>[https://pypi.org/project/scikit-learn/](https://pypi.org/project/scikit-learn/)</td>
<td>Accepts polars frames directly and can return polars output (set_output(transform="polars")), so pipelines for segmentation (k-means) or churn classification stay in polars.</td>
<td>session 4 optional segmentation lab. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>polars-ols</td>
<td>Azmy Rajab, 2024, software (polars plugin). Version 0.3.5, 25 August 2024, licence not declared on PyPI (MIT on GitHub, unverified).</td>
<td>[https://pypi.org/project/polars-ols/](https://pypi.org/project/polars-ols/)</td>
<td>OLS, WLS, ridge and rolling regressions as polars expressions with a patsy-style formula (pl.col("y").least_squares.ols(...)), handy for per-country regressions inside group_by. Little maintenance since 2024; for teaching, prefer statsmodels and mention this as an advanced option (polars-statistics is a newer alternative).</td>
<td>session 4 stretch material. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Software</td>
<td>pins (Python)</td>
<td>Posit (Isabel Zimmerman, Michael Chow), 2022 to 2025, software. Version 0.9.1, 3 October 2025, MIT.</td>
<td>[https://pypi.org/project/pins/](https://pypi.org/project/pins/)</td>
<td>Versioned sharing of dataframes to a folder, S3, Azure or Posit Connect with [http://board.pin_write(df](http://board.pin_write(df), "sales"); a simple way to distribute course datasets without committing CSVs to git.</td>
<td>background for the instructor. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Software</td>
<td>Ibis</td>
<td>Ibis project (Voltron Data origins, now community), 2015 to 2026, software. Version 12.0.0, 7 February 2026, Apache-2.0.</td>
<td>[https://pypi.org/project/ibis-framework/](https://pypi.org/project/ibis-framework/)</td>
<td>One dataframe API that compiles to DuckDB, Postgres, BigQuery, Snowflake and polars; shows students how the same expression logic scales to a warehouse.</td>
<td>background only. Free.</td>
<td>neu; Link geprüft</td>
</tr>
</table>
### Data (12)
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
<td>Palmer penguins (palmerpenguins, also bundled in plotnine)</td>
<td>Allison Horst, Alison Hill and Kristen Gorman (R package), Python port by Muhammad Chenariyan Nakhaee, 2020 to 2026, dataset package (0.1.6, 1 February 2026). CC0. 344 rows, 8 columns.</td>
<td>[https://pypi.org/project/palmerpenguins/](https://pypi.org/project/palmerpenguins/)</td>
<td>The standard first dataset for aesthetics, facets and group-by; [http://plotnine.data.penguins](http://plotnine.data.penguins) means no extra install. Not marketing, but ideal for the first plotnine lab.</td>
<td>session 2 warm-up. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Gapminder (gapminder Python package)</td>
<td>Jennifer Bryan (R), Python port by Jeff Stafford, 2018, dataset package (0.1, BSD-3-Clause). 1,704 rows, 6 columns (country, continent, year, life expectancy, population, GDP per capita, 1952 to 2007).</td>
<td>[https://pypi.org/project/gapminder/](https://pypi.org/project/gapminder/)</td>
<td>International by construction; perfect for facets by continent, log scales and animated or faceted time series, and for a first Great Tables country comparison.</td>
<td>sessions 1 and 2 labs, session 3 table demo. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>plotnine built-in datasets</td>
<td>plotnine ([http://plotnine.data](http://plotnine.data)), 2017 to 2026, 18 datasets ported from ggplot2: mpg, diamonds (about 54,000 rows), economics and economics_long, txhousing (8,602 rows), midwest, msleep, mtcars, penguins, presidential, anscombe_quartet and others. MIT with the package.</td>
<td>[https://github.com/has2k1/plotnine/tree/main/plotnine/data](https://github.com/has2k1/plotnine/tree/main/plotnine/data)</td>
<td>Every plotnine example and most ggplot2 tutorials use these, so students can follow any ggplot2 material directly; diamonds (prices by quality) and txhousing (sales by city and month) have a pricing and sales feel.</td>
<td>session 2 exercises. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Great Tables bundled datasets</td>
<td>Posit, 2024 to 2026, 16 datasets via great_[http://tables.data](http://tables.data) or load_dataset() (pandas or polars): gtcars (47 deluxe cars, 15 columns, prices and specs by country of origin), sza (solar zenith angles, 816 rows), towny (414 Ontario municipalities, population 1996 to 2021), countrypops (13,545 rows, country populations 1960 to 2022), sp500 (16,607 daily rows), pizzaplace (49,574 pizza sales rows), metro, films, peeps, exibble. MIT with the package.</td>
<td>[https://github.com/posit-dev/great-tables/blob/main/great_tables/data/__init__.py](https://github.com/posit-dev/great-tables/blob/main/great_tables/data/__init__.py)</td>
<td>gtcars (car prices by manufacturer country) and pizzaplace (a year of sales by category and size) are natural marketing tables; countrypops gives nanoplot time series per country.</td>
<td>session 3 lab. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>nycflights13 (Python port)</td>
<td>Hadley Wickham (R), Python port by Michael Chow, 2020, dataset package (0.0.3, CC0). Five tables: flights (336,776 rows), airlines, airports, planes, weather.</td>
<td>[https://pypi.org/project/nycflights13/](https://pypi.org/project/nycflights13/)</td>
<td>The classic relational dataset for joins and lazy pipelines at a size where polars' speed is noticeable; many dplyr tutorials use it.</td>
<td>session 1 or 4 joins lab. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Kaggle: Customer Personality Analysis (marketing campaign)</td>
<td>Akash Patel (Kaggle), 2021, dataset (2,240 customers, 29 columns: demographics, spend by product category, campaign responses, channel usage). CC0.</td>
<td>[https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)</td>
<td>Small, clean, genuinely marketing (campaign acceptance, RFM-style spend) and widely used for segmentation tutorials; good for group_by and scikit-learn clustering.</td>
<td>session 4 segmentation lab. Free (Kaggle account needed).</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>UCI Online Retail II</td>
<td>Daqing Chen, London South Bank University, UCI Machine Learning Repository, 2019 (data 2009 to 2011), dataset (about 1 million transaction lines, UK gift wholesaler, customers in over 40 countries). CC BY 4.0 at UCI; Kaggle mirrors.</td>
<td>[https://archive.ics.uci.edu/datasets?search=Online+Retail](https://archive.ics.uci.edu/datasets?search=Online+Retail)</td>
<td>International transactions by country with invoices, quantities and prices: ideal for revenue by country tables, time series by month and a "lazy pipeline on a million rows" demonstration.</td>
<td>sessions 1, 3 and 4. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Dunnhumby: The Complete Journey (completejourney-py)</td>
<td>dunnhumby, 2014, dataset (2,500 households, two years, eight tables: transactions of about 2.6 million lines, demographics, products, campaigns, coupons, redemptions, causal data); Python package completejourney-py 0.1.0 (November 2025, MIT, mirrors the R package). Data under dunnhumby's source-files terms (free for non-commercial use).</td>
<td>[https://pypi.org/project/completejourney-py/](https://pypi.org/project/completejourney-py/)</td>
<td>The best free retail loyalty-card dataset: campaign and coupon effects, basket analysis, household panels. US only, so pair with Eurostat or Online Retail II for the international angle.</td>
<td>session 4 case on promotion effects. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Eurostat via the eurostat package</td>
<td>Eurostat (data, CC BY 4.0) and Noemi Emanuela Cazzaniga's eurostat package 1.1.1 (June 2024, MIT), API client (get_data_df("prc_hicp_manr") returns a pandas frame; wrap with pl.from_pandas).</td>
<td>[https://pypi.org/project/eurostat/](https://pypi.org/project/eurostat/)</td>
<td>Live European data (retail trade volumes, e-commerce usage, HICP by country, tourism nights) for country-comparison tables and faceted plots; sizes range from a few hundred to millions of rows depending on the table.</td>
<td>sessions 2 and 3 international comparisons. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>World Bank via wbgapi</td>
<td>World Bank (World Development Indicators, CC BY 4.0) and Tim Herzog's wbgapi 1.0.14 (February 2026, MIT), API client ([http://wb.data.DataFrame("http://NY.GDP.PCAP.CD"](http://wb.data.DataFrame("http://NY.GDP.PCAP.CD"), time=range(2000, 2024))).</td>
<td>[https://pypi.org/project/wbgapi/](https://pypi.org/project/wbgapi/)</td>
<td>Market-sizing variables (GDP per capita, internet users, urban population) for 200+ economies, directly as wide or long pandas frames.</td>
<td>session 4 market attractiveness exercise. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Our World in Data: Chart API and owid-catalog</td>
<td>Our World in Data, 2024 to 2026, data API (append .csv to any grapher URL, e.g. [https://ourworldindata.org/grapher/life-expectancy.csv](https://ourworldindata.org/grapher/life-expectancy.csv)) and Python package owid-catalog 1.2.7 (October 2026, MIT). Data CC BY 4.0 (underlying sources vary).</td>
<td>[https://docs.owid.io/projects/etl/api/chart-api/](https://docs.owid.io/projects/etl/api/chart-api/)</td>
<td>One-line [http://pl.read_csv(url](http://pl.read_csv(url)) for thousands of curated country-year series with metadata; the simplest live international data source for a beginner lab.</td>
<td>session 1 (reading data from a URL) and session 2. Free.</td>
<td>neu; Link geprüft</td>
</tr>
<tr>
<td>Data</td>
<td>Kaggle: Marketing Campaign Performance Dataset</td>
<td>Manisha Bhatt (Kaggle), 2023, dataset (200,000 rows: campaign type, channel, target audience, impressions, clicks, conversion rate, acquisition cost, ROI, location, language). Synthetic; licence as listed on Kaggle (unverified).</td>
<td>[https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset](https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset)</td>
<td>Large enough to show polars speed and has channel and language fields for cross-market tables; because it is synthetic, use it for mechanics, not for substantive conclusions.</td>
<td>session 1 or 3 mechanics demo. Free.</td>
<td>neu; Link ungeprüft</td>
</tr>
</table>
