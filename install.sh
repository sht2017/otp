apt update
apt upgrade
apt dist-upgrade -y
apt install libsodium-dev nginx python3 python3-pip screen -y
pip install pyotp
systemctl start rc-local
systemctl enable rc-local
mkdir /etc/otp
wget -O /etc/otp/otp.py https://raw.githubusercontent.com/sht2017/otp/main/otp.py
chmod +x /etc/otp/otp.py
echo "screen -dmS otp-service /etc/otp/otp.py" >> /etc/rc.local
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubiBackup/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
reboot
