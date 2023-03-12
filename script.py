# -*- coding: utf-8 -*-
"""
Lt Cdr Shubham Mehta
EPHRA - 03
Data Randomiser
"""

import random
import pandas as pd

# Create a list of possible values as per the various columns in your dataset
genderValues = ["male", "female"]
ageValues = ["21 - 30", "31 - 40", "41 - 50", "50+"]
maritalValues = ["Married", "Not Married", "Divorced", "Widow / Widower"]
educationValues = ["Graduate", "Post Graduate", "PhD", "Diploma", "Other"]
experienceValues = ["2 - 5", "5 - 8", "8 - 11", "11 - 15", "15+"]
timingValues = ["Full-time", "Part-time"]
salaryValues = ["10,000 - 20,000", "20,000 - 30,000", "30,000 - 40,000", "40,000 n above"]
compensationValues = ["Yes", "No", "Maybe"]
pliValues = ["Yes", "No"]
bonusValues = ["Yes", "No"]
insuranceValues = ["Yes", "No", "Maybe"]
subsidyValues = ["Yes", "No"]
leaveValues = ["Yes", "No"]
pensionValues = ["Yes", "No", "Maybe"]
certificationValues = ["Yes", "No", "Maybe"]
deliverableValues = ["Yes", "No", "Maybe"]
appraisalValues = ["Yes", "No"]
feedbackValues = ["Yes", "No"]
rewardValues = ["Yes", "No"]
performanceValues = ["Yes", "No"]
developmentValues = ["3 months back", "6 months back", "9 months back", "1 year back"]
mentorValues = ["Yes", "No", "Not sure"]
profileValues = ["Strongly Agree", "Agree", "Strongly disagree", "Disagree"]
workValues = ["Yes", "No", "Occasional"]
sabbaticalValues = ["Yes", "No"]
teamValues = ["Yes", "No"]
instructionValues = ["Strongly Agree", "Agree", "Strongly disagree", "Disagree"]
biasValues = ["Yes", "No", "Maybe"]
hygieneValues = ["Yes", "No", "Neutral"]
belongingValues = ["Yes", "No", "Maybe"]

# Generate a random array of 50 items
genderArray = [random.choice(genderValues) for i in range(150)]
ageArray = [random.choice(ageValues) for i in range(150)]
maritalArray = [random.choice(maritalValues) for i in range(150)]
educationArray = [random.choice(educationValues) for i in range(150)]
experienceArray = [random.choice(experienceValues) for i in range(150)]
timingArray = [random.choice(timingValues) for i in range(150)]
salaryArray = [random.choice(salaryValues) for i in range(150)]
compensationArray = [random.choice(compensationValues) for i in range(150)]
pliArray = [random.choice(pliValues) for i in range(150)]
bonusArray = [random.choice(bonusValues) for i in range(150)]
insuranceArray = [random.choice(insuranceValues) for i in range(150)]
subsidyArray = [random.choice(subsidyValues) for i in range(150)]
leaveArray = [random.choice(leaveValues) for i in range(150)]
pensionArray = [random.choice(pensionValues) for i in range(150)]
certificationArray = [random.choice(certificationValues) for i in range(150)]
deliverableArray = [random.choice(deliverableValues) for i in range(150)]
appraisalArray = [random.choice(appraisalValues) for i in range(150)]
feedbackArray = [random.choice(feedbackValues) for i in range(150)]
rewardArray = [random.choice(rewardValues) for i in range(150)]
performanceArray = [random.choice(performanceValues) for i in range(150)]
developmentArray = [random.choice(developmentValues) for i in range(150)]
mentorArray = [random.choice(mentorValues) for i in range(150)]
profileArray = [random.choice(profileValues) for i in range(150)]
workArray = [random.choice(workValues) for i in range(150)]
sabbaticalArray = [random.choice(sabbaticalValues) for i in range(150)]
teamArray = [random.choice(teamValues) for i in range(150)]
instructionArray = [random.choice(instructionValues) for i in range(150)]
biasArray = [random.choice(biasValues) for i in range(150)]
hygieneArray = [random.choice(hygieneValues) for i in range(150)]
belongingArray = [random.choice(belongingValues) for i in range(150)]

