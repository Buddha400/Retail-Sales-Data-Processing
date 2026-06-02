import pandas as pd

file_path = r"Dataset/USECASE - Data Engineering.xlsx"

retail1 = pd.read_excel(
    file_path,
    sheet_name="retail_data1"
)

retail2 = pd.read_excel(
    file_path,
    sheet_name="retail_data2"
)

products = pd.read_excel(
    file_path,
    sheet_name="product_details"
)

print(retail1.head())
print(retail2.head())
print(products.head())

print(retail1.isnull().sum())
print(retail2.isnull().sum())

df = pd.concat(
    [retail1, retail2],
    ignore_index=True
)

print(df.shape)

df.drop_duplicates(inplace=True)

print(df.shape)

df["category"] = (
    df["category"]
    .replace({
        "ELEC": "Electronics",
        "electronics": "Electronics",
        "FURN": "Furniture",
        "CLOTH": "Clothing",
        "clothing": "Clothing",
        "HOME": "Home Appliances"
    })
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

def mask_email(email):

    if pd.isna(email):
        return email

    name, domain = str(email).split("@")

    return name[:2] + "****@" + domain

df["email"] = df["email"].apply(mask_email)

def mask_phone(phone):

    phone = str(phone)

    return "XXXXXX" + phone[-4:]

df["phone"] = df["phone"].apply(mask_phone)


df["Revenue"] = (
    df["price"]
    * df["quantity"]
    * (1 - df["discount"])
)


df.to_csv(
    "Output/cleaned_retail_dataset.csv",
    index=False
)