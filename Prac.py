import pandas as pd

#write a python script to give me all the students information that admission accepted
def information(data):
    """
    """
    accepted_students = data[data['Admission Status'] == 'Accepted']
    print(accepted_students)
    return accepted_students

#Student with highest marks
def high_score(data, accepted_students):
    highest_score = data["Admission Test Score"].max()
    Student_name = data.loc[(data['Admission Status'] == 'Rejected') & (data["Admission Test Score"] == data["Admission Test Score"].max())]
    print("Highest Admission Test Score:", Student_name)
    s1 = accepted_students[accepted_students["Admission Test Score"] == accepted_students["Admission Test Score"].max()]
    print(s1)


def fetch_city(data):
    v1 = data["City"].value_counts()
    print("Total number of student from each city----> ",v1)



#Ratio of M and F
def ratio(data):
    b1 = data[data["Gender"] == 'Male']
    b1 = b1[b1['Admission Status']=="Accepted"]

    b2 = data[data["Gender"] == 'Female']
    b2 = b2[b2['Admission Status']=="Accepted"]

    k1  = b1["Gender"].count()
    print("count of male",k1)
    k2 = b2["Gender"].count()
    print("count of female",k2)

    c2 = k1/k2
    print(c2)   
    return(c2) 

def main():
# Import the Dataset file. Pandas has read_csv method that help to load .csv file
    file_path = "student_admission_record_dirty.csv"
    data = pd.read_csv(file_path)
    # find all the students that took admission in college
    information(data)
    # Students with max score
    high_score(data)
    # City with Max students
    fetch_city(data)
    #Ration of M and F
    response  = ratio(data)
    print(response)



if __name__ == '__main__':
    main()