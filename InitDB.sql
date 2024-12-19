SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_adcarousel
-- ----------------------------
DROP TABLE IF EXISTS `t_adcarousel`;
CREATE TABLE `t_adcarousel`  (
  `id` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '轮播唯一编号',
  `isSelected` smallint NULL DEFAULT NULL COMMENT '是否参与轮播',
  `showTimeout` int NULL DEFAULT NULL COMMENT '配置显示多少秒',
  `fontColor` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '' COMMENT '文字颜色',
  `fontSize` smallint NULL DEFAULT NULL COMMENT '文字尺寸',
  `fontPosition` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '' COMMENT '文字位置',
  `picPath` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '轮播图片地址',
  `orderKey` int NULL DEFAULT NULL COMMENT '轮播顺序号',
  `createBy` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '创建人',
  `createAt` datetime NULL DEFAULT NULL COMMENT '创建日期',
  `updateBy` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '更新人',
  `updateAt` datetime NULL DEFAULT NULL COMMENT '更新日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
