#data preprocessing
data <- read.csv("C:/Users/parag/Udemy/A_Z_DataScience_MachineLearning/Data.csv")

#missing data
data$Age = ifelse(is.na(dataset$Age),
                  ave(data$Age, FUN = function(m)))
