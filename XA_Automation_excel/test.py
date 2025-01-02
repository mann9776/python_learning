"""
list_of_dict = []
Dict = {}

list_of_dict[0][1] = "Ram"
list_of_dict[0][2] = "Shyam"
list_of_dict[1][1] = "Vishnu"
list_of_dict[1][2] = "Shiv"

Dict[1] = "Ram"
Dict[2] = "Shyam"
list_of_dict.append(Dict)
print(list_of_dict)
"""
KPIs_header = (
"RRC Setup Success", "RRE_FAILURE_RATE (DROP RATE)", "RRC_Reestablishment_Fallback_Success_Rate", "RRC_ConnMean",
"RRC_CA_ConnMean", "DL PRB %")
for KPI in KPIs_header:
    print(f'{KPIs_header.index(KPI)}. {KPI}')
