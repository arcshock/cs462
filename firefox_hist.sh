#!/bin/bash
#Authors: Brahm Lower, Bucky Frost
#Purpose: Extract Firefox URL history from sqlite databases


readonly PROGNAME=$(basename @0)
readonly PROGDIR=$(readlink -m $(dirname $0))
readonly ARGS="$@"

read -d DB_QUERY <<EOF
'SELECT datetime(moz_historyvisits.visit_date/1000000,"unixepoch"), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;'
EOF

main() {
	HOME_DIRS=$(cat /etc/passwd | awk -F: '{print $6}')

	for DIR in $HOME_DIRS
	do
		PROFILE=${DIR}"/.mozilla/firefox/profiles.ini"
		FIREFOX_PROFILE=${DIR}"/.mozilla/firefox/"	
		if [ -f $PROFILE ]
		then
			cd $FIREFOX_PROFILE$(grep -i path $PROFILE | awk -F= '{print $2}')
			TEST=$FIREFOX_PROFILE$(grep -i path $PROFILE | awk -F= '{print $2}')
			echo $TEST'/places.sqlite'
			#echo $(sqlite3 $TEST'places.sqlite' $DB_QUERY)
			echo "$(sqlite3 $TEST'/places.sqlite' 'SELECT datetime(moz_historyvisits.visit_date/1000000,"unixepoch"), moz_places.url FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;')"
		fi
	done

}

main
