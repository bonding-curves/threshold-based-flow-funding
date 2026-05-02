# TBFF Resource Ecology (The Common Pool Spec)

We are modeling this system as a **Mycelial Network** in a 6-node forest, where all nutrient exchanges are mediated by a **Common Mycelial Pool**.

## 1. The Ecological Setup
*   **The Baseline ($3k):** The minimum nutrient requirement for a node. The **Common Pool** prioritizes filling these baselines for all nodes.
*   **The Saturation Point ($8k):** When a node hits its cap, all additional nutrients flow directly into the **Common Pool**.
*   **Directed Symbiosis:** Nodes provide "preference signals" to the Pool, suggesting where their personal contribution should flow *after* all baselines are met.

## 2. Laws of the Grove (System Invariants)
1.  **Pool-First Priority:** All exogenous nutrients (grants) and endogenous exudates (overflow) enter the Common Pool first.
2.  **Seniority Waterfall:** The Pool MUST satisfy all **Baselines** in the grove before any node is allowed to accumulate nutrients toward its Saturation Point.
3.  **The Reserve Guard:** The Pool maintains a perpetual buffer to protect the grove during "drought" seasons.

## 3. Ecological Stress Testing
*   **The Dragon-Proof Test:** We proved that a single node with a massive ceiling cannot starve the rest, because the Common Pool captures their excess and redistributes it to the thirsty saplings.
