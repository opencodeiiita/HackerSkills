


$ env | grep -i proxy


$ export http_proxy="http://172.31.1.4:8080"
$ export https_proxy="https://172.31.1.4:8080"
$ export ftp_proxy="http://172.31.1.4:8080"


function setproxy() {
    export {http,https,ftp}_proxy="http://PROXY_SERVER:PORT"
}


state=$(gsettings get org.gnome.system.proxy mode)

if [ $state == "'none'" ]; then
        gsettings set org.gnome.system.proxy mode 'manual'
elif [ $state == "'manual'" ]; then
        gsettings set org.gnome.system.proxy mode 'none'
fi