# Convert the array to a pandas DataFrame
df1 = pd.DataFrame(genderArray, columns=["Gender"])
df2 = pd.DataFrame(ageArray, columns=["Age Group"])
df3 = pd.DataFrame(maritalArray, columns=["Marital Status"])
df4 = pd.DataFrame(educationArray, columns=["Education"])
df5 = pd.DataFrame(experienceArray, columns=["Exprience"])
df6 = pd.DataFrame(timingArray, columns=["Full-time or part-time?"])
df7 = pd.DataFrame(salaryArray, columns=["Salary Range"])
df8 = pd.DataFrame(compensationArray, columns=["Are you satisfied with the compensation that you are getting as per your skills"])
df9 = pd.DataFrame(pliArray, columns=["Is there Performance Linked Incentive?"])
df10 = pd.DataFrame(bonusArray, columns=["Can retention bonus add to your job security?"])
df11 = pd.DataFrame(insuranceArray, columns=["Do you consider insurance an important benefit?"])
df12 = pd.DataFrame(subsidyArray, columns=["Would you be ready to pay for subsidized insurance premium?"])
df13 = pd.DataFrame(leaveArray, columns=["Do you get sufficient earned n sick leaves?"])
df14 = pd.DataFrame(pensionArray, columns=["Do you think getting pension after retirement will add to your job satisfaction level?"])
df15 = pd.DataFrame(certificationArray, columns=["Do you think institution should partly sponsor higher education or certification courses?"])
df16 = pd.DataFrame(deliverableArray, columns=["Will the above factor play a major role in your work deliverables?"])
df17 = pd.DataFrame(appraisalArray, columns=["Do you believe institution has strong performance appraisal system?"])
df18 = pd.DataFrame(feedbackArray, columns=["Is there a continuous feedback system available?"])
df19 = pd.DataFrame(rewardArray, columns=["Is the current reward & recognition system efficient?"])
df20 = pd.DataFrame(performanceArray, columns=["Does a strong R & R system affect your work performace?"])
df21 = pd.DataFrame(developmentArray, columns=["When was the last time you attended any employee development workshop?"])
df22 = pd.DataFrame(mentorArray, columns=["Do you feel the need for a strong mentor in institution for your career devlopment?"])
df23 = pd.DataFrame(profileArray, columns=["Does your job profile matches your skillset and qualification"])
df24 = pd.DataFrame(workArray, columns=["Are you required to work beyond normal hours / put in extra hours / overburdened with work?"])
df25 = pd.DataFrame(sabbaticalArray, columns=["Do you have option to go on sabbatical for higher education?"])
df26 = pd.DataFrame(teamArray, columns=["Are you comfortable working in a Team Environment"])
df27 = pd.DataFrame(instructionArray, columns=["Do you receive clear instructions / directions for work from management  / superiors?"])
df28 = pd.DataFrame(biasArray, columns=["Do you believe there is unconscious biasness or equal opportunity across institution?"])
df29 = pd.DataFrame(hygieneArray, columns=["Do you get hygienic work environment / infrastructure?"])
df30 = pd.DataFrame(belongingArray, columns=["Do you feel sense of belonging with the institution?"])

