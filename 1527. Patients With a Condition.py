import pandas as pd 
data = pd.DataFrame(data = {'patient_id' : [1, 2, 3, 4, 5, 6],
'patient_name' : ['Daniel','Alice', 'Bob', 'George', 'Alain', 'Daniel'],
'conditions':['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201', 'SADIAB100']})

# print(data)


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
        return patients[patients.conditions.str.split().apply(lambda conditions: any(cond.startswith('DIAB1') for cond in conditions))]
print(find_patients(data))