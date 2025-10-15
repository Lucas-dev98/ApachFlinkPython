#!/usr/bin/env python3
"""
PyFlink Table API example: Top-N customers by total spend.

This script demonstrates a simple batch job using the PyFlink Table API.
It reads a CSV of transactions, aggregates total amount per customer, orders
by total descending and outputs the top N customers.

Notes:
- Run this with a local Flink distribution available (FLINK_HOME set) or by
  submitting to a Flink cluster. See README.md for setup instructions.
"""
from pyflink.table import EnvironmentSettings, TableEnvironment
import argparse


def main(input_csv: str, top_n: int, output_path: str):
    env_settings = EnvironmentSettings.in_batch_mode()
    t_env = TableEnvironment.create(env_settings)

    # Register a table from CSV
    t_env.execute_sql(f"""
        CREATE TABLE transactions (
            transaction_id STRING,
            customer_id STRING,
            amount DOUBLE,
            ts TIMESTAMP(3)
        ) WITH (
            'connector' = 'filesystem',
            'path' = '{input_csv}',
            'format' = 'csv'
        )
    """)

    # Aggregate total amount per customer
    result = t_env.from_path('transactions') \
        .group_by('customer_id') \
        .select('customer_id, amount.sum as total_spent')

    # Order and take top N
    topn = result.order_by('total_spent.desc').limit(top_n)

    # Write results to filesystem (CSV)
    t_env.execute_sql(f"""
        CREATE TABLE topn_out (
            customer_id STRING,
            total_spent DOUBLE
        ) WITH (
            'connector' = 'filesystem',
            'path' = '{output_path}',
            'format' = 'csv'
        )
    """)

    topn.execute_insert('topn_out').wait()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/sample_transactions.csv')
    parser.add_argument('--top', type=int, default=5)
    parser.add_argument('--out', default='data/topn_output.csv')
    args = parser.parse_args()
    main(args.input, args.top, args.out)
