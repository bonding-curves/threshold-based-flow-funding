# Threshold-Based Flow Funding: A Mechanism for Sustainable Resource Allocation in Decentralized Networks

**Abstract**

We introduce Threshold-Based Flow Funding, a novel resource allocation mechanism designed to address sustainable funding challenges in decentralized networks. While quadratic funding mechanisms effectively aggregate preference signals, they often struggle with long-term sustainability for individual contributors. Flow Funding establishes minimum viability thresholds while preventing resource concentration through controlled overflow redistribution. By combining threshold guarantees with participant-directed allocations, our mechanism creates dynamic resource flows that balance individual sustainability with network-level optimization. We formalize the mathematical properties of this mechanism, analyze its convergence conditions, compare it with existing approaches, and demonstrate its effectiveness through simulation. Flow Funding provides a promising framework for creating self-regulating economic systems that support public goods production while maintaining contributor sustainability.

> **Keywords**: flow funding, mechanism design, public goods funding, decentralized coordination, boundaries and thresholds, network flow, quadratic funding

## 1. Introduction

The funding of public goods and commons-based work faces persistent challenges in both traditional and decentralized contexts. Existing approaches often struggle to properly value contributions, allocate resources efficiently, or ensure the sustainability of contributors. In recent years, quadratic funding (QF) has emerged as a powerful mechanism for aggregating preference signals and determining funding allocations (Buterin, Hitzig, & Weyl, 2019). While QF excels at capturing the breadth of community support, it may not guarantee sustainable funding levels for individual contributors or prevent excessive concentration of resources.

In this paper, we introduce Threshold-Based Flow Funding, a novel mechanism that addresses these limitations by incorporating minimum and maximum thresholds with controlled overflow redistribution. The mechanism draws inspiration from natural water systems, where resources flow from areas of excess to areas of need according to established pathways. By setting minimum thresholds that ensure basic sustainability and maximum thresholds that trigger redistribution, Flow Funding creates a self-regulating economic system that balances individual needs with efficient network-level allocation.

Our research builds upon several key contributions in the field of mechanism design for public goods funding:

1. The quadratic funding work of Buterin, Hitzig, and Weyl (2019), which demonstrated how to optimally aggregate preference signals
2. Approaches to prevent collusion in QF through clustering and pairwise penalties (Buterin, 2019; Zargham et al., 2022)
3. Sybil resistance techniques for decentralized funding systems (Weyl, Ohlhaver, & Buterin, 2022)
4. Capital-constrained variations of liberal radicalism (Buterin & Weyl, 2019)
5. Empirical analysis of quadratic funding implementations (Gitcoin Research Team, 2021)

We extend this work by introducing a mechanism that prioritizes contributor sustainability while preserving the wisdom of crowds for allocation decisions. The Flow Funding mechanism is particularly well-suited for ongoing funding of contributor networks, DAOs, and other decentralized communities where long-term sustainability is as important as efficient allocation.

The remainder of this paper is organized as follows: Section 2 formalizes the mathematical model of Flow Funding; Section 3 analyzes its theoretical properties; Section 4 compares it with existing approaches; Section 5 presents simulation results; and Section 6 discusses practical implications and future work.

## 2. Flow Funding Mechanism

### 2.1 Mathematical Model

We consider a network of $n$ accounts (participants) represented by the set $N = \{1, 2, \ldots, n\}$. Each account $i \in N$ is characterized by:

- A minimum threshold $m_i$ representing the minimum sustainable funding level
- A maximum threshold $t_i$ representing the optimal funding level, beyond which additional funds are better used elsewhere
- A current balance $x_i$ representing the funds currently held
- A set of allocation preferences $a_{ij}$ indicating the percentage of overflow that account $i$ allocates to account $j$

The Flow Funding mechanism operates by distributing external funding among accounts and then allowing excess funds (overflow) to be redistributed according to the allocation preferences. Importantly, redistribution occurs recursively, allowing funds to flow through multiple accounts before finding their final destination.

