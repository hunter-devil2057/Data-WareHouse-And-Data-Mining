import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\Sheewakoti-Manish\Documents\My-Codes\Data-Warehouse-And-Data-Mining\Practical\Lab-4\student.csv")

# Display the original data
print("Original Data")
print(data.head())

# Convert DOB column to datetime format
data["DOB"] = pd.to_datetime(data["DOB"], errors='coerce')
data = data.dropna(subset=["DOB"])
# Calculate the AGE column
today = pd.to_datetime("today")  # Current date
data["AGE"] = ((today - data["DOB"]).dt.days / 365.25).astype(int)  # Convert days to years

# Save the transformed data to a new file
data.to_csv(r"C:\Users\Sheewakoti-Manish\Documents\My-Codes\Data-Warehouse-And-Data-Mining\Practical\Lab-4\date_with_age.csv", index=False)

# Display the transformed data
print("Transformed Data")
print(data.head())
