#Step 1, create a text file for each date with measurements.
#Make a separate file for each 'Source'
library(stringr)
library(stringi)
library(lubridate)
library(readr)
library(dplyr)

df_year = "2015"
#df_year = "2010"

#You don't need the trailing 'slash', script uses 'file.path' which adds it
#Original data and R scripts are in this directory
path <- "/Users/lllowe/visit-for-fvcom/scatterplots"
#Put stations files where you will run the visit scripts
visitpath <- "/Users/lllowe/visit-for-fvcom/scatterplots"


#---You shouldn't need to modify past here
#Path for output files
firstdir <-file.path(path,"stations")
outputpath <- file.path(firstdir,df_year)
# make a directory if it doesn't exist
if (!dir.exists(firstdir)){
  dir.create(firstdir)}else{} #avoids 'already exists' warning
if (!dir.exists(outputpath)){
  dir.create(outputpath)}else{} #avoids 'already exists' warning

#Input...
#This was created in Step3_allstation_file.R
#This one for visit has dates next to each other repeating
load(file.path(outputpath,"all_stations.Rdata"))

#Prefix for final files, a date string is added later.
outprefix <- file.path(path,"stations",df_year)

#Use 'df' To reuse code
df <- all_stations
#Add 'dummy' Depth as Z
df$Z <- 1

#Make one for circles...
#if I make it later, I can't change Z (empty df)
dfc <- all_stations
#Add 'dummy' Depth as Z
dfc$Z <- (-10)

#Put in string padding so file names is consistent
mm <- str_pad(as.character(month(df$Date)),2,pad="0")
dd <- str_pad(as.character(day(df$Date)),2,pad="0")
yy <- as.character(year(df$Date))
#Define the filestring
filestring <- paste0("date_",mm,dd,yy,".txt")
df$sfile <- filestring

#Put the time zone for consistency (POSIX R stuff)
df$Date <- as.POSIXct(df$Date, tz="GMT")

#Rename so when we open the Rdata file it has a useful name
stationdata <- df
#Save the stationdata dataframe
filename <- file.path(outputpath,"station-data.Rdata")
save(stationdata,file=filename)

#Get the number of unique dates
uns <- unique(df$Date)
iunis <- length(uns)

#Print unique stations and locations
cat("There are ",iunis," unique dates.\n")
cat("There are ",length(unique(df$Station))," unique stations.\n")

#For every unique date
for(i in 1:iunis){
  #Get a dataframe containing only those dates
  df1 <- df[df$Date==uns[i],]
  df1c <- dfc[dfc$Date==uns[i],]
  #Assign two different time formats
  time1 <- uns[i]
  time2 <- as.POSIXct(time1, format="%Y-%m-%dT%H:%M:%S")
  mm <- str_pad(as.character(month(time2)),2,pad="0")
  dd <- str_pad(as.character(day(time2)),2,pad="0")
  yy <- as.character(year(time2))
  #This will name the file date_mmddyy.txt
  datestring <- paste0("date_",mm,dd,yy,".txt")
  #VisIt reads in text files in x,y,z,value format for the points
  #I divide by 1000 here instead of multiplying model by 1000 in VisIt
  ndf <- df1[,c('X','Y','Z','TP','Source')]
  ndf <- transform(ndf,TP=TP/1000.)
  ndf$X <- as.double(format(ndf$X,digits=8))
  ndf$Y <- as.double(format(ndf$Y,digits=8))
  #For circles
  ndfc <- df1c[,c('X','Y','Z','TP','Source')]
  ndfc <- transform(ndfc,TP=TP/1000.)
  ndfc$X <- as.double(format(ndfc$X,digits=8))
  ndfc$Y <- as.double(format(ndfc$Y,digits=8))
  #Save in a csv table, these are ALL stations
  filename <- file.path(path,"stations",df_year,datestring)
  write.table(ndf,file=filename,quote=FALSE,sep=",",row.names=FALSE)  
  #Make different files to have different shapes
  #Pothoven
  potdf <- ndf[ndf$Source=="Pothoven",]
  filename <- file.path(path,"stations",df_year,paste0("pot_",datestring))
  write.table(potdf,file=filename,quote=FALSE,sep=",",row.names=FALSE)
  #copy for the circles with different Z
  potdf <- ndfc[ndfc$Source=="Pothoven",]
  filename <- file.path(path,"stations",df_year,paste0("pot2_",datestring))
  write.table(potdf,file=filename,quote=FALSE,sep=",",row.names=FALSE)
  if(df_year=="2010"){
    #There is no CSMI, but make files so VisIt script works
    potdf <- ndf[ndf$Source=="Lisa",]
    filename <- file.path(path,"stations",df_year,paste0("csmi_",datestring))
    write.table(potdf,file=filename,quote=FALSE,sep=",",row.names=FALSE)
    #There is no CSMI, but make files so VisIt script works
    potdf <- ndfc[ndfc$Source=="Lisa",]
    filename <- file.path(path,"stations",df_year,paste0("csmi2_",datestring))
    write.table(potdf,file=filename,quote=FALSE,sep=",",row.names=FALSE)
  }
  #CSMI data
  if(df_year=="2015"){
    csmidf <- ndf[ndf$Source=="CSMI",]
    filename <- file.path(path,"stations",df_year,paste0("csmi_",datestring))
    write.table(csmidf,file=filename,quote=FALSE,sep=",",row.names=FALSE)  
    #copy for the circles with different Z
    csmidf <- ndfc[ndfc$Source=="CSMI",]
    filename <- file.path(path,"stations",df_year,paste0("csmi2_",datestring))
    write.table(csmidf,file=filename,quote=FALSE,sep=",",row.names=FALSE) 
  }
  
}

#If you want to check a map of where the stations were, uncomment
library(leaflet)
leaflet(data=df) %>% addTiles() %>%
     addCircles(~lon,~lat,radius=1000, label = ~as.character(Station),
                stroke=FALSE, fillOpacity=.8, fillColor="blue")

#This makes a pdf with a barplot of TP measurements
pdf(file.path(outputpath,"barplots.pdf"), width=16, height=10)
boxplot(TP ~ Date, data=df, main="Measurements in Study Area",col = "white")
stripchart(TP ~ Date,
           data = df,
           method = "jitter",
           pch = 19,
           cex = 0.6,
           col = 2:4,
           vertical = TRUE,
           add = TRUE)

dev.off()
