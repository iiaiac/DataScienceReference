There are three datasets.
1. Sales data (daily sale of SKU, with respect to store. From 1990-2021)
2. Master data (Reference/Mapping files for Sales Data)
2.1 SKU_Master (This dataset has information about SKU prices over the period of time, prices are recorded anually. "Price1990" denotes price of SKU in 1990.)
2.2 Store_Master (This dataset has information about store data, This data has information about the store commision date, name of store, pin code, district, state, and store region). hierarchy in this dataset is defined as State>>STORE REGION>>District>>Pin Code. OFFICE NAME and PINCODE has one to one mapping.



