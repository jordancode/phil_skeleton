DROP TABLE IF EXISTS `auth`;
CREATE TABLE IF NOT EXISTS `auth`(
	`id` BIGINT(20) UNSIGNED NOT NULL,
	`user_id`  BIGINT(20) UNSIGNED NOT NULL,
	`provider_id`  VARCHAR(50) NOT NULL,
	`secret` VARCHAR(255) NOT NULL,
	`provider_type` SMALLINT(3) UNSIGNED NOT NULL,
	`created_ts` DATETIME NOT NULL,
	`deleted` TINYINT(1) UNSIGNED NOT NULL DEFAULT 0,
	PRIMARY KEY( `id` ),
	UNIQUE KEY `provider_id.provider_type`(`provider_id`, `provider_type` )
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='maps authentication credentials to user_id';
