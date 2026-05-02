# TBFF: Mathematical Specification (Math Spec) v1.1

## 1. State Variables
- $P$: Common Pool Stock
- $b_i$: Node $i$ Nutrient Stock

## 2. The "Shared Tank" Algorithm

### 2.1 Drainage (Exudation)
For all $i$:
$$o_i = \max(0, b_i - t_i)$$
$$b_i \leftarrow b_i - o_i$$
$$P \leftarrow P + o_i + \Delta F$$

### 2.2 Rehydration (Priority Filling)
Total Shortfall $S = \sum \max(0, m_i - b_i)$.
Amount to distribute $D = \min(P, S)$.
$$b_i \leftarrow b_i + D \cdot \frac{\max(0, m_i - b_i)}{S}$$
$$P \leftarrow P - D$$

### 2.3 Growth (Preferential Flow)
Remaining Pool $R = P$.
If $R > 0$:
$$b_j \leftarrow b_j + R \cdot \text{Pref}_j(\mathbf{A})$$
$$P \leftarrow 0 \text{ (or retained buffer)}$$
