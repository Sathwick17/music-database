DMQL Music Store Database Project

Project Overview
----------------
This project implements a normalized and query-optimized version of a music store database using PostgreSQL. The schema includes 16 tables covering customer information, tracks, albums, artists, invoices, playlists, and more, all conforming to Boyce-Codd Normal Form (BCNF). The project demonstrates data loading, normalization, indexing, query execution analysis, and constraint enforcement.

Project Structure
-----------------
- create.sql           → SQL script to create all base and decomposed (BCNF) tables with constraints.
- load.sql             → SQL script to bulk load CSV data into the database using \COPY commands.
- create_load.ipynb    → Jupyter Notebook used for executing SQL commands interactively.
- *.csv                → Data files for each table in the schema.

CSV Files
---------
Each CSV file corresponds to a table in the schema:
- album.csv
- artist.csv
- customer.csv
- customer_location.csv
- customerbilling.csv
- employee.csv
- genre.csv
- invoice.csv
- invoice_line.csv
- location.csv
- media_type.csv
- media_type_pricing.csv
- playlist.csv
- playlist_track.csv
- track.csv
- track_price.csv

Running the Project
-------------------
1. Create the database and open a terminal with PostgreSQL access.
2. Run the schema:
   $ psql -d music -f create.sql

3. Load the data:
   $ psql -d music -f load.sql
If the load and create.sql won’t work, you can run the ipynb file.
Database name - “music”

4. Open create_load.ipynb to experiment with queries and indexes.

Features
--------
- Full normalization to BCNF with proper decomposition.
- Realistic data constraints including foreign keys, NOT NULLs, and enums.
- Query execution analysis using EXPLAIN before/after indexing.
- Example SELECT, JOIN, GROUP BY, ORDER BY, and Subquery queries included.
- Supports analytical insights like most diverse customers, top tracks, and total revenue by genre.