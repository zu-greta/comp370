Database Setup:

1. login to AWS management console and go to the EC2/lightsail dashboard, launch an instance
2. >>> ssh -i ~/.ssh/rsa user_name@ipaddress
3. >>> sudo apt udpate >>> sudo apt install -y mariadb-server
4. >>>sudo systemctl start mariadb >>>sudo systemctl enable mariadb
5. >>>sudo nano /etc/myswl/mariadb.conf.d/50-server.cnf ([myswld] port=6002)
6. >>>sudo systemctl restart mariadb
7. >>>sudo mysql -u root (CREATE DATABASE comp370_test; CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s'; GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%'; FLUSH PRIVILEGES; EXIT;)
8. AWS console, edit inbound rules, security group, inbound rules, edit inbound rules, add new rule, type custom TCP Rule, port range 6002, source custum or anywhere (0.0.0.0/0), save
9. test the connection: install DBeaver on PC, host <IPaddress>, port 6002, database comp370_test, user comp370, password $ungl@ss3s. connect to db and verify access