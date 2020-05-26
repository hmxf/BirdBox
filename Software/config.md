# Configuration

## 1.Python Configuration

### Delete python2.7

```bash
sudo apt autoremove python2.7 -y
```

### set python3.7 to default

```bash
sudo ln -s /usr/bin/python3.7 /usr/bin/python
sudo ln -s /usr/bin/pip3 /usr/bin/pip
```

## 2.Database Configuration

### install mysql

```bash
sudo apt install mariadb-server
```

### boot

```bash
systemctl enable mariadb
```

You need to type passward here.
