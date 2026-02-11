# Proxy Advantage and Effort Allocation

<p align="center">
  <em>
    “When a measure becomes a target, it ceases to be a good measure.”  
    <br>
    — Charles Goodhart, 1975
  </em>
</p>

## Overview

In many social, institutional, and creative domains, evaluators normatively prefer welfare-improving latent internal traits (e.g. competence, leadership ability, artisitic quality, creativity, romantic care), but face high costs or uncertainty in measuring them directly. As a result, they rely on observable proxies (e.g. popularity metrics, demographic markers, status signals, appearance) that are typically causally irrelevant for the internal trait of interest. 

This repository aims to formalise a consequential incentive distortion that arises under proxy-based evaluation. Agents with high proxy values optimally invest less in the internal trait, as they already receive much of the social reward associated with possessing it. Agents with moderately negative proxy values invest more, compensating for persistent evaluative disadvantage as they reside within a regime where effort still yields marginal returns. Agents with extremely low proxy values rationally disengage, viewing success as unattainable regardless of effort. 

This agent-based model demonstrates how proxy reliance produces stratified effort allocation, endogenous inequality, and systematic misinterpretation of motivation, talent, and merit, even when evaluators genuinely value the underlying internal trait. 

## 1. Motivation

Many debates about fairness and merit implicitly assume that social systems reward internal qualities directly. In practice, this assumption fails. Measuring latent traits is expensive, ambiguous, and error-prone, so evaluators substitute observable proxies:

- Popularity as a proxy for artistic quality
- Height and masculinity as a proxy for leadership
- Credentials as a proxy for competence
- Engagement metrics as a proxy for audience value

Proxies may not necessarily be arbitrary, but they are *cheaper* than ground-truth evaluation. The key question is not whether proxies exist, but how their presence reshapes incentives for agents attempting to succeed in the context. 

This project asks:

**How does reliance on observable proxies distort optimal investment in latent internal states?**

## 2. Model

### 2.1 Agents

Agents are instances of an Agent class parameterised by $$(P, c, \alpha, \beta)$$ where:

- $$P$$ (proxy value) denotes the proxy as it enters the evaluator's perception.
- $$c \gt 0$$ (investment cost) determines the convex cost of cultivating the internal trait.
- $$\alpha \gt 0$$ controls the weight placed on the proxy by evaluators.
- $$\beta \gt 0$$ controls the weight places on the latent trait by evaluators.

Agents choose a level of investment $$I \geq 0$$ into a latent internal trait to maximise expected utility given these parameters. Latent trait production exhibits deminishing returns:

$$T(I) = I^{\gamma}, \quad 0 \lt \gamma \lt 1.$$

$$\alpha$$ and $$\beta$$ are kept constant for each agent within a simulation to represent a shared evaluative context. 

Crucially, evaluative rewards depend on the *perceived* proxy value, which might align with its value in reality, but need not necessarily do so. I won't labour to make this point at every instance of mentioning the proxy however, because from the evaluator's point of view, at the time of evaluation, there might as well be no difference. Whether the proxy in reality is ontologically fixed (e.g. height), costly but attainable (e.g. credentials), or entirely signal-based (e.g. self-reported attributes) is immaterial for the incentive structure. 

### 2.2 Evaluation

Evaluators perceive agents through a noisy linear combination of the proxy value $$P$$ and the trait value $$T$$:

$$x = \alpha P + \beta T(I) + \varepsilon$$

where $$\varepsilon \sim \mathcal{N}(0, \sigma^2)$$ represents the evaluation noise. 

Two scenarios are considered:

- Perfect evaluation ($$\sigma^2 = 0$$)
- Noisy evaluation ($$\sigma^2 \gt 0$$)

The perceived social reward is given by a sigmoid function:

$$S(x) = \frac{1}{1 + e^{-x}}$$

This captures saturation effects: beyond a point, additional perceived value yields diminishing social returns.

### 2.3 Cost of Investment

Investment is costly and convex:

$$C(I) = \frac{c}{2}I^2$$

### 2.4 Utility 

Agents maximise utility:

$$U(I) = S(x) - C(I).$$

### 2.5 Agent Optimisation

Agents solve:

$$I^* = \arg \max_{I \geq 0} U(I)$$

via numerical optimisation.

## 3. Results

### 3.1 Simulation Output

The simulation produces:

- A red curve representing the optimal investment $$I^* (P)$$ under perfect evaluation.
- A noisy scatter of realised optimal investments under noisy evaluation. 

3 distinct regimes are revealed:

1. **High proxy agents**

      - Receive high perceived value, even at low investment
      - Rationally invest less
      - May appear "effortlessly talented" or "naturally gifted"

2. **Moderately negative proxy agents**

      - Face steep marginal returns on effort
      - Invest more relative to peers
      - May appear obsessive, hyper-motivated, or anxious

