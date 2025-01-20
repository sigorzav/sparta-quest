def solution(emergency):
    answer = []
    emergency_dict = {}
    
    emergency_sorted = sorted(emergency, reverse=True)
    for i in range(len(emergency_sorted)):
        emergency_dict[emergency_sorted[i]] = i + 1
        
    return [emergency_dict[i] for i in emergency if i in emergency_dict]