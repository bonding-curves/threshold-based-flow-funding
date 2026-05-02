# Threshold-Based Flow Funding (TBFF) — Requirements & Protocol Document

> **Status:** Draft / Template
> **Last Updated:** May 2026
> **Based on:** Experiment Overview V1 (Feb 2026 Draft)

## 1. Experiment Overview & Objectives

**Threshold-based Flow Funding** is a framework arising from the MycoFi movement. The core mechanism involves each participant defining a **minimum floor** (required for meaningful work) and a **maximum ceiling** (beyond which funds automatically flow outward). The network self-distributes resources based on participants' forward flow allocations.

### 1.1 Core Research Question

*Does a network's collective allocation preference converge toward something coherent — or just reflect whoever set their thresholds highest?*

### 1.2 Objectives

- Test the viability of TBFF in a live environment.
- Observe whether overflow circulates to create genuine abundance or if participants simply spend up to their ceilings.
- Evaluate how popularity dynamics compare against functional needs (via a skills matrix) for membrane entry.
- Measure the half-life of seed capital under live conditions.

## 2. Experiment Parameters

### 2.1 Phase 1: Mini-Network Flows

- **Duration:** 3 Months
- **Scale:** 1 Network, 10 Participants
- **Growth:** No extending invitations (closed membrane), no other holon types (subnets)
- **Visibility:** TBD (Are flows fully visible?)
- **Funding:** Philanthropic seed funding (No financial returns promised)

### 2.2 Phase 2: Multi-Holon Expansion

- **Duration:** 3 Months
- **Scale:** 20-100 Participants (spanning 2-4 core communities/networks)
- **Holon Types:** Networks, Subnets, People
- **Funding Required:** $300K - $1M+ in philanthropic seed funding (~$3,000 min income for experiment duration for everyone)
- **Thresholds:** Shift from fixed values to recommended caps.

## 3. Protocol Rules

The protocol applies to all "holons" (people in Phase 1; sub-nets, networks, and experiments in Phase 2).

### 3.1 Structural Rules (Immutable for the duration of the experiment)

1. **Holons All the Way Down:** The same rules apply to every node in the network.
2. **Membrane Integrity:** Creation of a non-human holon must meet minimum viable membrane definition and stewardship requirements.
3. **Inflow Tracking:** Thresholds track total *inflow per month*, not current account balances (designed to be ungameable).
4. **Funding Guarantee:** Everyone's minimum is fully funded for 6 months before they join the network.
5. **Automatic Routing:** Your maximum is never exceeded — overflow routes outward automatically.
6. **Expansion Constraint:** The membrane only opens to new people when the pool can cover 6 months of their minimum.

### 3.2 Working Rules (Adjustable by consent at Network/Subnet levels)

- **Starting Minimum:** $3,000/month (Uniform for first 90 days)
- **Starting Maximum:** $8,000/month (Uniform for first 90 days)
- **Community Pool:** The first $500/month of overflow goes into the community pool before a participant directs the rest elsewhere.
- **Surplus Flow:** Any surplus above the community pool contribution can be flowed to anyone/anything, with no approval needed.
- **Threshold Adjustments:** Thresholds can change a maximum of once per quarter, requiring 30 days notice.
- **Safety Trigger:** If **30%+ of participants are below their minimum** in any given month, the membrane closes, and a community conversation must occur within 14 days.
- **Onboarding:** New members join based on a **skills/functions matrix** defined by the founding cohort in Month 0, mitigating popularity-based entry.

## 4. Participant Roster (Phase 1)

1. Shawn Anderson
2. Christina Bowen
3. Jeff Emmett
4. Jessica Zartler
5. Hash

*(Note: See Context Document for links and collaborator details)*

## 5. Implementation & Timeline

| Phase                            | Timeline    | Key Activities                                                                     |
| -------------------------------- | ----------- | ---------------------------------------------------------------------------------- |
| **0. Design & Onboarding** | Month 0     | Finalize rules, build skills matrix, confirm pool funding, set transparency tiers. |
| **1. Flow Begins**         | Month 1     | Participants set thresholds, overflow begins moving, story collection starts.      |
| **2. Active Experiment**   | Months 2–4 | Experiments are funded, network diagnostics are monitored, signals are logged.     |
| **3. Membrane Check**      | Month 3     | Pool health review, decide on queue, conduct first real retrospective.             |
| **4. Synthesis**           | Month 5     | Gather stories, analyze flow data, write up findings for funders.                  |
| **5. Wrap / Renew**        | Month 6     | Publish learnings, decide whether to extend, expand, or redesign the protocol.     |

## 6. System Design Constraints (V1)

- **Manual Operations:** No automated fund transfers — manual entry is deliberate.
- **No Reputation Tokens:** No reputation scores or rankings.
- **No Voting:** No governance voting workflow.
- **Observation Only:** No punishment or exit mechanisms; the primary goal is observation.

## 7. Open Questions & Action Items

**To be resolved prior to launch:**

1. **Roles:** Who owns network diagnostics (weekly, ~15 min) and who is the "story lead"?
2. **Community Pool Utilization:** What does the community do with pool funds beyond guaranteed minimums (e.g., hold as reserve)?
3. **Skills Matrix Definition:** What specific skills/functions does the network actually need?
4. **Mathematical Modeling:** Review with Ken: what does the pool math look like, and what does the 30% alarm threshold mean in actual numbers?
5. **Visibility Design:** Review with Nathan (Raft Foundation) regarding the risks and designs of full financial transparency. How much should participants share about spending?
6. **Gaming Mitigation:** What happens if someone never contributes overflow or games their threshold?
7. **UI/UX:** What must the flow visualization show to be genuinely useful versus just visually impressive?
8. **Baseline Definition:** What constitutes the baseline for tracking signals and stories?