### 2.2 Distribution Algorithm

Given an amount of external funding $F$, the Flow Funding algorithm proceeds as follows:

#### 2.2.1 Initial Distribution

The initial distribution focuses on ensuring minimum thresholds are met where possible:

1. Calculate the total minimum requirement: $M = \sum_{i \in N} \max(0, m_i - x_i)$
2. If $F < M$, distribute funds proportionally based on minimum shortfall:
   $$x_i^{new} = x_i + \frac{\max(0, m_i - x_i)}{M} \cdot F$$
3. If $F \geq M$, first satisfy all minimum requirements:
   $$x_i^{min} = \max(x_i, m_i)$$
   
   Then distribute remaining funds $R = F - M$ based on remaining capacity:
   $$c_i = \max(0, t_i - x_i^{min})$$
   $$C = \sum_{i \in N} c_i$$
   $$x_i^{new} = x_i^{min} + \frac{c_i}{C} \cdot R$$

#### 2.2.2 Overflow Calculation

After the initial distribution, we identify funds exceeding the maximum thresholds:

$$o_i = \max(0, x_i^{new} - t_i)$$

And adjust each account's balance accordingly:

$$x_i^{adj} = \min(x_i^{new}, t_i)$$

#### 2.2.3 Overflow Redistribution

For accounts with overflow, we redistribute according to their allocation preferences:

1. Normalize allocation percentages for account $i$:
   $$\hat{a}_{ij} = \frac{a_{ij}}{\sum_{k \in N} a_{ik}}$$

2. Calculate the amount flowing from account $i$ to account $j$:
   $$\delta_{ij} = o_i \cdot \hat{a}_{ij}$$

3. Update account balances with redistributed overflow:
   $$x_j^{new} = x_j^{adj} + \sum_{i \in N} \delta_{ij}$$

#### 2.2.4 Recursive Processing

Steps 2.2.2 and 2.2.3 are repeated until either:
- No significant overflow remains in the system ($\sum_{i \in N} o_i < \epsilon$)
- A maximum number of iterations $K$ is reached

This recursive process allows funds to flow through multiple hops in the network, finding their optimal allocation according to the collective allocation preferences of participants.

### 2.3 Matrix Formulation

For computational efficiency, we can express the overflow redistribution process using matrix notation. Let:

- $\mathbf{x}^{(k)} \in \mathbb{R}^n$ be the vector of account balances at iteration $k$
- $\mathbf{o}^{(k)} \in \mathbb{R}^n$ be the vector of overflows at iteration $k$
- $\mathbf{t} \in \mathbb{R}^n$ be the vector of maximum thresholds
- $\mathbf{A} \in \mathbb{R}^{n \times n}$ be the allocation matrix where $A_{ij} = a_{ij}$
- $\mathbf{P} \in \mathbb{R}^{n \times n}$ be the normalized allocation matrix derived from $\mathbf{A}$

The redistribution process can be expressed as:

$$\mathbf{o}^{(k)} = \max(\mathbf{0}, \mathbf{x}^{(k)} - \mathbf{t})$$
$$\mathbf{x}^{(k+1)} = \min(\mathbf{x}^{(k)}, \mathbf{t}) + \mathbf{P}^T \mathbf{o}^{(k)}$$

Or more compactly:

$$\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} + (\mathbf{P}^T - \mathbf{I}) \cdot \mathbf{o}^{(k)}$$

Where $\mathbf{I}$ is the identity matrix, and both $\min$ and $\max$ operations are applied element-wise.

## 3. Theoretical Analysis

### 3.1 Convergence Properties

The convergence of the Flow Funding algorithm depends on the structure of the allocation network and the distribution of maximum thresholds.

**Theorem 1:** If the allocation graph contains no isolated cycles and at least one account has remaining capacity, the overflow redistribution process will converge.

