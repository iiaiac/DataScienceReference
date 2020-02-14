# This version is created by Dhananjay Srivastava
library(sqldf)
library(odbc)
con <- dbConnect(odbc(),
                 Driver = "SQL Server",
                 Server = "144.91.118.200",
                 Database = "Credit_Card_Reporting",
                 UID = "*****",
                 PWD = "*****")


Product_Base <- readxl::read_excel("Product_Base.xlsx")


dbWriteTable(conn = con, 
             name = "Product_Base", 
             value = Product_Base)


Customer_Base <- readxl::read_excel("Customer_Base.xlsx")


dbWriteTable(conn = con, 
             name = "Customer_Base", 
             value = Customer_Base)


Biller_Info <- readxl::read_excel("Biller_Info.xlsx")


dbWriteTable(conn = con, 
             name = "Biller_Info", 
             value = Biller_Info)





 Transaction_Data <- data.table::fread("AppendedData.txt")

 Transaction_Data <- as.data.frame(Transaction_Data)
 
 
 Transaction_Data_v1 <- Transaction_Data %>% select(Credit_Card, Transaction_ID, Transaction_Date, Biller, Transaction_Value, EMI_Application_Status) 
 
 
 
 dbWriteTable(conn = con, 
              name = "Transaction_Data", 
              value = Transaction_Data_v1)
 