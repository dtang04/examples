import pandas as pd
trees = pd.read_csv("2015StreetTreesCensus_TREES.csv", index_col = "tree_id")

def printbasicattributes(trees):
    print(trees.columns)
    print(trees.index) #Now our index is by tree_id
    print(trees.loc[201923]) #Using the loc keyword to get a row by tree_id
    print(trees.iloc[30]) #Using the iloc keyword to get a row by index position
    print(type(trees.iloc[30])) #pandas.Series object - a one dimensional labelled array

#printbasicattributes(trees)
tree10 = trees[0:10] #slice with rows of dataframe
print("Get all rows of spc_common: \n", tree10["spc_common"])
print("Another way to get all rows of spc_common: \n", tree10.spc_common) #this way is more limited because it has to follow Python standards
trees_narrow = trees[['spc_common', 'status', 'health', 'boroname', 'Latitude', 'longitude']] #new dataframe with only select rows
print("Now this dataframe has fewer columns: \n", trees_narrow)
print("The shape of the narrow dataframe is: ", trees_narrow.shape) #returns tuple of (numrow, numcol)
print("Number of unique tree species: ", trees.spc_common.nunique())
vc = trees.spc_common.value_counts()
print("How much of each unique tree species is planted: \n", vc)
print("Only index of value counts: \n", vc.index)
print("Count of London Planetree: ", vc["London planetree"]) #get row of series object, equivalent of calling vc.loc["London planetree"]
print("Count of Mimosa: ", vc.mimosa) #has to follow Python syntax (i.e. no spaces)
print("pd.describe: ", trees.spc_common.describe()) #pd.describe gives several statistics of a column
print("Relative frequency of each tree kind: \n", vc/len(trees)*100) #python operations are broadcast to entire series
"""
Filtering
"""
print("Most common tree in Brooklyn: ", trees[trees["boroname"] == "Brooklyn"]["spc_common"].mode()[0]) #mode returns a series of the element with highest frequency
#we can use bitwise operators to concatenate multiple filters together. However, note that bitwise operators
#have greater operator precedence over "==" operation, so we must use parenthesis over "=="
print("Percentage of trees in Queens in dead or poor health: ", len(trees[(trees["boroname"] == "Queens") & \
((trees["status"] == "Dead") | (trees["health"] == "Poor"))]) / len(trees[(trees["boroname"] == "Queens") & (trees["status"] != "Stump")]) * 100)
"""
Now we discuss the groupby, unstack, and where methds
"""
trees["combined"] = trees["status"].where(trees["status"] != "Alive", trees["health"])
#the where function takes in a sequence of conditions; when one of the earlier conditions is met (i.e. a tree is not alive)
#then it keeps entries there unchanged. Otherwise, it moves on to the next condition and gets corresponding entries.
bostatus = trees.groupby(["boroname", "combined"]).size()
print("Number of trees in each borough with status: \n", bostatus) #performs a groupby on boroname and status (hierarchial index)
bostatuspct = bostatus / trees.groupby(["boroname"]).size() * 100
print("Relative frequency of number of trees in each borough with status: \n", bostatuspct) #pandas broadcasts bostatuspct to the each hiearchial index of bostatus
bostatuspctdf = bostatuspct.unstack() #the unstack method turns a hierarchial index into a dataframe, using the outermost hierarchy as the dataframe index
print("Now the object is a dataframe: \n", bostatuspctdf[["Good","Fair","Poor","Dead","Stump"]]) #rearrange columns
trees.drop("combined", axis=1) #revert trees back to original form


