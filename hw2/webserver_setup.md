Webserver Setup:

1. login to AWS management console and go to the EC2/lightsail dashboard, launch an instance
2. >>> ssh -i ~/.ssh/rsa user_name@ipaddress
3. install Apache >>>sudo apt update >>>sudo apt install -y apache2
4. configure apache to port 8008 >>>sudo nano /etc/apache2/ports.conf (Listen 8008)
5. >>>sudo nano /etc/apache2/sites-available/000-default.conf (<VirtualHost *:8008> DocumentRoot /var/www/html> AllowOverride All Require all granted </Directory> </VirtualHost>
6. >>> echo "comp370_hw2.txt: Hello World!" | sudo tee /var/www/html/comp370_hw2.txt
7. >>>sudo chmod 644 /var/www/html/comp370_hw2.txt
8. on AWS console, Security group, inbound rules, edit inbound rules, add new rule, Custum TCP Rule, Port range 8008, source custum or anywhere (0.0.0.0/0), save
9. >>>sudo systemctl start apache2 >>>sudo systemctl enable apache2
10.open a web browser, httph://<publicIP>:8008/comp370_hw2.txt
