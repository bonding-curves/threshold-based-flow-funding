# TBFF Visual Ecosystem

This document provides visual maps of the **Mycelial Pulse** mechanism using Causal Loop Diagrams (CLD) and Stock & Flow representations.

## 1. Causal Loop Diagram: The Nutrient Pulse
This diagram shows how the system balances itself. We want to avoid "Overgrowth" (Hoarding) and encourage "Symbiosis" (Sharing).

```mermaid
graph TD
    %% Balancing Loop: Sustainability
    Baseline[Nutrient Baseline $3k] -->|Triggers| Inflow[External Inflow/Compost]
    Inflow -->|Increases| NodeBalance[Node Nutrient Level]
    NodeBalance -->|Reduces| Shortfall[Shortfall]
    Shortfall -->|Needs| Inflow
    
    %% Reinforcing Loop: Ecosystem Health
    NodeBalance -->|Exceeds| Saturation[Saturation Point $8k]
    Saturation -->|Creates| Exudate[Exudate/Overflow]
    Exudate -->|Feeds| SporeReserve[Spore Reserve/Pool]
    Exudate -->|Translocates| OtherNodes[Symbiotic Partners]
    OtherNodes -->|Strengthens| EcosystemHealth[Grove Resilience]
    EcosystemHealth -->|Attracts| MoreFunding[Future Seed Funding]
    MoreFunding --> Inflow

    %% Constraint: The Shadow
    HighSaturation[Abnormal Saturation $50k] -->|Shades Out| OtherNodes
    style HighSaturation fill:#f96,stroke:#333
    style SporeReserve fill:#bbf,stroke:#333
```

## 2. Stock & Flow: Nutrient Translocation
This is the "Plumbing" (Ecological Version). It shows how the nutrients actually move through a single node.

```mermaid
graph LR
    Compost((External Compost)) -->|Inflow| NodeStock[Node Balance]
    NodeStock -->|Baseline Satisfied| SaturationGate{Saturation?}
    
    SaturationGate -->|Below $8k| Growth[Internal Growth]
    SaturationGate -->|Above $8k| Exudation[Exudation/Overflow]
    
    Exudation -->|Tax| SporeReserve[(Spore Reserve)]
    Exudation -->|Flow| MycelialNetwork[Forward Flow to Partners]
    
    MycelialNetwork -->|Inflow| PartnerNode[Partner Node]
    
    style NodeStock fill:#dfd,stroke:#080
    style SporeReserve fill:#dff,stroke:#008
```

## 3. The 6-Node Grove (The Network)
This shows the 6-person cohort with the **Baseline Priority** rule active.

```mermaid
graph TD
    ExternalSource[Seed Funding / Compost]
    
    subgraph Grove [The 6-Node Mycelium]
        Node1((Node A))
        Node2((Node B))
        Node3((Node C))
        Node4((Node D))
        Node5((Node E))
        Node6((Node F))
    end
    
    ExternalSource -->|1. Fill Baselines| Grove
    
    Node1 -.->|2. Translocate| Node2
    Node2 -.->|2. Translocate| Node3
    Node3 -.->|2. Translocate| Node6
    Node6 -.->|2. Translocate| Node1
    
    Grove -->|3. Spore Tax| Pool[(Community Mycelium)]
    
    style Grove fill:#f5f5f5,stroke:#333,stroke-dasharray: 5 5
    style Pool fill:#e1f5fe,stroke:#01579b
```

## 4. Stability Check: The Loop Trap
We monitor the network for "closed circuits" that don't let nutrients reach the edges.

```mermaid
graph LR
    A((Node A)) -->|Exudate| B((Node B))
    B -->|Exudate| A
    
    subgraph Feedback [The Loop Trap]
        A
        B
    end
    
    C((Node C)) ---|Isolated| Feedback
    
    note[System Flag: Spectral Radius Check]
    
    style Feedback fill:#ffebee,stroke:#c62828
```
