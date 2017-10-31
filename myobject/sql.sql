/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.6.23-log : Database - myweb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`myweb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `myweb`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-07-24 19:26:02.134081'),(2,'auth','0001_initial','2017-07-24 19:26:04.167708'),(3,'admin','0001_initial','2017-07-24 19:26:04.600712'),(4,'admin','0002_logentry_remove_auto_add','2017-07-24 19:26:04.629508'),(5,'contenttypes','0002_remove_content_type_name','2017-07-24 19:26:05.251072'),(6,'auth','0002_alter_permission_name_max_length','2017-07-24 19:26:05.307630'),(7,'auth','0003_alter_user_email_max_length','2017-07-24 19:26:05.633139'),(8,'auth','0004_alter_user_username_opts','2017-07-24 19:26:05.666194'),(9,'auth','0005_alter_user_last_login_null','2017-07-24 19:26:06.021267'),(10,'auth','0006_require_contenttypes_0002','2017-07-24 19:26:06.035199'),(11,'auth','0007_alter_validators_add_error_messages','2017-07-24 19:26:06.075598'),(12,'auth','0008_alter_user_username_max_length','2017-07-24 19:26:06.207830'),(13,'sessions','0001_initial','2017-07-24 19:26:06.272178');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('9t4a5ec259mih6ijevo0as0rrahyn9we','NTQxMDNmMWVkNTAyMTcyMGQ1MTgxMzM1ZjgxZGNkMTBhMmI4NzM3NDp7InZlcmlmeWNvZGUiOiJEODBWIiwic2hvcGxpc3QiOnsiMTciOnsiaWQiOjE3LCJnb29kcyI6Ilx1NzI3OVx1NGVkMVx1ODJjZiIsInBpY25hbWUiOiIxNTAxNTY0NDg2LjA4NDcxOC5qcGciLCJwcmljZSI6ODUuMCwic3RvcmUiOjczLCJtIjoxfSwiMTUiOnsiaWQiOjE1LCJnb29kcyI6Ilx1NmQ3N1x1ODJkNCIsInBpY25hbWUiOiIxNTAxNTUzODk3LjM0ODg3MTcuanBnIiwicHJpY2UiOjE2LjAsInN0b3JlIjo1OCwibSI6Mn0sIjIiOnsiaWQiOjIsImdvb2RzIjoiXHU4MmY5XHU2NzljXHU2MjRiXHU2NzNhIiwicGljbmFtZSI6IjE1MDE1NTA4MTMuMzMxOTY2Mi5qcGciLCJwcmljZSI6NTYwMC4wLCJzdG9yZSI6MTI1NCwibSI6MX19LCJvcmRlcmxpc3QiOnsiMTciOnsiaWQiOjE3LCJnb29kcyI6Ilx1NzI3OVx1NGVkMVx1ODJjZiIsInBpY25hbWUiOiIxNTAxNTY0NDg2LjA4NDcxOC5qcGciLCJwcmljZSI6ODUuMCwic3RvcmUiOjczLCJtIjoxfSwiMTUiOnsiaWQiOjE1LCJnb29kcyI6Ilx1NmQ3N1x1ODJkNCIsInBpY25hbWUiOiIxNTAxNTUzODk3LjM0ODg3MTcuanBnIiwicHJpY2UiOjE2LjAsInN0b3JlIjo1OCwibSI6Mn0sIjIiOnsiaWQiOjIsImdvb2RzIjoiXHU4MmY5XHU2NzljXHU2MjRiXHU2NzNhIiwicGljbmFtZSI6IjE1MDE1NTA4MTMuMzMxOTY2Mi5qcGciLCJwcmljZSI6NTYwMC4wLCJzdG9yZSI6MTI1NCwibSI6MX19LCJ0b3RhbCI6NTcxNy4wLCJhZG1pbnVzZXIiOiJ6aG91IiwidmlwdXNlciI6eyJpZCI6OCwidXNlcm5hbWUiOiJhZG1pbiIsIm5hbWUiOiJ6aG91Iiwic2V4IjoxLCJhZGRyZXNzIjoiXHU1MzE3XHU0ZWFjXHU1ZTAyIiwiY29kZSI6IjAwMDAwIiwicGhvbmUiOiIxMTkiLCJlbWFpbCI6ImFiY0BxcS5jb20iLCJhZGR0aW1lIjoxNTAwOTMzMzEzfX0=','2017-08-21 04:25:07.149823'),('ald8qbv8thdi9jnqgtztmja30jz4sjfz','MWM0NWMwZDlmMTY4YmMxZTMzM2QxZWUyYmVlNWJhODU1NmM0YTU5Mjp7InZlcmlmeWNvZGUiOiJMUzRBIiwiYWRtaW51c2VyIjoiemhvdSJ9','2017-08-13 10:15:41.011700'),('alqwzfyc013p7cnmvwkrp8vb1jxui9o1','MDgxOWM5ZmU3ZDcwZTc1ZWVjYTE0MDYyMmQ3YTk2MjM3MmU3NzRlMTp7InZlcmlmeWNvZGUiOiJPV05BIiwidmlwdXNlciI6eyJpZCI6OCwibmFtZSI6Inpob3UifSwic2hvcGxpc3QiOnsiNSI6eyJpZCI6NSwiZ29vZHMiOiJcdTUzNGVcdTc4NTVcdTdiMTRcdThiYjBcdTY3MmNcdTc1MzVcdTgxMTEiLCJwaWNuYW1lIjoiMTUwMTU1MTE0MC4yNTY3MDY1LmpwZyIsInByaWNlIjo1NjAwLjAsInN0b3JlIjo1NjAsIm0iOjF9fSwib3JkZXJsaXN0Ijp7IjUiOnsiaWQiOjUsImdvb2RzIjoiXHU1MzRlXHU3ODU1XHU3YjE0XHU4YmIwXHU2NzJjXHU3NTM1XHU4MTExIiwicGljbmFtZSI6IjE1MDE1NTExNDAuMjU2NzA2NS5qcGciLCJwcmljZSI6NTYwMC4wLCJzdG9yZSI6NTYwLCJtIjoxfX0sInRvdGFsIjo1NjAwLjB9','2017-08-20 16:38:10.944434'),('n0ytyyswbemo8gcrsnwfsq3zqyye8yg8','ZGM3ZmU4MTUwNzNkOTkxNjA1ZGU4YWY4M2ExYWMwMjE3OTQzYTdiYTp7InZlcmlmeWNvZGUiOiJYQ0VDIiwidmlwdXNlciI6eyJpZCI6OCwidXNlcm5hbWUiOiJhZG1pbiIsIm5hbWUiOiJ6aG91In0sInNob3BsaXN0Ijp7fSwib3JkZXJsaXN0Ijp7IjIiOnsiaWQiOjIsImdvb2RzIjoiXHU4MmY5XHU2NzljXHU2MjRiXHU2NzNhIiwicGljbmFtZSI6IjE1MDE1NTA4MTMuMzMxOTY2Mi5qcGciLCJwcmljZSI6NTYwMC4wLCJzdG9yZSI6MTI1NCwibSI6MX19LCJ0b3RhbCI6NTYwMC4wfQ==','2017-08-21 01:06:12.026229'),('x201v0tzn2ki054pbd91tdv5qre5hugx','NGU3YTQyYzg5MzVlNGE4ZDk4NTJiMjkyYmUzMjMzOTcyMjE4YTNmZDp7InZlcmlmeWNvZGUiOiIwMkhBIiwidmlwdXNlciI6eyJpZCI6OCwibmFtZSI6Inpob3UifSwic2hvcGxpc3QiOnsiMTEiOnsiaWQiOjExLCJnb29kcyI6Ilx1NTE5Y1x1NTkyYlx1NWM3MVx1NmNjOVx1NzdmZlx1NmNjOVx1NmMzNCIsInBpY25hbWUiOiIxNTAxNTUzNDYxLjkyNjI0My5qcGciLCJwcmljZSI6NDUuMCwic3RvcmUiOjEzOCwibSI6MX19LCJvcmRlcmxpc3QiOnsiMTEiOnsiaWQiOjExLCJnb29kcyI6Ilx1NTE5Y1x1NTkyYlx1NWM3MVx1NmNjOVx1NzdmZlx1NmNjOVx1NmMzNCIsInBpY25hbWUiOiIxNTAxNTUzNDYxLjkyNjI0My5qcGciLCJwcmljZSI6NDUuMCwic3RvcmUiOjEzOCwibSI6MX19LCJ0b3RhbCI6NDUuMH0=','2017-08-20 17:26:58.234496'),('xus8mktlu7m064j3awh3btevi0tcxxkl','NGFiMDlkY2VmMzZiZjBhYmIxZjcyMDRmODgwM2I2MDY5OTIwZDBiOTp7ImFkbWludXNlciI6Inpob3UifQ==','2017-08-07 22:50:55.702832');

/*Table structure for table `myweb_detail` */

DROP TABLE IF EXISTS `myweb_detail`;

CREATE TABLE `myweb_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` int(11) DEFAULT NULL,
  `goodsid` int(11) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `price` double(6,2) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_detail` */

