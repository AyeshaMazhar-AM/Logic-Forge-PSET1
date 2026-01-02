def team_impact(contributions):
    ln = len(contributions)
    
    left = [1] * ln
    right = [1] * ln
    impact = [1] * ln

    for i in range(1, ln):
        left[i] = left[i - 1] * contributions[i - 1]
    for i in range(ln - 2, -1, -1):
        right[i] = right[i + 1] * contributions[i + 1]
    for i in range(ln):
        impact[i] = left[i] * right[i]
        
    return impact

print(team_impact([3, 5, 6, 2]))

