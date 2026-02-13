#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:55:41 2026

@author: ntsikamajozi
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

class Agent:
    
    def __init__(self, proxy, cost, alpha = 1.0, beta = 2.0):
        
        self.P = proxy
        self.c = cost
        self.alpha = alpha
        self.beta = beta
        
    def trait(self, I, gamma = 0.5):
        """internal trait cultivation has diminishing returns"""
        return I**gamma 
    
    def sigmoid(self, x):
        
        return 1/(1+np.exp(-x))
    
    def utility(self, I, eps = 0, phi = -2.0, gamma = 0.5):
        """U(I) = S(P,T) - (c/2) * I^2"""
        
        T = self.trait(I, gamma)
        perceived_value = (self.alpha * self.P) + (self.beta * T) + eps - phi
        S = self.sigmoid(perceived_value)
        
        cost = (self.c/2) * (I ** 2)
        
        return S - cost
    
    def best_response(self, eps = 0, phi = -2.0, gamma = 0.5):
        """finds the I* that maximises the utility"""
        
        def objective(I):
            
            return -self.utility(I, eps = eps, phi = phi, gamma = gamma)
        
        res = minimize_scalar(objective, bounds = (0, 20), method = 'bounded')
        
        if not res.success:
            raise RuntimeError("Optimisation failed")
        
        return res.x
    
def run_simulation(proxy_range, noise_variation, alpha = 1.0, beta = 2.0, c = 0.1, gamma = 0.5, phi = 0):
    
    results_i = []
    
    for p in proxy_range:
        
        eps = np.random.normal(0, np.sqrt(noise_variation))
        agent = Agent(proxy = p, cost = c, alpha = alpha, beta = beta)
        
        I_star = agent.best_response(eps = eps, phi = phi, gamma = gamma)
        
        results_i.append(I_star)
        
    return results_i
        
if __name__ == '__main__':
    
    proxies = np.linspace(-6,6,300)
    
    i_vals = run_simulation(proxies, noise_variation = 0.1)
    plt.scatter(proxies, i_vals, s = 7, alpha = 0.6, label = 'Agents (With Noise)')
    
    i_vals_perf = run_simulation(proxies, noise_variation = 0.0)
    plt.plot(proxies, i_vals_perf, color = 'red', linewidth = 1.4, label = 'Expected Effort (No Noise)')
    
    plt.grid(alpha = 0.25)
    plt.title('Optimal Investment ($I^*$) vs. Proxy Value ($P$)', fontsize = 12)
    plt.xlabel('Proxy Value(P)')
    plt.ylabel('Optimal Investment In Trait ($I^*$)')
    plt.legend()
    plt.show()
        
        
        
        
        
        
        