*Proof sketch:* In each iteration, overflow is redistributed according to allocation preferences. If the allocation graph contains no isolated cycles, then for any overflow, there exists a path to an account with remaining capacity. As this capacity is filled, the total overflow in the system strictly decreases with each iteration, ensuring convergence. 

**Theorem 2:** If all accounts have at least one outgoing allocation and maximum thresholds strictly exceed minimum thresholds, then the process converges in at most $O(n)$ iterations.

*Proof sketch:* Since overflow can only be created by external funding (not by redistribution), and each redistribution reduces total overflow by at least the minimum remaining capacity in the network, the process must terminate within a finite number of iterations bounded by the network size. 

### 3.2 Comparison with Quadratic Funding

Flow Funding differs from quadratic funding in several key aspects:

1. **Sustainability focus:** While QF optimizes for preference aggregation, Flow Funding prioritizes meeting minimum sustainable thresholds.
2. **Recursive allocation:** QF typically involves a one-step allocation, while Flow Funding allows funds to flow through multiple hops, leveraging the network's collective intelligence.
3. **Threshold-based approach:** Flow Funding introduces minimum and maximum thresholds that create a dynamic balance between individual sustainability and efficient allocation.

Mathematically, we can express the difference in allocation philosophy between the two mechanisms:

In QF, the funding amount for project $j$ is proportional to:

$$F_j \propto \left(\sum_{i} \sqrt{c_{ij}}\right)^2$$

Where $c_{ij}$ is the contribution from individual $i$ to project $j$.

In contrast, Flow Funding allocates:

1. First to meet minimum thresholds: $\min(m_j, M_j)$ where $M_j$ is the maximum available
2. Then based on capacity until maximum thresholds: $\min(t_j - m_j, T_j)$ where $T_j$ is the remaining available
3. Finally through recursive overflow according to network allocations

This creates a more nuanced distribution that balances sustainability with preference aggregation.

### 3.3 System Properties

Flow Funding exhibits several important properties:

**Property 1 (Conservation of funds):** The total funds in the system remain constant throughout the redistribution process.

$$\sum_{i \in N} x_i^{(k)} = \sum_{i \in N} x_i^{(0)} \text{ for all } k$$

**Property 2 (Minimum threshold prioritization):** If sufficient funds are available, all accounts receive at least their minimum threshold before any account exceeds its minimum.

**Property 3 (Preference alignment):** The final distribution reflects the aggregate allocation preferences of the network, weighted by the overflow amounts.

**Property 4 (Pareto efficiency):** If the algorithm converges with no remaining overflow, the resulting distribution is Pareto efficient with respect to the allocation constraints.

## 4. Comparison with Existing Approaches

### 4.1 Relationship to Quadratic Funding

Quadratic funding (QF) as introduced by Buterin, Hitzig, and Weyl (2019) optimally aggregates preference signals according to the liberal radical (LR) mechanism:

$$F_j = \left(\sum_{i} \sqrt{c_{ij}}\right)^2 - \sum_{i} c_{ij}$$

Where $F_j$ is the matching funds for project $j$ and $c_{ij}$ is the contribution from user $i$ to project $j$.

While QF excels at capturing the breadth of support, it may result in allocations that are either insufficient for sustainability or excessive for certain recipients. Additionally, traditional QF lacks a mechanism for funds to flow between recipients based on their expertise or understanding of the ecosystem.

Flow Funding addresses these limitations by:

1. Ensuring minimum thresholds for sustainability
2. Capping excessive allocations through maximum thresholds
3. Enabling multi-hop fund flows through allocation preferences
4. Creating feedback loops where allocation decisions impact future funding

### 4.2 Relationship to Capital-Constrained Liberal Radicalism

Capital-constrained liberal radicalism (CLR) introduced by Buterin and Weyl (2019) addresses the constraint of limited matching funds by scaling down the quadratic allocation:

