True_values=[100,90,80]
predicted_values=[99,85,76]

def MSE(True_values,predicted_values):
    SE_list=[]
    from statistics import mean
    for i in range(len(True_values)):
        SE=(True_values[i]-predicted_values[i])**2
        SE_list.append(SE)
    return mean(SE_list)    
     

assert MSE(True_values,predicted_values)==14 , 'it must be 14'
