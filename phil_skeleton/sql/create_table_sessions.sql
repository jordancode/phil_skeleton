DROP TABLE IF EXISTS `sessions`;
CREATE TABLE IF NOT EXISTS `sessions`(
	`id` BIGINT(20) UNSIGNED NOT NULL,
	`user_id`  BIGINT(20) UNSIGNED NOT NULL,
	`user_agent_id`  BIGINT(20) NOT NULL,
	`auth_id` BIGINT(20) UNSIGNED NOT NULL,
	`created_ts` DATETIME NOT NULL,
	`modified_ts` DATETIME NOT NULL,
	`log_out_ts` DATETIME DEFAULT NULL,
	`last_location_id` BIGINT(20) UNSIGNED DEFAULT NULL,
	`flags` BIGINT(20) UNSIGNED DEFAULT NULL,
	`token` CHAR(20) NOT NULL,
	PRIMARY KEY( `id` ),
	KEY `user_id.logged_out_ts`(`user_id`,`log_out_ts`),
	KEY `user_id.auth_id`(`user_id`,`auth_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='represents a user session';
