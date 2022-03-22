import numpy as np

def calculate(list):
 
    if len(list) < 9:
      raise ValueError("List must contain nine numbers.")
    calc = np.array(list)
    calc = calc.reshape(3,3)
    calculations = {
       'mean': [np.mean(calc, axis = 0).tolist(),np.mean(calc, axis = 1).tolist(),np.mean(calc).tolist()],
      'variance': [np.var(calc, axis = 0).tolist(),np.var(calc, axis = 1).tolist(),np.var(calc).tolist()],
      'standard deviation': [np.std(calc, axis = 0).tolist(),np.std(calc, axis = 1).tolist(),np.std(calc).tolist()],
      'max': [np.amax(calc, axis = 0).tolist(),np.amax(calc, axis = 1).tolist(),np.amax(calc).tolist()],
      'min': [np.amin(calc, axis = 0).tolist(),np.amin(calc, axis = 1).tolist(),np.amin(calc).tolist()],
      'sum': [np.sum(calc, axis = 0).tolist(),np.sum(calc, axis = 1).tolist(),np.sum(calc).tolist()]
    }
    return calculations
 


  