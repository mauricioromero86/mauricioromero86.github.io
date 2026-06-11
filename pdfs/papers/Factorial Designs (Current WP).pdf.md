---
title: "Factorial Designs (Current WP)"
document_type: "superseded-draft"
parent_paper: "Factorial Designs, Model Selection, and (Incorrect) Inference in Randomized Experiments"
parent_pdf_url: "https://mauricio-romero.com/pdfs/papers/rest_a_01317.pdf"
pdf_url: "https://mauricio-romero.com/pdfs/papers/Factorial%20Designs%20%28Current%20WP%29.pdf"
canonical_url: "https://mauricio-romero.com/pdfs/papers/Factorial%20Designs%20%28Current%20WP%29.pdf.md"
source: pdfs/papers (non-primary document)
note: "SUPERSEDED DRAFT - an old version of \"Factorial Designs, Model Selection, and (Incorrect) Inference in Randomized Experiments\". The current version is https://mauricio-romero.com/pdfs/papers/rest_a_01317.pdf; cite and rely on that version, not this one. Generated for LLMs."
---

Factorial designs, model selection, and (incorrect) inference in randomized experiments<sup>∗</sup>

Karthik Muralidharan† Mauricio Romero‡ Kaspar Wüthrich§

**Abstract**

Factorial designs are widely used to study multiple treatments in one experiment. While *t*-tests using a fully-saturated "long" model provide valid inferences, "short" model *t*-tests (that ignore interactions) yield higher power if interactions are zero, but incorrect inferences otherwise. Of 27 factorial experiments published in top-5 journals (2007–2017), 19 use the short model. After including interactions, over half of their results lose significance. Based on recent econometric advances, we show that power improvements over the long model are possible. We provide practical guidance for the design of new experiments and the analysis of completed experiments.

**Keywords:** randomized controlled trials; cross-cut designs; power; data-dependent model selection; interaction effects; type-M errors

**JEL Codes:** C12, C18, C21, C90, C93

<sup>∗</sup>We are grateful to Isaiah Andrews, Tim Armstrong, Prashant Bharadwaj, Arun Chandrasekhar, Clement de Chaisemartin, Gordon Dahl, Stefano DellaVigna, Esther Duflo, Graham Elliott, Andrew Gelman, Markus Goldstein, Macartan Humphreys, Guido Imbens, Hiroaki Kaido, Lawrence Katz, Michal Kolesar, Adam McCloskey, Craig McIntosh, Rachael Meager, Paul Niehaus, Ben Olken, Gautam Rao, Andres Santos, Jesse Shapiro, Diego Vera-Cossio, and many seminar participants for comments and suggestions. We are also grateful to the authors of the papers we reanalyze for answering our questions and fact-checking that their papers are characterized correctly. Finally, we would like to thank Tim Armstrong, Adam McCloskey, Graham Elliott, Michal Kolesar, and Soonwoo Kwon who graciously answered questions about the econometric methods they developed and how to implement them. Sameem Siddiqui provided excellent research assistance. All errors are our own. Financial support from the Asociación Mexicana de Cultura, A.C. is gratefully acknowledged by Romero.

<sup>†</sup>Department of Economics, UC San Diego; NBER; J-PAL; E-mail: [kamurali@ucsd.edu](mailto:kamurali@ucsd.edu)

<sup>‡</sup> ITAM, Mexico City, Mexico; J-PAL; E-mail: [mtromero@itam.mx](mailto:mtromero@itam.mx)

<sup>§</sup>Department of Economics, UC San Diego; CESifo; Ifo Institute; E-mail: [kwuthrich@ucsd.edu](mailto:kwuthrich@ucsd.edu)

# **1 Introduction**

