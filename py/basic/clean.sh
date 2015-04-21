SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

rm "$SCRIPT_DIR"/.Python
rm "$SCRIPT_DIR"/pip-selfcheck.json
rm -rf "$SCRIPT_DIR"/bin
rm -rf "$SCRIPT_DIR"/include
rm -rf "$SCRIPT_DIR"/lib
rm -rf "$SCRIPT_DIR"/*.egg-info
