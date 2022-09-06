#Step 1, Get just the needed data from Pothoven
#This step reads Pothoven csvfile, which contains all the years
# and creates Rdata files with the subset of data needed
#At the end, check the stations used with leaflet command
library(dplyr)

df_year = "2015"
#df_year = "2010"

#You don't need the trailing 'slash', script uses 'file.path' which adds it
#Original data and R scripts are in this directory
path <- "/Users/lllowe/visit-for-fvcom/scatterplots"

#The csvs are here
inputpath <- file.path(path,"inputdata") 

#- You should not need to modify from here, but after sourcing, 
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

#---Reformat Pothoven data----
#Read CSV's, James sent by email and I reformatted
#TODO, start with the ones Wilson sent to reproduce formatting
#I modified this by hand to get the lat/lon in decimals
csvfile <- file.path(inputpath,"Pauer_sites.csv")
df <- read.csv(csvfile)
#Restrict to study area
df <- filter(df,Lat >= 42.95)
df <- filter(df,Lat <= 43.35)
df <- filter(df,Lon >= -86.6)
#Remove GH45
df <- subset(df,Station!="GH 45")
#Rename smallcase lat/lon for Mark's projection script
colnames(df) <- c('Station','lat','lon','Depth')
df <- projUtm(df)
df$X <- df$X*1000
df$Y <- df$Y*1000
#Make it not have ridiculous 'precision'.  
#Digits means total numbers, not numbers after decimal place
df$X <- format(df$X,digits=8)
df$Y <- format(df$Y,digits=8)
#save with a useful name
Pothoven_locations <- df
#Add 'Source' for later calculations
Pothoven_locations$Source <- "Pothoven"

#James sent by email and I reformatted
csvfile <- file.path(inputpath,"Pauer_WQ_data.csv")
df <- read.csv(csvfile)
#Grab just the year
df <- df[df$Year==df_year,]
#Just get ones with TP values
df <- df[!is.na(df$TP),]
#Restrict to the Stations we chose above
thestations <- Pothoven_locations$Station
df <- subset(df,Station %in% thestations)
#Check if it makes sense
length(unique(df$Station))
#Add Date variable in POSIX format
df$Date <- paste(df$Month,df$Day,df$Year,sep="/")
df$Date <- as.POSIXct(df$Date, format="%m/%d/%Y")
#Sort by Date, easier to check
df <- arrange(df,Date)
#Prints out the different depths
unique(df$Depth)

#Add coordinates to the dataframe
df$Lat <- NA
df$Lon <- NA
df$X <- NA
df$Y <- NA
thelats <- Pothoven_locations$lat
thelons <- Pothoven_locations$lon
thexs <- Pothoven_locations$X
theys <- Pothoven_locations$Y
#Match coordinates with stations
for (i in 1:length(thestations)){
  df[df$Station == thestations[i], "Lat"] <- thelats[i]
  df[df$Station == thestations[i], "Lon"] <- thelons[i]
  df[df$Station == thestations[i], "X"] <- thexs[i]
  df[df$Station == thestations[i], "Y"] <- theys[i]
}

#Add 'Source' for later calculatons
df$Source = "Pothoven"

#Save by depth
df_surface <- filter(df,Depth<=7)
df_mid <- filter(df,Depth>7)
df_mid <- filter(df_mid,Depth<=60)
df_bot <- filter(df,Depth>60)
Pothoven_data <- df
Pothoven_surface <- df_surface
Pothoven_mid <- df_mid
Pothoven_bot <- df_bot

#Save data and locations
save(Pothoven_data,Pothoven_surface,Pothoven_mid,Pothoven_bot,file=file.path(outputpath,"Pothoven_data.Rdata"))
save(Pothoven_locations,file=file.path(outputpath,"Pothoven_locations.Rdata"))

#---end reformat Pothoven data

#If you want to check a map of where the stations were, uncomment
library(leaflet)
leaflet() %>% addTiles() %>%
  addCircles(data=Pothoven_locations,~lon,~lat,radius=500, label = ~as.character(Station),
             stroke=FALSE, fillOpacity=1, fillColor="blue")

