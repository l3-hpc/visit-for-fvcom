#Step3, create an 'allstation' file
#This was needed in earlier incarnations of these scripts
#It could possibly be eliminated with modifications to Step4
#(This note means to say:  Don't try to guess what I was thinking.)

#Combine datasets
library(dplyr)

df_year = "2010"
#df_year = "2015"

#You don't need the trailing 'slash', script uses 'file.path' which adds it
#Original data and R scripts are in this directory
path <- "/Users/lllowe/visit-for-fvcom/scatterplots"

#---You shouldn't need to modify past here
#Path for output files
firstdir <-file.path(path,"stations")
outputpath <- file.path(firstdir,df_year)
# make a directory if it doesn't exist
if (!dir.exists(firstdir)){
  dir.create(firstdir)}else{} #avoids 'already exists' warning
if (!dir.exists(outputpath)){
  dir.create(outputpath)}else{} #avoids 'already exists' warning

load(file.path(outputpath,"Pothoven_locations.Rdata"))
load(file.path(outputpath,"Pothoven_data.Rdata"))

#Make one dataframe for surface stations
#Just take needed variables
if(df_year=="2015"){
  load(file.path(outputpath,"CSMI_locations.Rdata"))
  load(file.path(outputpath,"CSMI_data.Rdata"))
  df_csmi <- CSMI_data %>% select(Station,Depth,TP,Date,lat,lon,X,Y,Source)
}
## Just doing surface
#df_pot <- Pothoven_data %>% select(Station,Depth,TP,Date,Lat,Lon,X,Y,Source)
df_pot <- Pothoven_surface %>% select(Station,Depth,TP,Date,Lat,Lon,X,Y,Source)

#Both dataframes need to have the same column names
colnames(df_pot) <- c('Station','Depth','TP','Date','lat','lon','X','Y','Source')
#Combine dataframes
if(df_year=="2015"){
  df_all <- rbind(df_csmi,df_pot)
} else {
  df_all <- df_pot
}

#Sort by Date and check to see if it makes sense
df_all <- arrange(df_all,Date)

all_stations <- df_all

save(all_stations,file=file.path(outputpath,"all_stations.Rdata"))

#Save to csv so humans can look at it
write.table(df_all,file=file.path(outputpath,"all_stations.csv"),row.names=FALSE,col.names=TRUE,quote=FALSE,sep=",")

