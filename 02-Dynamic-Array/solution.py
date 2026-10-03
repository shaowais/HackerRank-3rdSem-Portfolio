# Problem 2: Dynamic Array
def dynamicArray(n, queries):
    nested_list = [[] for _ in range(n)]
    last_answer = 0
    result_list = []
    
    for item in queries:
        query_type = item[0]
        x_val = item[1]
        y_val = item[2]
        
        target_index = (x_val ^ last_answer) % n
        
        if query_type == 1:
            nested_list[target_index].append(y_val)
        elif query_type == 2:
            element_index = y_val % len(nested_list[target_index])
            last_answer = nested_list[target_index][element_index]
            result_list.append(last_answer)
            
    return result_list