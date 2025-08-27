class Univariate ():
    def QualQuan(ds) :
        qual,quan = [] , []
        for items in ds.columns :
            (qual if ds[items].dtype == 'O' else quan).append(items)
        return qual, quan