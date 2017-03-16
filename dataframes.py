from pandas import dataframe, read_excel, set_index

#takes argument of filename and returns dataframe object
def fileToDataframe(fname):
	df = pd.read_excel(fname, sheetname = "Money Lover Report")
	df = df.set_index("NO.")		#make our index equal to the id from our report
	return df

#takes arguments dataframe, filename, returns 1 on success and -1 on failure
def dataframeToFile(df, fname):
	try:
		writer = pd.ExcelWriter(fname, engine='xlsxwriter')
		df.to_excel(writer,'Money Lover Report')
		return 1
	except:
		print "Dataframe file write failed"
		return -1

def dataframeTomlRow(df):
	pass

def mlRowToDataframe(ls):
	pass
