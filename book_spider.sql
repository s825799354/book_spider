/*
Navicat MySQL Data Transfer

Source Server         : 1111
Source Server Version : 50553
Source Host           : localhost:3306
Source Database       : book_spider

Target Server Type    : MYSQL
Target Server Version : 50553
File Encoding         : 65001

Date: 2020-03-07 15:30:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for book_chapter
-- ----------------------------
DROP TABLE IF EXISTS `book_chapter`;
CREATE TABLE `book_chapter` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) unsigned NOT NULL COMMENT '对应书籍表的信息',
  `chapter_name` varchar(128) NOT NULL DEFAULT '' COMMENT '文章标题',
  `chapter_id` int(11) unsigned NOT NULL DEFAULT '0',
  `content` text NOT NULL COMMENT '文章内容',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=16939 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for book_info
-- ----------------------------
DROP TABLE IF EXISTS `book_info`;
CREATE TABLE `book_info` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cat` varchar(255) DEFAULT '' COMMENT '分类',
  `book_id` int(11) NOT NULL COMMENT '来源站的id方便抓取',
  `book_name` varchar(32) NOT NULL DEFAULT '' COMMENT '书籍名字',
  `author_id` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '作者ID',
  `last_update_time` int(11) NOT NULL DEFAULT '0' COMMENT '最后更新时间',
  `author_name` varchar(36) NOT NULL DEFAULT '' COMMENT '作者',
  `create_time` int(11) unsigned NOT NULL DEFAULT '0',
  `update_time` int(11) unsigned NOT NULL DEFAULT '0',
  `new_chapter` varchar(255) NOT NULL DEFAULT '' COMMENT '最新章节名称',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=855 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
