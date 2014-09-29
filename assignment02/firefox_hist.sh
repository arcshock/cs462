#!/bin/bash
#Authors: Brahm Lower, Bucky Frost
#Purpose: Extract Firefox URL history from sqlite databases


readonly PROGNAME=$(basename @0)
readonly PROGDIR=$(readlink -m $(dirname $0))
readonly ARGS="$@"

# Some reason this is failing...
read -d '' DB_QUERY <<EOF
'SELECT datetime(moz_historyvisits.visit_date/1000000,"unixepoch"), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;'
EOF

main() {
	HOME_DIRS=$(cat /etc/passwd | awk -F: '{print $6}')

	for DIR in $HOME_DIRS
	do
		FIREFOX_DIR=${DIR}"/.mozilla/firefox/"	
		FIREFOX_PROFILE=${FIREFOX_DIR}"/profiles.ini"
		if [ -f $FIREFOX_PROFILE ]
		then
			CONFIG=$FIREFOX_DIR$(grep -i path $FIREFOX_PROFILE | awk -F= '{print $2}')
			cd $CONFIG
			DB=$CONFIG'/places.sqlite'
			sqlite3 $DB 'SELECT datetime(moz_historyvisits.visit_date/1000000,"unixepoch"), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id ORDER by visit_date;'
		fi
	done

}

main
