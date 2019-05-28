-- Adminer 4.1.0 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `student_phone` varchar(45) NOT NULL,
  `server_id` varchar(45) NOT NULL,
  `order_id` varchar(45) DEFAULT NULL,
  `order_money` varchar(45) DEFAULT NULL,
  `order_way` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`student_phone`,`server_id`),
  KEY `server_id` (`server_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `courier`;
CREATE TABLE `courier` (
  `courier_id` varchar(45) NOT NULL,
  `courier_name` varchar(45) NOT NULL,
  `courier_phone` varchar(45) DEFAULT NULL,
  `foodshop_shop_name` varchar(45) NOT NULL,
  PRIMARY KEY (`courier_id`),
  KEY `foodshop_shop_name` (`foodshop_shop_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `delivery`;
CREATE TABLE `delivery` (
  `student_phone` varchar(45) NOT NULL,
  `courier_id` varchar(45) NOT NULL,
  `delivery_time` varchar(45) NOT NULL,
  PRIMARY KEY (`student_phone`,`courier_id`),
  KEY `courier_id` (`courier_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `foodshop`;
CREATE TABLE `foodshop` (
  `shop_name` varchar(45) NOT NULL,
  `salenum` varchar(45) NOT NULL,
  KEY `shop_name` (`shop_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

INSERT INTO `foodshop` (`shop_name`, `salenum`) VALUES
('菜肉包',	'100');

DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
  `server_id` varchar(45) NOT NULL,
  `server_name` varchar(45) NOT NULL,
  `foodshop_shop_name` varchar(45) NOT NULL,
  PRIMARY KEY (`server_id`),
  KEY `foodshop_shop_name` (`foodshop_shop_name`),
  KEY `foodshop_shop_name_2` (`foodshop_shop_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `student_phone` varchar(45) NOT NULL,
  `student_name` varchar(45) NOT NULL,
  `studen_dorm` varchar(45) NOT NULL,
  PRIMARY KEY (`student_phone`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- 2019-05-28 13:15:10
