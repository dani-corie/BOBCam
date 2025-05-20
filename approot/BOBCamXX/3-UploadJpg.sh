#!/bin/bash
        
#NextCloud Uni-Bremen        TestUpload
#https://nc.uni-bremen.de/index.php/s/2wLtaTHjS7WqMRt?path=%2FTestUpload
KAMERA="BOBCamXX" 
NC_PASSWORD="GDtotEMKZq"
SHARE="kjSo6p2Mdw4YGty"
LINK="https://nc.uni-bremen.de/public.php/dav/FILES"

# NextCloud Uni-Bremen     
# https://nc.uni-bremen.de/index.php/s/nejNiskggRg6djQ?path=%2FBOBCam10
KAMERA="BOBCam10"
NC_PASSWORD="6K9JGYxpFX"
SHARE="78DeHfgg9JrYg2D"
LINK="https://nc.uni-bremen.de/public.php/dav/FILES"

RECORDED_DIR="a-recorded"
UPLOADED_DIR="b-uploaded"
LOG_DIR="c-logs"


LOG_FILE="${LOG_DIR}"/"upload.log"

log() {
    echo "$(date "+[%d.%m.%Y %H:%M:%S%z] ")" "$@" | tee -a "${LOG_FILE}"
}
log_line() {
    log "---------------------------------"
}

if [[ -z "${NC_PASSWORD}" ]]; then
    log "password is undefined"
    exit 2
fi

if [[ -z "${SHARE}" ]]; then
    log "share is undefined"
    exit 2
fi
if [[ -z "${LINK}" ]]; then
    log "link is undefined"
    exit 2
fi

if [[ ! -d "${UPLOADED_DIR}" ]]; then
    mkdir -p "${UPLOADED_DIR}"
fi

log_line
log "start upload"

upload() {
    log "start upload of" "$1"
    BFILE=$(basename "$1")
    RESPONSE=$(curl -o /dev/null -s \
                    -w "%{response_code}" \
                    -X PUT -H 'X-Requested-With: XMLHttpRequest' \
                    -u "${SHARE}":"${NC_PASSWORD}" \
                    -T "${FILE}" \
                    --limit-rate 500K \
                    --expect100-timeout 30 \
                    --retry 5 \
                    --retry-all-errors \
                    "${LINK}/${SHARE}/${BFILE}")
    log "RESPONSE" "${RESPONSE}"
    if [ "${RESPONSE}" -eq "201" ]; then
        log "      upload of" "${BFILE}" "was successful."
        mv "${FILE}" "${UPLOADED_DIR}"/
    else
        log "upload of" "$1" "failed"
    fi
}

for FILE in "${RECORDED_DIR}"/*.jpg; do
    upload "${FILE}"
done
