#Step 2, Get just the needed data from CSMI
#This step reads CSMI csvfile, which contains data from only 2015
# and creates Rdata files with the subset of data needed
#At the end, check the stations used with leaflet command
library(stringr)  
library(stringi)
library(dplyr)

#This should only be 2015 for CSMI
df_year = "2015"

#You don't need the trailing 'slash', script uses 'file.path' which adds it
#Original data and R scripts are in this directory
path <- "/Users/lllowe/visit-for-fvcom/scatterplots"

#The csvs are here
inputpath <- file.path(path,"inputdata") 

#---You shouldn't need to modify past here, but after sourcing, 
#-- go to the end of the script to make the map and check stations
#Path for output files
firstdir <-file.path(path,"stations")
outputpath <- file.path(firstdir,df_year)
# make a directory if it doesn't exist
if (!dir.exists(firstdir)){
  dir.create(firstdir)}else{} #avoids 'already exists' warning
if (!dir.exists(outputpath)){
  dir.create(outputpath)}else{} #avoids 'already exists' warning

#Mark Rowe's Projection functions
filename <- file.path(path,"proj_functions.R")
source(filename)

#---Reformat CSMI data----
#Read CSV's, Wilson sent by email
csvfile <- file.path(inputpath,"MI_CSMI_2015_pts_ID_zones.csv")
df <- read.csv(csvfile)

#Restrict to study area
df <- filter(df,LatDD_targ >= 42.95)
df <- filter(df,LatDD_targ <= 43.35)
df <- filter(df,LonDD_targ >= -86.6)
#Remove Stations in Rivers, MuskMouth and GrandMouth
df <- subset(df,StationCod!="MuskMouth")
df <- subset(df,StationCod!="GrandMouth")
#Check if they are what you expect
uns <- unique(df$StationCod)
uns
length(uns)

#Just keep some columns
df <- df %>% select(StationCod,WQdepth_m,Chla_ugL,TP_ugL,SampleDate,LatDD_targ,LonDD_targ)
#Rename
colnames(df) <- c('Station','Depth','CHL','TP','Date','lat','lon')

#Add X,Y
df <- projUtm(df)
df$X <- df$X*1000
df$Y <- df$Y*1000
#Make it not have ridiculous 'precision'.  
#Digits means total numbers, not numbers after decimal place
df$X <- format(df$X,digits=8)
df$Y <- format(df$Y,digits=8)

#Remove hr:min:sec, convert to POSIX
df$Date <- str_replace(df$Date," 0:00:00","")
df$Date <- as.POSIXct(df$Date, format="%m/%d/%Y")
#Sort by Date. take a look
df <- arrange(df,Date)

#Add 'Source' for later calculations
df$Source <- "CSMI"

CSMI_data <- df

#Save just the stations
CSMI_locations <- distinct(df,Station,.keep_all=TRUE)
CSMI_locations <- CSMI_locations %>% select(Station,lat,lon,Depth,X,Y,Source)

save(CSMI_data,file=file.path(outputpath,"CSMI_data.Rdata"))
save(CSMI_locations,file=file.path(outputpath,"CSMI_locations.Rdata"))

#If you want to check a map of where the stations were, uncomment
library(leaflet)
leaflet() %>% addTiles() %>%
  addCircles(data=CSMI_locations,~lon,~lat,radius=500, label = ~as.character(Station),
             stroke=FALSE, fillOpacity=.8, fillColor="blue")


