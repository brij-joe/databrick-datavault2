import os

from dotenv import load_dotenv
from databricks import sql

load_dotenv(verbose=True)


def main():
    connection = sql.connect(
        server_hostname="dbc-4be625a8-3511.cloud.databricks.com",
        http_path="/sql/1.0/warehouses/b555d45d8079cc1b",
        access_token=os.getenv("ACCESS_TOKEN"),
    )

    cursor = connection.cursor()

    cursor.execute("""SELECT d.year, p.category, sum(o.amount) as order_total, count(1) as order_count
                      from brij_lakehouse.gold.fact_orders o
                               join brij_lakehouse.gold.dim_date d on o.order_date = d.date
                               join brij_lakehouse.gold.dim_product p on o.product_id = p.product_id
                      group by d.year, p.category
                      order by d.year
                   """)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
