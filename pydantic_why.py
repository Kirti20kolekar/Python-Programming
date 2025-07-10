def insert_patient_data(name,age):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cannot be Negative')
        else:
            print(name)
            print(age)
            print('Inserted into Database')
    else:
        raise TypeError['Incorrect Datatype']

def update_patient_data(name,age):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('Updated into Database')
    else:
        raise TypeError['Incorrect Datatype']
    
