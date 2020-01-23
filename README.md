# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:23:45 2020

@author: naman
"""

# TOPSIS

A python package for implementation of multiple criteria decision making using TOPSIS method.

Topsis is a method of compensatory aggregation that compares a set of alternatives by identifying weights for
each criterion, normalising scores for each criterion and calculating the geometric distance between each
alternative and the ideal alternative, which is the best score in each criterion. An assumption of TOPSIS
is that the criteria are monotonically increasing or decreasing. Normalisation is usually required as the
parameters or criteria are often of incongruous dimensions in multi-criteria problems.Compensatory
methods such as TOPSIS allow trade-offs between criteria, where a poor result in one criterion can be
negated by a good result in another criterion. This provides a more realistic form of modelling than 
non-compensatory methods, which include or exclude alternative solutions based on hard cut-offs.