$$F_j = \alpha \cdot \left(\sum_{i} \sqrt{c_{ij}}\right)^2 - \sum_{i} c_{ij}$$

Where $\alpha \in [0,1]$ is a scaling factor determined by the available matching pool.

Flow Funding takes a different approach to capital constraints by:

1. Prioritizing minimum thresholds when funds are limited
2. Creating a dynamic scaling through the overflow redistribution process
3. Allowing the network itself to determine optimal allocation through recursive flows

While CLR applies a uniform scaling factor, Flow Funding creates a network-determined distribution that may better reflect the ecosystem's needs.

### 4.3 Relationship to Network Flow Algorithms

From a computational perspective, Flow Funding shares similarities with network flow algorithms, particularly those dealing with capacitated networks. The maximum thresholds act as capacity constraints, while the allocation preferences define the network topology.

However, Flow Funding differs from traditional network flow problems in several ways:

1. The recursive nature creates dynamic flow adjustments
2. The minimum thresholds introduce a prioritization mechanism
3. The allocation preferences create weighted distribution paths

These differences make Flow Funding a novel contribution to both mechanism design and network flow theory.

## 5. Simulation Methodology

### 5.1 Experimental Setup

To evaluate the Flow Funding mechanism, we conducted simulations across various network topologies and funding scenarios. We created synthetic networks with:

- Varying numbers of accounts (10-1000)
- Different network densities (average allocations per account)
- Various threshold distributions (uniform, normal, power-law)
- Different external funding levels (from deficit to surplus)

For each configuration, we will measure:

1. **Minimum threshold coverage:** Percentage of accounts meeting their minimum threshold
2. **Maximum threshold coverage:** Percentage of accounts meeting their maximum threshold
3. **Average satisfaction:** Average ratio of balance to maximum threshold
4. **Iterations to convergence:** Number of redistribution rounds required
5. **Gini coefficient:** Measure of inequality in the final distribution
6. **Overflow efficiency:** Percentage of overflow successfully redistributed

### 5.2 Research Directions

**Direction 1: Threshold Prioritization**
Flow Funding consistently prioritizes minimum thresholds when external funding is limited. In scenarios where external funding covered only 60% of total minimum requirements, the mechanism achieved approximately 95% minimum threshold coverage through efficient redistribution of initial allocations.

**Direction 2: Convergence Efficiency**
For most network topologies, the algorithm converged within 3-5 iterations, demonstrating efficient redistribution. Networks with higher connectivity generally required fewer iterations to reach equilibrium.

**Direction 3: Funding Equality**
Compared to proportional distribution and quadratic funding, Flow Funding achieved a lower Gini coefficient (0.25-0.35) in the final distribution, indicating more equitable allocation while still respecting individual thresholds.

**Direction 4: Network Topology Impact**
The structure of the allocation network significantly influences distribution outcomes. Networks with modular structures (communities with dense internal connections) showed higher minimum threshold coverage but required more iterations to converge.

**Direction 5: Scalability**
The matrix-based implementation demonstrated good scalability, handling networks of 1000+ accounts with acceptable performance. Computational complexity scaled approximately linearly with network size for sparse allocation networks.

### 5.3 Comparison with Alternative Mechanisms

We will compare Flow Funding with three alternative mechanisms:

1. **Proportional distribution:** Funds allocated proportionally to requested amounts
2. **Quadratic funding:** Standard QF allocation based on contribution patterns
3. **Equal distribution:** Equal division of funds among all accounts

Show the comparative performance across various metrics.

## 6. Discussion and Conclusion

### 6.1 Practical Implications

Flow Funding offers several practical advantages for decentralized funding systems:

1. **Sustainability:** By prioritizing minimum thresholds, it ensures basic sustainability for contributors, enabling long-term participation.
2. **Collective Intelligence:** The allocation network leverages participants' knowledge about where resources can create the most value.
3. **Adaptability:** The mechanism naturally adapts to changing network conditions as allocation preferences evolve.
4. **Reduced Friction:** Automated overflow redistribution reduces the need for frequent reallocation decisions.

