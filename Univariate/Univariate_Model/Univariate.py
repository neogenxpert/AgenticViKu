class Univariate ():
    def QualQuan(ds) :
        qual,quan = [] , []
        for items in ds.columns :
            (qual if ds[items].dtype == 'O' else quan).append(items)
        return qual, quan

    def outlier(Quan,Univariate):
        lesser,greater = [], []
        for columnName in Quan:
            if (descriptive.loc["Lesser Quartile",columnName] > descriptive.loc["Min Value",columnName]):
                lesser.append(columnName)
            if (descriptive.loc["Greater Quartile",columnName] < descriptive.loc["Max Value",columnName]):
                greater.append(columnName)
        return lesser, greater

    def freqTable(columnName,ds):
        freqTable = pd.DataFrame(columns=["Unique Value","Frequency","Rel_Frequency","CumSum"])
        freqTable["Unique Value"] = ds[columnName].value_counts().index
        freqTable["Frequency"] = ds[columnName].value_counts().values
        freqTable["Rel_Frequency"] = (freqTable["Frequency"]/103)
        freqTable["CumSum"] = freqTable["Rel_Frequency"].cumsum()
        return freqTable

    def Univariate(Quan,ds):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100","IQR","1.5 Rule","Lesser Quartile",
                                        "Greater Quartile","Min Value","Max Value"],columns=Quan)
        for columnName in Quan:
            descriptive.loc["Mean",columnName]=ds[columnName].mean()
            descriptive.loc["Median",columnName]=ds[columnName].median()
            descriptive.loc["Mode",columnName]=ds[columnName].mode()[0]
            descriptive.loc["Q1:25%",columnName]=ds.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%",columnName]=ds.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%",columnName]=ds.describe()[columnName]["75%"]
            descriptive.loc["99%",columnName]=np.percentile(ds[columnName],99)
            descriptive.loc["Q4:100",columnName]=ds.describe()[columnName]["max"]
            descriptive.loc["IQR",columnName]=descriptive.loc["Q3:75%",columnName] - descriptive.loc["Q1:25%",columnName]
            descriptive.loc["1.5 Rule",columnName]= 1.5 * descriptive.loc["IQR",columnName]
            descriptive.loc["Lesser Quartile",columnName]= ds.describe()[columnName]["25%"] - descriptive.loc["1.5 Rule",columnName]
            descriptive.loc["Greater Quartile",columnName]=descriptive.loc["Q3:75%",columnName] + descriptive.loc["1.5 Rule",columnName]
            descriptive.loc["Min Value",columnName]=ds[columnName].min()
            descriptive.loc["Max Value",columnName]=ds[columnName].max()
        return descriptive