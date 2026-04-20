import os
import logging

from dotenv import load_dotenv
from databricks import sql

load_dotenv(verbose=True)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
QUERY = """SELECT d.year, p.category, sum(o.amount) as order_total, count(1) as order_count
                      from brij_lakehouse.gold.fact_orders o
                               join brij_lakehouse.gold.dim_date d on o.order_date = d.date
                               join brij_lakehouse.gold.dim_product p on o.product_id = p.product_id
                      group by d.year, p.category
                      order by d.year
                   """


def main():
    """Main function to connect to Databricks and execute query."""
    # Load environment variables
    server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    access_token = os.getenv("ACCESS_TOKEN")

    if not all([server_hostname, http_path, access_token]):
        logger.error(
            "Missing required environment variables: DATABRICKS_SERVER_HOSTNAME, DATABRICKS_HTTP_PATH, ACCESS_TOKEN"
        )
        return

    try:
        with sql.connect(
            server_hostname=server_hostname,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(QUERY)
                results = cursor.fetchall()
                for row in results:
                    print(row)
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
