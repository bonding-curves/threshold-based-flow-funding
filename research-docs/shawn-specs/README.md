# The Anderson Mechanism: Implementation Spec (Common Pool Grade)
**Author:** Shawn Anderson | **Lead Dev Notes**

## 1. The State Object
- `b`: `np.array([6])`
- `P`: `float` (The Common Pool Reservoir)

## 2. The Atomic Update Map

### Phase 1: The Collection (Drainage)
Move all excess nutrients and external grants into the Pool.
```python
# External Inflow
P += Delta_F

# Node Exudation (ReLU)
overflow = np.maximum(0, b - t)
P += np.sum(overflow)
b = np.minimum(b, t)
```

### Phase 2: The Priority Fill (Rehydration)
Satisfy all sustainability floors ($m$) using the Pool.
```python
shortfall = np.maximum(0, m - b)
S = np.sum(shortfall)

if S > 0 and P > 0:
    fill_amount = min(P, S)
    b += (shortfall / S) * fill_amount
    P -= fill_amount
```

### Phase 3: The Directed Flow (Translocation)
Redistribute any remaining Pool nutrients based on Preference Matrix $A$.
```python
if P > 0:
    # Use A matrix to weigh the distribution
    # Simplified: b += A.T @ (P / n) 
    # Or specific allocation logic
    pass
```
