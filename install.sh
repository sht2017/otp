apt update
apt dist-upgrade -y
apt install libsodium-dev nginx python3 python3-pip screen -y
pip install pyotp pyqrcode
systemctl start rc-local
systemctl enable rc-local
mkdir /etc/otp
wget -O /etc/otp/otp.py https://raw.githubusercontent.com/sht2017/otp/main/otp.py
chmod +x /etc/otp/otp.py
wget -O /etc/otp/setup.py https://raw.githubusercontent.com/sht2017/otp/main/setup.py
chmod +x /etc/otp/setup.py
echo "screen -dmS otp-service /etc/otp/otp.py" >> /etc/rc.local
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubiBackup/doubi/master/ssr.sh && chmod +x ssr.sh && bash ssr.sh
/etc/otp/setup.py
cat /root/.otp/.qrcode
read -p "Press any key to reboot, [Ctrl+C] reboot later"
reboot
