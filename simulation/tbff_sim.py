import numpy as np
import pandas as pd

class TBFFSimulator:
    def __init__(self, n_participants=6, seed=42, attack_mode=False):
        np.random.seed(seed)
        self.n = n_participants
        
        # 1. State Space (X)
        self.balances = np.zeros(self.n)
        self.min_thresholds = np.full(self.n, 3000)
        self.max_thresholds = np.full(self.n, 8000)
        
        if attack_mode:
            # Participant 0 is the Maximalist Attacker
            self.max_thresholds[0] = 50000 # Massive ceiling to trap all inflow
            # Attacker only flows to one friend (P1), trapping the rest
            self.A = np.random.rand(self.n, self.n)
            self.A[0, :] = 0
            self.A[0, 1] = 1.0 
        else:
            self.A = np.random.rand(self.n, self.n)
            
        np.fill_diagonal(self.A, 0)
        self.A = self.A / self.A.sum(axis=1)[:, None]
        
        self.community_pool = 0
        self.history = []

    def step(self, external_funding, floor_priority=True):
        """Perform one monthly transition (f)"""
        
        if floor_priority:
            # Step 1: Priority 1: Fill all Min Thresholds (Senior Tranche)
            shortfalls = np.maximum(0, self.min_thresholds - self.balances)
            total_shortfall = shortfalls.sum()
            
            if external_funding <= total_shortfall:
                self.balances += (shortfalls / total_shortfall) * external_funding
                inflow_remaining = 0
            else:
                self.balances += shortfalls
                inflow_remaining = external_funding - total_shortfall
                
                # Priority 2: Fill toward Max Thresholds (Junior Tranche)
                capacity = np.maximum(0, self.max_thresholds - self.balances)
                total_capacity = capacity.sum()
                if total_capacity > 0:
                    share = min(inflow_remaining, total_capacity)
                    self.balances += (capacity / total_capacity) * share
                    inflow_remaining -= share
                
                self.community_pool += inflow_remaining
        else:
            # NO FLOOR PRIORITY: Inflow is distributed by 'Influence' (A matrix)
            # This simulates a popularity-based distribution where floors aren't guaranteed
            self.balances += self.A.T @ np.full(self.n, external_funding / self.n)

        # Step 2: Recursive Flow
        iterations = 0
        while iterations < 10:
            overflow = np.maximum(0, self.balances - self.max_thresholds)
            if overflow.sum() < 1.0: break
            
            self.balances = np.minimum(self.balances, self.max_thresholds)
            # Pool Tax
            tax = np.minimum(overflow, 500)
            self.community_pool += tax.sum()
            
            # Flow
            self.balances += self.A.T @ (overflow - tax)
            iterations += 1
            
        self.history.append({
            'balances': self.balances.copy(),
            'pool': self.community_pool,
            'under_min': (self.balances < self.min_thresholds).sum(),
            'attacker_balance': self.balances[0]
        })

    def run(self, months=6, funding_per_month=20000, floor_priority=True):
        for _ in range(months):
            # Simulation of external variance
            monthly_funding = np.random.normal(funding_per_month, funding_per_month * 0.2)
            self.step(max(0, monthly_funding), floor_priority=floor_priority)
            
        return pd.DataFrame(self.history)

if __name__ == "__main__":
    months = 12
    funding = 18000 # Exactly enough for $3k floors
    
    print(f"--- Scenario 1: Floor Priority (Senior Tranche Guaranteed) ($ {funding}/mo) ---")
    sim_prio = TBFFSimulator(attack_mode=True)
    res_prio = sim_prio.run(months=months, funding_per_month=funding, floor_priority=True)
    print(res_prio[['pool', 'under_min', 'attacker_balance']])
    
    print(f"\n--- Scenario 2: Influence-Based (No Floor Priority) ($ {funding}/mo) ---")
    print("Participants receive funds based on influence, then flow residuals.")
    sim_inf = TBFFSimulator(attack_mode=True)
    res_inf = sim_inf.run(months=months, funding_per_month=funding, floor_priority=False)
    print(res_inf[['pool', 'under_min', 'attacker_balance']])
    
    trigger = (res_inf['under_min'] >= 2).sum()
    print(f"\n30% Trigger Alarm count (No Floor Prio): {trigger} / {months} months")
    
    print("\nSummary: Without a contract-enforced 'Floor Priority' (Senior Tranche),")
    print("the Maximalist (P0) successfully traps liquidity, leaving others in scarcity.")
