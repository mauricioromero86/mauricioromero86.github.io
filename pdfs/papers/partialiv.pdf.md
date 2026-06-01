---
title: "Using Instrumental Variables under Partial Observability of Endogenous Variables for Assessing Effects of Air Pollution on Health"
authors_and_venue: "with Tarik Benmarhnia and Prashant Bharadwaj"
abstract: "This paper highlights a common issue with instrumental variables (IV) techniques in evaluating the impact of air pollution on health. Since pollutants are almost always produced alongside other pollutants, instrumenting a single endogenous pollutant requires additional assumptions for correct inference and interpretation. We clarify these assumptions and propose that researchers place more structure on the relationship between the instrument and all the relevant pollutants."
pdf_url: "https://mauricio-romero.com/pdfs/papers/partialiv.pdf"
canonical_url: "https://mauricio-romero.com/pdfs/papers/partialiv.pdf.md"
source: research.qmd
note: >-
  Machine-readable Markdown version of the paper, generated for LLMs.
---

# Using Instrumental Variables for Assessing the Effects of Air

Pollution on Health: A Cautionary Tale<sup>∗</sup>

Tarik Benmarhnia† Prashant Bharadwaj‡ Mauricio Romero§

#### Abstract

This paper highlights a common issue with instrumental variables (IV) techniques in evaluating the impact of air pollution on health. Since pollutants are almost always produced alongside other pollutants, instrumenting a single endogenous pollutant requires additional assumptions for correct inference and interpretation. We clarify these assumptions and propose that researchers place more structure on the relationship between the instrument and all the relevant pollutants.

<sup>∗</sup>Corresponding author: Tarik Benmarhnia. E-mail: [tbenmarhnia@ucsd.edu.](mailto:tbenmarhnia@ucsd.edu) Romero acknowledges financial support from the Asociaci´on Mexicana de Cultura.

<sup>†</sup>University of California, San Diego - Department of Family Medicine and Public Health, and Scripps

<sup>‡</sup>University of California, San Diego - Department of Economics

ITAM - Centro de Investigaci´on Econ´omica

### 1 Introduction

Instrumental variable (IV) methods are frequently used to estimate causal effects in economics. In particular, air pollution and its effect on health is an area of research in which the use of IV methods is widespread. In this paper, we search the literature that uses IV methods to assess the impact of atmospheric air pollution on health outcomes and point out an important but largely unemphasized assumption implicit in most of these papers. The basis of this paper is simple: while instruments are often used to create plausibly exogenous variation in single pollutants, pollutants are generally co-produced. Hence, IV models treating a single pollutant as endogenous will yield biased estimates. The direction of bias depends on how co-pollutants interact with each other and with the instrument. In some cases, it is impossible to assess whether biased IV estimates are closer to the true parameters than OLS estimates.