with pd.ExcelWriter("dataset.xlsx") as writer:
    df1.to_excel(writer, index=False, sheet_name="Sheet1")
    print("Exported Genders to Sheet1")
    df2.to_excel(writer, index=False, sheet_name="Sheet1", startcol=1, startrow=0)
    print("Exported Ages to Sheet1")
    df3.to_excel(writer, index=False, sheet_name="Sheet1", startcol=2, startrow=0)
    print("Exported Marital Status to Sheet1")
    df4.to_excel(writer, index=False, sheet_name="Sheet1", startcol=3, startrow=0)
    print("Exported Education to Sheet1")
    df5.to_excel(writer, index=False, sheet_name="Sheet1", startcol=4, startrow=0)
    print("Exported Years of Experience to Sheet1")
    df6.to_excel(writer, index=False, sheet_name="Sheet1", startcol=5, startrow=0)
    print("Exported Timings to Sheet1")
    df7.to_excel(writer, index=False, sheet_name="Sheet1", startcol=6, startrow=0)
    print("Exported Salaries to Sheet1")
    df8.to_excel(writer, index=False, sheet_name="Sheet1", startcol=7, startrow=0)
    print("Exported Compensations to Sheet1")
    df9.to_excel(writer, index=False, sheet_name="Sheet1", startcol=8, startrow=0)
    print("Exported PLI to Sheet1")
    df10.to_excel(writer, index=False, sheet_name="Sheet1", startcol=9, startrow=0)
    print("Exported Bonuses to Sheet1")
    df11.to_excel(writer, index=False, sheet_name="Sheet1", startcol=10, startrow=0)
    print("Exported Insurances to Sheet1")
    df12.to_excel(writer, index=False, sheet_name="Sheet1", startcol=11, startrow=0)
    print("Exported Subsidies to Sheet1")
    df13.to_excel(writer, index=False, sheet_name="Sheet1", startcol=13, startrow=0)
    print("Exported Leaves to Sheet1")
    df14.to_excel(writer, index=False, sheet_name="Sheet1", startcol=14, startrow=0)
    print("Exported Pensions to Sheet1")
    df15.to_excel(writer, index=False, sheet_name="Sheet1", startcol=15, startrow=0)
    print("Exported Certifications to Sheet1")
    df16.to_excel(writer, index=False, sheet_name="Sheet1", startcol=16, startrow=0)
    print("Exported Deliverables to Sheet1")
    df17.to_excel(writer, index=False, sheet_name="Sheet1", startcol=17, startrow=0)
    print("Exported Appraisals to Sheet1")
    df18.to_excel(writer, index=False, sheet_name="Sheet1", startcol=18, startrow=0)
    print("Exported Feedbacks to Sheet1")
    df19.to_excel(writer, index=False, sheet_name="Sheet1", startcol=19, startrow=0)
    print("Exported Rewards to Sheet1")
    df20.to_excel(writer, index=False, sheet_name="Sheet1", startcol=20, startrow=0)
    print("Exported Performances to Sheet1")
    df21.to_excel(writer, index=False, sheet_name="Sheet1", startcol=21, startrow=0)
    print("Exported Developments to Sheet1")
    df22.to_excel(writer, index=False, sheet_name="Sheet1", startcol=22, startrow=0)
    print("Exported Mentors to Sheet1")
    df23.to_excel(writer, index=False, sheet_name="Sheet1", startcol=23, startrow=0)
    print("Exported Profiles to Sheet1")
    df24.to_excel(writer, index=False, sheet_name="Sheet1", startcol=24, startrow=0)
    print("Exported Works to Sheet1")
    df25.to_excel(writer, index=False, sheet_name="Sheet1", startcol=25, startrow=0)
    print("Exported Sabbaticals to Sheet1")
    df26.to_excel(writer, index=False, sheet_name="Sheet1", startcol=26, startrow=0)
    print("Exported Teams to Sheet1")
    df27.to_excel(writer, index=False, sheet_name="Sheet1", startcol=27, startrow=0)
    print("Exported Instructions to Sheet1")
    df28.to_excel(writer, index=False, sheet_name="Sheet1", startcol=28, startrow=0)
    print("Exported Biases to Sheet1")
    df29.to_excel(writer, index=False, sheet_name="Sheet1", startcol=29, startrow=0)
    print("Exported Hygienes to Sheet1")
    df30.to_excel(writer, index=False, sheet_name="Sheet1", startcol=30, startrow=0)
    print("Exported Belongings to Sheet1")

print("Dataset exported successfully.")
