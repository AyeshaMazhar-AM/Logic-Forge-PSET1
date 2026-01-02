# def team_impact(contributions):
#     ln = len(contributions)
    
#     left = [1] * ln
#     right = [1] * ln
#     impact = [1] * ln

#     for i in range(1, ln):
#         left[i] = left[i - 1] * contributions[i - 1]
#     for i in range(ln - 2, -1, -1):
#         right[i] = right[i + 1] * contributions[i + 1]
#     for i in range(ln):
#         impact[i] = left[i] * right[i]
        
#     return impact

def team_impact(contributions):
    ln = len(contributions)

    impact = [1]*ln
    left_product = 1
    for i in range(ln):
        impact[i] = left_product           #add left_product in impact array
        left_product *= contributions[i]   #update left_product
    right_product = 1
    for i in range(ln-1, -1, -1):           #starts from end
        impact[i] *= right_product
        right_product *= contributions[i]
    return impact

print(team_impact([1, 2, 3, 4]))          #output: [24, 12, 8, 6]

