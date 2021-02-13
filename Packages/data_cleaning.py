import pandas as pd

def data_cleaning(caminho):
    df = pd.read_csv(caminho + 'Output\\glassdoor_jobs.csv')    

    df['Per Hour'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
    df['Employer_Provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

    df = df[df['Salary Estimate']!='-1']
    salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

    minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
    min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

    df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0])) 
    df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
    df['med_salary'] = (df['min_salary'] + df['max_salary'])/2

    df['Company Name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)

    df['State'] = df['Location'].apply(lambda x: x.split(',')[1])

    df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2020 - x)

    df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

    df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

    df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

    df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

    df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

    df.drop(columns=['Unnamed: 0'], inplace=True)

    df.to_excel(caminho + "\\Output\\glassdoor_jobs.xlsx", index=False)

data_cleaning("C:\\Users\\anny_\\Documents\\The_Glassdoor_Project\\")