insert  into `myweb_detail`(`id`,`orderid`,`goodsid`,`name`,`price`,`num`) values (1,1,13,'红牛',128.00,1),(2,2,12,'索尼电视',6888.00,1),(3,3,7,'韩版流行男装',326.00,2),(4,4,17,'特仑苏',85.00,2),(5,5,5,'华硕笔记本电脑',5600.00,1),(6,6,18,'亲嘴烧',5.00,1),(7,7,18,'亲嘴烧',5.00,1),(8,8,16,'哈尔滨啤酒',65.00,1),(9,9,16,'哈尔滨啤酒',65.00,1),(10,10,17,'特仑苏',85.00,1),(11,11,11,'农夫山泉矿泉水',45.00,1),(12,12,17,'特仑苏',85.00,1),(13,13,3,'苹果手机2',5400.00,1),(14,14,15,'海苔',16.00,1),(15,15,15,'海苔',16.00,1),(16,16,15,'海苔',16.00,1),(17,17,17,'特仑苏',85.00,1),(18,17,15,'海苔',16.00,2),(19,17,2,'苹果手机',5600.00,1);

/*Table structure for table `myweb_goods` */

DROP TABLE IF EXISTS `myweb_goods`;

CREATE TABLE `myweb_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) DEFAULT NULL,
  `goods` varchar(32) DEFAULT NULL,
  `company` varchar(50) DEFAULT NULL,
  `descr` text,
  `price` double(6,2) DEFAULT NULL,
  `picname` varchar(255) DEFAULT NULL,
  `state` tinyint(1) DEFAULT '1',
  `store` int(11) DEFAULT '0',
  `num` int(11) DEFAULT '0',
  `clicknum` int(11) DEFAULT '0',
  `addtime` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_goods` */