Cross-cutting or factorial designs are widely used in field experiments. For example, 27 out of 124 field experiments published in top-5 economics journals during 2007–2017 use cross-cutting designs. One rationale is that the power for detecting main treatment effects is higher if interactions between treatments are ignored in estimation and inference (with the implicit assumption that interactions are zero or negligible). This can make factorial designs a cost-effective way of studying multiple treatments.[1](#page-1-0) A second rationale is to "explore" if there are meaningful interactions across treatments. This paper is motivated by the observation that both of these rationales can be problematic in practice.

To fix ideas, consider a setup with two randomly-assigned binary treatments. The researcher can estimate either a fully-saturated "long" model (with dummies for both treatments and their interaction) or a "short" model (only including dummies for both treatments). The long model yields consistent estimators for the main treatment effects of both treatments and is always correct for inference regardless of the true value of the interaction effect. However, if the true value of the interaction effect is zero, the short model yields consistent estimators and has greater power for conducting inference on the main effects.

The power gains from the short model, however, come at the cost of an increased likelihood of incorrect inference relative to a business-as-usual counterfactual (defined as outcomes in a pure experimental control group) if the interaction effect is not zero. Out of 27 field experiments published in top-5 economics journals during 2007–2017 using cross-cutting designs, 19 (over 70%) do not include all interaction terms in the main specifications. We reanalyzed the data from these papers by also including the interaction terms.[2](#page-1-1) Doing so has non-trivial implications for inference on the main treatment effects. The median absolute value of the change in the point estimates is 96%, about

<span id="page-1-0"></span><sup>1</sup>As [Kremer](#page-31-0) [\(2003\)](#page-31-0) puts it: "Conducting a series of evaluations in the same area allows substantial cost savings...Since data collection is the most costly element of these evaluations, cross-cutting the sample reduces costs dramatically...This tactic can be problematic, however, if there are significant interactions between programs".

<span id="page-1-1"></span><sup>2</sup>The full list of 27 papers is in Table [A.1.](#page-44-0) We reanalyzed 15 out of the 19 that do not include all interactions in the main specification. The other four papers did not have publiclyaccessible data.

26% of estimates change sign, and 53% (29 out of 55) of estimates reported to be significant at the 5% level are no longer so after including interactions. Even if we reanalyze only "policy" experiments, 32% of the estimates (6 out of 19) are no longer significant after including interactions.[3](#page-2-0)

In practice, researchers often estimate the long model first and test if the interaction is significant, and then focus on the short model if they do not reject that the interaction is zero. However, such data-dependent model selection leads to invalid inferences [\(Leeb & Pötscher,](#page-31-1) [2005,](#page-31-1) [2006,](#page-31-2) [2008;](#page-31-3) [Kahan,](#page-30-0) [2013\)](#page-30-0) and should thus be avoided. Further, cross-cutting experiments are rarely adequately powered to detect meaningful interactions (see Section [2.6\)](#page-12-0). Thus, this two-step procedure will almost always fail to reject that the interaction term is zero, even when it is different from zero. As a result, the rate of incorrect inference using this two-step model-selection procedure will continue to be nearly as high as that from just running the short model.

The lack of power to detect interactions combined with a focus on statistical significance also makes it challenging to use factorial designs to "explore" whether interactions are meaningful. The interaction estimator's variance is always larger than that of the main effects estimators, making the sample size requirements for detecting interactions much more onerous.[4](#page-2-1) This leads to most factorial experiments being under-powered to detect interactions. As a result, point estimates of interactions will on average substantially overstate the true effect, conditional on being significant. This problem has been referred to by [Gelman & Carlin](#page-29-0) [\(2014\)](#page-29-0) as Type-M error.

Textbook treatments of factorial designs [\(Cochran & Cox,](#page-28-0) [1957;](#page-28-0) [Gerber & Green,](#page-30-1) [2012\)](#page-30-1) and guides to practice [\(Kremer,](#page-31-0) [2003;](#page-31-0) [Duflo et al.,](#page-29-1) [2007\)](#page-29-1) are careful to clarify that treatment effects using the short model should be interpreted as either (a) being conditional on the distribution of the other treatment arms in the experiment, or (b) as a composite treatment effect that includes a weighted-average of the interactions with other treatments. However, as we argue in Section

<span id="page-2-0"></span><sup>3</sup>We define a policy experiment as one which studies a program or intervention that could be scaled up; as opposed to a conceptual experiment, which aims to test for the existence of facts or concepts such as discrimination (e.g., resume audit experiments).

<span id="page-2-1"></span><sup>4</sup>For example, one would need an 8 times larger sample to detect an interaction than to detect a main effect when the interaction is half the size of the main effect; see Section [2.6](#page-12-0) and Appendix [A.3.](#page-62-0)

[2.3,](#page-8-0) this weighted average is a somewhat arbitrary construct, can be difficult to interpret in highdimensional factorial designs, and is typically neither of primary academic interest nor policy-relevant. Consistent with this view, none of the 19 experimental papers that focus on the short model motivate their experiment as being about estimating a weighted-average treatment effect.

The status quo of focusing on the short model is problematic for at least three reasons. First, ignoring interactions affects internal validity against a "business-as-usual" counterfactual. If the interventions studied are new, the other programs may not even exist in the study population. Even if they do, there is no reason to believe that the distributions in the population mirror those in the experiment. Thus, to the extent that estimation and inference of treatment effects depend on what other interventions are being studied in the same experiment, ignoring interactions is a threat to internal validity.

Second, "absence of evidence" of significant interactions may be erroneously interpreted as "evidence of absence". The view that interactions are second-order (as implied when papers only present the short model) may have been influenced partly by the lack of evidence of significant interactions in most experiments to date. However, as we show in Section [2.6,](#page-12-0) this is at least partly because few experiments are adequately powered to detect meaningful interactions. There is now both experimental [\(Duflo et al.,](#page-29-2) [2015;](#page-29-2) [Mbiti et al.,](#page-32-0) [2019\)](#page-32-0) and non-experimental [\(Kerwin &](#page-31-4) [Thornton,](#page-31-4) [2021;](#page-31-4) [Gilligan et al.,](#page-30-2) [2022\)](#page-30-2) evidence that interactions matter. Indeed, a long tradition in development economics has highlighted the importance of complementarities across programs in alleviating poverty traps [\(Ray,](#page-32-1) [1998;](#page-32-1) [Banerjee & Duflo,](#page-27-0) [2005\)](#page-27-0), which suggests that assuming away interactions in empirical work may be a mistake.

Third, there is well-documented publication bias towards significant findings (e.g., [Franco et al.,](#page-29-3) [2014;](#page-29-3) [Andrews & Kasy,](#page-26-0) [2018;](#page-26-0) [Christensen & Miguel,](#page-28-1) [2018;](#page-28-1) [Abadie,](#page-26-1) [2020\)](#page-26-1). This can also affect evidence aggregation because meta-analyses and evidence reviews often only include published studies. Thus, the sensitivity of the significance of main effect estimates to the inclusion/exclusion of interaction terms (which we document in this paper), is likely to have non-trivial implications for how evidence is published, summarized, and translated into policy.

Having documented the limitations of the short model, we consider if it is possible to improve power relative to the long model while maintaining size control for relevant values of the interactions. The two-sided long model *t*-test is the uniformly most powerful unbiased test (e.g., [van der Vaart,](#page-32-2) [1998;](#page-32-2) [Elliott et al.,](#page-29-4) [2015a\)](#page-29-4). This result implies that if one insists on size control for all values of the interaction effect, any procedure that is more powerful than the *t*-test for some values of the interactions must have lower power somewhere else. This classical result motivates imposing restrictions on the interaction effects based on prior knowledge to improve power. We explore three different approaches.[5](#page-4-0)

The first approach, based on [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4), is a nearly optimal test that targets power towards an a priori likely value of the interaction (e.g., a value of zero), while controlling size for all values of the interaction. This approach comes close to achieving the maximal theoretically possible power near the likely value of the interaction but exhibits lower power than the long model *t*-test farther away. We then consider two approaches based on [Armstrong et al.](#page-27-1) [\(2020\)](#page-27-1) and [Imbens](#page-30-3) [& Manski](#page-30-3) [\(2004\)](#page-30-3) for constructing confidence intervals for the main effects under restrictions on the magnitude of the interactions based on prior knowledge. When the prior knowledge is correct, these approaches control size and yield substantial power gains relative to the long model *t*-tests. However, these power gains come at the cost of size distortions if the prior knowledge is incorrect.

Based on the analysis above, we recommend — in the interest of transparency — that factorial experiments report results from the long regression model (even if only in an appendix). Long model *t*-tests are easy to compute even in complicated factorial designs and have appealing optimality properties. Further, the justification for omitting interactions should not be that these were not significant in the long model (because of the model selection issue discussed above). Rather, if researchers would like to focus on results from the short model, they should clearly indicate that treatment effects should be interpreted as composite effects that include a weighted-average of interactions with other treatments (and specify the estimand of interest in a pre-analysis plan). This will enable readers to assess the extent to which other treatments may be typical background factors that can be ignored.

For the design of new experiments, if the primary parameters of interest are the main effects, a natural alternative is to leave the "interaction cells" empty and increase the number of units

<span id="page-4-0"></span><sup>5</sup> In Appendix [A.6,](#page-71-0) we explore a fourth approach based on [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4), which is based on a Bonferroni-type correction after consistent model selection.

assigned to the main treatment(s) or the control group. Our simulations show that this designbased approach yields more power gains than the econometric methods discussed above for most of the relevant values of the interaction.

Reviewing classic texts on experimental design, we identify four cases where factorial designs and analyses of the short model may be appropriate. The first is where the goal is to explore several treatments efficiently to identify promising interventions for further testing (e.g., [Cochran & Cox,](#page-28-0) [1957\)](#page-28-0). However, most policy experiments are run only once, making factorial designs and short model estimates less desirable.

The second is when the goal is not to test whether a given treatment has a "significant" effect, but to minimize mean squared error (MSE) criteria (or other loss functions) involving a bias-variance trade-off in estimating the main effects (e.g., [Blair et al.,](#page-28-2) [2019\)](#page-28-2). However, a key rationale for experimental evaluations of policies and programs is to generate unbiased estimates, making the bias in the short model unattractive.

The third is to improve external validity. [Cochran & Cox](#page-28-0) [\(1957,](#page-28-0) p.152) recommend bringing in subsidiary factors into factorial designs to test main effects over a wide range of conditions; also see [Fisher](#page-29-5) [\(1992\)](#page-29-5). Thus, factorial designs and analyses of the short model may be fine when one dimension of the experiment is studying reasonable variants of the main treatment, but less so when all treatments are of primary interest.

The fourth is the case of conceptual (as opposed to policy) experiments, such as resume audit studies, where many of the characteristics that are randomized (such as age, education, race, and gender) do exist in the population. When feasible, we recommend having the treatment share of various characteristics being studied be the same as their population proportion. Doing so will make the short-model coefficient more likely to approximate a population relevant parameter of interest. We discuss each of these four rationales along with relevant examples in Section [5.](#page-23-0)

Our first contribution is to the literature on the design of field experiments. [Bruhn & McKenzie](#page-28-3) [\(2009\)](#page-28-3), [List et al.](#page-32-5) [\(2011\)](#page-32-5), and [Athey & Imbens](#page-27-2) [\(2017\)](#page-27-2) provide guidance on the design of field experiments, but do not discuss when and when not to implement factorial designs. [Duflo et al.](#page-29-1) [\(2007,](#page-29-1) p.3932) implicitly endorse the use of factorial designs by noting that they "[have] proved very important in allowing for the recent wave of randomized evaluations in development economics".

Our reanalysis of existing experiments as well as simulations suggest that there is no free lunch. The perceived gains in power and cost-effectiveness from factorial designs come at the cost of not controlling size and an increased rate of false positives relative to a business-as-usual counterfactual. Alternatively, they come at the cost of a more complicated interpretation of the main results as a weighted-average of interactions with other treatments that may not represent a typical counterfactual. Further, using under-powered factorial designs to explore whether interactions are significant comes at the risk of overestimating the true effect, conditional on rejecting the null of no effect.

We also contribute to the literature that aims to improve the analysis of field experiments (e.g., [Young,](#page-33-0) [2018;](#page-33-0) [List et al.,](#page-32-6) [2019\)](#page-32-6). Our paper follows in this tradition by documenting a problem with the status quo, quantifying its importance, and identifying the most relevant recent advances in theoretical econometrics that can mitigate the problem. Specifically, we show that the econometric analysis of nonstandard inference problems can improve inference in factorial designs which are ubiquitous in field experiments.

Finally, we contribute to the literature on the pitfalls of focusing on statistical significance in applied work (e.g., [Brodeur et al.,](#page-28-4) [2016;](#page-28-4) [Wasserstein & Lazar,](#page-33-1) [2016;](#page-33-1) [Amrhein et al.,](#page-26-2) [2019;](#page-26-2) [Wasserstein et al.,](#page-33-2) [2019;](#page-33-2) [Brodeur et al.,](#page-28-5) [2020\)](#page-28-5). Specifically, the problems we highlight in this paper are less due to factorial designs per se. Rather they stem from the combination of a focus on statistical significance to assess if effects are meaningful, and most factorial experiments being under-powered to detect interactions.

# **2 Factorial designs in theory**

# **2.1 Setup**

This section discusses theoretical aspects of experiments with factorial (or "cross-cut") designs. We focus on factorial designs with two treatments, *T*<sup>1</sup> and *T*2, ("2×2 designs"), where researchers randomly assign some subjects to receive treatment *T*1, some subject to receive treatment *T*2, and some subjects to receive both treatments (see Table [1\)](#page-41-0). The analysis straightforwardly extends to cross-cut designs with more than two treatments.

[Table 1 about here.]

We are interested in the causal effect of  $T_1$  and  $T_2$  on an outcome Y. We use the potential outcomes framework (Rubin, 1974). The potential outcomes  $\{Y_{t_1,t_2}\}$  are indexed by both treatments,  $T_1=t_1$  and  $T_2=t_2$ , and are related to the observed outcome as  $Y=\sum_{t_1\in\{0,1\}}\sum_{t_2\in\{0,1\}}\mathbf{1}(T_1=t_1,T_2=t_2)\cdot Y_{t_1,t_2}$ . We assume that both treatments are randomly assigned and independent of each other, which is common in practice (e.g., Olken, 2007; Bertrand et al., 2010).

#### <span id="page-7-3"></span>2.2 Long and short regression models

Researchers analyzing experiments based on cross-cut designs typically consider one of the following two population regression models:

#### Long (or fully saturated) model:

<span id="page-7-0"></span>
$$Y = \beta_0 + \beta_1 T_1 + \beta_2 T_2 + \beta_{12} T_1 T_2 + \varepsilon \tag{1}$$

Short model:

<span id="page-7-1"></span>
$$Y = \beta_0^s + \beta_1^s T_1 + \beta_2^s T_2 + \varepsilon^s \tag{2}$$

The long model (1) includes both treatment indicators as well as their interaction, while the short model (2) only includes the two treatment indicators.<sup>6</sup>

The population regression coefficients in the long regression model correspond to the main average treatment effects (ATEs) of  $T_1$  and  $T_2$  against a business-as-usual counterfactual (this counterfactual can also be interpreted as the outcomes in a pure experimental control group) and the interaction effect:

$$\beta_1 = E(Y_{1,0} - Y_{0,0})$$
 (ATE of  $T_1$  relative to a counterfactual where  $T_2 = 0$ ) (3)

$$\beta_2 = E(Y_{0,1} - Y_{0,0})$$
 (ATE of  $T_2$  relative to a counterfactual where  $T_1 = 0$ ) (4)

<span id="page-7-2"></span>
$$\beta_{12} = E(Y_{1,1} - Y_{0,1} - Y_{1,0} + Y_{0,0})$$
 (interaction effect)<sup>7</sup> (5)

<sup>6</sup>Following Angrist & Pischke (2009, Chapter 3) and Hansen (2022, Chapter 2), we interpret  $\beta = (\beta_0, \beta_1, \beta_2, \beta_3)' = E(XX')^{-1}E(XY)$ , where  $X = (1, T_1, T_2, T_{12})'$ , as the population regression coefficient (or linear projection coefficient) and  $\varepsilon = Y - X'\beta$  as the population residual (or projection error). Similarly, we interpret  $\beta^s = (\beta_0^s, \beta_1^s, \beta_2^s)' = E(XX')^{-1}E(XY)$ , where  $X^s = (1, T_1, T_2)'$ , and  $\varepsilon^s = Y - X^s\beta^s$  as the population regression coefficient and the population residual, respectively.

By contrast, the regression coefficients in the short model are

<span id="page-8-2"></span>
$$\beta_1^s = E(Y_{1,1} - Y_{0,1})P(T_2 = 1) + E(Y_{1,0} - Y_{0,0})P(T_2 = 0)$$
(6)

$$= E(Y_{1,0} - Y_{0,0}) + E(Y_{1,1} - Y_{0,1} - Y_{1,0} + Y_{0,0})P(T_2 = 1)$$
(7)

$$\beta_2^s = E(Y_{1,1} - Y_{1,0})P(T_1 = 1) + E(Y_{0,1} - Y_{0,0})P(T_1 = 0)$$
(8)

$$= E(Y_{0,1} - Y_{0,0}) + E(Y_{1,1} - Y_{0,1} - Y_{1,0} + Y_{0,0})P(T_1 = 1)$$

$$(9)$$

Equation (6) shows that  $\beta_1^s$  yields a weighted average of the ATE of  $T_1$  relative to a counterfactual where  $T_2 = 1$  and the ATE of  $T_1$  relative to a business-as-usual counterfactual where  $T_2 = 0$ . The weights,  $P(T_2 = 1)$  and  $P(T_2 = 0)$ , are determined by the experimental design. Alternatively,  $\beta_1^s$  can be written as the sum of the ATE of  $T_1$  relative to the  $T_2 = 0$  counterfactual and the interaction effect multiplied by  $P(T_2 = 1)$  (Equation (7)). Equations (8) and (9) present the corresponding expressions for  $\beta_2^s$ . Unless the interaction effect is zero,  $\beta_1^s$  and  $\beta_2^s$  do not correspond to the main effects but yield composite treatment effects that are weighted averages of ATEs relative to different counterfactuals.

Remark 1. The problem of choosing between the long model and the short model is not unique to factorial designs and arises in many contexts. For example, when estimating treatment effects in observational studies, researchers need to decide whether to include the covariates linearly or consider fully interacted specifications (e.g., Angrist & Krueger, 1999; Angrist & Pischke, 2009). However, the practical implications are not the same because experimental treatments are fundamentally different in nature from standard covariates, as we discuss below in Section 2.3. The choice between the short and the long model (with interactions between the treatment and strata indicators) is also relevant in stratified experiments (e.g., Imbens & Rubin, 2015; Ansel et al., 2018; Bugni et al., 2018, 2019).

# <span id="page-8-0"></span>2.3 Long or short model: What do we care about?

Section 2.2 shows that the short model yields a weighted average of treatment effects that depends on the nature and distribution of the other treatment arms in the experiment. This weighted average is typically neither of primary academic interest nor policy-relevant. This view is consistent with how papers we reanalyze motivate their object of interest, which is usually the main treatment

<span id="page-8-1"></span><sup>&</sup>lt;sup>7</sup>The interaction effect is the difference between the effect of jointly providing both treatments and the sum of the main effects.

effect against a business-as-usual counterfactual. Of the 19 papers in Table A.1 in Appendix A.1 that present results from the short model without all interactions, we did not find any study that mentioned (in the main text or a footnote) that the presented treatment effects should be interpreted as either (a) a composite effect that includes a weighted average of the interaction with the other treatments or (b) as being against a counterfactual that was not business-as-usual but one that also had the other treatments in the same experiment.

One way to make the case for the short model is to recast the problem we identify as one of external rather than internal validity. Specifically, all experiments are carried out in a context with several unobserved "background" covariates. Thus, any experimental treatment effect is a weighted average of effects conditional on unobserved covariates. If the other experimental arms are considered analogous to unobserved background covariates, inference on treatment effects based on the short model can be considered internally valid. In this view, the challenge is that the unobserved covariates (including other treatment arms) will vary across contexts.

However, experimental treatments are fundamentally different from standard background covariates. They are determined by the experimenter based on research interest, and rarely represent real-world counterfactuals. In some cases, the interventions studied are new and the other treatments may not even exist in the study population. Even if they do exist, there is no reason to believe that the distributions in the population mirror those in the experiment. Thus, we view this issue as a challenge to internal validity. Further, papers with factorial designs often use the two-step procedure described in Section 2.5, and present results from the short model *after* mentioning that the interactions are not significantly different from zero (e.g., Banerjee et al., 2007; Karlan & List, 2007). This suggests that our view that interactions matter for internal validity is shared broadly.

Finally, even in settings where the coefficients in the short model are of interest, they can always be constructed based on the coefficients in the long model, while the converse is not true. One can also use the long model to test hypotheses about the coefficients in the short regression model:  $H_0: \beta_1^s = \beta_1 + \beta_{12} P(T_2 = 1) = 0$ . Which test is more powerful depends on the relative sample size in the four experimental cells.<sup>8</sup> Unlike the short model, the long model additionally allows for testing a rich variety

<span id="page-9-0"></span><sup>&</sup>lt;sup>8</sup>In practice, we recommend comparing both tests when doing power calculations. If both tests have the same power, the short model is more straightforward.

of hypotheses about counterfactual effects such as  $H_0: \beta_1 + \beta_{12}p = 0$  for policy-relevant values of p, which generally differ from the experimental assignment probability  $P(T_2=1)$ . For instance, resume audit experiments may vary characteristics such as age, gender, race, education, and experience with the sample size allocated to various combinations of these characteristics being different from their proportion in the population. In such a case, short model estimates are difficult to interpret, whereas estimating the long model and calculating a weighted average of main and interaction effects with weights equal to their population proportions may yield a more policy-relevant treatment effect.

To summarize, the long model estimates all the underlying parameters of interest (the main effects and the interactions). In contrast,  $\beta_1^s$  is rarely of interest in its own right, and even if it is, the long model allows for estimation and inference on  $\beta_1^s$  as well.

#### <span id="page-10-1"></span>2.4 Inference on main effects

Suppose that the researcher has access to a random sample  $\{Y_i, T_{1i}, T_{2i}\}_{i=1}^N$ . Consider the problem of testing hypotheses about the main effect of  $T_1$  relative to a business-as-usual counterfactual:  $H_0: \beta_1 = E(Y_{1,0} - Y_{0,0}) = 0$ .

To illustrate, suppose the data generating process is given by

<span id="page-10-0"></span>
$$Y_i = \beta_0 + \beta_1 T_{1i} + \beta_2 T_{2i} + \beta_{12} T_{1i} T_{2i} + \varepsilon_i, \quad \varepsilon_i \sim N(0, \sigma^2),$$
 (10)

where  $\varepsilon_i$  is independent of  $(T_{1i},T_{2i})$  and  $\sigma^2$  is known. If the interaction effect  $\beta_{12}$  is zero, conditional on  $\{T_{1i},T_{2i}\}_{i=1}^N$ ,  $\hat{\beta}_1 \sim N\left(\beta_1,Var\left(\hat{\beta}_1\right)\right)$  and  $\hat{\beta}_1^s \sim N\left(\beta_1,Var\left(\hat{\beta}_1^s\right)\right)$ , where  $Var\left(\hat{\beta}_1\right) = \sigma^2\left(\frac{1}{N_1} + \frac{1}{N_2}\right) \geq Var\left(\hat{\beta}_1^s\right) = \sigma^2\left(\frac{N_1N_3 + N_1N_4 + N_2N_3 + N_2N_4}{N_1N_2N_4 + N_1N_3N_4 + N_2N_3N_4}\right)$ . As a result, the short model t-test exhibits higher power than the long model t-test.

If, on the other hand,  $\beta_{12}\neq 0$ , ignoring the interaction can lead to substantial size distortions. To illustrate, we introduce a simple running example. Consider a  $2\times 2$  design with a total sample size of N=1,000 and  $N_1=N_2=N_3=N_4=250$ . The data are generated based on Model (10) with  $\varepsilon_i\sim N(0,1)$ ,  $T_{1i}$  and  $T_{2i}$  randomly assigned and independent of each other, and  $P(T_{1i}=1)=P(T_{2i}=1)=0.5$ . This design has power 90% to detect an effect of  $0.2\sigma$   $(0.29\sigma)$  at the 5% level using the short model (long model).

Figure 1 shows how power, bias, and size vary across different values of  $\beta_{12}$  in both the long and the short model. When  $\beta_{12}$ =0, the short model t-test controls size and exhibits higher power than the long model t-test as discussed before. However, these power gains come at the cost of bias and

size distortions whenever *β*12=0 ̸ . Importantly, even modest values of |*β*12| lead to considerable size distortions. For instance, |*β*12|*>*0*.*1*σ* more than doubles the rate of false rejection of the null (in the data we reanalyze in Section [3.2,](#page-14-0) we find that |*β*ˆ <sup>12</sup>|*>*0*.*1*σ* in over 36% of cases). By contrast, the long model is unbiased and exhibits correct size for all values *β*12. The main takeaway from Figure [1](#page-34-0) is that researchers should avoid the short model for making inference on the main effects, unless they are certain that *β*12=0.

#### [Figure 1 about here.]

#### <span id="page-11-0"></span>**2.5 Model selection (or pre-testing) yields invalid inferences**

Researchers often recognize that using the short model is only correct for inference on the main treatment effect if the interaction is close to zero (as implied by the quote from [Kremer](#page-31-0) [\(2003\)](#page-31-0) in the introduction). However, the problem is that the value of the interaction is unknown ex ante. Therefore, a common practice is to employ a data-driven two-step procedure to determine whether to ignore the interaction:

- 1. Estimate the long model and test the null hypothesis that *β*<sup>12</sup> is zero (i.e., *H*<sup>0</sup> :*β*12=0) using a two-sided *t*-test.
- 2. (a) If *H*<sup>0</sup> :*β*12=0 is rejected, test *H*<sup>0</sup> : *β*1=0 using the long model *t*-test.
  - (b) If *H*<sup>0</sup> :*β*12=0 is not rejected, test *H*<sup>0</sup> :*β*1=0 using the short model *t*-test.

While seemingly attractive, such data-dependent model selection leads to invalid inferences (e.g., [Leeb & Pötscher,](#page-31-1) [2005,](#page-31-1) [2006,](#page-31-2) [2008;](#page-31-3) [Kahan,](#page-30-0) [2013\)](#page-30-0). Figure [2](#page-35-0) shows the size properties of the twostep model selection approach in our running example. For reference, we also include results for the short and long model *t*-tests. The main takeaway from Figure [2](#page-35-0) is that model selection leads to incorrect inferences and false positives for a wide range of values of *β*12. [9](#page-11-1) Model selection can be particularly problematic for program evaluation field experiments because they are expensive to run, and therefore typically not adequately powered to reject that the interactions are zero (Section [2.6\)](#page-12-0).

The range of values for |*β*12| for which model selection leads to substantial size distortions shrinks as the sample size (and power) of the experiment increases. However, it can be quite large

<span id="page-11-1"></span><sup>9</sup>This is true even when *β*12=0 (as seen in the blue line in Figure [2\)](#page-35-0) because the tests in the first and second step are not independent.

in realistic settings. In our running example, with 1,000 observations one would need  $|\beta_{12}|$  to be above 0.5 to avoid notable size distortions. Even with 10,000 observations, only values of  $|\beta_{12}|$  above 0.2 lead to negligible size distortions (see Figure A.13). Since the true value of the interaction is unknown and likely to be in this "problematic range" in many practical settings (see Figure 3), we recommend that researchers avoid the data-driven model-selection approach.

#### [Figure 2 about here.]

Remark 2. As Figure 2 shows, model selection is less of a concern when the interactions are either zero or very large, but is a first-order issue when interactions are in the problematic range noted above. This issue is relevant in many settings. For instance, Banerjee et al. (2021) have proposed a LASSO-based method for selecting and making inferences on the most effective combination of treatments. However, they do so by imposing the restriction that "[treatments and their interactions] have either no effect or have sufficiently large (positive or negative) influence on the outcomes". In other words, they avoid the problem noted above by assuming that the interactions are outside the "problematic range" in Figure 2. While their goal differs from ours (making inferences on the best treatment combination vs. making inferences on main and interaction effects), this example illustrates the continued prevalence of model selection in the analysis of field experiments.

#### <span id="page-12-0"></span>2.6 Inference on interaction effects

An alternative motivation for factorial designs is to learn about interactions and jointly explore the parameter space of main and interaction effects.

However, detecting interaction effects requires much larger sample sizes than needed for detecting main effects. To illustrate, we compare the standard errors of the OLS estimator of the interaction effect,  $\hat{\beta}_{12}$ , and the main effect,  $\hat{\beta}_1$ . Under the assumptions in Section 2.4, the standard errors are  $SE(\hat{\beta}_1) = \sigma\sqrt{\frac{1}{N_1} + \frac{1}{N_2}}$  and  $SE(\hat{\beta}_{12}) = \sigma\sqrt{\frac{1}{N_1} + \frac{1}{N_2} + \frac{1}{N_3} + \frac{1}{N_4}}$ . Since  $SE(\hat{\beta}_1) < SE(\hat{\beta}_{12})$ , the power for detecting interaction effects is always lower than the power for detecting main effects, and the required sample size for detecting interaction effects is always larger than the required sample size for detecting main effects of equal magnitude. For example, we need eight times the sample

<span id="page-12-1"></span><sup>&</sup>lt;sup>10</sup>See their Assumption 3 and footnote 11 for a formal statement.

size to have the same power to detect an interaction effect as to detect the main effect, when the interaction is half the size of the main effect (see Appendix [A.3\)](#page-62-0). Given the more onerous sample size requirements to detect interactions relative to main effects, it is not surprising that only few of the interaction effects are significant in the reanalysis in Section [3.2.1.](#page-15-0)

Further, even when interactions estimates are significant, they can be misleading because significant results in under-powered studies are much more likely to reflect an outlier estimate of the interaction. In particular, low power is associated with a high Type-M error (or exaggeration ratio) [\(Gelman & Carlin,](#page-29-0) [2014\)](#page-29-0). The Type-M error is the expectation of the absolute value of the estimator in a hypothetical replication study based on the same design as the original study, conditional on being significant, divided by the true effect (see p.643 and Figure 1 in [Gelman & Carlin,](#page-29-0) [2014\)](#page-29-0). For example, if the experiment has 80% power to detect treatment effects of 0*.*2*σ* or larger at the 5% level using the long model and the true value of the interaction is 0*.*1*σ*, then the Type-M error for *β*ˆ <sup>12</sup> is ∼251%. That is, the estimator of the interaction would, on average, be over two times larger than the true value, conditional on being significant. Figure [A.9](#page-65-0) in Appendix [A.3](#page-62-0) shows the relationship between the Type-M error and the power of the experiment.

Note that using the long model to estimate and learn about interactions is fine since the long model estimator is always consistent and asymptotically normal, even if noisy in finite samples. The problem we document here arises because of the focus on statistical significance to assess whether a result is meaningful. Combined with the well-documented publication bias towards significant results (e.g., [Franco et al.,](#page-29-3) [2014;](#page-29-3) [Andrews & Kasy,](#page-26-0) [2018;](#page-26-0) [Christensen & Miguel,](#page-28-1) [2018;](#page-28-1) [Abadie,](#page-26-1) [2020\)](#page-26-1), the discussion above suggests that published results from under-powered studies are likely to meaningfully exaggerate the true effect. Following [Gelman & Carlin](#page-29-0) [\(2014\)](#page-29-0), we suggest studies report power to detect interactions (as well as Type-M errors) in their pre-analysis plan.

# **3 Factorial designs in practice**

In this section we document common practices among researchers studying field experiments with factorial designs.

#### **3.1 Data and descriptive statistics**

We analyze all articles published between 2007 and 2017 in the top five journals in Economics.[11](#page-14-1) Of the 3,505 articles published in this period, 124 (3.5%) are field experiments (Table [A.6](#page-73-0) provides more details). Factorial designs are widely used: Among 124 field experiments 27 (22%) had a factorial design.[12](#page-14-2) Only 8 of these 27 articles with factorial designs (∼30%) used the long model including all interaction terms as their main specification (see Table [2\)](#page-42-0).

[Table 2 about here.]

#### <span id="page-14-0"></span>**3.2 Ignoring interactions in practice**

In Section [2.4,](#page-10-1) we have shown that ignoring interactions can lead to substantial size distortions and false positives. Here, we examine the practical implications of ignoring the interactions in the papers listed in Table [A.1.](#page-44-0) We reanalyze the data from all field experiments with factorial designs and publicly available data that do not include all the interactions in the main specification.[13](#page-14-3) Of the ten most-cited papers with factorial designs listed in Table [A.1,](#page-44-0) only one includes all the interactions in the main specification. More recent papers (which are less likely to be among the most cited) are more likely to include all interaction terms. Out of the 27 papers with factorial designs published in

<span id="page-14-1"></span><sup>11</sup>These journals are *The American Economic Review*, *Econometrica*, *The Journal of Political Economy*, *The Quarterly Journal of Economics*, and *The Review of Economic Studies*. We exclude the May issue of the American Economic Review, known as "AER: Papers and Proceedings".

<span id="page-14-2"></span><sup>12</sup>We do not consider two-stage randomization designs as factorial designs. A two-stage randomization design is where some treatment is randomly assigned in one stage. In the second stage, treatment status is re-randomized to study behavioral changes conditional on a realization of the previous treatment. Examples of studies with two-stage randomization designs include [Karlan & Zinman](#page-30-7) [\(2009\)](#page-30-7), [Ashraf et al.](#page-27-7) [\(2010\)](#page-27-7), and [Cohen & Dupas](#page-28-8) [\(2010\)](#page-28-8). Finally, we do not include experiments where there is no "treatment", but rather conditions are randomized to elicit individuals preference parameters (e.g., [Andersen et al.,](#page-26-5) [2008;](#page-26-5) [Fisman](#page-29-6) [et al.,](#page-29-6) [2008;](#page-29-6) [Gneezy et al.,](#page-30-8) [2009\)](#page-30-8).

<span id="page-14-3"></span><sup>13</sup>We also reanalyze the effect of not including the interaction in the studies that do include all the interactions in their main specification in Appendix [A.1.4.](#page-59-0)

top-5 journals, 19 papers do not include all interaction terms (over 70%).[14](#page-15-1) Of these 19, 4 papers did not have publicly-available replication data. In an online appendix we describe the experimental design of each of the 27 papers and provide details on our replication analysis.[15](#page-15-2)

We downloaded the publicly-available data files and replicated the main results in each of the remaining 15 papers. We standardized the outcome variable in each paper to have mean zero and standard deviation of one. We then compared the original treatment effects (estimated without the interaction terms) with those estimated including the interaction terms.[16](#page-15-3) In other words, we compare estimates based on the short model (Equation [\(2\)](#page-7-1)) to those based on the long model (Equation [\(1\)](#page-7-0)).

#### <span id="page-15-0"></span>**3.2.1 Key facts about interactions**

As the discussion in Section [2.4](#page-10-1) highlights, the extent to which the short model will not control size depends on the value of the interactions in practice. We therefore start by plotting the distribution of estimated interaction effects (Figure [3\)](#page-36-0) and documenting facts regarding interactions from our reanalysis. We find that interactions are quantitatively important and typically not second-order. All estimates are measured in standard deviations (*σ*) of the outcome variable. While the median (mean) interaction for these papers is 0.00*σ* (0.00*σ*), the median (mean) absolute value of the interaction is 0.07*σ* (0.13*σ*). The median (mean) absolute value of interactions relative to the main treatment effects is 0.37 (1.55). Thus, while it may be true that interactions are small on average across all studies, they are often sizeable in any given study. In our data, the absolute value of the interactions is greater than 0.1*σ* in 36% and greater than 0.2*σ* in 19% of the cases. These magnitudes lead to a 12% and 35% chance of rejecting the null of no effect in our running example (as seen in Figure [1\)](#page-34-0), which corresponds to more than a doubling and a sextupling, respectively, in the rate of false rejections at the 5% level.

The second key finding is that most experiments will rarely reject the null hypothesis that the interactions are zero (Figure [3](#page-36-0) shades the fraction of the interactions that are significant in the

<span id="page-15-1"></span><sup>14</sup>While we restrict our reanalysis to papers published in "top five" journals, factorial designs are also prevalent in papers published in lower-ranked journals. Hence, the total number of articles focusing on the short model published in this period is likely much larger.

<span id="page-15-3"></span><span id="page-15-2"></span><sup>15</sup>Available at [http://mauricio-romero.com/pdfs/papers/Appendix\\_crosscuts.pdf](http://mauricio-romero.com/pdfs/papers/Appendix_crosscuts.pdf)

<sup>16</sup>If studies have factorial designs that cross-randomize more than two treatments, we only include two-way interactions in this calculation.

studies that we reanalyze). Among the 15 papers that we reanalyzed, 6.2% of interactions (spread across 4 papers) are significant at the 10% level, 3.6% are significant at the 5% level (spread across 3 papers), and 0.9% are significant at the 1% level (in 1 paper).[17](#page-16-0) These findings are not surprising because factorial designs are rarely powered to detect meaningful interactions.

The fact that most experiments were not explicitly powered to detect interactions suggests that the main reason for running experiments with factorial designs seems to be the increase in power for detecting main effects. However, as we show below, this comes at the considerable cost of an increased rate of false positives (which is unsurprising based on the distribution of interactions shown in Figure [3\)](#page-36-0).

#### [Figure 3 about here.]

**3.2.2 Ignoring interactions has important implications for estimation and inference** Figure [4a](#page-37-0) compares the original treatment effect estimates based on the short model to the estimates based on the long model which includes the interaction terms (Figure [4b](#page-37-0) zooms in to cases where the value of the main treatment effects in the short model is between -1 to 1 standard deviation). The median change in the absolute value of the point estimate of the main treatment effect is 96%. Roughly 26% of estimated treatment effects change sign when they are estimated using the long regression.

Table [3](#page-43-0) shows how the significance of the main treatment estimates changes when using the long instead of the short model. About 48% of treatment estimates that were significant at the 10% level based on the short model are no longer significant based on the long model. 53% and 57% of estimates lose significance at the 5% and 1% levels, respectively. A much smaller fraction of treatment effects that were not significant in the short model are significant based on the long regression (6%, 5%, and 1%, at the 10%, 5%, and 1% levels, respectively).[18](#page-16-1)

<span id="page-16-0"></span><sup>17</sup>Among the papers that originally included all interactions, 4.5% of interactions are significant at the 10% level, 1.1% are significant at the 5% level, and 0.0% are significant at the 1% level. See Appendix [A.1.4](#page-59-0) for more details.

<span id="page-16-1"></span><sup>18</sup>These results are not driven by just a few papers. If we first estimate the median change in the absolute value of the estimate *within* each paper, and then the median change across

We find similar results when we restrict our reanalysis to the ten most cited papers with factorial designs that do not include the interaction terms (with data available for reanalysis). When we re-estimate the treatment effects in these papers after including interactions, we find that out of 21 results that were significant at the 5% level in the paper, 9 (or 43%) are no longer so after including interactions. Corresponding figures and tables are presented in Appendix [A.1.2](#page-53-0) (Figure [A.2](#page-53-1) and Table [A.2\)](#page-54-0).

Finally, we also distinguish between policy and conceptual experiments in Table [A.1](#page-44-0) (the latter typically have more treatments and interactions) and see that the problem of incorrect inference from ignoring interaction terms remains even when we restrict attention to the policy experiments. Of the 12 policy experiments, 9 do not include all interactions. When we re-estimate the treatment effects in these 9 papers after including interactions, we find that out of 19 results that were significant at the 5% level in the paper, 6 (or 32%) are no longer so after including interactions. Corresponding figures and tables are presented in Appendix [A.1.3](#page-56-0) (Figure [A.4](#page-56-1) and Table [A.3\)](#page-57-0).[19](#page-17-0)

[Figure 4 about here.]

[Table 3 about here.]

# **4 Improving power for detecting main effects**

We now examine whether it is possible to improve power for detecting main effects relative to long model *t*-tests, while maintaining size control for relevant values of the interactions. We consider papers, the result is similar to estimating the median absolute changes across all estimates at 97%. Likewise, if we first estimate the proportion of estimates that change sign within each paper, and then estimate the average across papers the result is 25%, which is similar to estimating the proportion of estimates that change sign. Finally, 73% of papers have at least one estimate that is no longer significant at the 10% level when estimating the full model, 77% have at least one estimate that is no longer significant at the 5% level, and 82% have at least one estimate that is no longer significant at the 1% level.

<span id="page-17-0"></span><sup>19</sup>Among the papers that originally included all interactions, 23% of results that are significant at the 5% level in the short model are not significant in the long model. See Appendix [A.1.4](#page-59-0) for more details.

2×2 factorial designs and briefly comment on factorial designs with more than two treatments at the end of each subsection. Throughout, we will focus on the main ideas underlying the different econometric methods. Appendix [A.4](#page-65-1) provides detailed descriptions and implementation details.

### **4.1 Setup**

We focus on *β*<sup>1</sup> and partial out *T*<sup>2</sup> and the constant, keeping the partialling-out implicit. Defining *T*12=*T*1*T*2, the regression model of interest is

<span id="page-18-2"></span>
$$Y = \beta_1 T_1 + \beta_{12} T_{12} + \varepsilon. \tag{11}$$

Our goal is to test hypotheses about the main effect *β*1.

The two-sided long model *t*-test is the uniformly most powerful test among tests that are unbiased for all values of the interaction effect (e.g., [van der Vaart,](#page-32-2) [1998;](#page-32-2) [Elliott et al.,](#page-29-4) [2015a\)](#page-29-4).[20](#page-18-0) This implies that any test that is more powerful than the long model *t*-test for some values of *β*<sup>12</sup> must have lower power somewhere else. Thus, to achieve higher power than the long model *t*-test, one has to choose which values of *β*<sup>12</sup> to direct power to based on prior knowledge.

If one insists on size control for all *β*12, the scope for power improvements relative to the long model *t*-test is theoretically limited.[21](#page-18-1) For example, at the 5%-level, the maximal theoretically possible power improvement over the long model two-sided *t*-test is 12.5 percentage points. Section [4.2](#page-19-0) proposes a nearly optimal test that comes close to achieving the maximal power gain at a priori likely values of the interaction, while controlling size for all values of the interaction. In Appendix [A.6,](#page-71-0) we show that a Bonferroni-style correction after model selection leads to local power improvements for a range of positive values of the interaction.

The limited scope for power improvements relative to the long model *t*-test motivates relaxing the uniform size control requirement and imposing additional restrictions on *β*12. An extreme example is the short model *t*-test, which can improve power relative to long model *t*-test by much more than 12.5%, but only controls size under the restrictive assumption that *β*12=0. In Section

<span id="page-18-1"></span><span id="page-18-0"></span><sup>20</sup>A test is unbiased if its power is larger than its size.

<sup>21</sup>This is because the one-sided long model *t*-tests are uniformly most powerful (e.g., Proposition 15.2 in [van der Vaart,](#page-32-2) [1998\)](#page-32-2) so that, for any *β*12, the maximal power is achieved by a one-sided *t*-test (e.g., [Armstrong & Kolesar,](#page-27-8) [2015,](#page-27-8) [2021\)](#page-27-9). See [Armstrong & Kolesar](#page-27-10) [\(2018\)](#page-27-10) for a discussion of the implications for confidence intervals.

[4.3,](#page-19-1) we explore an intermediate approach that restricts the magnitude of *β*12, which is often more realistic than assuming that *β*<sup>12</sup> is exactly equal to zero.

<span id="page-19-0"></span>**4.2 Nearly optimal tests targeting power towards a likely value** *β*¯ 12 Suppose that a particular value *β*<sup>12</sup> = *β*¯ <sup>12</sup> is a priori likely and that we want to find a test that controls size for all values of *β*<sup>12</sup> and is as powerful as possible when *β*12=*β*¯ <sup>12</sup>. For concreteness, we focus on the case where *β*¯ <sup>12</sup>=0 and consider the testing problem

<span id="page-19-2"></span>
$$H_0: \beta_1 = 0, \ \beta_{12} \in \mathbb{R} \quad \text{against} \quad H_1: \beta_1 \neq 0, \ \beta_{12} = 0.$$
 (12)

We use the numerical algorithm developed by [Elliott et al.](#page-29-4) [\(2015a,](#page-29-4)[b\)](#page-29-7) to construct a nearly optimal test for the testing problem [\(12\)](#page-19-2). [22](#page-19-3) [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4) consider a setting where one is interested in maximizing weighted average power. The best test in this setting is a Neyman-Pearson test based on the least favorable distribution (LFD). Since the LFD is often difficult to compute analytically, [Elliott](#page-29-4) [et al.](#page-29-4) [\(2015a\)](#page-29-4) instead focus on an approximate LFD, which yields feasible and nearly optimal tests.

#### [Figure 5 about here.]

Figure [5](#page-38-0) displays the results of applying the nearly optimal test in our running example. The test controls size for all values of *β*<sup>12</sup> and, by construction, is nearly optimal when *β*12=0. For example, when *β*<sup>1</sup> = 0*.*2 the power of the nearly optimal test is 98.5% of the maximal possible power at *β*12=0 (implied by the corresponding uniformly most powerful one-sided *t*-test). A comparison with the long model *t*-test shows that the nearly optimal test is more powerful when *β*<sup>12</sup> is close to zero.

However, these power gains come at a cost. For certain values of *β*12, the power can be much lower than that of the long model *t*-test. Appendix [A.7.3](#page-76-0) provides a comprehensive assessment of the performance of the nearly optimal tests by plotting power curves for different values of *β*1.

Finally, the nearly optimal test of [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4) becomes computationally prohibitive with many interactions (i.e., many nuisance parameters) and, thus, cannot be recommended for complicated factorial designs. The Bonferroni approach of [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4) discussed in Appendix [A.6](#page-71-0) constitutes a possible alternative in such settings.

<span id="page-19-3"></span><span id="page-19-1"></span><sup>22</sup>Our code to implement this procedure for 2×2 factorial designs is available at [https://](https://mtromero.shinyapps.io/elliott/) [mtromero.shinyapps.io/elliott/](https://mtromero.shinyapps.io/elliott/)

# 4.3 Inference under a priori restrictions on the magnitude of $\beta_{12}$ If the researcher is certain that $\beta_{12} = \bar{\beta}_{12}$ , she can obtain powerful tests based on a regression of $Y - \bar{\beta}_{12}T_{12}$ on $T_1$ . If $\bar{\beta}_{12} = 0$ , this corresponds to the short model t-test. As shown in Section 2.4, short model t-tests are more powerful than long model t-tests when $\beta_{12} = 0$ , but do not control size when $\beta_{12} \neq 0$ .

Exact knowledge of  $\beta_{12}$  may be too strong of an assumption. Suppose instead that the researcher imposes prior knowledge in the form of a restriction on the magnitude of the interaction effect  $\beta_{12}$ .

# <span id="page-20-0"></span>Assumption 1. $|\beta_{12}| \leq C$ for some $C < \infty$ .

Assumption 1 restricts the parameter space for  $\beta_{12}$  and implies that  $\beta_{12} \in [-C,C]$ . We explore two different approaches for making inferences under this assumption. First, we construct optimal confidence intervals under Assumption 1 based on the approach developed by Armstrong et al. (2020). Their confidence intervals are based on linear estimators for  $\beta_1$  and account for the worst case bias of the estimators. As a result, the length of the confidence interval is determined by the bias and the variance of the estimator, and to obtain optimal confidence intervals one has to solve a bias-variance trade-off. This problem can be solved using convex optimization. We refer to this approach as the Armstrong-Kolesar-Kwon (AKK) approach.

The second approach is based on constructing bounds on the main effect implied by Assumption 1. In particular, upper and lower bounds on  $\beta_1$  can be obtained from regressions of  $Y+CT_{12}$  on  $T_1$  and  $Y-CT_{12}$  on  $T_1$ , respectively. We apply the procedure of Imbens & Manski (2004) and Stoye (2009) to construct valid confidence intervals for  $\beta_1$ . We refer to this approach as the Imbens-Manski-Stoye (IMS) approach.<sup>23</sup>

<span id="page-20-1"></span>In Figure 6, we report the rejection probabilities of tests that reject if zero is not in the AKK and  $\overline{\phantom{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa$ 

IMS confidence intervals. To illustrate, we assume that *C* =0*.*1, implying that *β*12∈[−0*.*1*,*0*.*1]. [24](#page-21-0) Our results suggest that AKK and IMS can be substantially more powerful than long model *t*tests when the prior knowledge is correct, but may exhibit size distortions when it is not. Panel (b) shows that the AKK and IMS power curves cross at zero. Thus, the choice between the two approaches should be based on which values of the interaction the researchers want to direct power to. Appendices [A.7.4](#page-77-0) and [A.7.5](#page-78-0) present the corresponding power curves for different values of *β*1.

When researchers are primarily interested in the main effects and feel confident that the interactions are second-order, AKK and IMS should be strictly preferred to the short model, since it is more realistic to pre-specify that the interaction is in a range than exactly zero. However, pre-specifying the appropriate range of prior values for the interaction is non-trivial and requires judgment.[25](#page-21-1)

AKK and IMS remain computationally feasible in more complicated factorial designs. However, both approaches require reliable prior knowledge on the magnitude of potentially very many interactions to yield notable power improvements.

#### [Figure 6 about here.]

<span id="page-21-2"></span><span id="page-21-0"></span><sup>24</sup>Note that in our simulations *σ*=1. This is similar to standardizing the outcome by the sample variance in the control group. Thus, the scale of the coefficients (*β*1, *β*2, and *β*12) and of *C* can be interpreted as "standard deviations of the outcome". As mentioned above, in the papers we replicate, the median (mean) *absolute* value of the interaction is 0.07 (0.13) of the standard deviation of the outcome. Further, the absolute value of the interactions is greater than 10% of the standard deviation of the outcome in 36% of cases. Thus, in many settings it might be reasonable to assume *β*12∈[−0*.*1*,*0*.*1], but researchers will need to judge, depending on the context, what a reasonable value for *C* is.

<span id="page-21-1"></span><sup>25</sup>It is problematic to use AKK or IMS based on first running the long model and not rejecting that the interaction is in a certain range. This would result in data-dependent model selection issue similar to those documented in Section [2.5.](#page-11-0) Thus, while AKK and IMS are improvements over the short model, they do not solve the underlying problem of not knowing the true value of the interaction.

#### **4.4 A design-based approach for improving power**

The discussion above focused on improving power for detecting main effects in existing experiments with factorial designs. While these techniques can also be used to analyze new experiments (and be included in a pre-analysis plan), a design-based alternative is to leave the "interaction cell" empty (i.e., to set *N*4=0) and to re-assign those subjects to the other cells (see Table [A.5\)](#page-70-0).

Leaving the interaction cell empty yields power improvements for testing hypotheses about the main effects relative to long model *t*-tests (see Appendix [A.5\)](#page-69-0). Figure [7](#page-40-0) provides an illustration based on our running example. Leaving the interaction cell empty yields tests that control size for all values of the interaction and achieve the highest power among the approaches with uniform size control (the long model *t*-test and the nearly optimal test).

This design (with interaction cells empty) yields power gains relative to running two separate experiments, because the control group is used twice. But it avoids the problem of interactions discussed above. An example of such a design is provided by [Muralidharan & Sundararaman](#page-32-10) [\(2011\)](#page-32-10) who study the impact of four different interventions in one experiment with one common control group, but no cross-cutting treatment arms.

#### [Figure 7 about here.]

# **4.5 Which econometric approach should one use in practice?**

For the design of new experiments, if the primary objects of interest are the main effects, we recommend leaving the interaction cells empty and increasing the number of units assigned exclusively to the treatment or the control groups. This design-based approach controls size and yields notable power improvements over the long model *t*-tests based on a factorial design.

For the reanalysis of existing experiments, the choice of the econometric method for making inferences on the main effects should be based on the strength of the available prior knowledge. If researchers have little prior knowledge about the interaction effects, we recommend using the long model *t*-tests, which are the uniformly most powerful unbiased tests. If prior knowledge about the interaction effects is available, but the researchers are not confident enough to be willing to sacrifice size control for all values of the interactions, we recommend [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal tests. The nearly optimal test allows for targeting power based on prior knowledge while

ensuring uniform size control. If precise prior knowledge about the interaction effects is available, researchers can use the AKK or the IMS approach to leverage such prior knowledge to improve power substantially. However, unlike the other methods, these two approaches exhibit size distortions when the prior knowledge is incorrect.

Irrespective of which method researchers use to improve power by incorporating prior knowledge, such prior knowledge should be pre-specified in the pre-analysis plan. In addition, we recommend always complementing the results with long model *t*-tests (even if only in an appendix). These tests have desirable optimality properties and allow for communicating results without subjective priors about interactions.

In some high-dimensional factorial designs, estimating the long model with all interactions may not be realistic. In this case, we recommend that the authors pre-specify which interactions they will ignore and which treatments they will pool in the pre-analysis plan. To avoid model selection issues, it is crucial that such choices are made ex-ante (and pre-specified) and not be data-driven.

# <span id="page-23-0"></span>**5 When does the short model make sense?**

Our discussion so far shows how using factorial designs and ignoring interactions can lead to incorrect inferences relative to a business-as-usual counterfactual (or pure experimental control group). At the same time, this approach is widely used in practice, perhaps reflecting a perception that classic texts on experimental design endorse it. We revisit these texts and review the historical use of factorial designs in field experiments to clarify the conditions and caveats under which factorial designs and the short model may be appropriate. We highlight four relevant cases below.

The first case is where the goal of initial experiments is to explore several treatment dimensions in an efficient way to generate promising interventions for further testing. For example, [Cochran](#page-28-0) [& Cox](#page-28-0) [\(1957,](#page-28-0) p.152) recommend factorial designs for "exploratory work where the object is to determine quickly the effects of a number of factors over a specified range". Examples of such experiments include (a) agricultural experiments that vary soil, moisture, temperature, fertilizer, and several other inputs; and (b) online A/B testing where large technology companies run thousands of randomized experiments each year to optimize profits over several dimensions (e.g., [Kohavi et al.,](#page-31-6) [2020\)](#page-31-6). Both sets of examples feature sequential testing, making factorial designs an efficient way to quickly learn about which of several treatment dimensions that could be manipulated may be worth

studying and testing further. In contrast, policy experiments are typically run only once, making factorial designs and short model estimates less desirable.

The second case is when the goal of the experiment is not hypothesis testing but to minimize MSE criteria (or other loss functions), which involve a bias-variance trade-off in estimating the main effects. For example, for small values of the interaction effects, estimators based on the short model can yield a lower root MSE than the estimators based on the design which leaves the interaction cell empty [\(Blair et al.,](#page-28-2) [2019\)](#page-28-2). These alternative criteria also justify the use of factorial designs for agricultural experiments and online A/B testing, since their goal is to optimize decision-making over several factors (to maximize yields or profits) as opposed to testing if individual factors are "significant". Again, this contrasts with the case of policy experiments, where the goal is typically to test if a program or policy had a significant effect, and factorial designs and short-model inferences may therefore be problematic.

The third case is to improve an experiment's external validity. [Cochran & Cox](#page-28-0) [\(1957,](#page-28-0) p.152) recommend factorial designs for "experiments designed to lead to recommendations that must apply over a wide range of conditions. Subsidiary factors may be brought into an experiment so as to test the principal factors under a variety of conditions similar to those that will be encountered in the population to which recommendations are to apply"; see also the discussion in [Fisher](#page-29-5) [\(1992\)](#page-29-5). Thus, factorial designs and the short model may be fine when one dimension of the experiment is studying reasonable variants of the main treatment, but less so when all treatments are of primary interest.[26](#page-24-0)

The fourth case is conceptual (as opposed to policy) experiments, such as resume audit studies, where many or all of the characteristics that are randomized (e.g., age, education, race, and gender) do exist in the population. In these cases, a weighted average short model effect may be a reasonable target parameter subject to researchers indicating how the resulting effect should be interpreted. However, even for such experiments, we recommend (when feasible) designing the experiments such that the treatment share of various characteristics being studied is the same as their population proportion. Doing so will make the short-model coefficient more likely to approximate a population relevant parameter of interest.

<span id="page-24-0"></span><sup>26</sup>For example, in [Alatas et al.](#page-26-6) [\(2012\)](#page-26-6), the primary treatment effect of interest is the impact of community-based targeting, but they also randomize different aspects of how to run the community meeting (which are reasonable variants of the main treatment).

# **6 Conclusion**

In this paper we study the theory and practice of inference in randomized experiments with factorial designs. These designs have been widely used and motivated by two main considerations: (i) studying more treatments in a cost-effective way, and (ii) learning about interactions. We show that both of these uses can be problematic in practice, driven to a large extent by the lack of power to detect interactions.

Given our discussion and results, we recommend that (if realistic) studies using factorial designs should always present the fully-saturated long regression model (even if only in an appendix) for transparency. If researchers would like to focus on results from the short model, they should clearly indicate that treatment effects should be interpreted as a composite effect that includes a weightedaverage of interactions with other treatments. Further, if the estimand of interest is based on the short model, this should be specified in a pre-analysis plan, and not justified ex-post based on estimated interactions being insignificant (due to the problem of data-dependent model selection).

In practice, researchers' use of factorial designs and the short model is often motivated by prior beliefs that the absolute values of the interactions are "small". In such cases, the econometric approaches we discuss allow power gains for inference against a business-as-usual counterfactual (over the long model) while maintaining size control for relevant values of the interaction. In such cases, we recommend that researchers pre-specify their priors and intended econometric approach for inference.

If the primary objects of interest are the main effects, an alternative design is to leave the interaction cells empty. This design-based approach naturally controls size and yields notable power improvements. If interaction effects are of primary interest, we recommend that experiments be explicitly powered to detect interactions and to indicate this in the pre-analysis plan (as, for example, in [Mbiti et al.](#page-32-0) [\(2019\)](#page-32-0)).

Recently, our recommendations have been characterized as too conservative by [Banerjee et al.](#page-27-6) [\(2021\)](#page-27-6), who propose a LASSO-based method for making inferences on the most effective combination of treatments. Applying their approach to high-dimensional factorial designs is appealing: it allows researchers to explore the parameter space of main and interaction effects. However, their method relies on the strong assumption that "[treatments and interactions] have either no effect or have sufficiently large (positive or negative) influence on the outcomes." This restriction avoids model

<span id="page-26-9"></span><span id="page-26-8"></span><span id="page-26-7"></span>selection issues by assumption. It may be a good approximation in highly-powered experiments or when researchers have strong prior knowledge about effect sizes.

Finally, it is worth noting that factorial designs do provide an efficient way of learning about multiple treatments as well as their interactions in the same experiment. The problems we highlight stem in large part from using factorial designs in conjunction with a focus on statistical significance for inference on whether treatment effects or interactions are meaningful. This approach reflects the default frequentist paradigm in experimental economics. Going forward, Bayesian methods (that do not privilege a binary "significant or not" threshold for inference) may constitute a promising framework for efficient learning in experiments with cross-cutting designs (e.g., [Kassler et al.,](#page-31-7) [2019\)](#page-31-7).

# <span id="page-26-1"></span>**References**

- Abadie, Alberto. (2020). Statistical nonsignificance in empirical economics. American Economic Review: Insights, 2(2), 193-208.
- <span id="page-26-6"></span>Alatas, Vivi, Banerjee, Abhijit, Hanna, Rema, Olken, Benjamin A., & Tobias, Julia. (2012). Targeting the poor: Evidence from a field experiment in Indonesia. American Economic Review, 102(4), 1206-40.
- Allcott, Hunt, & Taubinsky, Dmitry. (2015). Evaluating behaviorally motivated policy: Experimental evidence from the lightbulb market. American Economic Review, 105(8), 2501-38.
- <span id="page-26-2"></span>Amrhein, Valentin, Greenland, Sander, & McShane, Blake. (2019). Scientists rise up against statistical significance. Nature, 567, 305–307.
- <span id="page-26-5"></span>Andersen, Steffen, Harrison, Glenn W., Lau, Morten I., & Rutström, E. Elisabet. (2008). Eliciting risk and time preferences. Econometrica, 76(3), 583–618.
- Andreoni, James, Rao, Justin M, & Trachtman, Hannah. (2017). Avoiding the ask: A field experiment on altruism, empathy, and charitable giving. Journal of Political Economy, 125(3), 625–653.
- <span id="page-26-0"></span>Andrews, Isaiah, & Kasy, Maximilian. (2018). Identification of and correction for publication bias. forthcoming American Economic Review.
- <span id="page-26-4"></span>Angrist, Joshua D., & Krueger, Alan B. (1999). Chapter 23 - empirical strategies in labor economics. In Orley C. Ashenfelter & David Card (Eds.), (Vol. 3, p. 1277 - 1366). Elsevier.
- <span id="page-26-3"></span>Angrist, Joshua D., & Pischke, Jörn-Steffen. (2009). Mostly harmless econometrics an empiricist's companion. Princeton University Press.

- <span id="page-27-13"></span><span id="page-27-12"></span><span id="page-27-11"></span><span id="page-27-4"></span>Ansel, Jason, Hong, Han, & Li, Jessie. (2018). OLS and 2SLS in randomized and conditionally randomized experiments. Jahrbücher für Nationalökonomie und Statistik, 238(3-4), 243–293.
- <span id="page-27-8"></span>Armstrong, Timothy B., & Kolesar, Michal. (2015). Optimal inference in a class of regression models. arXiv:1511.06028v2. Retrieved from <https://arxiv.org/abs/1511.06028>
- <span id="page-27-10"></span>Armstrong, Timothy B., & Kolesar, Michal. (2018). Optimal inference in a class of regression models. Econometrica, 86(2), 655-683.
- <span id="page-27-9"></span>Armstrong, Timothy B., & Kolesar, Michal. (2021). Sensitivity analysis using approximate moment condition models. Quantitative Economics, 12(1), 77-108.
- <span id="page-27-1"></span>Armstrong, Timothy B., Kolesar, Michal, & Kwon, Soonwoo. (2020). Bias-aware inference in regularized regression models. arXiv:2012.14823.
- <span id="page-27-7"></span>Ashraf, Nava, Berry, James, & Shapiro, Jesse M. (2010). Can higher prices stimulate product use? evidence from a field experiment in zambia. American Economic Review, 100(5), 2383-2413.
- <span id="page-27-2"></span>Athey, Susan, & Imbens, Guido W. (2017). The econometrics of randomized experiments. In Handbook of economic field experiments (Vol. 1, pp. 73–140). Elsevier.
- Balafoutas, Loukas, Beck, Adrian, Kerschbamer, Rudolf, & Sutter, Matthias. (2013). What drives taxi drivers? a field experiment on fraud in a market for credence goods. Review of Economic Studies, 80(3), 876–891.
- <span id="page-27-6"></span>Banerjee, Abhijit, Chandrasekhar, Arun G, Dalpath, Suresh, Duflo, Esther, Floretta, John, Jackson, Matthew O, .. . Shrestha, Maheshwor (2021). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization (Working Paper No. 28726). National Bureau of Economic Research.
- <span id="page-27-5"></span>Banerjee, Abhijit, Cole, Shawn, Duflo, Esther, & Linden, Leigh. (2007). Remedying education: Evidence from two randomized experiments in India. The Quarterly Journal of Economics, 122(3), 1235-1264.
- <span id="page-27-0"></span>Banerjee, Abhijit, & Duflo, Esther. (2005). Chapter 7 growth theory through the lens of development economics. In Philippe Aghion & Steven N. Durlauf (Eds.), (Vol. 1, p. 473 - 552). Elsevier.
- <span id="page-27-3"></span>Bertrand, Marianne, Karlan, Dean, Mullainathan, Sendhil, Shafir, Eldar, & Zinman, Jonathan. (2010). What's advertising content worth? evidence from a consumer credit marketing field experiment. The Quarterly Journal of Economics, 125(1), 263-306.

- <span id="page-28-13"></span><span id="page-28-12"></span><span id="page-28-11"></span><span id="page-28-10"></span><span id="page-28-9"></span><span id="page-28-2"></span>Blair, Graeme, Cooper, Jasper, Coppock, Alexander, & Humphreys, Macartan. (2019). Declaring and diagnosing research designs. American Political Science Review, 113(3), 838?859.
- Blattman, Christopher, Jamison, Julian C., & Sheridan, Margaret. (2017). Reducing crime and violence: Experimental evidence from cognitive behavioral therapy in Liberia. American Economic Review, 107(4), 1165-1206.
- <span id="page-28-5"></span>Brodeur, Abel, Cook, Nikolai, & Heyes, Anthony. (2020). Methods matter: p-hacking and publication bias in causal analysis in economics. American Economic Review, 110(11), 3634-60.
- <span id="page-28-4"></span>Brodeur, Abel, Le, Mathias, Sangnier, Marc, & Zylberberg, Yanos. (2016). Star wars: The empirics strike back. American Economic Journal: Applied Economics, 8(1), 1-32.
- Brown, Jennifer, Hossain, Tanjim, & Morgan, John. (2010). Shrouded attributes and information suppression: Evidence from the field. The Quarterly Journal of Economics, 125(2), 859–876.
- <span id="page-28-3"></span>Bruhn, Miriam, & McKenzie, David. (2009). In pursuit of balance: Randomization in practice in development field experiments. American Economic Journal: Applied Economics, 1(4), 200- 232.
- <span id="page-28-6"></span>Bugni, Federico A., Canay, Ivan A., & Shaikh, Azeem M. (2018). Inference under covariate-adaptive randomization. Journal of the American Statistical Association, 113(524), 1784-1796.
- <span id="page-28-7"></span>Bugni, Federico A., Canay, Ivan A., & Shaikh, Azeem M. (2019). Inference under covariate-adaptive randomization with multiple treatments. Quantitative Economics, 10(4), 1747-1785.
- <span id="page-28-1"></span>Christensen, Garret, & Miguel, Edward. (2018). Transparency, reproducibility, and the credibility of economics research. Journal of Economic Literature, 56(3), 920-80.
- <span id="page-28-8"></span><span id="page-28-0"></span>Cochran, William G, & Cox, Gertrude M. (1957). Experimental designs. John Wiley & Sons.
- Cohen, Jessica, & Dupas, Pascaline. (2010). Free distribution or cost-sharing? evidence from a randomized malaria prevention experiment. The Quarterly Journal of Economics, 125(1), 1-45.
- Cohen, Jessica, Dupas, Pascaline, & Schaner, Simone. (2015). Price subsidies, diagnostic tests, and targeting of malaria treatment: evidence from a randomized controlled trial. American Economic Review, 105(2), 609–45.
- DellaVigna, Stefano, List, John A, Malmendier, Ulrike, & Rao, Gautam. (2016). Voting to tell others. The Review of Economic Studies, 84(1), 143–181.
- Duflo, Esther, Dupas, Pascaline, & Kremer, Michael. (2011). Peer effects, teacher incentives, and

- <span id="page-29-11"></span><span id="page-29-10"></span><span id="page-29-9"></span><span id="page-29-8"></span>the impact of tracking: Evidence from a randomized evaluation in Kenya. American Economic Review, 101(5), 1739-74.
- <span id="page-29-2"></span>Duflo, Esther, Dupas, Pascaline, & Kremer, Michael. (2015). Education, hiv, and early fertility: Experimental evidence from Kenya. American Economic Review, 105(9), 2757-97.
- <span id="page-29-1"></span>Duflo, Esther, Glennerster, Rachel, & Kremer, Michael. (2007). Using randomization in development economics research: A toolkit. Handbook of development economics, 4, 3895–3962.
- <span id="page-29-4"></span>Elliott, Graham, Müller, Ulrich K, & Watson, Mark W. (2015a). Nearly optimal tests when a nuisance parameter is present under the null hypothesis. Econometrica, 83(2), 771–811.
- <span id="page-29-7"></span>Elliott, Graham, Müller, Ulrich K, & Watson, Mark W. (2015b). Supplement to 'nearly optimal tests when a nuisance parameter is present under the null hypothesis'. Econometrica Supplemental Material.
- Eriksson, Stefan, & Rooth, Dan-Olof. (2014). Do employers use unemployment as a sorting criterion when hiring? evidence from a field experiment. American Economic Review, 104(3), 1014-39.
- Fischer, Greg. (2013). Contract structure, risk-sharing, and investment choice. Econometrica, 81(3), 883–939.
- <span id="page-29-5"></span>Fisher, R. A. (1992). The arrangement of field experiments. In Samuel Kotz & Norman L. Johnson (Eds.), Breakthroughs in statistics: Methodology and distribution (pp. 82–91). New York, NY: Springer New York.
- <span id="page-29-6"></span>Fisman, Raymond, Iyengar, Sheena S, Kamenica, Emir, & Simonson, Itamar. (2008). Racial preferences in dating. The Review of Economic Studies, 75(1), 117–132.
- Flory, Jeffrey A, Leibbrandt, Andreas, & List, John A. (2014). Do competitive workplaces deter female workers? a large-scale natural field experiment on job entry decisions. The Review of Economic Studies, 82(1), 122–155.
- <span id="page-29-3"></span>Franco, Annie, Malhotra, Neil, & Simonovits, Gabor. (2014). Publication bias in the social sciences: Unlocking the file drawer. Science, 345(6203), 1502–1505.
- <span id="page-29-12"></span>Gelman, Andrew. (2018). You need 16 times the sample size to estimate an interaction than to estimate a main effect. Retrieved from [https://statmodeling.stat.columbia.edu/2018/](https://statmodeling.stat.columbia.edu/2018/03/15/need-16-times-sample-size-estimate-interaction-estimate-main-effect/) [03/15/need-16-times-sample-size-estimate-interaction-estimate-main-effect/](https://statmodeling.stat.columbia.edu/2018/03/15/need-16-times-sample-size-estimate-interaction-estimate-main-effect/)
- <span id="page-29-0"></span>Gelman, Andrew, & Carlin, John. (2014). Beyond power calculations: Assessing type S (sign) and

- <span id="page-30-13"></span><span id="page-30-12"></span><span id="page-30-11"></span><span id="page-30-10"></span><span id="page-30-9"></span>type M (magnitude) errors. Perspectives on Psychological Science, 9(6), 641–651.
- <span id="page-30-1"></span>Gerber, A.S., & Green, D.P. (2012). Field experiments: Design, analysis, and interpretation. W. W. Norton.
- <span id="page-30-2"></span>Gilligan, Daniel O, Karachiwalla, Naureen, Kasirye, Ibrahim, Lucas, Adrienne M, & Neal, Derek. (2022). Educator incentives and educational triage in rural primary schools. Journal of Human Resources, 57(1), 79–111.
- <span id="page-30-8"></span>Gneezy, Uri, Leonard, Kenneth L, & List, John A. (2009). Gender differences in competition: Evidence from a matrilineal and a patriarchal society. Econometrica, 77(5), 1637–1664.
- <span id="page-30-4"></span>Hansen, Bruce E. (2022). Econometrics. Princeton University Press.
- Haushofer, Johannes, & Shapiro, Jeremy. (2016). The short-term impact of unconditional cash transfers to the poor: experimental evidence from Kenya. The Quarterly Journal of Economics, 131(4), 1973–2042.
- <span id="page-30-3"></span>Imbens, Guido W., & Manski, Charles F. (2004). Confidence intervals for partially identified parameters. Econometrica, 72(6), 1845–1857.
- <span id="page-30-5"></span>Imbens, Guido W., & Rubin, Donald B. (2015). Stratified randomized experiments. In Causal inference for statistics, social, and biomedical sciences: An introduction (pp. 187–218). Cambridge University Press.
- Jakiela, Pamela, & Ozier, Owen. (2015). Does africa need a rotten kin theorem? experimental evidence from village economies. The Review of Economic Studies, 83(1), 231–268.
- <span id="page-30-0"></span>Kahan, Brennan C. (2013). Bias in randomised factorial trials. Statistics in medicine, 32(26), 4540–4549.
- <span id="page-30-6"></span>Karlan, Dean, & List, John A. (2007). Does price matter in charitable giving? evidence from a large-scale natural field experiment. American Economic Review, 97(5), 1774-1793.
- Karlan, Dean, Osei, Robert, Osei-Akoto, Isaac, & Udry, Christopher. (2014). Agricultural decisions after relaxing credit and risk constraints. The Quarterly Journal of Economics, 129(2), 597–652.
- Karlan, Dean, & Zinman, Jonathan. (2008). Credit elasticities in less-developed economies: Implications for microfinance. American Economic Review, 98(3), 1040-68.
- <span id="page-30-7"></span>Karlan, Dean, & Zinman, Jonathan. (2009). Observing unobservables: Identifying information asymmetries with a consumer credit field experiment. Econometrica, 77(6), 1993–2008.

- <span id="page-31-11"></span><span id="page-31-10"></span><span id="page-31-9"></span><span id="page-31-8"></span><span id="page-31-7"></span>Kassler, Daniel, Nichols-Barrer, Ira, & Finucane, Mariel. (2019). Beyond treatment versus control: How bayesian analysis makes factorial experiments feasible in education research. Evaluation Review.
- Kaur, Supreet, Kremer, Michael, & Mullainathan, Sendhil. (2015). Self-control at work. Journal of Political Economy, 123(6), 1227–1277.
- Kendall, Chad, Nannicini, Tommaso, & Trebbi, Francesco. (2015). How do voters respond to information? evidence from a randomized campaign. American Economic Review, 105(1), 322- 53.
- <span id="page-31-4"></span>Kerwin, Jason T., & Thornton, Rebecca L. (2021). Making the Grade: The Sensitivity of Education Program Effectiveness to Input Choices and Outcome Measures. The Review of Economics and Statistics, 103(2), 251-264.
- <span id="page-31-5"></span>Ketz, Philipp, & McCloskey, Adam. (2021). Short and simple confidence intervals when the directions of some effects are known. Working paper.
- Khan, Adnan Q, Khwaja, Asim I, & Olken, Benjamin A. (2015). Tax farming redux: Experimental evidence on performance pay for tax collectors. The Quarterly Journal of Economics, 131(1), 219–271.
- Kleven, Henrik Jacobsen, Knudsen, Martin B., Kreiner, Claus Thustrup, Pedersen, S�ren, & Saez, Emmanuel. (2011). Unwilling or unable to cheat? evidence from a tax audit experiment in Denmark. Econometrica, 79(3), 651-692.
- <span id="page-31-6"></span>Kohavi, Ron, Tang, Diane, & Xu, Ya. (2020). Trustworthy online controlled experiments: A practical guide to a/b testing. Cambridge University Press.
- <span id="page-31-0"></span>Kremer, Michael. (2003). Randomized evaluations of educational programs in developing countries: Some lessons. The American Economic Review, 93(2), pp. 102-106.
- <span id="page-31-1"></span>Leeb, Hannes, & Pötscher, Benedikt M. (2005). Model selection and inference: Facts and fiction. Econometric Theory, 21(1), 21-59.
- <span id="page-31-2"></span>Leeb, Hannes, & Pötscher, Benedikt M. (2006). Can one estimate the conditional distribution of post-model-selection estimators? The Annals of Statistics, 2554–2591.
- <span id="page-31-3"></span>Leeb, Hannes, & Pötscher, Benedikt M. (2008). Can one estimate the unconditional distribution of post-model-selection estimators? Econometric Theory, 24(02), 338–376.

- <span id="page-32-15"></span><span id="page-32-13"></span><span id="page-32-12"></span><span id="page-32-11"></span>Lehmann, Erich L, & Romano, Joseph P. (2005). Testing statistical hypotheses. Springer Science & Business Media.
- <span id="page-32-5"></span>List, John A, Sadoff, Sally, & Wagner, Mathis. (2011). So you want to run an experiment, now what? some simple rules of thumb for optimal experimental design. Experimental Economics, 14(4), 439.
- <span id="page-32-6"></span>List, John A, Shaikh, Azeem M, & Xu, Yang. (2019). Multiple hypothesis testing in experimental economics. Experimental Economics, 1–21.
- <span id="page-32-14"></span>Lu, Jiannan, Qiu, Yixuan, & Deng, Alex. (2019). A note on Type S/M errors in hypothesis testing. British Journal of Mathematical and Statistical Psychology, 72(1), 1-17.
- <span id="page-32-0"></span>Mbiti, Isaac, Muralidharan, Karthik, Romero, Mauricio, Schipper, Youdi, Manda, Constantine, & Rajani, Rakesh. (2019). Inputs, incentives, and complementarities in education: Experimental evidence from Tanzania. The Quarterly Journal of Economics, 134(3), 1627-1673.
- <span id="page-32-3"></span>McCloskey, Adam. (2017). Bonferroni-based size-correction for nonstandard testing problems. Journal of Econometrics.
- <span id="page-32-4"></span>McCloskey, Adam. (2020). Asymptotically uniform tests after consistent model selection in the linear regression model. Journal of Business & Economic Statistics, 38(4), 810-825.
- <span id="page-32-10"></span>Muralidharan, Karthik, & Sundararaman, Venkatesh. (2011). Teacher performance pay: Experimental evidence from India. Journal of Political Economy, 119(1), 39–77.
- <span id="page-32-8"></span>Olken, Benjamin A. (2007). Monitoring corruption: Evidence from a field experiment in Indonesia. Journal of Political Economy, 115(2), 200-249.
- Pallais, Amanda, & Sands, Emily Glassberg. (2016). Why the referential treatment? evidence from field experiments on referrals. Journal of Political Economy, 124(6), 1793–1828.
- <span id="page-32-7"></span><span id="page-32-1"></span>Ray, D. (1998). Development economics. Princeton University Press.
- Rubin, Donald B. (1974). Estimating causal effects of treatments in randomized and nonrandomized studies. Journal of Educational Psychology, 66(5), 688.
- <span id="page-32-9"></span>Stoye, J�rg. (2009). More on confidence intervals for partially identified parameters. Econometrica, 77(4), 1299–1315.
- Thornton, Rebecca L. (2008). The demand for, and impact of, learning HIV status. American Economic Review, 98(5), 1829-63.
- <span id="page-32-2"></span>van der Vaart, A.W. (1998). Asymptotic statistics. Cambridge University Press.

- <span id="page-33-1"></span>Wasserstein, Ronald L., & Lazar, Nicole A. (2016). The asa statement on p-values: Context, process, and purpose. The American Statistician, 70(2), 129-133.
- <span id="page-33-2"></span>Wasserstein, Ronald L., Schirm, Allen L., & Lazar, Nicole A. (2019). Moving to a world beyond *p<*0*.*05. The American Statistician, 73(sup1), 1-19.
- <span id="page-33-0"></span>Young, Alwyn. (2018). Channeling Fisher: Randomization Tests and the Statistical Insignificance of Seemingly Significant Experimental Results. The Quarterly Journal of Economics, 134(2), 557-598.

<span id="page-34-0"></span>Figure 1: The perceived power gains from the short model come at the cost of biased estimators and not controlling size, unless *β*<sup>12</sup> is exactly equal to zero

*Note: Simulations are based on the running example with sample size N, normal iid errors, and 10,000 repetitions. The size for Figures [1c](#page-34-0) and [1a](#page-34-0) is α*=0*.*05*.*

Figure 2: Model selection does not control size

<span id="page-35-0"></span>*Note: Simulations are based on the running example with sample size N, normal iid errors, and 10,000 repetitions. The size is α*=0*.*05*. For the model selection, the short model is estimated if one fails to reject β*12=0 *at the 5% level.*

Figure 3: Distribution of the estimated interaction effects

<span id="page-36-0"></span>*Note: This figure shows the distribution of the interactions between the main treatments (N=868 in this figure). We trim the top and bottom 1% of the distribution. The median interaction for these papers is 0.00σ (dashed vertical line), the median absolute value of the interaction is 0.07σ (solid vertical line), and the median relative absolute value of the interaction with respect to the main treatment effect is 0.37. 6.2% of interactions are significant at the 10% level, 3.6% are significant at the 5% level, and 0.9% are significant at the 1% level.*

Figure 4: Treatment effects estimates based on the long and the short model

<span id="page-37-0"></span>*Note: This figure shows how the main treatment estimates change between the short and the long model across all studies (N=172 in this figure). Figure [4a](#page-37-0) has all the treatment effects, while Figure [4b](#page-37-0) zooms in to cases where the value of the main treatment effects in the short model is between -1 to 1 standard deviation. The median main treatment estimate from the short model is 0.01σ, the median main treatment estimate from the long model is 0.02σ, the average absolute difference between the treatment estimates of the short and the long model is 0.05σ, the median absolute difference in percentage terms between the treatment estimates of the short and the long model is 96%, and 26% of treatment estimates change sign when they are estimated using the long model instead of the short model.*

<span id="page-38-0"></span>Figure 5: [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test controls size and yields power gains over running the full model near *β*¯ <sup>12</sup>=0

*Note: Simulations are based on the running example with sample size N, normal iid errors, and 10,000 repetitions. The size for Figures [5a](#page-38-0) and [5b](#page-38-0) is α*=0*.*05*. EMW refers to [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test. The power bound in Figure [5b](#page-38-0) is the power of the one-sided long model t-test for the testing problem H*<sup>0</sup> :*β*1=0 *vs. H*<sup>1</sup> :*β*1*>*0*.*

<span id="page-39-0"></span>Figure 6: Restrictions on the magnitude of *β*<sup>12</sup> yield power gains if they are correct but lead to incorrect inferences if they are not

*Note: Simulations are based on the running example with sample size N, normal iid errors, and 10,000 repetitions. The size for Figures [6a](#page-39-0) and [6b](#page-39-0) is α*=0*.*05*. AKK refers to [Armstrong](#page-27-1) [et al.](#page-27-1) [\(2020\)](#page-27-1)'s approach for constructing optimal confidence intervals under prior knowledge about the magnitude of β*12*,* |*β*12| ≤ 0*.*1 *(dashed vertical lines). IMS refers to the [Imbens &](#page-30-3) [Manski](#page-30-3) [\(2004\)](#page-30-3) and [Stoye](#page-32-9) [\(2009\)](#page-32-9) approach for constructing valid confidence intervals under prior knowledge about the magnitude of β*12*,* |*β*12|≤0*.*1 *(dashed vertical lines).*

<span id="page-40-0"></span>Figure 7: Leaving the interaction cell empty increases power relative to approaches that control size for all *β*<sup>12</sup>

*Note: Simulations are based on the running example with sample size N, normal iid errors, and 10,000 repetitions. The size for Figures [7a](#page-40-0) and [7b](#page-40-0) is α* = 0*.*05*. EMW refers to [Elliott](#page-29-4) [et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test. AKK refers to [Armstrong et al.](#page-27-1) [\(2020\)](#page-27-1)'s approach for constructing optimal confidence intervals under prior knowledge about the magnitude of β*12*. IMS refers to the [Imbens & Manski](#page-30-3) [\(2004\)](#page-30-3) and [Stoye](#page-32-9) [\(2009\)](#page-32-9) approach for constructing valid confidence intervals under prior knowledge about the magnitude of β*12*. The design of the experiment with the empty interaction cell is optimal for achieving equal power to detect both main effects; see Appendix [A.5](#page-69-0) for details.*

Table 1: 2×2 factorial design

|    |     | T1 |     |  |  |
|----|-----|----|-----|--|--|
|    |     | No | Yes |  |  |
|    | No  | N1 | N2  |  |  |
| T2 | Yes | N3 | N4  |  |  |

<span id="page-41-0"></span>*Note: N<sup>j</sup>* is the number of individuals randomly assigned to cell *j*.

<span id="page-42-0"></span>Table 2: Field experiments published in top-5 journals between 2007 and 2017

|                           | AER | ECMA | JPE | QJE | ReStud | Total |
|---------------------------|-----|------|-----|-----|--------|-------|
| Field experiments         | 43  | 9    | 14  | 45  | 13     | 124   |
| With factorial designs    | 11  | 2    | 4   | 6   | 4      | 27    |
| Interactions included     | 3   | 1    | 1   | 2   | 1      | 8     |
| Interactions not included | 8   | 1    | 3   | 4   | 3      | 19    |

<span id="page-43-0"></span>Table 3: Significance of treatment estimates based on the long and the short model

**Panel A: Significance at the 10% level**

Without interaction

| With interaction | Not significant | Significant | Total |  |
|------------------|-----------------|-------------|-------|--|
| Not significant  | 95              | 34          | 129   |  |
| Significant      | 6               | 37          | 43    |  |
| Total            | 101             | 71          | 172   |  |

**Panel B: Significance at the 5% level**

Without interaction

| With interaction | Not significant | Significant | Total |  |
|------------------|-----------------|-------------|-------|--|
| Not significant  | 111             | 29          | 140   |  |
| Significant      | 6               | 26          | 32    |  |
| Total            | 117             | 55          | 172   |  |

**Panel C: Significance at the 1% level**

Without interaction

| With interaction | Not significant | Significant | Total |  |
|------------------|-----------------|-------------|-------|--|
| Not significant  | 140             | 17          | 157   |  |
| Significant      | 2               | 13          | 15    |  |
| Total            | 142             | 30          | 172   |  |

This table shows the number of significant coefficients at a given level when estimating the long regression (columns) and the short regression (rows). It includes information from all papers with factorial designs and publicly available data that do not include the interactions in the original study. Panel A uses a 10% significance level, Panel B uses 5%, and Panel C uses 1%.

# <span id="page-44-1"></span>A Online appendix for "Factorial designs, model selection, and (incorrect) inference in randomized experiments"

# A.1 Papers with factorial designs published in Top-5 economics journals

Table A.1: Papers with factorial designs published between 2007 and 2017 in top-5 economics journals sorted by citation count (as of July 4, 2019)

<span id="page-44-0"></span>

|             | Authors                | Title                         | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|-------------|------------------------|-------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|             |                        |                               |         |      |           |            | In Design    | Included     | Available | Evaluation |
| <del></del> | Olken (2007)           | Monitoring Corruption: Evi-   | JPE     | 2007 | 1529      | 3          | 2            | 0            | Yes       | Yes        |
|             |                        | dence from a Field Experiment |         |      |           |            |              |              |           |            |
|             |                        | in Indonesia                  |         |      |           |            |              |              |           |            |
|             | Banerjee et al. (2007) | Remedying Education: Evi-     | QJE     | 2007 | 1213      | 2          | 1            | 0            | Yes       | Yes        |
|             |                        | dence from Two Randomized     |         |      |           |            |              |              |           |            |
|             |                        | Experiments in India          |         |      |           |            |              |              |           |            |

| 2 |  |
|---|--|

| Table A.1 – continued from previous page |                                  |         |      |           |            |              |              |           |            |
|------------------------------------------|----------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
| Authors                                  | Title                            | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|                                          |                                  |         |      |           |            | In Design    | Included     | Available | Evaluation |
| Duflo et al. (2011)                      | Peer Effects, Teacher Incen-     | AER     | 2011 | 787       | 3          | 4            | 0            | Yes       | Yes        |
|                                          | tives, and the Impact of Track-  |         |      |           |            |              |              |           |            |
|                                          | ing: Evidence from a Random-     |         |      |           |            |              |              |           |            |
|                                          | ized Evaluation in Kenya         |         |      |           |            |              |              |           |            |
| Kleven et al. (2011)                     | Unwilling or Unable to Cheat?    | ECMA    | 2011 | 776       | 2          | 1            | 0            | No        | Yes        |
|                                          | Evidence From a Tax Audit        |         |      |           |            |              |              |           |            |
|                                          | Experiment in Denmark            |         |      |           |            |              |              |           |            |
| Karlan et al. (2014)                     | Agricultural Decisions after Re- | QJE     | 2014 | 612       | 2          | 1            | 1            | No        | Yes        |
|                                          | laxing Credit and Risk Con-      |         |      |           |            |              |              |           |            |
|                                          | straints                         |         |      |           |            |              |              |           |            |
| Bertrand et al. (2010)                   | What's Advertising Content       | QJE     | 2010 | 522       | 14         | 85           | 0            | Yes       | No         |
|                                          | Worth? Evidence from a Con-      |         |      |           |            |              |              |           |            |
|                                          | sumer Credit Marketing Field     |         |      |           |            |              |              |           |            |
|                                          | Experiment                       |         |      |           |            |              |              |           |            |

|         | Table A.1 – continued | from previous page             |         |      |           |            |              |              |           |            |
|---------|-----------------------|--------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|         | Authors               | Title                          | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
| _       |                       |                                |         |      |           |            | In Design    | Included     | Available | Evaluation |
|         | Karlan & List (2007)  | Does Price Matter in Charita-  | AER     | 2007 | 506       | 7          | 28           | 0            | Yes       | No         |
|         |                       | ble Giving? Evidence from a    |         |      |           |            |              |              |           |            |
|         |                       | Large-Scale Natural Field Ex-  |         |      |           |            |              |              |           |            |
|         |                       | periment                       |         |      |           |            |              |              |           |            |
|         | Thornton (2008)       | The Demand for, and Impact     | AER     | 2008 | 453       | 2          | 1            | 0            | Yes       | Yes        |
| ಬ       |                       | of, Learning HIV Status        |         |      |           |            |              |              |           |            |
| <b></b> | Haushofer & Shapiro   | The Short-term Impact of Un-   | QJE     | 2016 | 393       | 6          | 8            | 3            | Yes       | Yes        |
|         | (2016)                | conditional Cash Transfers to  |         |      |           |            |              |              |           |            |
|         |                       | the Poor: Experimental Evi-    |         |      |           |            |              |              |           |            |
|         |                       | dence from Kenya               |         |      |           |            |              |              |           |            |
|         | Alatas et al. (2012)  | Targeting the Poor: Evidence   | AER     | 2012 | 330       | 4          | 16           | 0            | Yes       | Yes        |
|         |                       | from a Field Experiment in In- |         |      |           |            |              |              |           |            |
| _       |                       | donesia                        |         |      |           |            |              |              |           |            |

|              | Table A.1 – continued  | from previous page             |         |      |           |            |              |              |           |            |
|--------------|------------------------|--------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|              | Authors                | Title                          | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|              |                        |                                |         |      |           |            | In Design    | Included     | Available | Evaluation |
|              | Karlan & Zinman (2008) | Credit Elasticities in Less-   | AER     | 2008 | 311       | 3          | 2            | 0            | Yes       | No         |
|              |                        | Developed Economies: Impli-    |         |      |           |            |              |              |           |            |
|              |                        | cations for Microfinance       |         |      |           |            |              |              |           |            |
|              | Duflo et al. (2015)    | Education, HIV, and Early Fer- | AER     | 2015 | 282       | 3          | 3            | 1            | Yes       | Yes        |
|              |                        | tility: Experimental Evidence  |         |      |           |            |              |              |           |            |
| 4            |                        | from Kenya                     |         |      |           |            |              |              |           |            |
| <del>-</del> | Andreoni et al. (2017) | Avoiding the Ask: A Field Ex-  | JPE     | 2017 | 270       | 2          | 1            | 1            | Yes       | No         |
|              |                        | periment on Altruism, Empa-    |         |      |           |            |              |              |           |            |
|              |                        | thy, and Charitable Giving     |         |      |           |            |              |              |           |            |
|              | Jakiela & Ozier (2015) | Does Africa Need a Rot-        | ReStud  | 2016 | 245       | 3          | 6            | 6            | Yes       | No         |
|              |                        | ten Kin Theorem? Experi-       |         |      |           |            |              |              |           |            |
|              |                        | mental Evidence from Village   |         |      |           |            |              |              |           |            |
|              |                        | Economies                      |         |      |           |            |              |              |           |            |

|    | Table A.1 – continued   | from previous page             |         |      |           |            |              |              |           |            |
|----|-------------------------|--------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|    | Authors                 | Title                          | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|    |                         |                                |         |      |           |            | In Design    | Included     | Available | Evaluation |
|    | Eriksson & Rooth (2014) | Do Employers Use Unemploy-     | AER     | 2014 | 238       | 34         | 71680        | 0            | Yes       | No         |
|    |                         | ment as a Sorting Criterion    |         |      |           |            |              |              |           |            |
|    |                         | When Hiring? Evidence from     |         |      |           |            |              |              |           |            |
|    |                         | a Field Experiment             |         |      |           |            |              |              |           |            |
|    | Allcott & Taubinsky     | Evaluating Behaviorally Moti-  | AER     | 2015 | 237       | 2          | 1            | 0            | No        | No         |
| ೮ಇ | (2015)                  | vated Policy: Experimental Ev- |         |      |           |            |              |              |           |            |
| ٠, |                         | idence from the Lightbulb Mar- |         |      |           |            |              |              |           |            |
|    |                         | ket                            |         |      |           |            |              |              |           |            |
|    | Flory et al. (2014)     | Do Competitive Workplaces      | ReStud  | 2015 | 204       | 10         | 24           | 12           | Yes       | No         |
|    |                         | Deter Female Workers? A        |         |      |           |            |              |              |           |            |
|    |                         | Large-Scale Natural Field Ex-  |         |      |           |            |              |              |           |            |
|    |                         | periment on Job Entry Deci-    |         |      |           |            |              |              |           |            |
|    |                         | sions                          |         |      |           |            |              |              |           |            |

| Authors                  | Title                          | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|--------------------------|--------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|                          |                                |         |      |           |            | In Design    | Included     | Available | Evaluation |
| Brown et al. (2010)      | Shrouded Attributes and Infor- | QJE     | 2010 | 189       | 3          | 6            | 6            | No        | No         |
|                          | mation Suppression: Evidence   |         |      |           |            |              |              |           |            |
|                          | from the Field                 |         |      |           |            |              |              |           |            |
| DellaVigna et al. (2016) | Voting to Tell Others          | ReStud  | 2017 | 169       | 4          | 15           | 0            | Yes       | No         |
| Fischer (2013)           | Contract Structure, Risk-      | ECMA    | 2013 | 162       | 7          | 9            | 9            | Yes       | No         |
|                          | Sharing, and Investment        |         |      |           |            |              |              |           |            |
|                          | Choice                         |         |      |           |            |              |              |           |            |
| Kaur et al. (2015)       | Self-Control at Work           | JPE     | 2015 | 154       | 8          | 16           | 0            | Yes       | No         |
| Cohen et al. (2015)      | Price Subsidies, Diagnostic    | AER     | 2015 | 151       | 3          | 7            | 7            | Yes       | Yes        |
|                          | Tests, and Targeting of        |         |      |           |            |              |              |           |            |
|                          | Malaria Treatment: Evidence    |         |      |           |            |              |              |           |            |
|                          | from a Randomized Controlled   |         |      |           |            |              |              |           |            |
|                          | Trial                          |         |      |           |            |              |              |           |            |

|   | Table A.1 – continued from previous page |                              |         |      |           |            |              |              |           |            |
|---|------------------------------------------|------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
|   | Authors                                  | Title                        | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|   |                                          |                              |         |      |           |            | In Design    | Included     | Available | Evaluation |
|   | Blattman et al. (2017)                   | Reducing Crime and Violence: | AER     | 2017 | 135       | 2          | 1            | 1            | Yes       | Yes        |
|   |                                          | Experimental Evidence from   |         |      |           |            |              |              |           |            |
|   |                                          | Cognitive Behavioral Therapy |         |      |           |            |              |              |           |            |
|   |                                          | in Liberia                   |         |      |           |            |              |              |           |            |
|   | Khan et al. (2015)                       | Tax Farming Redux: Exper-    | QJE     | 2016 | 133       | 6          | 8            | 0            | Yes       | Yes        |
| 7 |                                          | imental Evidence on Perfor-  |         |      |           |            |              |              |           |            |
| 7 |                                          | mance Pay for Tax Collectors |         |      |           |            |              |              |           |            |
|   | Balafoutas et al. (2013)                 | What Drives Taxi Drivers? A  | ReStud  | 2013 | 126       | 5          | 6            | 0            | Yes       | No         |
|   |                                          | Field Experiment on Fraud in |         |      |           |            |              |              |           |            |
|   |                                          | a Market for Credence Goods  |         |      |           |            |              |              |           |            |
|   | Kendall et al. (2015)                    | How Do Voters Respond to     | AER     | 2015 | 116       | 5          | 5            | 5            | Yes       | No         |
|   |                                          | Information? Evidence from a |         |      |           |            |              |              |           |            |
|   |                                          | Randomized Campaign          |         |      |           |            |              |              |           |            |

| Table A.1 – continued from previous page |                                                         |         |      |           |            |              |              |           |            |
|------------------------------------------|---------------------------------------------------------|---------|------|-----------|------------|--------------|--------------|-----------|------------|
| Authors                                  | Title                                                   | Journal | Year | Citations | Treatments | Interactions | Interactions | Data      | Policy     |
|                                          |                                                         |         |      |           |            | In Design    | Included     | Available | Evaluation |
| Pallais & Sands (2016)                   | Why the Referential Treat-<br>ment? Evidence from Field | JPE     | 2016 | 85        | 3          | 12           | 0            | No        | No         |
|                                          | Experiments on Referrals                                |         |      |           |            |              |              |           |            |

Note: This table provides relevant information from all articles with factorial designs published in top-5 journals. Citation counts are from Google Scholar on July 4th of 2019. Treatments is the number of different treatments in the paper. "Interactions in Design" is the number of interactions in the experimental design. "Interactions Included" is the number of interactions included in the main specification of the paper. Data available, refers to whether the data is publicly available or not. Allcott & Taubinsky (2015) has two field experiments. The table refers to the second one. One of the three dimensions of randomization in Flory et al. (2014) does not appear in the publicly available data. An Online Appendix (in http://mauricio-romero.com/pdfs/papers/Appendix\_crosscuts.pdf) describes the experimental design of each of the 27 papers and provides further details on our replication analysis.

#### **A.1.1 All papers**

Figure A.1: Distribution of the *t*-value of interaction terms across studies

*Note: If studies have factorial designs that cross-randomize more than two treatments only two-way interactions are included in this calculation. The vertical lines are at* ±*1.96.*

#### <span id="page-53-1"></span><span id="page-53-0"></span>**A.1.2 Ten most cited papers**

Long model estimates

Figure A.2: Treatment estimates based on the long and the short model

(a) Main treatment estimates −0.4 −0.2 0.0 0.2 0.4 −0.2 0.0 0.2 0.4 0.6 Short model estimates (b) Interaction Significant − 5% level Not significant − 5% level Frequency 0.00 0.05 0.10 0.15 0.20 0.25 −0.6 −0.4 −0.2 0 0.2 0.4 0.6

Interaction coefficient

*Note: Both figures show treatment estimates from the ten most cited papers with factorial designs and publicly available data that do not include the interactions in the original study. Figure [A.2a](#page-53-1) shows how the main treatment estimates change across the short and the long model across studies (N=85 in this figure). The median main treatment estimate from the short model is 0.01σ, the median main treatment estimate from the long model is 0.01σ, the average absolute difference between the treatment estimates of the short and the long model is 0.05σ, the median absolute difference in percentage terms between the treatment estimates of the short and the long model is 131%, and 28% of treatment estimates change sign when they are estimated using the long instead of the short model. Figure [A.2b](#page-53-1) shows the distribution of the interactions between the main treatments (N=266 in this figure). We trim the top and bottom 1% of the distribution. The median interaction is -0.00σ (dashed vertical line), the median absolute value of the interactions is 0.05σ (dashed vertical line), 5.6% of interactions are significant at the 10% level, 2.6% are significant at the 5% level, and 0.0% are significant at the 1% level, and the median relative absolute value of the interaction with respect to the main treatment effect is 0.37.*

<span id="page-54-0"></span>Table A.2: Significance of treatment estimates based on the long and the short model

**Panel A: Significance at the 10% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 49              | 13          | 62    |
| Significant      | 6               | 17          | 23    |
| Total            | 55              | 30          | 85    |

**Panel B: Significance at the 5% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 60              | 9           | 69    |
| Significant      | 4               | 12          | 16    |
| Total            | 64              | 21          | 85    |

**Panel C: Significance at the 1% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 73              | 3           | 76    |
| Significant      | 1               | 8           | 9     |
| Total            | 74              | 11          | 85    |

This table shows the number of coefficients that are significant at a given level when estimating the long regression (columns) and the short regression (rows). This table only includes information from the ten most cited papers with factorial designs and publicly available data that do not include the interactions in the original study. Table [3](#page-43-0) has data for all papers with factorial designs and publicly available data that do not include the interaction in the original study. Panel A uses a 10% significance level, Panel B uses 5%, and 11

Figure A.3: Distribution of the *t*-value of interaction terms across studies

*Note: If studies have factorial designs that cross-randomize more than two treatments only two-way interactions are included in this calculation. The vertical lines are at* ±*1.96.*

#### <span id="page-56-1"></span><span id="page-56-0"></span>**A.1.3 Policy experiments**

Figure A.4: Treatment estimates from the long and the short regression

(a) Main treatment estimates

(b) Interaction

*Note: Both figures show treatment estimates from the papers with factorial designs and publicly available data that do not include the interactions in the original study and do policy evaluation (N=67 in this figure). Figure [A.4a](#page-56-1) shows how the main treatment estimates change across the short and the long model across studies. The median main treatment estimate from the short model is 0.06σ, the median main treatment estimate from the long model is 0.05σ, the average absolute difference between the treatment estimates of the short and the long model is 0.07σ, the median absolute difference in percentage terms between the treatment estimates of the short and the long model is 69%, and 21% of treatment estimates change sign when they are estimated using the long model instead of the short model. Figure [A.4b](#page-56-1) shows the distribution of the interactions between the main treatments (N=126 in this figure). We trim the top and bottom 1% of the distribution. The median interaction is -0.01σ (dashed vertical line), the median absolute value of interactions is 0.23σ (solid vertical line), 6.3% of interactions are significant at the 10% level, 3.2% are significant at the 5% level, and 0.0% are significant at the 1% level, and the median relative absolute value of the interaction with respect to the main treatment effect is 1.01.*

<span id="page-57-0"></span>Table A.3: Significance of treatment estimates from the long and the short regression

**Panel A: Significance at the 10% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 31              | 10          | 41    |
| Significant      | 5               | 21          | 26    |
| Total            | 36              | 31          | 67    |

**Panel B: Significance at the 5% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 43              | 6           | 49    |
| Significant      | 5               | 13          | 18    |
| Total            | 48              | 19          | 67    |

**Panel C: Significance at the 1% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 56              | 3           | 59    |
| Significant      | 1               | 7           | 8     |
| Total            | 57              | 10          | 67    |

This table shows the number of coefficients that are significant at a given level when estimating the long regression (columns) and the short regression (rows). This table only includes information from papers with factorial designs and publicly available data that do not include the interactions in the original study and do policy evaluation. Table [3](#page-43-0) has data for all papers with factorial designs and publicly available data that do not include the interaction in the original study. Panel A uses a 10% significance level, Panel B uses 14

Figure A.5: Distribution of the *t*-value of interaction terms across studies

*Note: If studies have factorial designs that cross-randomize more than two treatments only two-way interactions are included in this calculation. The vertical lines are at* ±*1.96.*

#### <span id="page-59-1"></span><span id="page-59-0"></span>**A.1.4 Studies with all interactions included**

Figure A.6: Treatment estimates based on the long and the short model

*Note: Both figures show treatment estimates from the papers with factorial designs and publicly available data that do not include the interaction in the original study and do policy evaluation. Figure [A.6a](#page-59-1) shows how the main treatment estimates change across the short and the long model across studies (N=117 in this figure). The median main treatment estimate from the short model is -0.03σ, the median main treatment estimate from the long model is -0.02σ, the average absolute difference between the treatment estimates of the short and the long model is 0.05σ, the median absolute difference in percentage terms between the treatment estimates of the short and the long model is 37%, and 14% of treatment estimates change sign when they are estimated using the long or the short model. Figure [A.6b](#page-59-1) shows the distribution of the interactions between the main treatments (N=104 in this figure). We trim the top and bottom 1% of the distribution. The median interaction is -0.01σ (dashed vertical line), the median absolute value of interactions is 0.08σ (solid vertical line), 4.5% of interactions are significant at the 10% level, 1.1% are significant at the 5% level, and 0.0% are significant at the 1% level, and the median relative absolute value of the interaction with respect to the main treatment effect is 0.52.*

Table A.4: Significance of treatment estimates based on the long and the short model

**Panel A: Significance at the 10% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 61              | 13          | 74    |
| Significant      | 4               | 39          | 43    |
| Total            | 65              | 52          | 117   |

**Panel B: Significance at the 5% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 68              | 10          | 78    |
| Significant      | 6               | 33          | 39    |
| Total            | 74              | 43          | 117   |

**Panel C: Significance at the 1% level**

Without interaction

| With interaction | Not significant | Significant | Total |
|------------------|-----------------|-------------|-------|
| Not significant  | 77              | 12          | 89    |
| Significant      | 2               | 26          | 28    |
| Total            | 79              | 38          | 117   |

This table shows the number of coefficients that are significant at a given level when estimating the long regression (columns) and the short regression (rows). This table only includes information from papers with factorial designs and publicly available data that do include the interaction in the original study. Table [3](#page-43-0) has data for all papers with factorial designs and publicly available data that do not include the interaction in the original study. Panel A uses a 10% significance level, Panel B uses 5%, and Panel C uses 1%. 17

Figure A.7: Distribution of the *t*-value of interaction terms across studies

*Note: If studies have factorial designs that cross-randomize more than two treatments only two-way interactions are included in this calculation. The vertical lines are at* ±*1.96.*

## **A.2 Derivation of expressions for the regression coefficients**

#### **A.2.1 Derivation of the expressions for** *β*1**,** *β*2**, and** *β*<sup>12</sup>

Because the long regression model [\(1\)](#page-7-0) is fully saturated, we have

$$\beta_1 = E(Y|T_1=1,T_2=0) - E(Y|T_1=0,T_2=0),$$

$$\beta_2 = E(Y|T_1=0,T_2=1) - E(Y|T_1=0,T_2=0),$$

$$\beta_{12} = E(Y|T_1=1,T_2=1) - E(Y|T_1=0,T_2=1)$$

$$-[E(Y|T_1=1,T_2=0) - E(Y|T_1=0,T_2=0)].$$

Random assignment implies that, for (*t*1*,t*2)∈{0*,*1}×{0*,*1},

$$E(Y|T_1=t_1,T_2=t_2) = E(Y_{t_1,t_2}|T_1=t_1,T_2=t_2)$$
  
=  $E(Y_{t_1,t_2}).$ 

Thus, it follows that

$$\beta_1 = E(Y_{1,0} - Y_{0,0}),$$

$$\beta_2 = E(Y_{0,1} - Y_{0,0}),$$

$$\beta_{12} = E(Y_{1,1} - Y_{0,1} - Y_{1,0} + Y_{0,0}).$$
18

#### A.2.2 Derivation of the expressions for $\beta_1^s$ and $\beta_2^s$

Here we derive Equation (6). Equation (7) then follows from rearranging terms. The derivations of Equations (8) and (9) are similar and thus omitted.

For the short regression model (2), independence of  $T_1$  and  $T_2$  implies that

$$\beta_1^s = E(Y | T_1 = 1) - E(Y | T_1 = 0).$$

Consider

$$E(Y|T_1=1) = E(Y|T_1=1,T_2=1)P(T_2=1|T_1=1)$$

$$+E(Y|T_1=1,T_2=0)P(T_2=0|T_1=1)$$

$$= E(Y_{1,1})P(T_2=1)+E(Y_{1,0})P(T_2=0),$$

where the first equality follows from the law of iterated expectations and the second equality follows by the definition of potential outcomes and random assignment. Similarly, obtain

$$E(Y|T_1=0) = E(Y_{0,1})P(T_2=1) + E(Y_{0,0})P(T_2=0).$$

Thus, we have

$$\beta_1^s = E(Y|T_1=1) - E(Y|T_1=0)$$
  
=  $E(Y_{1,1}-Y_{0,1})P(T_2=1) + E(Y_{1,0}-Y_{0,0})P(T_2=0).$ 

# <span id="page-62-0"></span>A.3 Power to detect interactions in the long model

Under the assumptions in Section 2.4, the standard errors of the long model are

$$SE\left(\hat{\beta}_{1}\right) = \sigma\sqrt{\frac{1}{N_{1}} + \frac{1}{N_{2}}} \quad \text{and} \quad SE\left(\hat{\beta}_{12}\right) = \sigma\sqrt{\frac{1}{N_{1}} + \frac{1}{N_{2}} + \frac{1}{N_{3}} + \frac{1}{N_{4}}}.$$

To achieve power  $\kappa$ , the true interaction effect needs to satisfy (e.g., Duflo et al., 2007)

$$\beta_{12} > (\Phi^{-1}(\kappa) + \Phi^{-1}(1 - \alpha/2))SE(\hat{\beta}_{12}) = MDE_{\beta_{12}}.$$

where  $\alpha$  is the size of the test. Here MDE stands for minimum detectable effect size. Similarly, to achieve power  $\kappa$  for detecting the main effect, it must satisfy

$$\beta_1 \! > \! \left(\Phi^{-1}(\kappa) \! + \! \Phi^{-1}(1\! - \! \alpha/2)\right) \! SE\!\left(\hat{\beta}_1\right) \! = \! MDE_{\beta_1}.$$

We can relate the MDEs to the overall sample size required for detecting interactions,  $N_I$ , and main effects,  $N_M$ , respectively. To illustrate, suppose that the overall sample size is equally distributed across all four cells (the power-maximizing design for detecting interactions). In this case, the standard errors are  $SE(\hat{\beta}_1) = \sigma \sqrt{8/N_M}$  and  $SE(\hat{\beta}_{12}) = \sigma \sqrt{16/N_I}$ , such that

$$\frac{MDE_{\beta_1}}{MDE_{\beta_{12}}} = \frac{\sigma\sqrt{\frac{8}{N_M}}}{\sigma\sqrt{\frac{16}{N_I}}} \quad \text{and} \quad 2\left(\frac{MDE_{\beta_1}}{MDE_{\beta_{12}}}\right)^2 = \frac{N_I}{N_M}.$$

Suppose that the MDE for the interaction effect is half the MDE for the main effect. Then the relative sample size needed to be adequately powered  $(N_I/N_M)$  is 8. That is, we need eight times the sample size to detect an interaction effect that is half the size of the main effect.<sup>1</sup> Even if the MDE for the interaction is the same as the MDE for the main effect, one would need twice the sample size to detect the interaction effect than to detect the main effect. Figure A.8 illustrates the general relationship between  $N_I/N_M$  and  $MDE_{\beta_{12}}/MDE_{\beta_1}$ .

<span id="page-63-1"></span>Figure A.8: Relative sample size

Note: For We assume the sample is divided equally among the four cells in Table 1. This figure plots the relative sample size  $\left(\frac{N_I}{N_M}\right)$  as a function of the relative MDEs  $\left(\frac{MDE_{\beta_{12}}}{MDE_{\beta_1}}\right)$ .

<span id="page-63-0"></span>Figure A.9 shows the Type-M error for different values of the interaction (relative to the MDE  $^{-1}$ Alternatively, one can compare  $MDE_{\beta_{12}}$  to the MDE based on the short model,  $MDE_{\beta_1^s}$ , as in Gelman (2018). Because  $SE(\hat{\beta}_1^s) = \sigma \sqrt{4/N}$ , the required sample size for detecting an interaction is 16 times larger than for detecting main effects based on the short model.

of the main effect, which determines the sample size).[2](#page-64-0) We use the closed form formula provided by [Lu et al.](#page-32-14) [\(2019\)](#page-32-14) for the Type-M error. In the figure, we assume the MDE for the main effect is 0.2*σ* (or equivalently, a sample of 1,570 equally divided among the four cells, assuming size is *α*=0*.*05 and power is *κ*=0*.*8).

<span id="page-64-0"></span><sup>2</sup>A related problem with under-powered studies is the *Type S error rate*, which is the probability that conditional on being significant, the estimate of the interaction in a hypothetical replication study based on the same design as the original study has an incorrect sign (see p.643 in [Gelman & Carlin,](#page-29-0) [2014\)](#page-29-0).

Figure A.9: Type-M error

<span id="page-65-0"></span>Note: We assume the sample is divided equally among the four cells in Table 1. This figure plots the Type-M error for different values of the interaction (relative to the MDE of the main effect, which determines the sample size). We use the closed form formula provided by Lu et al. (2019) for the Type-M error. We assume that size is  $\alpha = 0.05$ , power is  $\kappa = 0.8$ , and the MDE for the main effect is  $0.2\sigma$  (i.e., a sample of 1,570 equally divided among the four cells).

# <span id="page-65-1"></span>A.4 Detailed description of the econometric methods

#### A.4.1 The EMW approach

To describe Elliott et al. (2015a)'s nearly optimal test, note that under standard conditions, the *t*-statistics are approximately normally distributed in large samples

$$\begin{pmatrix} \hat{t}_1 \\ \hat{t}_{12} \end{pmatrix} \stackrel{a}{\sim} N \begin{pmatrix} t_1 \\ t_{12} \end{pmatrix}, \begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}, \tag{13}$$

where  $\hat{t}_1 = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}$ ,  $\hat{t}_{12} = \frac{\hat{\beta}_{12}}{SE(\hat{\beta}_{12})}$ ,  $t_1 = \frac{\beta_1}{SE(\hat{\beta}_1)}$ ,  $t_{12} = \frac{\beta_{12}}{SE(\hat{\beta}_{12})}$ , and  $\rho = Cov(\hat{t}_1, \hat{t}_{12})$ . Define  $\hat{t} = (\hat{t}_1, \hat{t}_{12})$  and  $t = (t_1, t_{12})$ . In practice, we replace the unknown  $SE(\hat{\beta}_1)$ ,  $SE(\hat{\beta}_{12})$ , and  $Cov(\hat{t}_1, \hat{t}_{12})$  with heteroskedasticity robust estimators, which are consistent under weak conditions.

Consider the problem of maximizing power in the following hypothesis testing problem:

$$H_0: t_1 = 0, t_{12} \in \mathbb{R}$$
 against  $H_1: t_1 \neq 0, t_{12} = 0.$  (14)

A common approach to construct powerful tests for problems with composite hypotheses is to choose tests based on their weighted average power. In particular, we seek a powerful test for " $H_0$ : the density of  $\hat{t}$  is  $f_t, t_1 = 0, t_{12} \in \mathbb{R}$ " against the simple alternative " $H_{1,F}$ : the density of  $\hat{t}$  is  $\int f_t dF(t)$ ", where the weighting function F is chosen by the researcher. Following Elliott et al. (2015a), we choose F so that it assigns equal mass to  $f_t$  and  $f_t$  and  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  against  $f_t$  ag

Since it is generally difficult to analytically determine and computationally approximate  $\Lambda^{LF}$ , Elliott et al. (2015a) suggest to instead focus on an approximate LFD,  $\Lambda^{ALF}$ , which yields a nearly optimal test for  $H_0$  against  $H_{1,F}$ . The resulting test is then just a Neyman-Pearson test based on  $\Lambda^{ALF}$ .

#### A.4.2 The AKK approach

To describe Armstrong et al. (2020)'s approach, we write model (11) in vector form as

$$\mathbf{Y} = \beta_1 \mathbf{T}_1 + \beta_{12} \mathbf{T}_{12} + \varepsilon. \tag{15}$$

Suppose that  $\mathbf{X} = (\mathbf{T}_1, \mathbf{T}_{12})$  is fixed and  $\varepsilon \sim N(0, \sigma^2 \mathbf{I}_N)$ , where  $\sigma^2$  is known.<sup>4</sup> The algorithm we describe below accommodates non-Gaussian and heteroskedastic errors. A linear estimator of  $\beta_1$  can be written as  $\hat{\beta}_1 = a'\mathbf{Y}$ , for some a that can depend on  $\mathbf{X}$ . Given parameters  $(\beta_1, \beta_{12})$ , the bias of  $\hat{\beta}_1$  is  $a'(\beta_1\mathbf{T}_1 + \beta_{12}\mathbf{T}_{12}) - \beta_1$ . The "worst case" bias of  $\hat{\beta}_1$  is

$$\overline{\mathsf{bias}} = \sup_{\beta_1 \in \mathbb{R}, \beta_{12} \in [-C, C]} a'(\beta_1 \mathbf{T}_1 + \beta_{12} \mathbf{T}_{12}) - \beta_1. \tag{16}$$

The standard error of  $\hat{\beta}_1$ ,  $SE(\hat{\beta}_1) = \sigma \sqrt{a'a}$ , does not depend on  $(\beta_1, \beta_{12})$ .

<span id="page-66-0"></span><sup>&</sup>lt;sup>3</sup>To improve the performance of their procedure, Elliott et al. (2015a) suggest a switching rule that depends on  $|\hat{t}_{12}|$  such that for large enough values of  $|\hat{t}_{12}|$ , one switches to regular hypothesis testing. Following their suggestion, we use 6 as the switching value.

<span id="page-66-1"></span> $<sup>{}^{4}</sup>$ If **X** is random, the procedure remains valid, as it is valid conditional on **X**.

The t-ratio  $\frac{\hat{\beta}_1 - \beta_1}{SE(\hat{\beta}_1)}$  is normally distributed,  $\frac{\hat{\beta}_1 - \beta_1}{SE(\hat{\beta}_1)} \sim N(b,1)$ , where  $|b| \leq \frac{\overline{\mathrm{bias}}}{SE(\hat{\beta}_1)}$ . Thus, a two-sided  $(1-\alpha)$  confidence interval centered at  $\hat{\beta}_1$  can be constructed as

<span id="page-67-0"></span>
$$\hat{\beta}_1 \pm cv_\alpha \left(\frac{\overline{\text{bias}}}{SE(\hat{\beta}_1)}\right) SE(\hat{\beta}_1), \tag{17}$$

where  $cv_{\alpha}(x)$  is the  $(1-\alpha)$  quantile of a |N(x,1)| distribution. The length of the confidence interval (17) is increasing in  $\overline{\text{bias}}$  and  $SE(\hat{\beta}_1)$ . Thus, to construct optimal confidence intervals, a is chosen to solve this bias variance trade-off.<sup>5</sup> Armstrong et al. (2020) show that this problem can be solved using a regularized regression of  $\mathbf{T}_1$  on  $\mathbf{T}_{12}$ .

We use Algorithm 3.1 in Section 3 of Armstrong et al. (2020), which accommodates heteroskedastic and non-Gaussian errors.<sup>6</sup> To describe the algorithm, let  $\pi^*_{\lambda}$  denote the solution to the following penalized regression problem

<span id="page-67-3"></span>
$$\min_{\pi} \|\mathbf{T}_1 - \pi \mathbf{T}_{12}\|_2^2 + \lambda |\pi|. \tag{18}$$

The algorithm has three steps.

- 1. Compute initial estimates of the residuals  $\hat{\varepsilon}_1,...,\hat{\varepsilon}_N$  from the long regression model and obtain an initial variance estimator  $\hat{\sigma}^2 = \frac{1}{N} \sum_{i=1}^N \hat{\varepsilon}_i^2$ .
- 2. Compute the solution path  $\{\pi_{\lambda}^*\}_{\lambda>0}$  for the regularized regression (18), indexed by  $\lambda$ . For each  $\lambda$ , compute  $\hat{\beta}_{1,\lambda}$  as

$$\hat{\beta}_{1,\lambda} = \frac{(\mathbf{T}_1 - \pi_{\lambda}^* \mathbf{T}_{12})' \mathbf{Y}}{(\mathbf{T}_1 - \pi_{\lambda}^* \mathbf{T}_{12})' \mathbf{T}_1}$$

$$\tag{19}$$

and obtain  $\overline{\mathrm{bias}}_\lambda$  and  $SE_\lambda$  as

$$\overline{\text{bias}}_{\lambda} = \frac{C}{|\pi_{\lambda}|} \frac{(\mathbf{T}_{1} - \pi_{\lambda}^{*} \mathbf{T}_{12})' \mathbf{T}_{12} \pi_{\lambda}^{*}}{(\mathbf{T}_{1} - \pi_{\lambda}^{*} \mathbf{T}_{12})' \mathbf{T}_{1}} \quad \text{and} \quad SE_{\lambda}^{2} = \frac{\hat{\sigma}^{2} ||\mathbf{T}_{1} - \pi_{\lambda}^{*} \mathbf{T}_{12}||_{2}^{2}}{\left[(\mathbf{T}_{1} - \pi_{\lambda}^{*} \mathbf{T}_{12})' \mathbf{T}_{1}\right]^{2}}.$$
 (20)

<span id="page-67-1"></span>3. Choose  $\lambda^* = \arg\min_{\lambda} cv_{\alpha}\left(\frac{\overline{\mathrm{bias}_{\lambda}}}{SE_{\lambda}}\right) SE_{\lambda}$  and compute robust standard errors  $\widehat{SE_{\mathrm{r},\lambda^*}} =$ 

<sup>5</sup>Optimality here refers to minimizing the width of the confidence intervals. We focus on the width of the confidence intervals because of the intuitive appeal and practical relevance of this criterion. If one were to optimize the power of the test that the confidence interval inverts, the resulting procedure can be different.

<span id="page-67-2"></span><sup>6</sup>The implementation of the optimal confidence intervals with potentially heteroskedastic and non-Gaussian errors mimics the common practice of applying OLS in conjunction with heteroskedasticity robust standard errors, rather than weighted least squares; see Remark 3.2 in Armstrong et al. (2020) for a discussion.

$$\begin{split} \sqrt{\sum_{i=1}^{N} a_{\lambda^*,i}^2 \hat{\varepsilon}_i^2}, \text{ where } a_{\lambda^*} &= \frac{(\mathbf{T}_1 - \pi_{\lambda^*}^* \mathbf{T}_{12})}{(\mathbf{T}_1 - \pi_{\lambda^*}^* \mathbf{T}_{12})' \mathbf{T}_1}. \text{ Return the optimal } (1 - \alpha) \text{ confidence interval} \\ \hat{\beta}_{1,\lambda^*} &\pm c v_\alpha \Bigg( \frac{\overline{\mathrm{bias}}_{\lambda^*}}{\widehat{SE_{\mathrm{r},\lambda^*}}} \Bigg) \widehat{SE_{\mathrm{r},\lambda^*}}. \end{split} \tag{21}$$

#### <span id="page-68-0"></span>A.4.3 The IMS approach

For a given  $\beta_{12} \in [C_1, C_2]$ , the population regression coefficient from a regression of  $Y - \beta_{12}T_{12}$  on  $X = (1, T_1, T_2)'$  is

$$\beta(\beta_{12}) = E(XX')^{-1}E(X(Y-\beta_{12}T_{12}))$$
$$= E(XX')^{-1}E(XY)-\beta_{12}E(XX')^{-1}E(XT_{12})$$

Note that  $E(XX')^{-1}E(XT_{12}) = (\gamma_0, \gamma_1, \gamma_2)'$  is the population regression coefficient from a regression of  $T_{12}$  on X. Independence of  $T_1$  and  $T_2$  implies that  $\gamma_1 = E(T_{12} \mid T_1 = 1) - E(T_{12} \mid T_1 = 0)$  and  $\gamma_2 = E(T_{12} \mid T_2 = 1) - E(T_{12} \mid T_2 = 0)$  both of which are positive. Consequently, the identified set for  $\beta_t$ ,  $t \in \{1,2\}$ , is given by

$$\beta_t \in [\beta_t(C_2), \beta_t(C_1)] = [\beta_t^l, \beta_t^u].$$

The lower bound  $\beta_t^l$  can be estimated from an OLS regression of  $Y-C_2T_{12}$  on X. Similarly, the upper bound  $\beta_t^u$  can be obtained from an OLS regression of  $Y-C_1T_{12}$  on X. Under standard conditions, the OLS estimators  $\hat{\beta}_t^l$  and  $\hat{\beta}_t^u$  are asymptotically normal and the asymptotic variances  $Avar(\hat{\beta}_t^l)$  and  $Avar(\hat{\beta}_t^u)$  can be estimated consistently. We can therefore apply the approach of Imbens & Manski (2004) and Stoye (2009) to construct confidence intervals for  $\beta_t$ :

$$CI_{1-\alpha} = \left[ \hat{\beta}_t^l - c_{IM} \cdot \sqrt{\frac{\widehat{Avar}(\hat{\beta}_t^l)}{N}}, \hat{\beta}_t^u + c_{IM} \cdot \sqrt{\frac{\widehat{Avar}(\hat{\beta}_t^u)}{N}} \right], \tag{22}$$

where the critical value  $c_{IM}^{\ \ \ \ \ }$  solves

$$\Phi\!\left(\!c_{IM}\!+\!\sqrt{N}\!\cdot\!\frac{\hat{\beta}_t^u\!-\!\hat{\beta}_t^l}{\sqrt{\max\!\left(\widehat{Avar}\!\left(\hat{\beta}_t^l\right)\!,\!\widehat{Avar}\!\left(\hat{\beta}_t^u\right)\right)}}\right)\!-\!\Phi(-c_{IM})\!=\!1\!-\!\alpha.$$

By Imbens & Manski (2004) and Stoye (2009),  $CI_{1-\alpha}$  is a valid confidence interval for  $\beta_t$ .

In the running example in the main text we imposed  $C_1=-0.1$  and  $C_2=0.1$ . Figure A.10 shows size and power of the IMS approach for  $C_1=0$  and  $C_2=0.1$  and for  $C_1=-0.1$  and  $C_2=0.1$ 

<span id="page-68-1"></span><sup>&</sup>lt;sup>7</sup>By construction,  $P(\hat{\beta}_t^u \ge \hat{\beta}_t^l) = 1$  so that Lemma 3 in Stoye (2009) ensures that the conditions in Imbens & Manski (2004) hold.

Figure A.10: Two sided and one-sided restrictions on  $\beta_{12}$  under IMS

<span id="page-69-1"></span>Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size for Figures 6a and 6b is  $\alpha$ =0.05. IMS refers to the Imbens & Manski (2004) and Stoye (2009) approach for constructing valid confidence intervals under prior knowledge about the magnitude of  $\beta_{12}$ . The dashed vertical lines are placed at  $\beta_{12}$ =-0.1 and  $\beta_{12}$ =0.1.

#### <span id="page-69-0"></span>A.5 Econometric details for the design-based solution

#### A.5.1 Power improvements

Consider a factorial design with an empty interaction cell as in Section 4.4 (see Table A.5) and the following population regression model

<span id="page-69-3"></span>
$$Y = \beta_0^* + \beta_1^* T_1 + \beta_2^* T_2 + \varepsilon^*. \tag{23}$$

Let  $\hat{\beta}_1^*$  and  $\hat{\beta}_2^*$  denote the OLS estimators of  $\beta_1^*$  and  $\beta_2^*$ . If  $T_1$  and  $T_2$  are randomly assigned,  $\hat{\beta}_1^*$  and  $\hat{\beta}_2^*$  are consistent for the respective main effects (see Appendix A.5.2).

To illustrate the power implications of leaving the interaction cell empty, consider an experiment where the researcher cares equally about power to detect an effect of  $T_1$  and  $T_2$ , and thus assigns the same sample size to both treatments:  $N_2^* = N_3^* = N_T^*$ . To illustrate, we focus on  $\beta_1^*$ . The variance

<span id="page-69-2"></span><sup>8</sup> Note in this case  $T_1$  and  $T_2$  are not independent of each other because of the negative correlation between the probability of being assigned to  $T_1$  and  $T_2$ .

<span id="page-70-0"></span>of  $\hat{\beta}_1^*$  is given by  $Var\left(\hat{\beta}_1^*\right) = \sigma^2 \frac{N - N_T^*}{(N - 2N_T^*)N_T^*}$ .  $Var\left(\hat{\beta}_1^*\right)$  is minimized when  $N_T^* = \frac{N}{2}\left(2 - \sqrt{2}\right)$  and we assume that the experiment is designed in this manner. A comparison to the variance of the estimator based on the long model,  $\hat{\beta}_1$ , shows that  $Var(\hat{\beta}_1^*) \leq Var(\hat{\beta}_1)^{10}$ . Thus, leaving the interaction cell empty yields power improvements for testing hypotheses about the main effects relative to long model t-tests.

Table A.5: Leaving the interaction cell empty

|       |     | $T_1$   |         |  |
|-------|-----|---------|---------|--|
|       |     | No      | Yes     |  |
| $T_2$ | No  | $N_1^*$ | $N_2^*$ |  |
|       | Yes | $N_3^*$ | 0       |  |

#### <span id="page-70-1"></span>Consistency of the OLS estimators based on model (23)

Here we show that when the interaction cell is empty and  $T_1$  and  $T_2$  are randomly assigned, the OLS estimators based on the regression model (23) are consistent for the main effects.

Define  $\hat{\beta}^* = (\hat{\beta}_0^*, \hat{\beta}_1^*, \hat{\beta}_2^*)'$  and  $\beta^* = (\beta_0^*, \beta_1^*, \beta_2^*)' = E(XX')^{-1}E(XY)$ , where  $X = (1, T_1, T_2)'$ Under standard conditions,  $\hat{\beta}^* \xrightarrow{p} \beta^*$ . Hence, it remains to show that  $\beta_1^*$  and  $\beta_2^*$  are equal to the main effects. In what follows, we focus on  $\beta_1^*$ . The derivation for  $\beta_2^*$  is similar. To simplify the exposition, we define  $p_1 = P(T_1 = 1)$ ,  $p_2 = P(T_2 = 1)$ , and  $p_{12} = P(T_1 = 1, T_2 = 1)$ .

Multiplying out yields the following expressions for 
$$\beta_1^*$$
: 
$$\beta_1^* = \frac{(p_2p_{12} - p_1p_2)E(Y) + p_1(p_2 - p_2^2)E(Y\,|\,T_1 = 1) + p_2(p_1p_2 - p_{12})E(Y\,|\,T_2 = 1)}{-p_1^2p_2 - p_1p_2^2 + p_1p_2 + 2p_1p_2p_{12} - p_{12}^2}.$$

Using the fact that the interaction cell is empty, which implies that  $p_{12}\!=\!0$ , obtain

<span id="page-70-4"></span>
$$\beta_1^* = \frac{-p_1 p_2 E(Y) + p_1 p_2 (1 - p_2) E(Y \mid T_1 = 1) + p_1 p_2^2 E(Y \mid T_2 = 1)}{-p_1^2 p_2 - p_1 p_2^2 + p_1 p_2}.$$
 (24)

Because  $p_{12} = 0$ , we have that

<span id="page-70-5"></span><span id="page-70-2"></span>
$$E(Y) = E(Y \mid T_1 = 1, T_2 = 0)p_1 + E(Y \mid T_1 = 0, T_2 = 0)(1 - p_1 - p_2) + E(Y \mid T_1 = 0, T_2 = 1)p_2.$$
 (25)

<span id="page-70-3"></span><sup>10</sup>For this comparison, we assume that both experiments are designed such that they exhibit equal power to detect an effect of  $T_1$  and  $T_2$ .

<sup>&</sup>lt;sup>9</sup>This exact sample split is impossible in any application since  $\frac{N}{2}(2-\sqrt{2})$  is not an integer. In our simulations we therefore use  $N_T^* = 0.29N$  and  $N_1^* = 0.42N$ .

Combining (24) and (25) and simplifying yields:

$$\beta_1^* = E(Y | T_1 = 1, T_2 = 0) - E(Y | T_1 = 0, T_2 = 0)$$

<span id="page-71-0"></span>The result now follows by random assignment of  $T_1$  and  $T_2$  and the definition of potential outcomes.

#### A.6 Bonferroni-correction with consistent model selection

In Section 4.2, we discussed a nearly optimal test that yields power improvements over the long model t-test near a priori likely values of the interaction. Here we discuss an alternative to the nearly optimal test: the Bonferroni approach of McCloskey (2017, 2020).

To achieve size control in the presence of model selection, one could employ tests based on the largest critical value across all possible values of the interaction effect  $\beta_{12}$ . However, this so-called least favorable approach is known to be very conservative due to its worst case nature. McCloskey (2017, 2020) suggests a procedure that improves upon the least favorable approach and asymptotically controls size. The basic insight of this approach is that one can construct an asymptotically valid confidence interval for  $\beta_{12}$ . As a consequence, one can search for the largest critical value over the values of  $\beta_{12}$  in the confidence interval rather than over the entire real line as in the least favorable approach. The uncertainty about the nuisance parameter ( $\beta_{12}$ ) and the test statistic can be accounted for using a Bonferroni-correction.

McCloskey (2017, 2020) considers both conservative and consistent model selection. Under conservative model selection, one uses a fixed threshold to select the model irrespective of the sample size. An example is the model selection algorithm in Section 2.5 where one employs a 5% t-test in the first step, irrespective of the sample size. Under consistent model selection, the model selection threshold is allowed to grow with the sample size. We explored both approaches and found that consistent model selection leads to more powerful tests in our context. We therefore only report results for consistent model selection. Specifically, we implement the adjusted Bonferroni critical values outlined in Section 3.2 of McCloskey (2017) and in Section 5 of McCloskey (2020).  $^{11}$ 

<span id="page-71-1"></span><sup>&</sup>lt;sup>11</sup>Specifically, we use the algorithm "Bonf-Adj Post-Sel" outlined in both papers. We employ consistent model selection using the BIC criteria. We use  $\beta = 0.5$  which results in  $\bar{a} = 0.45$ , as suggested by McCloskey (2017). To speed our simulations, we use the true OLS standard errors (as opposed to the estimated ones).

<span id="page-72-0"></span>Figure A.11: [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s consistent model selection exhibits small size distortions and yields power gains over running the full model for positive values of *β*<sup>12</sup>

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size for Figures [5a](#page-38-0) and [5b](#page-38-0) is α* = 0*.*05*. Consistent MS refers to [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s consistent model selection.*

Figure [A.11](#page-72-0) reports the results of applying [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s Bonferroni-style correction to our running example. It shows that consistent model selection with state-of-the-art Bonferroni adjustments leads to local power improvements relative to the long model for a short range of positive values of the interaction effect *β*12. However, unlike the nearly optimal test discussed in Section [4.2,](#page-19-0) researchers cannot choose where those power gains occur.

As expected, these power improvements come at the cost of much lower power for other values of *β*12. While the Bonferroni-correction asymptotically controls size for all values of the interaction, we find some small size distortions in our simulations. Appendix [A.7.7](#page-80-0) provides a more comprehensive assessment of the performance by plotting power curves for different values of *β*1.

#### <span id="page-73-0"></span>**A.7 Additional figures and tables**

Table A.6: Articles published in top-5 journals between 2007 and 2017

|                  | AER  | ECMA | JPE | QJE | ReStud | Total |
|------------------|------|------|-----|-----|--------|-------|
| Other            | 1218 | 678  | 367 | 445 | 563    | 3271  |
|                  |      |      |     |     |        |       |
| Field experiment | 43   | 9    | 14  | 45  | 13     | 124   |
|                  |      |      |     |     |        |       |
| Lab experiment   | 61   | 16   | 5   | 10  | 18     | 110   |
|                  |      |      |     |     |        |       |
| Total            | 1322 | 703  | 386 | 500 | 594    | 3505  |
|                  |      |      |     |     |        |       |

#### **A.7.1 Ignoring the interaction**

Figure A.12: Long and short model: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for the short model.*

#### <span id="page-75-0"></span>**A.7.2 Model selection (pre-testing)**

Figure A.13: Long model and model selection: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for model selection.*

#### <span id="page-76-0"></span>**A.7.3 [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test**

Figure A.14: Long model and [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for [Elliott et al.](#page-29-4) [\(2015a\)](#page-29-4)'s nearly optimal test.*

#### <span id="page-77-0"></span>**A.7.4 Restrictions on the magnitude of** *β*12**: [Armstrong et al.](#page-27-1) [\(2020\)](#page-27-1)**

Figure A.15: Long model and [Armstrong et al.](#page-27-1) [\(2020\)](#page-27-1)'s approach: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for [Armstrong et al.](#page-27-1) [\(2020\)](#page-27-1)'s approach based on restrictions on the magnitude of β*12*.*

# <span id="page-78-0"></span>**A.7.5 Restrictions on the magnitude of** *β*12**: [Imbens & Manski](#page-30-3) [\(2004\)](#page-30-3) and [Stoye](#page-32-9) [\(2009\)](#page-32-9)**

Figure A.16: Long model and [Imbens & Manski](#page-30-3) [\(2004\)](#page-30-3) and [Stoye](#page-32-9) [\(2009\)](#page-32-9)'s approach: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for [Imbens & Manski](#page-30-3) [\(2004\)](#page-30-3) and [Stoye](#page-32-9) [\(2009\)](#page-32-9)'s approach based on restrictions on the magnitude of β*12*.*

#### **A.7.6 Leaving the interaction cell empty**

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α*=0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power a design with the same sample size but leaving the interaction cell empty.*

# <span id="page-80-0"></span>**A.7.7 [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s consistent model selection with Bonferroni-type correction**

Figure A.18: Long model and [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s consistent model selection with Bonferroni-type correction: Power curves

*Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions. The size across all figures is α* = 0*.*05*. In each figure, dashed lines show the power for the long model, while solid lines show power for [McCloskey](#page-32-3) [\(2017,](#page-32-3) [2020\)](#page-32-4)'s consistent model selection with Bonferroni-type correction.*

#### A.7.8 Comparison across methods

Figure A.19: No factorial design: Size and power

Note: Simulations are based on sample size N, normal iid errors, and 10,000 repetitions.  $N_T^*=0.29N$  and  $N_1^*=0.42N$ . The size across all figures is  $\alpha=0.05$ .
