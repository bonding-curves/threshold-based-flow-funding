# TBFF: Formal Generalized Dynamical Systems (GDS) Specification

## 1. The State Space ($X$)
$x(k) = \langle \mathbf{b}, \mathbf{m}, \mathbf{t}, \mathbf{A}, P \rangle$
- $P \in \mathbb{R}_{\ge 0}$: The **Common Pool** (Central Stock).

## 2. The State Update Map ($f$)
The update is mediated entirely by the Pool ($P$).

### PSUB 1: Collection
All exogenous inflow ($\Delta F$) and node exudates ($o_i$) are added to the Pool.
$$P' = P + \Delta F + \sum \max(0, b_i - t_i)$$
$$b_i' = \min(b_i, t_i)$$

### PSUB 2: Senior Distribution (Floors)
The Pool fills all shortfalls $s_i = \max(0, m_i - b_i')$.
$$b_i'' = b_i' + \min(P', \sum s_i) \cdot \frac{s_i}{\sum s_i}$$
$$P'' = P' - \min(P', \sum s_i)$$

### PSUB 3: Junior Distribution (Preferences)
If $P'' > 0$, the Pool translocates nutrients based on the Preference Matrix $\mathbf{A}$.
$$\mathbf{b}^+ = \mathbf{b}'' + \text{Translocate}(P'', \mathbf{A})$$
