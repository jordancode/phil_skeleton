#!/bin/sh

# usage:
# > ./create_dbs.sh "main" 1024 | mysql >

DB_NAME=$1;
SHARD_COUNT=$2

if [ "$1" == "" ]; then
    DB_NAME=main
else
    DB_NAME="$1"    
fi

if [ "$2" == "" ]; then
    SHARD_COUNT=1024
else
    SHARD_COUNT="$2"
fi

i=0
while [[ $SHARD_COUNT -gt $i ]]; do

    printf "CREATE DATABASE IF NOT EXISTS %s_%s CHARACTER SET utf8 COLLATE utf8_general_ci;\n" $DB_NAME $i
    let i+=1
done