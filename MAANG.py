#amazon
# QUESTION 1
# Given:
# Tenant count for a list of buildings
# Array of range for each router
# Array of location of each router
# If a router location is i and it's range is k then it will serve buildings at indices i-k to i+k inclusive.
# A building is considered as served if the number of routers serving that building is greater than or equal to head count of that building.
# Test case:
# tenantCount: [2, 3, 3, 1, 5,6]
# routerLocation: [2,4,1]
# routerRange: [2,4,3]
# Number of routers serving each building would be [2,2,3,3,1].
# Buildings at indices 0 2 and 3 would be considered as served, and the output would be 2 (number of served buildings).

def routerReach(headCount,routerRange,routerLocation):
    totals = [0 for i in range(len(headCount))]
    for i in range(len(routerRange)):
        loc = routerLocation[i]
        r = routerRange[i]
        totals[loc-r:loc+r+1] = [count+1 for count in totals[loc-r:loc+r+1]]
    count = 0
    for i in range(len(headCount)):
        if headCount[i] <= totals[i]:
            count += 1
            
    return count

#Binary Search Tree
