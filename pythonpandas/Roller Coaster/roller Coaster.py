import pandas as pd

df = pd.read_csv("roller_coasters_data.csv")
df = df[["coaster_name",#"Length","Speed",
"Location","Status",#"Opening date","Type",
"Manufacturer",#"Height restriction","Model","Height","Inversions","Lift/launch system","Cost",
#"Trains","Park section","Duration","Capacity","G-force","Designer","Max vertical angle","Drop","Soft opening date","Fast Lane available","Replaced","Track layout",
#"Fastrack available","Soft opening date.1","Closing date", "Opened", "Replaced by", "Website","Flash Pass available","Acceleration","Restraints","Name",
"year_introduced","latitude","longitude","Type_Main","opening_date_clean",#"speed1","speed2","speed1_value","speed1_unit",
"speed_mph",#"height_value","height_unit",
"height_ft","Inversions_clean","Gforce_clean"]].copy()

df["opening_date_clean"] = pd.to_datetime(df["opening_date_clean"])
df=df.rename(columns={
    "coaster_name":"Coaster_Name",
    "year_introduced":"Year_Introduced",
    "opening_date_clean":"Opened_Date",
    "latitude":"Latitude",
    "longitude":"Longitude",
    "speed_mph":"Speed_mph",
    "height_ft":"Height_ft",
    "Inversions_clean":"Inversions",
    "Gforce_clean":"Gforce"
})
df=df.loc[~df.duplicated(subset=["Coaster_Name","Manufacturer","Location"])]

df=df.query('Status != "Removed"')
df=df.query('Status != "Closed"')
df=df.query('Status != None')
df=df.reset_index(drop=True)

print(df.to_string())
df.to_csv("new_roller_coaster.csv",index=False)