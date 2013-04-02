#! /bin/bash
# Author: Ryan Faulkner
# Date: 2013-04-01

#    LICENSE
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    DESCRIPTION
#
#    Use a virtualenv to execute client script for Wikimedia User Metrics API.
#    Once the call to "call_client" is complete the result is written to
#    the "json" folder of the umapi_client working folder.

VIRTUAL_ENV_HOME="/home/user/venv"
cd $VIRTUAL_ENV_HOME
source bin/activate

DATE_END=$(date "+%Y%m%d")
DATE_START=$(date --date '1 day ago' "+%Y%m%d")
UMAPI_TIMEOUT=14400
UMAPI_INTERVAL=1
UMAPI_URL=$(printf "cohorts/all/threshold?time_series&interval=%d&start=%s&end=%s&aggregator=average&group=input&refresh" \
$UMAPI_INTERVAL $DATE_START $DATE_END)

/home/rfaulk/umapi_client/umapi_client/scripts/call_client $UMAPI_URL -s -t $UMAPI_TIMEOUT