We conducted a systematic search to identify all published literature on air pollution and health using IV methods through April 2017. Our goal was to illustrate the variety of studies conducted in this area and to highlight how exclusion criteria violations may occur.[1](#page-1-0) We searched keywords, titles, and abstracts in PubMed, Elsevier, Embase, and Web of Science.[2](#page-1-1) The boolean search used was: ("air pollution" OR "air quality") AND "instrumental variable\*" AND (health OR mortality OR morbidity OR hospital\* OR emergency).[3](#page-1-2) . Twenty-five studies fulfilled the inclusion criteria (see Panel A, Table [1\)](#page-2-0), although only a fraction of them (n=8) were relevant for the issues considered in this paper. Table [2](#page-13-0) lists the non-relevant studies. In Panel B, we show other articles that, based on our knowledge of the field, use IV methods to examine the causal effect of air pollution on health. The papers in Panel B are a selective subsample of a broader set of papers that may exist in this area. Combining the "relevant" papers from Panel A and the papers in Panel B, we examine a total of 20 papers.

IV methods are rather recent in this space (the earliest relevant study in our sample is from 2003). We categorize the types of IVs used in three groups: 1) IVs related to regulatory or economic shocks[\(Bombardini](#page-7-0) [& Li,](#page-7-0) [2016;](#page-7-0) [Chay & Greenstone,](#page-7-1) [2003b;](#page-7-1) [Deschenes et al.,](#page-8-0) [2012;](#page-8-0) [Lagravinese et al.,](#page-8-1) [2014\)](#page-8-1). Some studies used geographical variations in regulation [\(Chay et al.,](#page-7-2) [2003;](#page-7-2) [Chay & Greenstone,](#page-7-3) [2003a;](#page-7-3) [Gutierrez,](#page-8-2) [2015;](#page-8-2)

<span id="page-1-1"></span><span id="page-1-0"></span><sup>1</sup>The search was conducted on May 1, 2017.

<sup>2</sup>We did not use Google Scholar because its search function is limited to either the title or the entire body; it does not allow for abstract searches.

<span id="page-1-2"></span><sup>3</sup>For PubMed the exact search was: (((instrumental variable\*[Title/Abstract]) AND (Air quality[Title/Abstract] OR Air pollution[Title/Abstract])) AND (health [Title/Abstract] OR mortality[Title/Abstract] OR morbidity OR hospital\*[Title/Abstract] OR emergency[Title/Abstract])). For Eslevier it was: title-abs-key(instrumental variable\*) AND (titleabs-key(Air quality) OR title-abs-key(Air pollution)) AND (title-abs-key(health) OR title-abs-key(mortality) OR title-abskey(morbidity) OR title-abs-key(hospital\*) OR title-abs-key(emergency)). For Embase it was: 'instrumental variable\*':ab,ti AND ('air quality':ab,ti OR 'air pollution':ab,ti) AND ('health':ab,ti OR 'mortality':ab,ti OR 'morbidity':ab,ti OR 'hospital\*':ab,ti OR 'emergency':ab,ti). For Web of Science it was: TS=("instrumental variable\*") AND (TS=("Air quality") OR TS=("Air pollution")) AND TS=(health OR mortality OR morbidity OR hospital\* OR emergency).

| Table 1: Summary | table of studies us | ing IV the health | effects of air polli | ution |
|------------------|---------------------|-------------------|----------------------|-------|
|                  |                     |                   |                      |       |

<span id="page-2-0"></span>

| Study                                                                   | Journal                                                   | Location        | Health outc                                                  | ome    | Air pollutant                                                                                      | IV used                                                                                                           |
|-------------------------------------------------------------------------|-----------------------------------------------------------|-----------------|--------------------------------------------------------------|--------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Panel A: Relevant artciles fro                                          |                                                           |                 |                                                              | -      |                                                                                                    |                                                                                                                   |
| Ebenstein, Frank, and Reingewertz (2015)                                | The Israel Medicine Association Journal                   | Israel          | Hospital a                                                   | dmis-  | PM10                                                                                               | Sandstorms                                                                                                        |
| Knittel, Miller, and Sanders (2016)                                     | Review of Economics and<br>Statistics                     | USA             | Infant mortali                                               | ty     | PM10,CO                                                                                            | Fluctuations in traffic and their interaction with local weather conditions                                       |
| Lagravinese, Moscone, Tosetti,<br>and Lee (2014)                        | Regional Science and Urban Economics                      | Italy           | Hospital a<br>sions                                          | dmis-  | PM10, CO, NO2,<br>CO and O3                                                                        | Climate conditions and humar<br>activity (traffic congestion and<br>concentration of manufacturing<br>industries) |
| Moretti and Neidell (2011)                                              | Journal of Human Resources                                | USA             | Hospital a<br>sions                                          | dmis-  | O3, NO2 and CO                                                                                     | Boat traffic into the two major<br>ports of Los Angeles                                                           |
| Schlenker and Walker (2016)                                             | Review of Economic Studies                                | USA             | Hospital a<br>sions                                          | dmis-  | CO                                                                                                 | Variation in airport congestion<br>on the East Coast                                                              |
| Schwartz, Austin, Bind,<br>Zanobetti, and Koutrakis<br>(2015)           | American Journal of Epidemiology                          | USA             | Total mortality                                              | У      | PM 2.5                                                                                             | Back trajectories of air masses                                                                                   |
| Schwartz, Bind, and Koutrakis (2017)                                    | Environmental Health<br>Perspectives                      | USA             | Total mortality                                              | У      | $\begin{array}{ccc} \mathrm{PM2.5}, & \mathrm{BC}, & \mathrm{and} \\ \mathrm{NO2} & & \end{array}$ | Combined height of the plane-<br>tary boundary layer and wind<br>speed                                            |
| Tonne et al. (2010)                                                     | Occupational and Envi-<br>ronmental Medicine              | England         | Hospital a                                                   | dmis-  | NO(x)                                                                                              | Indicator for congestion charging<br>zone                                                                         |
|                                                                         | The Economic Journal                                      | Mexico          | Infant mortali                                               | ty     | PM10 & CO                                                                                          | Meteorological thermal inversions                                                                                 |
| Arceo-Gomez, Hanna, and Oliva<br>(in press)<br>Bombardini and Li (2016) | The Economic Journal Working Paper                        | Mexico<br>China | Infant mortali                                               |        | PM10 & CO<br>SO2                                                                                   | Meteorological thermal inversions Export shocks                                                                   |
| Chay and Greenstone (2003b)                                             | Quarterly Journal of Economics                            | USA             | Infant mortali                                               |        | TSP                                                                                                | Income shocks                                                                                                     |
| Chay and Greenstone (2003a)                                             | Working Paper                                             | USA             | Infant mortali                                               |        | TSP                                                                                                | Regulatory nonattainment status                                                                                   |
| Chay, Dobkin, and Greenstone (2003)                                     | The Journal of Risk and<br>Uncertainty                    | USA             | Adult mortalit                                               |        | TSP                                                                                                | Regulatory nonattainment sta-<br>tus                                                                              |
| Deryugina, Heutel, Miller, Molitor, and Reif (2016)                     | Working Paper                                             | USA             | Mortality, hos<br>ization rate, ar<br>tal hospital sp<br>ing | nd to- | PM 2.5                                                                                             | Changes in the local wind direction                                                                               |
| Deschenes, Greenstone, and<br>Shapiro (2012)                            | Working Paper                                             | USA             | Mortality and<br>pital admission                             |        | PM 2.5, O3, SO2,<br>and CO2                                                                        | Emissions cap and trade market                                                                                    |
| Gutierrez (2015)                                                        | Journal of Population<br>Economics                        | Mexico          | Infant mortali                                               | ty     | Aerosol Optical<br>Depth (AOD)                                                                     | Power plants in operation                                                                                         |
| He, Fan, and Zhou (2016)                                                | Journal of Environmental<br>Economics and Manage-<br>ment | China           | Total mortality                                              | У      | PM10                                                                                               | Olympic Games air pollution regulation                                                                            |
| Jayachandran (2009)                                                     | Journal of Human Resources                                | Indonesia       | Infant mortali                                               | ty     | Satellite based O3                                                                                 | Wildfire smoke                                                                                                    |
| Luechinger (2014)                                                       | Journal of Health Economics                               | Germany         | Infant mortali                                               | ty     | SO2                                                                                                | Regulatory desulfurization a<br>power plants, power plants' lo<br>cation and prevailing wind direc-<br>tion       |
| Zhong (2015)                                                            | Working Paper                                             | China           | Hospital a<br>sions                                          | dmis-  | NO2                                                                                                | Driving restrictions and superstitions concerning the number 4                                                    |

[Luechinger,](#page-8-8) [2014\)](#page-8-8) and one study took advantage of air pollution regulations in Beijing during the 2008 Olympic Games [\(He et al.,](#page-8-6) [2016\)](#page-8-6). 2) IVs related to variations in road, port, and airport traffic flows [\(Knittel](#page-8-4) [et al.,](#page-8-4) [2016;](#page-8-4) [Moretti & Neidell,](#page-9-0) [2011;](#page-9-0) [Schwartz et al.,](#page-9-2) [2015;](#page-9-2) [Zhong,](#page-10-0) [2015\)](#page-10-0). 3) IVs related to meteorological or other exogenous environmental events, like thermal inversions [\(Arceo-Gomez et al.,](#page-7-4) [in press\)](#page-7-4), changes in local wind direction [\(Deryugina et al.,](#page-8-5) [2016\)](#page-8-5), smoke from wildfires [\(Jayachandran,](#page-8-7) [2009\)](#page-8-7) or back trajectories of air masses [\(Schwartz et al.,](#page-9-2) [2015\)](#page-9-2) as IVs. One study used a combination of the three types of IV described above [\(Lagravinese et al.,](#page-8-1) [2014\)](#page-8-1).

As mentioned earlier, we want to highlight a particular violation of the exclusion restriction that is likely to occur in settings where the exposure or treatment is an aggregate variable such as air pollution (e.g., PM10 and CO) and the chosen IV (e.g., thermal inversions) affects this aggregate variable but the researcher only observes a part of what makes up overall air pollution. The converse, where the parameter of interest is the impact of a specific component of an aggregate variable (PM10, rather than overall pollution) but the instrument affects the aggregate variable (pollution), is another form of the same exclusion restriction violation. Some of the papers identified in Table [1](#page-2-0) address the issue we highlight in this paper [\(Deryugina](#page-8-5) [et al.,](#page-8-5) [2016;](#page-8-5) [Moretti & Neidell,](#page-9-0) [2011;](#page-9-0) [Zhong,](#page-10-0) [2015\)](#page-10-0). [Deschenes et al.](#page-8-0) [\(2012\)](#page-8-0) even acknowledge the possibility of violating the exclusion restriction (p. 16-17) by including various pollutants affected by a common IV.[4](#page-3-0)

### 2 The basic IV setting

To fix ideas, suppose we want to measure the effect of pollution on a health outcome (y) and that the true relationship between the two is:

$$y = x_1 \beta_1 + x_2 \beta_2 + \varepsilon, \tag{1}$$

where x<sup>1</sup> is one component of pollution (e.g., PM10), and x<sup>2</sup> is another component of pollution (e.g., CO2). For ease of exposition and without loss of generality, assume all variables have been standardized such that V (X1) = V (x2) = V (ε) = 1.

Additionally, assume cov(x1, ε) 6= 0, so that x<sup>1</sup> is endogenous. Suppose the statistician only observes x1. If the statistician were to estimate the following regression

$$y = x_1 \beta_1 + \eta \tag{2}$$

<span id="page-3-0"></span><sup>4</sup>The authors of two studies claim to have met this exclusion restriction [\(Knittel et al.,](#page-8-4) [2016;](#page-8-4) [Schwartz et al.,](#page-9-2) [2015\)](#page-9-2).

where η = x2β<sup>2</sup> + ε then

$$\widehat{\beta_1^{ols}} = (x_1'x_1)^{-1}x_1'y 
\to_p V(x_1)^{-1}cov(x_1, y) 
= \beta_1 + V(x_1)^{-1}cov(x_1, x_2)\beta_2 + V(x_1)^{-1}cov(x_1, \varepsilon) 
= \beta_1 + \rho_{x_1, x_2}\beta_2 + \rho_{x_1, \varepsilon}$$

If cov(x1, ε) = 0 and cov(x1, x2) = 0 then βols is consistent.[5](#page-4-0) If either cov(x1, x2) 6= 0 or cov(x1, ε) 6= 0 then the OLS estimator of β<sup>1</sup> will be asymptotically biased.

Assume we have an instrument z, such that cov(z, ε) = 0 and cov(z, x1) 6= 0. Then the IV estimate of β<sup>1</sup> is

$$\widehat{\beta_1^{iv}} = (z'x_1)^{-1}z'y$$

$$\rightarrow_p cov(z, x_1)^{-1}cov(z, y)$$

$$= \beta_1 + cov(z, x_1)^{-1}cov(z, x_2)\beta_2$$

$$= \beta_1 + \rho_{z, x_1}^{-1}\rho_{z, x_2}\beta_2$$

Going from OLS to IV eliminates the bias term caused by the "direct" endogeneity of x<sup>1</sup> (ρx1,εσε) and the "indirect" biased term caused by the correlation of x<sup>1</sup> and x<sup>2</sup> (β2ρx1,x<sup>2</sup> ), but introduces another "indirect" biased caused by the correlation between the instrument and x<sup>2</sup> (β2ρ −1 z,x<sup>1</sup> ρz,x<sup>2</sup> β2). This is not an omittedvariable problem: If x<sup>2</sup> is observable, then both OLS and IV may be biased (i.e., ontrolling for pollutants does not solve the problem if the instrument is correlated with these pollutants).[6](#page-4-1)

The IV estimate will be consistent as long as cov(z, x2) = 0 and cov(z, x1) 6= 0. The instrument can only be correlated with the component of pollution we observe. If the instrument is correlated with any other component of pollution, then the estimate may be biased. For example, suppose we observe PM10 and want

$$\begin{array}{ccc} \widehat{\beta^{ols}} & \rightarrow_p & \beta_1 + \rho_{x_1,\varepsilon} \\ \\ \widehat{\beta^{iv}} & \rightarrow_p & \beta_1 + \rho_{z,x_1}^{-1} \rho_{z,x_2} \beta_2 \end{array}$$

<span id="page-4-0"></span><sup>5</sup>This is different from the standard measurement error problem.

<span id="page-4-1"></span><sup>6</sup> In this case

to use an instrument (such as thermal inversions, driving restrictions, or environmental regulations) to study the effect of PM10 on health. In that case, our estimate of β<sup>1</sup> will not be consistent if our instrument affects other non-observable components of pollution such as SO2 (i.e., cov(z, x2) = 0) and if that component of pollution affects health (i.e., β<sup>2</sup> 6= 0). We provide a more general framework in Appendix [A.](#page-10-1)

#### 2.1 Results

Based on results in the previous section, some (intuitive) observations immediately arise:

- 1. If β<sup>2</sup> = 0 (i.e., if the other pollutant has no effect on health) then IV is consistent .
- 2. If cov(z, x2) = 0 (i.e., the instrument only impacts health through PM10) then IV is consistent.

One could either assume β<sup>2</sup> = 0 or cov(z, x2) = 0 while using IV methods to assess the impact of air pollution on health (only one of these assumptions is needed). However, neither assumption is realistic in many settings. For example, cars emit hundreds of volatile organic compounds (VOCs) [\(Caplain et al.,](#page-7-5) [2006\)](#page-7-5). Thus, using driving restrictions as an instrument for any particular pollutant would lead to biased estimates.

In terms of reducing bias, is IV better than OLS? Intuitively, if β<sup>2</sup> is relatively small, then the "indirect" bias is relatively small for both OLS and IV. Assume without loss of generality that β<sup>1</sup> > 0, ρx1,x<sup>2</sup> > 0 and ρz,x<sup>1</sup> > 0. Then:

<span id="page-5-0"></span>Lemma 1. If ρz,x<sup>2</sup> ≥ 0 and ρx1,ε ≥ 0, then

$$\rho_{x_1,x_2} > \rho_{z,x_1}^{-1} \rho_{z,x_2}$$

is a sufficient condition for

$$Bias(\widehat{\beta^{iv}}) < Bias(\widehat{\beta^{ols}})$$

where Bias refers to the difference between the probability limit of the estimator and the true value. Proof of Lemma 1 is the Appendix [C](#page-13-1)

To assess whether IV "perform better" than OLS, we need assumptions on: 1) the correlation between the endogenous pollutant and the error term; 2) the correlation between the measured pollutant and its unmeasured counterparts; and 3) the ratio of the correlation between the instrument and the various pollutants. For example, if the correlation between the instrument and various pollutants is the same, then it would be unfeasible for the bias in IV to be less than the bias in OLS (since ρx1,x<sup>2</sup> < 1). If the instrument is mostly correlated with a specific pollutant, then ρ −1 z,x<sup>1</sup> ρz,x<sup>2</sup> is small, and Lemma 1 is likely to hold, implying that IV perform better than OLS. In general, authors should be specific about their assumptions on the pollution production function and how their chosen instrument affects individual pollutants.

#### 2.2 Case study

To showcase the problem's extent, we estimate the bias from both OLS and IV in one setting based on [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1). [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1) study the effect of pollution on hospitalization rates for asthma by using flight delays originating in the eastern US to instrument air pollution daily variation near airports in California. They focus on CO and NO2 since airports are a major source of these two pollutants. These two pollutants are highly correlated (see Panel A in Table [3](#page-14-0) in Appendix [C\)](#page-13-1), even after controlling for a rich set of weather and seasonal controls (see Panel B in Table [3](#page-14-0) in Appendix [C\)](#page-13-1). The instrument (taxi time at an airport in the eastern US) is correlated with both pollutants. The authors of the study are aware of this: "Since various pollutants are often correlated with one another, these estimates should be interpreted with caution, as the pollutant of interest will proxy for other correlated air pollutants." The authors overcome this problem by using wind speed and wind direction interacted with taxi time as additional sources of exogenous variation.

Using all three sources of exogenous variation, an increase of 1 ppb of CO and NO2 increases asthma rates (per 10 million people) by 0.222 (p-value<0.01) and -2.2 (p-value>0.1) (see Table 5 in [Schlenker and](#page-9-1) [Walker](#page-9-1) [\(2016\)](#page-9-1)). Had [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1) ignored that these pollutants are correlated, an increase of 1 ppb of CO and NO2 would be (wrongly) associated with increases in asthma rates (per 10 million people) of 0.194 (p-value<0.01) and 12.4 (p-value<0.01) (see Table 4 in [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1)). Considering both pollutants to be endogenous did not change the magnitude of the effect of CO but makes a significant difference for NO2.

#### 3 Discussion

While instrumental variables are often used to create exogenous variation in single pollutants, pollutants are generally co-produced and any instrument that affects one component of pollution (e.g., PM10) is likely to affect other pollutants not considered in the analysis (e.g., SO2). If pollutants are co-produced, IV models that treat a single pollutant as endogenous will yield biased estimates. We encourage researchers to place more structure on the relationship between instruments and pollutants while interpreting estimates from IV models in the context of air quality and health.

#### References

- <span id="page-7-6"></span>Agrawal, S., & Yamamoto, S. (2015). Effect of indoor air pollution from biomass and solid fuel combustion on symptoms of preeclampsia/eclampsia in Indian women. Indoor Air , 25 (3), 341–352. doi: 10.1111/ ina.12144
- <span id="page-7-7"></span>Ambrey, C. L., & Fleming, C. M. (2014). The causal effect of income on life satisfaction and the implications for valuing non-market goods. Economics Letters, 123 (2), 131–134. doi: 10.1016/j.econlet.2014.01.031
- <span id="page-7-4"></span>Arceo-Gomez, E. O., Hanna, R., & Oliva, P. (in press). Does the effect of pollution on infant mortality differ between developing and developed countries? evidence from Mexico city [Working Paper]. Economic Journal. Retrieved from <http://www.nber.org/papers/w18349> doi: 10.3386/w18349
- <span id="page-7-8"></span>Bilger, M., & Carrieri, V. (2013). Health in the cities: When the neighborhood matters more than income. Journal of Health Economics, 32 (1), 1–11. doi: 10.1016/j.jhealeco.2012.09.010
- <span id="page-7-0"></span>Bombardini, M., & Li, B. (2016). Trade, pollution and mortality in China (Tech. Rep.). National Bureau of Economic Research.
- <span id="page-7-9"></span>Brown, T. T. (2013). A monetary valuation of individual religious behaviour: the case of prayer. Applied Economics, 45 (15), 2031–2037. doi: 10.1080/00036846.2011.648318
- <span id="page-7-5"></span>Caplain, I., Cazier, F., Nouali, H., Mercier, A., D´echaux, J.-C., Nollet, V., . . . Vidon, R. (2006). Emissions of unregulated pollutants from European gasoline and diesel passenger cars. Atmospheric Environment, 40 (31), 5954–5966.
- <span id="page-7-2"></span>Chay, K., Dobkin, C., & Greenstone, M. (2003). The clean air act of 1970 and adult mortality. Journal of Risk and Uncertainty, 27 (3), 279–300. doi: 10.1023/A:1025897327639
- <span id="page-7-3"></span>Chay, K., & Greenstone, M. (2003a). Air quality, infant mortality, and the clean air act of 1970 (Working Paper No. 10053). National Bureau of Economic Research. Retrieved from [http://www.nber.org/](http://www.nber.org/papers/w10053) [papers/w10053](http://www.nber.org/papers/w10053) doi: 10.3386/w10053
- <span id="page-7-1"></span>Chay, K., & Greenstone, M. (2003b). The impact of air pollution on infant mortality: Evidence from geographic variation in pollution shocks induced by a recession. The Quarterly Journal of Economics, 118 (3), 1121–1167. Retrieved from [http://qje.oxfordjournals.org/content/118/3/](http://qje.oxfordjournals.org/content/118/3/1121.abstract) [1121.abstract](http://qje.oxfordjournals.org/content/118/3/1121.abstract) doi: 10.1162/00335530360698513

- <span id="page-8-5"></span>Deryugina, T., Heutel, G., Miller, N. H., Molitor, D., & Reif, J. (2016). The mortality and medical costs of air pollution: Evidence from changes in wind direction (Tech. Rep.). National Bureau of Economic Research.
- <span id="page-8-0"></span>Deschenes, O., Greenstone, M., & Shapiro, J. S. (2012). Defensive investments and the demand for air quality: Evidence from the nox budget program and ozone reductions (Tech. Rep.). National Bureau of Economic Research.
- <span id="page-8-3"></span>Ebenstein, A., Frank, E., & Reingewertz, Y. (2015). Particulate matter concentrations, sandstorms and respiratory hospital admissions in israel. Israel Medical Association Journal, 17 (10), 628–632.
- <span id="page-8-2"></span>Gutierrez, E. (2015). Air quality and infant mortality in Mexico: evidence from variation in pollution concentrations caused by the usage of small-scale power plants. Journal of Population Economics, 28 (4), 1181–1207. Retrieved from [http://EconPapers.repec.org/RePEc:spr:jopoec:v:28:y:2015:i:4:](http://EconPapers.repec.org/RePEc:spr:jopoec:v:28:y:2015:i:4:p:1181-1207) [p:1181-1207](http://EconPapers.repec.org/RePEc:spr:jopoec:v:28:y:2015:i:4:p:1181-1207)
- <span id="page-8-6"></span>He, G., Fan, M., & Zhou, M. (2016). The effect of air pollution on mortality in China: Evidence from the 2008 Beijing olympic games. Journal of Environmental Economics and Management, 79 , 18–39.
- <span id="page-8-9"></span>Ho, C.-S., & Hite, D. (2009). Toxic chemical releases, health effects, and productivity losses in the united states. Journal of Community Health, 34 (6), 539–546. doi: 10.1007/s10900-009-9180-6
- <span id="page-8-10"></span>Howley, P. (2017). Less money or better health? evaluating individual's willingness to make trade-offs using life satisfaction data. Journal Of Economic Behavior & Organization, 135 , 53–65. doi: 10.1016/ j.jebo.2017.01.010
- <span id="page-8-7"></span>Jayachandran, S. (2009). Air quality and early-life mortality evidence from Indonesia's wildfires. Journal of Human Resources, 44 (4), 916–954.
- <span id="page-8-11"></span>Jones, A. M. (2007). Identification of treatment effects in health economics. Health Economics, 16 (11), 1127–1131. doi: 10.1002/hec.1302
- <span id="page-8-4"></span>Knittel, C. R., Miller, D. L., & Sanders, N. J. (2016). Caution, drivers! children present: Traffic, pollution, and infant health. Review of Economics and Statistics, 98 (2), 350–366. doi: 10.1162/REST\ a\ 00548
- <span id="page-8-1"></span>Lagravinese, R., Moscone, F., Tosetti, E., & Lee, H. (2014). The impact of air pollution on hospital admissions: Evidence from Italy. Regional Science and Urban Economics, 49 , 278–285. Retrieved from <http://www.sciencedirect.com/science/article/pii/S0166046214000581> doi: 10.1016/ j.regsciurbeco.2014.06.003
- <span id="page-8-8"></span>Luechinger, S. (2014). Air pollution and infant mortality: A natural experiment from power plant desulfurization. Journal of Health Economics, 37 , 219–231.

- <span id="page-9-0"></span>Moretti, E., & Neidell, M. (2011). Pollution, health, and avoidance behavior: Evidence from the ports of los angeles. Journal of Human Resources, 46 (1), 154–175. Retrieved from [http://jhr.uwpress.org/](http://jhr.uwpress.org/content/46/1/154.abstract) [content/46/1/154.abstract](http://jhr.uwpress.org/content/46/1/154.abstract)
- <span id="page-9-5"></span>Mullahy, J., & Portney, P. R. (1990). Air pollution, cigarette smoking, and the production of respiratory health. Journal of Health Economics, 9 (2), 193–205. Retrieved from [http://www.sciencedirect](http://www.sciencedirect.com/science/article/pii/016762969090017W) [.com/science/article/pii/016762969090017W](http://www.sciencedirect.com/science/article/pii/016762969090017W) doi: 10.1016/0167-6296(90)90017-W
- <span id="page-9-6"></span>Nordberg, K., Filipsson, H. L., Gustafsson, M., Harland, R., & Roos, P. (2001). Climate, hydrographic variations and marine benthic hypoxia in koljo fjord, Sweden. Journal of Sea Research, 46 , 187–200. Retrieved from <http://www.sciencedirect.com/science/article/pii/S1385110101000843> doi: 10.1016/S1385-1101(01)00084-3
- <span id="page-9-7"></span>Pant, K. P. (2013). Economics of indoor air pollution and respiratory health: A case study of the effects of improved stove and biogas adoptions on health costs in rural Nepal. Respirology.
- <span id="page-9-8"></span>Saha, S., Pattanayak, S. K., Sills, E. O., & Singha, A. K. (2011). Under-mining health: Environmental justice and mining in india. Health & Place, 17 (1), 140–148. doi: 10.1016/j.healthplace.2010.09.007
- <span id="page-9-9"></span>Schennach, S. M. (2013). Regressions with berkson errors in covariates-a nonparametric approach. Annals Of Statistics, 41 (3), 1642–1668. doi: 10.1214/13-AOS1122
- <span id="page-9-1"></span>Schlenker, W., & Walker, W. R. (2016). Airports, air pollution, and contemporaneous health. Review Of Economic Studies, 83 (2), 768–809. doi: 10.1093/restud/rdv043
- <span id="page-9-2"></span>Schwartz, J., Austin, E., Bind, M.-A., Zanobetti, A., & Koutrakis, P. (2015). Estimating causal associations of fine particles with daily deaths in boston. American Journal of Epidemiology, 182 (7), 644–650. doi: 10.1093/aje/kwv101
- <span id="page-9-3"></span>Schwartz, J., Bind, M. A., & Koutrakis, P. (2017). Estimating Causal Effects of Local Air Pollution on Daily Deaths: Effect of Low Levels. Environmental Health Perspectives, 125 (1), 23–29.
- <span id="page-9-10"></span>Sim, A., Suryadarma, D., & Suryahadi, A. (2017). The consequences of child market work on the growth of human capital. World Development, 91 , 144–155. doi: 10.1016/j.worlddev.2016.11.007
- <span id="page-9-11"></span>Strand, M., Sillau, S., Grunwald, G. K., & Rabinovitch, N. (2015). Regression calibration with instrumental variables for longitudinal models with interaction terms, and application to air pollution studies. Environmetrics, 26 (6), 393–405.
- <span id="page-9-4"></span>Tonne, C., Beevers, S., Kelly, F. J., Jarup, L., Wilkinson, P., & Armstrong, B. (2010). An approach for estimating the health effects of changes over time in air pollution: an illustration using cardiorespiratory hospital admissions in London. Occupational and Environmental Medicine, 67 (6), 422–

427.

- <span id="page-10-2"></span>Weldesilassie, A. B., Boelee, E., Drechsel, P., & Dabbert, S. (2011). Wastewater use in crop production in peri-urban areas of addis ababa: impacts on health in farm households. Environment And Development Economics, 16 (1), 25–49. doi: 10.1017/S1355770X1000029X
- <span id="page-10-3"></span>Zaman, K., & el Moemen, M. A. (2017). The influence of electricity production, permanent cropland, high technology exports, and health expenditures on air pollution in latin America and the caribbean countries. Renewable and Sustainable Energy Reviews, 76 , 1004–1010. Retrieved from [http://www](http://www.sciencedirect.com/science/article/pii/S1364032117304446) [.sciencedirect.com/science/article/pii/S1364032117304446](http://www.sciencedirect.com/science/article/pii/S1364032117304446) doi: 10.1016/j.rser.2017.03.103
- <span id="page-10-0"></span>Zhong, N. (2015). Superstitious driving restriction: Traffic congestion, ambient air pollution, and health in beijing. In Working paper.
- <span id="page-10-4"></span>Zivin, J. G., & Neidell, M. (2014). Pollution and health. In A. J. Culyer (Ed.), Encyclopedia of health economics (pp. 98–102). San Diego: Elsevier. Retrieved from [http://www.sciencedirect.com/](http://www.sciencedirect.com/science/article/pii/B9780123756787003060) [science/article/pii/B9780123756787003060](http://www.sciencedirect.com/science/article/pii/B9780123756787003060) doi: 10.1016/B978-0-12-375678-7.00306-0

# <span id="page-10-1"></span>A A more general case

Suppose the true underlying model is the following:

$$y = \sum_{k=1}^{N} x_k \beta_k + \varepsilon \tag{3}$$

and that cov(x1, ε) 6= 0, so that x<sup>1</sup> is endogenous. Additionally, suppose we have an instrument z such that cov(z, ε) = 0 and cov(z, x1) 6= 0. Finally, suppose the statistician only observes x1.

Then the OLS estimate of β<sup>1</sup> is

$$\widehat{\beta^{ols}} = (x_1'x_1)^{-1}x_1'y$$

$$\to_p V(x_1)^{-1}cov(x_1, y)$$

$$= \sum_{k=1}^K \left[ V(x_1)^{-1}cov(x_1, x_k)\beta_k \right] + V(x_1)^{-1}cov(x_1, \varepsilon)$$

$$= \beta_1 + \sum_{k=2}^K \beta_k V(x_1)^{-1}cov(x_1, x_k) + V(x_1)^{-1}cov(x_1, \varepsilon)$$

and the IV estimate of β<sup>1</sup> is

$$\widehat{\beta^{iv}} = (z'x_1)^{-1}z'y$$

$$\to_p cov(z, x_1)^{-1}cov(z, y)$$

$$= \sum_{k=1}^K cov(z, x_1)^{-1}cov(z, x_k)\beta_k + cov(z, x_1)^{-1}cov(z, \varepsilon)$$

$$= \beta_1 + \sum_{k=2}^K \beta_k cov(z, x_1)^{-1}cov(z, x_k)$$

Assuming, without loss of generality, that σ<sup>k</sup> = 1 for all k and that σ<sup>ε</sup> = 1, then

$$\begin{split} \widehat{\beta^{ols}} & \to_p & \beta_1 + \sum_{k=2}^K \beta_k \rho_{x_1, x_k} + \rho_{x_1, \varepsilon} \\ \widehat{\beta^{iv}} & \to_p & \beta_1 + \sum_{k=2}^K \beta_k \rho_{z, x_1}^{-1} \rho_{z, x_k} \end{split}$$

Thus, going from OLS to IV one eliminates the bias term caused by the "direct" endogeneity of x<sup>1</sup> (ρx1,ε). But introduces an"indirect" biased term caused by the correlation of x<sup>1</sup> and x<sup>k</sup> ( P<sup>K</sup> <sup>k</sup>=2 βkρx1,x<sup>k</sup> ) and the correlation between the instrument and x<sup>k</sup> ( P<sup>K</sup> <sup>k</sup>=2 βkρ −1 z,x<sup>1</sup> ρz,x<sup>k</sup> ).

#### B Proof of Lemma [1](#page-5-0) and some corollaries

Proof of Lemma [1](#page-5-0) in the general setting. Suppose the true underlying model is the following:

$$y = \sum_{k=1}^{N} x_k \beta_k + \varepsilon \tag{4}$$

and that cov(x1, ε) 6= 0, so that x<sup>1</sup> is endogenous. Additionally, suppose we have an instrument z such that cov(z, ε) = 0 and cov(z, x1) 6= 0. Finally, suppose the statistician only observes x1.

Assuming, without loss of generality, that σ<sup>k</sup> = 1 for all k, σ<sup>ε</sup> = 1, β<sup>1</sup> ≥ 0, ρ<sup>x</sup>1,x<sup>k</sup> > 0 for all k, and ρz,x<sup>1</sup> > 0.

From σ<sup>k</sup> = 1 for all k and σ<sup>ε</sup> = 1:

$$Bias(\beta^{ols}) \rightarrow_{p} \sum_{k=2}^{K} \beta_{k} \rho_{x_{1},x_{k}} + \rho_{x_{1},\varepsilon}$$
$$Bias(\beta^{iv}) \rightarrow_{p} \sum_{k=2}^{K} \beta_{k} \rho_{z,x_{1}}^{-1} \rho_{z,x_{k}}$$

Additionally, assume that β<sup>k</sup> > 0 for all k, ρz,x<sup>k</sup> ≥ 0 for all k, ρx1,ε ≥ 0, and ρx1,x<sup>k</sup> > ρ−<sup>1</sup> z,x<sup>1</sup> ρz,x<sup>k</sup> for all k. Then it follows that:

$$\rho_{x_{1},x_{k}} > \rho_{z,x_{1}}^{-1}\rho_{z,x_{k}}$$

$$\sum_{k=2}^{K} \beta_{k}\rho_{x_{1},x_{k}} > \sum_{k=2}^{K} \beta_{k}\rho_{z,x_{1}}^{-1\rho_{z,x_{k}}}$$

$$\sum_{k=2}^{K} \beta_{k}\rho_{x_{1},x_{k}} + \rho_{x_{1},\varepsilon} > \sum_{k=2}^{K} \beta_{k}\rho_{z,x_{1}}^{-1}\rho_{z,x_{k}}$$

$$|\sum_{k=2}^{K} \beta_{k}\rho_{x_{1},x_{k}} + \rho_{x_{1},\varepsilon}| > |\sum_{k=2}^{K} \beta_{k}\rho_{z,x_{1}}^{-1}\rho_{z,x_{k}}|$$

$$|Bias(\beta^{ols})| > |Bias(\beta^{iv})|$$

$$Bias(\beta^{ols}) > Bias(\beta^{iv})$$

Two immediate corollaries that can be proved in an almost identical manner are:

Corollary 1. If β<sup>k</sup> > 0 for all k, ρz,x<sup>k</sup> > 0 for all k, ρ<sup>x</sup>1,ε < 0, and ρ −1 z,x<sup>1</sup> ρz,x<sup>k</sup> > ρ<sup>x</sup>1,x<sup>k</sup> for all k, then

$$\widehat{\beta^{iv}} > \widehat{\beta^{ols}}$$

Corollary 2. If β<sup>k</sup> > 0 for all k, ρz,x<sup>k</sup> > 0 for all k, ρ<sup>x</sup>1,ε > 0, and ρ −1 z,x<sup>1</sup> ρz,x<sup>k</sup> < ρ<sup>x</sup>1,x<sup>k</sup> for all k, then

$$\widehat{\beta^{iv}} < \widehat{\beta^{ols}}$$

Table 2: Non-relevant research articles found in the systematic search

<span id="page-13-1"></span><span id="page-13-0"></span>

| Study                                                     | Journal                                     |
|-----------------------------------------------------------|---------------------------------------------|
| Agrawal and Yamamoto (2015)                               | Indoor Air                                  |
| Ambrey and Fleming (2014)                                 | Economics Letters                           |
| Bilger and Carrieri (2013)                                | Journal of Health Economics                 |
| Brown (2013)                                              | Applied Economics                           |
| Ho and Hite (2009)                                        | Journal of Community Health                 |
| Howley (2017)                                             | Journal of Economic Behavior & Organization |
| Jones (2007)                                              | Health economics                            |
| Mullahy and Portney (1990)                                | Journal of Health Economics                 |
| Nordberg, Filipsson, Gustafsson, Harland, and Roos (2001) | Journal of Sea Research                     |
| Pant (2013)                                               | Respirology                                 |
| Saha, Pattanayak, Sills, and Singha (2011)                | Health & Place                              |
| Schennach (2013)                                          | Annals of Statistics                        |
| Sim, Suryadarma, and Suryahadi (2017)                     | World Development                           |
| Strand, Sillau, Grunwald, and Rabinovitch (2015)          | Environmetrics                              |
| Weldesilassie, Boelee, Drechsel, and Dabbert (2011)       | Environment and Development Economics       |
| Zaman and el Moemen (2017)                                | Renewable and Sustainable Energy Reviews    |
| Zivin and Neidell (2014)                                  | Encyclopedia of Health Economics            |

# C Extra tables

<span id="page-14-0"></span>Table 3: Correlation between pollutants and IV in [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1) Panel A: Unconditional correlation

|           | Taxi time | CO       | NO2 |
|-----------|-----------|----------|-----|
| Taxi time | 1         |          |     |
| CO        | 0.105∗∗∗  | 1        |     |
| NO2       | 0.0305∗∗∗ | 0.798∗∗∗ | 1   |

<sup>∗</sup> p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Panel B: Conditional correlation

|           | Taxi time  | CO       | NO2 |
|-----------|------------|----------|-----|
| Taxi time | 1          |          |     |
| CO        | -0.0118∗∗∗ | 1        |     |
| NO2       | -0.0103∗∗∗ | 0.583∗∗∗ | 1   |

<sup>∗</sup> p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Correlations are based on the supplementary material data provided by [Schlenker and Walker](#page-9-1) [\(2016\)](#page-9-1). Panel A shows the raw correlation, while Panel B shows the conditional correlation after controlling for weather and seasonal controls.
