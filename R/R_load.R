library(RMongo)
# library(devtools)
# install.packages('Rmongo')
# mg1 <- mongoDbConnect('db')
# 
# install_github("Rmongo", "tc")

mg1 <- mongoDbConnect('mydb')
dbShowCollections(mg1)

dbGetQuery(mg1, 'instagram_test', "{'}")
