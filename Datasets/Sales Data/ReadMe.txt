There are Four types of datasets.
1. Sales data (daily sale of SKU, with respect to store. From 1990-2021) (Sale = Cost Price + Profit + Tax)
2. Master data (Reference/Mapping files for Sales Data)
2.1 SKU_Master (This dataset has information about SKU prices over the period of time, prices are recorded anually. "Price1990" denotes price of SKU in 1990.)
2.2 Store_Master (This dataset has information about store data, This data has information about the store commision date, name of store, pin code, district, state, and store region). hierarchy in this dataset is defined as State>>STORE REGION>>District>>Pin Code. OFFICE NAME and PINCODE has one to one mapping.
2.3 Profit Master: Profit Percentage for SKU in specified year (Profit = Cost*Profit Rate)
2.4 Tax Master : Tax for SKU in specified year (Tax = Profit*Tax Rate)
3 Sales-Data-1990-2021.zip is a single file with all the historical sales data

# ******************************************************************
if cost of an SKU in a specified year is X then Sale price can be defined as
Sale = X + X*Profit Rate + X*Profit Rate*Tax Rate
# ******************************************************************




