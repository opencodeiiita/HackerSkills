OPTION=$1

USER=username
PASS=password

HTTP_PROXY_HOST=172.31.1.4
HTTP_PROXY_PORT=8080

HTTPS_PROXY_HOST=172.31.1.4
HTTPS_PROXY_PORT=8080

APT_FILE=/etc/apt/apt.conf
ENVIRONMENT_FILE=/etc/environment

###### Backup file
function backup_file
{
	if [ -f "$1" ];
	then
		sudo sed -i.bak '/http[s]::proxy/Id' "$1"
	fi
}

function proxy_gnome
{
	gsettings set org.gnome.system.proxy mode manual
	gsettings set org.gnome.system.proxy.http host "$HTTP_PROXY_HOST"
	gsettings set org.gnome.system.proxy.http port "$HTTP_PROXY_PORT"
	gsettings set org.gnome.system.proxy.http authentication-user "$USER"
	gsettings set org.gnome.system.proxy.http authentication-password "$PASS"
	gsettings set org.gnome.system.proxy.https host "$HTTPS_PROXY_HOST"
	gsettings set org.gnome.system.proxy.https port "$HTTPS_PROXY_PORT"
	
}

function proxy_apt_file
{
	backup_file "$APT_FILE"
	sudo tee -a "$APT_FILE" \
<<EOF
Acquire::http::proxy "http://$USER:$PASS@$HTTP_PROXY_HOST:$HTTP_PROXY_PORT/";
Acquire::https::proxy "http://$USER:$PASS@$HTTPS_PROXY_HOST:$HTTPS_PROXY_PORT/";
EOF
}

function proxy_environment_file
{
	backup_file "$ENVIRONMENT_FILE"
	sudo tee -a "$ENVIRONMENT_FILE" \
<<EOF
http_proxy="http://$USER:$PASS@$HTTP_PROXY_HOST:$HTTP_PROXY_PORT/"
https_proxy="http://$USER:$PASS@$HTTPS_PROXY_HOST:$HTTPS_PROXY_PORT/"
EOF
}

function proxy_git
{
	git config --global http.proxy http://$USER:$PASS@$HTTP_PROXY_HOST:$HTTP_PROXY_PORT/
	git config --global https.proxy http://$USER:$PASS@$HTTPS_PROXY_HOST:$HTTPS_PROXY_PORT/
}

###### Proxy start
function proxy_start
{
	proxy_gnome
	proxy_apt_file
	proxy_environment_file
	proxy_git

	
}

###### Proxy stop
function proxy_stop
{
	gsettings set org.gnome.system.proxy mode none
	sudo sed -i -e '/Acquire::http::proxy/d' "$APT_FILE"
	sudo sed -i -e '/Acquire::https::proxy/d' "$APT_FILE"
	sudo sed -i -e '/http_proxy/d' "$ENVIRONMENT_FILE"
	sudo sed -i -e '/https_proxy/d' "$ENVIRONMENT_FILE"
	unset http_proxy
	unset https_proxy
	npm config delete http-proxy
	npm config delete https-proxy
	export http_proxy=
	export https_proxy=
	http_proxy=
	https_proxy=
	git config --global --unset http.proxy
	git config --global --unset https.proxy
}

###### Proxy switch case
function proxy
{
	case $OPTION in
		"start")
			echo "Setting proxy..."
			proxy_start
			echo "Done."
		;;
		"stop")
			echo "Unsetting proxy..."
			proxy_stop
			echo "Done."
		;;
		*)
			echo "Invalid option!"
			echo "Error."
		;;
	esac
}

# Main software
if [ -n "$OPTION" ];
then
	proxy
else
	echo 'Option is null'
	echo 'Error.'
fi
exit
