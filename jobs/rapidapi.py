import requests


def data_dismantler(x):
    z = {
    "employer_name": x['employer_name'],
    "employer_logo": x['employer_logo'],
    "job_publisher": x['job_publisher'],
    "job_id": x['job_id'],
    "job_title": x['job_title'],
    "job_employment_type": x['job_employment_type'],
    "job_apply_link": x['job_apply_link'],
    "job_description": x['job_description'],
    "job_city": x['job_city'],
    "job_state": x['job_state'],
    "job_country": x['job_country'],
    "job_google_link": x['job_google_link'],
    "job_highlights": x['job_highlights']
    }
    return z



#print(data)

