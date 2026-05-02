# TBFF High-Fidelity Engineering Specification

This document provides advanced **Model-Based Systems Engineering (MBSE)** diagrams for the TBFF **Generalized Dynamical System (GDS)**.

## 1. GDS Functional Block Diagram
This separates the **Behavioral Policy** (Participant Choices) from the **Mechanism Logic** (The Protocol).

```mermaid
graph TD
    subgraph Environment [External Factors]
        Funding[Seed Funding / Compost]
        Shock[Market Shocks / Volatility]
    end

    subgraph Controller [Behavioral Policy g: X -> U]
        UserChoice[Participant i]
        MatrixA[Allocation Matrix A]
        ThresholdSet[Threshold Adjustment m_i, t_i]
    end

    subgraph Plant [Mechanism Logic f: X * U -> X]
        PriorityMap[1. Baseline Priority Map]
        StateUpdate[2. State Transition Map]
        ConvergenceCheck[3. Convergence Logic]
    end

    subgraph State_Space [System State X]
        Balances[Vector x: Current Balances]
        Pool[Scalar P: Community Pool]
    end

    %% Flow of Information
    Environment -->|Exogenous Input| Plant
    State_Space -->|Feedback| Controller
    Controller -->|Admissible Input u| Plant
    Plant -->|State Update x+| State_Space

    style State_Space fill:#fff9c4,stroke:#fbc02d,stroke-width:2px
    style Plant fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Controller fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
```

## 2. The Internal "Nutrient Waterfall" (Node Logic Gate)
Detailed internal processing for a single participant node $i$.

```mermaid
graph TD
    Inflow([Total Inflow: Peer + External]) --> Node_i{Node i State}
    
    Node_i -->|x < m_i| Survival[Survival Mode]
    Survival -->|Accumulate| FloorBalance[Fill to $3k]
    
    Node_i -->|m_i <= x < t_i| Growth[Growth Mode]
    Growth -->|Accumulate| CeilingBalance[Fill to $8k]
    
    Node_i -->|x > t_i| Saturation[Saturation Mode]
    Saturation -->|Exudate| PoolTax{First $500?}
    
    PoolTax -->|Yes| CommunityPool[(Community Pool)]
    PoolTax -->|No| Translocation[Forward Flow]
    
    Translocation -->|Matrix A| PeerNodes([Peer Node Inflows])

    style Survival fill:#ffebee,stroke:#c62828
    style Growth fill:#e3f2fd,stroke:#1976d2
    style Saturation fill:#e8f5e9,stroke:#2e7d32
```

## 3. Recursive Convergence State-Machine
The iterative process for the redistribution of overflow until equilibrium is reached.

```mermaid
stateDiagram-v2
    [*] --> Calculate_Overflow
    
    state "Iteration k" as Iter {
        Calculate_Overflow --> Identify_Exudate: o_i = max(0, x_i - t_i)
        Identify_Exudate --> Apply_Tax: o_i' = o_i - tax
        Apply_Tax --> Matrix_Multiplication: x_next = x_adj + A^T * o_i'
    }
    
    Matrix_Multiplication --> Check_Convergence
    
    Check_Convergence --> Calculate_Overflow: Σo_i > ε (Not Converged)
    Check_Convergence --> Check_Spectral_Radius: Σo_i < ε (Equilibrium)
    
    Check_Spectral_Radius --> [*]: ρ(A) < 1 (Stable)
    Check_Spectral_Radius --> Alarm: ρ(A) >= 1 (Loop Trap Detected)
    
    Alarm --> Discussion: Human Intervention Required
```

## 4. Matrix-Vector Transition Logic
The mathematical mapping of the state update $x^+ = f(x,u)$.

```mermaid
graph LR
    subgraph Input_Vector
        X[x_t: State Vector]
    end

    subgraph Operators
        direction TB
        M[m: Baseline Constraint]
        T[t: Saturation Constraint]
        A[A_T: Translocation Matrix]
    end

    subgraph Output_Vector
        XP[x_t+1: Posterior State]
    end

    X --> M
    M --> T
    T -- "Residual (x - t)" --> A
    T -- "Saturated" --> XP
    A --> XP

    style M fill:#f9f,stroke:#333
    style T fill:#bbf,stroke:#333
    style A fill:#dfd,stroke:#333
```