insert  into `myweb_goods`(`id`,`typeid`,`goods`,`company`,`descr`,`price`,`picname`,`state`,`store`,`num`,`clicknum`,`addtime`) values (1,4,'华硕笔记本电脑','华硕',' 性价高，质量好。',4800.00,'1501550183.597974.jpg',1,3219,0,0,1501550183),(2,5,'苹果手机','苹果',' 耐用',5600.00,'1501550813.3319662.jpg',1,1254,0,3,1501550813),(3,5,'苹果手机2','苹果',' 好',5400.00,'1501550882.9414492.jpg',1,1982,0,1,1501550882),(4,4,'苹果笔记本电脑','苹果',' 实用性强',9800.00,'1501551058.8783495.jpg',1,3210,0,0,1501551058),(5,4,'华硕笔记本电脑','华硕',' 好用',5600.00,'1501551140.2567065.jpg',1,560,0,1,1501551140),(6,6,'索尼电视','索尼',' 每家必备',5800.00,'1501551213.374813.jpg',1,1524,0,0,1501551213),(7,7,'韩版流行男装','美特斯邦威',' 高端',326.00,'1501553036.6479585.jpg',1,78,0,1,1501552763),(8,8,'流行连衣裙','森马','漂亮 ',568.00,'1501553121.759795.jpg',1,74,0,0,1501553121),(9,8,'个性连衣裙','森马',' 漂亮，大方',168.00,'1501553264.89567.jpg',1,58,0,0,1501553264),(10,7,'商务T恤','海澜之家',' 舒适，有档次',388.00,'1501553368.8244774.jpg',1,158,0,0,1501553368),(11,10,'农夫山泉矿泉水','农夫山泉',' 实惠',45.00,'1501553461.926243.jpg',1,138,0,4,1501553461),(12,6,'索尼电视','索尼',' 实用性强，外观漂亮',6888.00,'1501565893.1357534.jpg',1,126,0,1,1501553550),(13,10,'红牛','农夫山泉','激素饮料',128.00,'1501553653.2807727.jpg',1,68,0,3,1501553653),(14,9,'金鸽瓜子','洽洽',' 无聊时刻来一包',8.00,'1501553709.6356618.jpg',1,68,0,0,1501553709),(15,9,'海苔','波力',' 嘎嘎脆',16.00,'1501553897.3488717.jpg',1,58,0,1,1501553897),(16,10,'哈尔滨啤酒','哈尔滨',' 聚餐少不了。',65.00,'1501554395.2888558.jpg',1,136,0,1,1501554395),(17,10,'特仑苏','蒙牛',' 不是所有的牛奶都叫特仑苏。',85.00,'1501564486.084718.jpg',1,73,0,2,1501564486),(18,9,'亲嘴烧','卫龙',' 好吃的不得了',5.00,'1501564624.8669293.jpg',1,1634,0,2,1501564624);

