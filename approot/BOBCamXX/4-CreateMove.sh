#!/bin/bash
     
DATE=$(date +"%Y%m%d-%H%M%S")
YEAR="$(date "+%Y")"
MONTH="$(date "+%m")"
DAY="$(date "+%d")"

CREATED_DIR=$YEAR
if    [ ! -d "${CREATED_DIR}" ]; then
    mkdir -p "${CREATED_DIR}"
fi

CREATED_DIR=$YEAR/$MONTH
if    [ ! -d "${CREATED_DIR}" ]; then
    mkdir -p "${CREATED_DIR}"
fi

CREATED_DIR=$YEAR/$MONTH/$DAY
if    [ ! -d "${CREATED_DIR}" ]; then
    mkdir -p "${CREATED_DIR}"
fi
   
SOURCE_DIR="b-uploaded"
TARGET_DIR=$YEAR/$MONTH/$DAY
sudo mv $SOURCE_DIR/*.jpg  $TARGET_DIR
ls  $TARGET_DIR