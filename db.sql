-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'users'
-- 用户表
-- ---

DROP TABLE IF EXISTS `users`;
		
CREATE TABLE `users` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `nickname` VARCHAR(64) NULL DEFAULT NULL COMMENT '名称',
  `email` VARCHAR(120) NULL DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`)
) COMMENT '用户表';

-- ---
-- Table 'posts'
-- 文章
-- ---

DROP TABLE IF EXISTS `posts`;
		
CREATE TABLE `posts` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `body` MEDIUMTEXT NULL DEFAULT NULL COMMENT '内容',
  `timestamp` DATETIME NULL DEFAULT NULL COMMENT '发布时间',
  `user_id` INTEGER NULL DEFAULT NULL COMMENT '用户id',
  PRIMARY KEY (`id`)
) COMMENT '文章';

-- ---
-- Table 'followers'
-- 用户关注关系表
-- ---

DROP TABLE IF EXISTS `followers`;
		
CREATE TABLE `followers` (
  `follower_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL COMMENT '关注者',
  `followed_id` INTEGER NULL DEFAULT NULL COMMENT '被关注者',
  PRIMARY KEY (`follower_id`)
) COMMENT '用户关注关系表';

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `posts` ADD FOREIGN KEY (user_id) REFERENCES `users` (`id`);
ALTER TABLE `followers` ADD FOREIGN KEY (follower_id) REFERENCES `users` (`id`);
ALTER TABLE `followers` ADD FOREIGN KEY (followed_id) REFERENCES `users` (`id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `users` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `posts` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `followers` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `users` (`id`,`nickname`,`email`) VALUES
-- ('','','');
-- INSERT INTO `posts` (`id`,`body`,`timestamp`,`user_id`) VALUES
-- ('','','','');
-- INSERT INTO `followers` (`follower_id`,`followed_id`) VALUES
-- ('','');
