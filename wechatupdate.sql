/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 80013
Source Host           : localhost:3306
Source Database       : mywechatupdate

Target Server Type    : MYSQL
Target Server Version : 80013
File Encoding         : 65001

Date: 2019-03-08 21:55:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for wechatupdate
-- ----------------------------
DROP TABLE IF EXISTS `wechatupdate`;
CREATE TABLE `wechatupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(200) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `username` varchar(25) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of wechatupdate
-- ----------------------------
INSERT INTO `wechatupdate` VALUES ('1', '我要飞的更高', 'static/img/201903/08/成绩单.jpg', '1234', '2019-03-08 13:41:22.979958');
INSERT INTO `wechatupdate` VALUES ('2', '我要飞的更高', 'static/img/201903/08/成绩单_dPxViKF.jpg', '1234', '2019-03-08 13:46:43.227275');
INSERT INTO `wechatupdate` VALUES ('3', '我要飞的更高', 'static/img/201903/08/成绩单_iKJtfY5.jpg', '1234', '2019-03-08 13:46:48.107554');
INSERT INTO `wechatupdate` VALUES ('4', '我要飞的更高', 'static/img/201903/08/成绩单_b0npmAf.jpg', '1234', '2019-03-08 13:46:50.614698');
INSERT INTO `wechatupdate` VALUES ('5', '我要飞的更高', 'static/img/201903/08/成绩单_5w9XNZ5.jpg', '1234', '2019-03-08 13:46:54.402915');
INSERT INTO `wechatupdate` VALUES ('6', '我要飞的更高', 'static/img/201903/08/成绩单_KQvw0er.jpg', '1234', '2019-03-08 13:46:57.801109');
