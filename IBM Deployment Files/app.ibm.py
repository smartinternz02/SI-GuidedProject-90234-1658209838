# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:18:51 2022

@author: SmartBridge-PC
"""

import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "w6ZT-5yZ2DztpUtKA-igU-YVqCm4cCmsUlfRC_y581cr"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']], "values": [[1,1,1,1,1,1056,111,1,50,1,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/48db5d2a-14c9-44ea-a4cd-305e63763dbc/predictions?version=2022-08-11', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