/*Table structure for table `myweb_orders` */

DROP TABLE IF EXISTS `myweb_orders`;

CREATE TABLE `myweb_orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `linkman` varchar(32) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `addtime` int(11) DEFAULT NULL,
  `total` double(8,2) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_orders` */

insert  into `myweb_orders`(`id`,`uid`,`linkman`,`address`,`code`,`phone`,`addtime`,`total`,`status`) values (1,8,'zhou','wreaw','4543','524252',1502010971,128.00,2),(2,8,'zhou','rwew','4131','32121',1502023605,6888.00,1),(3,8,'zhou','243243','243','2424423',1502032166,652.00,0),(4,8,'zhou','fdfsd','12234','21434',1502034396,170.00,0),(5,8,'zhou','rttgtgr','4143','24323',1502037505,5600.00,0),(6,8,'zhou','wrew','2432','24324',1502038917,5.00,0),(7,8,'zhou','wrew','2432','24324',1502038993,5.00,0),(8,8,'zhou','gfds','2432','2432',1502039948,65.00,0),(9,8,'zhou','gfds','2432','2432',1502040085,65.00,0),(10,8,'zhou','fwd','2342','342',1502040261,85.00,0),(11,8,'zhou','DSWX','3434','23323',1502040418,45.00,0),(12,8,'zhou','fwd','2342','342',1502040562,85.00,0),(13,8,'zhou','sfds','232','4232',1502071946,5400.00,0),(14,8,'zhou','fsads','1321','412134',1502072591,16.00,0),(15,8,'zhou','fsads','1321','412134',1502072651,16.00,0),(16,8,'zhou','fsads','1321','412134',1502072692,16.00,0),(17,8,'zhou','北京市','00000','119',1502079907,5717.00,0);

/*Table structure for table `myweb_pic` */

DROP TABLE IF EXISTS `myweb_pic`;

CREATE TABLE `myweb_pic` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `picname` varchar(32) DEFAULT NULL,
  `addtime` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_pic` */

insert  into `myweb_pic`(`id`,`name`,`age`,`picname`,`addtime`) values (1,'a',11,'a8.png',1500821217);

/*Table structure for table `myweb_types` */

DROP TABLE IF EXISTS `myweb_types`;

CREATE TABLE `myweb_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `pid` int(11) DEFAULT '0',
  `path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_types` */

insert  into `myweb_types`(`id`,`name`,`pid`,`path`) values (1,'数码',0,'0,'),(2,'服装',0,'0,'),(3,'食品',0,'0,'),(4,'电脑',1,'0,1,'),(5,'手机',1,'0,1,'),(6,'电视',1,'0,1,'),(7,'男装',2,'0,2,'),(8,'女装',2,'0,2,'),(9,'零食',3,'0,3,'),(10,'饮料',3,'0,3,');

/*Table structure for table `myweb_users` */

DROP TABLE IF EXISTS `myweb_users`;

CREATE TABLE `myweb_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `name` varchar(16) DEFAULT NULL,
  `passwd` char(32) NOT NULL,
  `sex` tinyint(1) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `code` char(6) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `state` tinyint(1) DEFAULT '1',
  `addtime` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`,`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `myweb_users` */

insert  into `myweb_users`(`id`,`username`,`name`,`passwd`,`sex`,`address`,`code`,`phone`,`email`,`state`,`addtime`) values (8,'admin','zhou','e10adc3949ba59abbe56e057f20f883e',1,'北京市','00000','119','abc@qq.com',0,1500933313),(9,'1234567','哈哈哈','e10adc3949ba59abbe56e057f20f883e',1,'非洲','000050','1431541351','43153@126.com',1,1501993890);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