3. **Low proxy agents**

      - Face near-zero marginal returns on effort
      - Rationally disengage
      - May appear lazy, bitter, or unmotivated

Evaluation noise introduces dispersion around the optimal response, producing "lucky" agents (those below the optimal curve) and "unlucky" agents (those above the optimal curve), but does not eliminate the underlying incentive structure. The resulting shape highlights a systematic motivational gradient induced purely by proxy reliance; not differences in preferences, discipline, or intrinsic motivation.

### 3.2 Key Result: Proxy Advantage Suppresses Optimal Output

**Proposition: 

## 4. Proxy-Gaming as a Diagnostic Symptom of Evaluative Failure

A common reaction in proxy-based systems is moral outrage at *proxy-gaming*: exaggeration, misrepresentation, or outright deception aimed at inflating the guilty agent's proxy values. This project takes a different view.

**Wide-spread proxy-gaming is not a failure of individual ethics; it is a diagnostic symptom of misaligned evaluation**

When rewards are allocated based on observable proxies rather than latent traits, rational agents will attempt to manipulate proxies directly (especially when doing so is cheaper than cultivating the actual underlying trait).

### 4.1 Height Inflation on Dating Apps

A familiar example arises in heterosexual dating apps, where women frequently report that men lie about their height. This criticism is usually framed as a character flaw or moral failing. However, within the present framework, height inflation is an entirely predictable response to the incentive structure:

- Height functions as a proxy for romantic competence, attractiveness, or dominance.
- Directly signalling romantic competence is costly, noisy, and often impossible within the platform constraints.
- Increasing reported height is cheap, immediate, and disproportionately rewarded.

Inevitably, the asymmetry exposes the entire game: **almost no man revises their height downwards**. This directional manipulation reveals where the reward gradient lies. 

If romantic competence were directly observable and reliably rewarded, height misrepresentation would have no utility. Agents would instead invest in, and signal, romantic competence itself. And in a hypothetical world where such competence could be measured accurately, the only stable way to signal it would be to actually possess it. 

Thus deception here is not an aberration; it is evidence that the proxy has partially displaced the trait. 

### 4.2 Proxy-Gaming as Evidence of Measurement Failure

From this perspective, widespread proxy manipulation indicates:
- That evaluators care about some latent quality,
- That proxies are causally irrelevant for the internal trait,
- And that the cost structure favours proxy manipulation over genuine cultivation.

Proxy-gaming therefore should function as a *revealed preference* of the context itself. The more aggressively a proxy is gamed, the less confidence we should have that it tracks the underlying trait it was intended to measure. 

This logic applies equally to:

- Inflated engagement metrics in creative platforms,
- Credential inflation in labour markets,
- Strategic branding detached from substance,
- And performative signals of virtue or competence.

The problem is not that agents game proxies. The problem is that the context made proxy-gaming optimal. In other words, **when a proxy becomes a trait, it ceases to be a good proxy**. 

## 5. Implications

This framework challenges several common assumptions:
- That higher-status individuals necessarily exert more effort
- That observed success reflects superior intrinsic motivation
- That low participation implies low valuation of success

Instead, effort is shown to be endogenously shaped by evaluative structure. 

We can reasonably expect proxy-based incentive distortions to arise endogenously whenever the following conditions hold:

1. **Evaluators value some latent internal trait and aim to reward it**

   These traits could be normatively preferred and welfare-maximising, but they need not necessarily be in order for the distortion to emerge within the context.

3. **Direct measurement is costly, ambiguous, and/or error-prone**

   The trait is difficult to observe reliably, slow to evaluate, or requires contextual or expert judgement.
  
5. **Evaluators substitute a causally irrelevant observable proxy**

   Because direct measurement is impractical, evaluators rely on a proxy that is cheaper, more legible, or more scalable. Crucially, how well the proxy correlates with the trait in equilibrium is immaterial. All that need occur is for the proxy and trait to be causally disjoint.

7. **Agents rationally optimise effort against utility**

   Agents respond strategically to the reward structure, allocating effort to maximise expected utility. 

## 6. Application: Music, Art, and Algorithmic Platforms

### 6.1 Proxies in Artistic Systems

On music and art platforms, evaluators rely heavily on proxies:
- Stream counts
- Follower numbers
- Engagement rates
- Playlist placement
- Visual aesthetics
- Demographic priors

These proxies are used because directly evaluating artistic quality is slow, subjective, and expensive. 

### 6.2 Incentive Distortions

The model predicts several well-documented phenomena:
- Artists with early algorithmic traction can afford to experiment less or stagnate artistically.
- Artists with moderate traction are incentivised to over-optimise, over-produce, or stylistically contort themselves to compensate.
- Artists with minimal initial traction rationally disengage or self-censor, interpreting lack of reward as futility.

Crucially, these outcomes arise even if platforms genuinely care about artistic quality. 







