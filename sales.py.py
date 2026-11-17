import pandas as pd

import matplotlib.pyplot as plt

from sqlalchemy import create_engine,URL


connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Sami@2025",
    host="localhost",
    port=3306,
    database="y5"
)

engine = create_engine(connection_url)



# MySQL se data load karo

query = "SELECT * FROM y5"

df = pd.read_sql(query, engine)


# Revenue column banao

df["revenue"] = df["quantity"] * df["price"]


print("Data preview:")

print(df.head())


print("\nTotal revenue:", df["revenue"].sum())


# Product-wise revenue

product_sales = (

    df.groupby("product")["revenue"]

    .sum()

    .sort_values(ascending=False)

)

print("\nProduct-wise revenue:")

print(product_sales)


# City-wise revenue

city_sales = (

    df.groupby("city")["revenue"]

    .sum()

    .sort_values(ascending=False)

)

print("\nCity-wise revenue:")

print(city_sales)


# Chart: product-wise revenue

product_sales.plot(kind="bar", color="teal")

plt.title("Revenue by Product")

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()