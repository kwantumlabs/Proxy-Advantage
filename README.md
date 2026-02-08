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

## Motivation

Mnay debates about fairness and merit implicitly assume that social systems reward internal qualities directly. In practice, this assumption fails. Measuring latent traits is expensive, ambiguous, and error-prone, so evaluators substitute observable proxies:

- Popularity as a proxyfor artistic quality
- Height and masculinity as a proxy for leadership
- Credentials as a proxy for competence
- Engagement metrics as a proxy for audience value

Whether or not proxies are arbitrary, they are *cheaper* than ground-truth evaluation. The key question is not whether proxies exist, but how their presence reshapes incentives for agents attempting to succeed in the context. 

This project asks:

**How does the existence of observable proxies distort optimal investment in latent internal states?**

## Model

### Agents

Agents are instances of an Agent class parameterised by $$(P, c, \alpha, \beta)$$ where:

- $$P$$ (proxy value) denotes the proxy as it enters the evaluator's perception.
- $$c \gt 0$$ (investment cost) determines the convex cost of cultivating the internal trait.
- $$\alpha \gt 0$$ controls the weight placed on the proxy by evaluators.
- $$\beta \gt 0$$ controls the weight places on the latent trait by evaluators.

Agents choose a level of investment $$I \geq 0$$ into a latent internal trait to maximise expected utility given these parameters and the evaluative environment. Latent trait production exhibits deminishing returns:

$$T(I) = I^{\gamma}, \quad 0 \lt \gamma \lt 1.$$

$$\alpha$$ and $$\beta$$ are kept constant for each agent within a simulation to represent a shared evaluative context and the optimal investment is computed via numerical optimisation. 

Crucially, evaluative rewards depend on the *perceived* proxy value, which might align with its value in reality, but need not necessarily do so. I won't labour to make this point at every instance of mentioning the proxy however, because from the evaluator's point of view, there is no difference. Whether the proxy in reality is ontologically fixed (e.g. height), costly but attainable (e.g. credentials), or entirely signal-based (e.g. self-reported attributes) is immaterial for the incentive structure. 

### Evaluation

Evaluators assign value based on a noisy linear combination of the proxy and the latent trait:

$$x = \alpha P + \beta T(I) + \varepsilon$$

where $$\varepsilon \sim \mathcal{N}(0, \sigma^2)$$ is the evaluation noise.

Agent success is given by a sigmoid function:

$$S(x) = \frac{1}{1 + e^{-x}}$$

### Utility 

Agents maximise utility:

$$U(I) = S(x) - \frac{c}{2} I^2$$

## Results

The simulation reveals 3 distinct regimes:

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
  - May appear lazy, bitter, and unmotivated

Evaluation noise introduces dispersion around the investment curve that would be produced under perfect evaluators:
- Points below the curve correspond to "lucky" agents, because due to encountering a more lenient evaluator, they could afford to invest less for the same reward.
- Points above the curve correspond to "unlucky" agents, because due to encountering a more critical evaluator, they had to invest more to acquire the same reward.

**Proposition: 