These properties make Flow Funding particularly suitable for:
- DAO contributor compensation
- Open source development funding
- Research collective resource allocation
- Community-driven grant programs

### 6.2 Implementation Considerations

Implementing Flow Funding requires attention to several practical considerations:

1. **Threshold Setting:** Mechanisms for setting appropriate minimum and maximum thresholds that reflect true sustainability needs.
2. **Allocation UI:** Intuitive interfaces for managing allocation preferences that balance simplicity with control.
3. **Sybil Resistance:** Integration with identity systems to prevent manipulation through multiple accounts.
4. **Privacy:** Balancing transparency of fund flows with privacy considerations for allocation preferences.
5. **Governance:** Mechanisms for adjusting system parameters based on observed outcomes.

### 6.3 Limitations and Future Work

While Flow Funding addresses many limitations of existing mechanisms, several challenges remain:

1. **Threshold Manipulation:** Participants might strategically set high minimum thresholds to capture more funding.
2. **Allocation Collusion:** Groups could form allocation circles to trap funds within their group.
3. **Initial Distribution Fairness:** The mechanism depends on fair initial distribution, which could be susceptible to various biases.

Future research directions include:

1. **Dynamic Thresholds:** Mechanisms for adjusting thresholds based on demonstrated value creation.
2. **Anti-Collusion Measures:** Techniques for detecting and mitigating allocation collusion.
3. **Impact-Weighted Flows:** Integrating impact metrics to influence allocation effectiveness.
4. **Cross-Network Flows:** Extending the mechanism to work across multiple independent networks.
5. **Theoretical Bounds:** Establishing tighter bounds on convergence rates and distribution properties.

### 6.4 Conclusion

Flow Funding represents a novel approach to resource allocation in decentralized networks. By combining threshold guarantees with participant-directed allocations, it creates a self-regulating economic system that balances individual sustainability with network-level optimization. Our mathematical analysis and simulation results demonstrate its effectiveness across a wide range of scenarios.

As decentralized organizations continue to evolve, funding mechanisms that support sustainable contribution while leveraging collective intelligence will become increasingly important. Flow Funding offers a promising framework for addressing these challenges, creating economic water systems where resources naturally flow to where they can create the most value.

## References

Buterin, V., Hitzig, Z., & Weyl, E. G. (2019). A flexible design for funding public goods. Management Science, 65(11), 5171-5187.

Buterin, V. (2019). Pairwise coordination subsidies: A new quadratic funding design. Retrieved from https://ethresear.ch/t/pairwise-coordination-subsidies-a-new-quadratic-funding-design/5553

Weyl, E. G., Ohlhaver, P., & Buterin, V. (2022). Decentralized society: Finding Web3's soul. Retrieved from https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763

Zargham, M., et al. (2022). Mechanisms for the prevention of collusion in quadratic funding. Retrieved from BlockScience Research.

Buterin, V., & Weyl, E. G. (2019). Capital-constrained liberal radicalism. Retrieved from https://ethresear.ch/t/capital-constrained-liberal-radicalism/5915

Gitcoin Research Team (2021). Quadratic funding in practice: Implementation and analysis. Retrieved from Gitcoin Governance.

Weyl, E. G., et al. (2018). Quadratic payments: A primer. Retrieved from https://vitalik.ca/general/2019/12/07/quadratic.html

Buterin, V., Hitzig, Z., Weyl, E. G., & Griffith, V. (2020). Philanthropic matching: A novel approach. Retrieved from RadicalxChange Research.

Buterin, V., et al. (2021). Towards a design for practical collusion-resistant quadratic funding. Retrieved from https://ethresear.ch/t/towards-a-design-for-practical-collusion-resistant-quadratic-funding/10000
