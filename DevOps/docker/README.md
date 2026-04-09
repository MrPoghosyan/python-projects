# 🐳 Docker Practice (Storage, Compose & Final Tasks)

This repository contains all completed Docker tasks divided into 3 main sections:

* 📦 Storage & Volumes
* 🧩 Docker Compose
* 🚀 Final Tasks

---

# 📦 1. Storage & Volumes

After completing all tasks:

```bash
checkup-storage
```

---

## Task 1 – Bind Mount

* Run container from `alpine:3.17` in detached mode
* Mount:

```
/opt/docker/storage/task1 → /home
```

* Create files:

```
myfile1 → Hello world!
myfile2 → Hello from EPAM!
```

* Verify files exist on host
* Delete `myfile1` → verify inside container
* Check volumes:

```bash
docker volume ls
```

**Secret:**

```
iehohs8koonaYi
```

---

## Task 2 – PostgreSQL Auto Volume

* Run:

```
postgres:15.1 (name: mypostgres)
POSTGRES_PASSWORD=mysecretpassword
```

* Find volume:

```bash
docker inspect
docker volume ls
docker volume inspect
```

* Share volume:

```
--volumes-from mypostgres
```

* Check:

```
/var/lib/postgresql/data/
```

**Secret:**

```
jaaSheiD2ZahGa
```

---

## Task 3 – Named Volume

```bash
docker volume create my_volume
```

* Run postgres (`mypostgres2`)
* Mount to:

```
/var/lib/postgresql/data
```

* Inspect mountpoint
* Share volume with another container

**Secret:**

```
ohth7Goo3bahv1
```

---

## Task 4 – tmpfs vs Bind

* Container: `nginx:1.23`

Mounts:

```
tmpfs → /my_folder1
bind → /tmp:/my_folder2
```

* Compare:

```bash
docker inspect
```

* Speed test:

```bash
dd if=/dev/zero of=/my_folder1/speed_file bs=512M count=1
dd if=/dev/zero of=/my_folder2/speed_file bs=512M count=1
```

* Save results → `result`

* Create:

```
/my_folder1/my_file1
/my_folder2/my_file2
```

* Remove container → check `/tmp/my_file2`

**Secret:**

```
VohsheK9puFai7
```

---

## Task 5 – Backup & Restore

### Backup

```bash
tar cvf /backup/backup.tar /etc/nginx
```

Check:

```
/opt/docker/storage/task5/backup.tar
```

### Restore

```bash
tar xvf /backup/backup.tar --strip 2 -C /etc/nginx
```

**Secret:**

```
ieci2wuKo6koqu
```

---

## Task 6 – Sidecar Pattern

```bash
docker volume create sidecar_volume
```

### Producer

```bash
while sleep 5; do echo "Hello from EPAM!" >> /home/logs; done
```

### Consumer

```bash
tail -f /opt/logs
```

**Secret:**

```
yah9meejahw4Pu
```

---

# 🧩 2. Docker Compose

Work directory:

```
/opt/docker/dockercompose
```

Check:

```bash
checkup-compose
```

---

## Setup

* Services:

  * phpMyAdmin (frontend)
  * MariaDB (mydb)

* Custom network:

```
dockercompose-frontend
```

* Port:

```
8080 → 80
```

* Healthcheck:

```bash
mysqladmin ping
```

---

## Database

```sql
create database mydb;

use mydb;

create table mytable (
  id int AUTO_INCREMENT primary key,
  data text,
  datamodified timestamp default now()
);

insert into mytable(data) values("testdata01");
insert into mytable(data) values("testdata02");
insert into mytable(data) values("testdata03");
```

---

## Dump

```
/opt/docker/dockercompose/task-13/mydb.sql
```

---

## Secrets

```
Task 1: hoh9leeMahCh1o
Task 2: Ahligievie2ahc
Task 3: ux6ahl8aht4OK2
Task 4: Igho5veh9Hifee
Task 5: shae7laeCh9eid
Task 6-7: ohh6iefu0Bupei
Task 8: Chio8eevaiGei4
Task 9: ahngohv3cuo6Ce
Task 10: ahNiteech4phee
Task 11: shuraiMi1eimoo
Task 13: uneishai1hahGe
```

---

# 🚀 3. Final Tasks

---

## Sub-task 1 – Wordpress + MySQL

* Containers:

  * my-awesome-wordpress
  * my-awesome-database

* Features:

  * Custom Dockerfile
  * wp-config.php config
  * Network:

```
my-awesome-network
```

* Port:

```
8080
```

* Volumes:

```
mysql
wordpress
```

**Secret:**

```
yiepoWeexoo0ge
```

---

## Sub-task 2 – Petclinic Fix

* Fix broken environment
* Ensure:

  * App works on 8080
  * DB connection works
  * Healthcheck OK
  * CRUD works

**Secret:**

```
ohtoocojah4Pha
```

---

# 📌 Summary

This project demonstrates:

* Docker volumes (bind, named, tmpfs)
* Data persistence
* Backup & restore
* Sidecar pattern
* Docker Compose
* Multi-container architecture

---

# 👨‍💻 Author

Vahagn Poghosyan
Linux | Docker | DevOps | Python | C++
