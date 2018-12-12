import sys
sys.path.append("/home/astha/Desktop/major3/")
print(".......................Through cosine similarity........................")
import cosinesim
print("\n.....................Through knn................")
import knnfinal
import pandas as pd
from prettytable import from_csv
from prettytable import PrettyTable
# The system shall authenticate user credentials to view the profile

def intersection(list1,list2):
	list3= [value for value in list1 if value in list2]
	return list3
def main():
	status = "************* Your Recommendations ***************"
	print (status)
	x = PrettyTable()
	x.field_names = ["ID","Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]


	b=intersection(knnfinal.b,cosinesim.req_index)
	list1=[]
	for i in b:
		
		list1.append(knnfinal.data_copy.iloc[i].values)
		x.add_row(knnfinal.data_copy.iloc[i].values)
		# print(list1)
		i=i+1
	df=pd.DataFrame(list1,columns=['ID','Requirements','project category','Requirement Category','Magnitude of Risk','Impact','Priority'])
	df.to_csv('intersect.csv',index=False)
	print(x.get_string(fields=["Requirements", "project category", "Requirement category", "Magnitude of Risk", "Impact", "Priority"]))

# with open("intersect.csv", "r") as fp: 
    # x = from_csv(fp)
# print(x)
		
if __name__ == '__main__':
	main()
