#!/bin/bash
sqlite3 dictionary.db
.mode csv
.import "../dictionary.csv" dictionary.db