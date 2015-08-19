DROP TABLE IF EXISTS `user_agents`;
CREATE TABLE IF NOT EXISTS `user_agents`(
	`id` BIGINT(20) UNSIGNED NOT NULL,
	`user_agent_hash`  BINARY(16) NOT NULL,
	`user_agent_string`  BLOB NOT NULL,
	`created_ts` DATETIME NOT NULL,
	PRIMARY KEY( `id` ),
	UNIQUE KEY( `user_agent_hash` )
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='represents a unique user agent';
