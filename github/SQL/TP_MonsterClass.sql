/*
 Navicat Premium Dump SQL

 Source Server         : Local
 Source Server Type    : SQL Server
 Source Server Version : 16001135 (16.00.1135)
 Source Host           : 127.0.0.1:1433
 Source Catalog        : FNLParm1602
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 16001135 (16.00.1135)
 File Encoding         : 65001

 Date: 19/12/2024 01:39:32
*/


-- ----------------------------
-- Table structure for TP_MonsterClass
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[TP_MonsterClass]') AND type IN ('U'))
	DROP TABLE [dbo].[TP_MonsterClass]
GO

CREATE TABLE [dbo].[TP_MonsterClass] (
  [MClass] int  NOT NULL,
  [MName] nvarchar(40) COLLATE Cyrillic_General_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[TP_MonsterClass] SET (LOCK_ESCALATION = TABLE)
GO

EXEC sp_addextendedproperty
'MS_Description', N'Классы монстров',
'SCHEMA', N'dbo',
'TABLE', N'TP_MonsterClass'
GO


-- ----------------------------
-- Records of TP_MonsterClass
-- ----------------------------
INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'1', N'A')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'3', N'C')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'4', N'D')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'5', N'E')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'6', N'F')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'7', N'G')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'8', N'H')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'9', N'I')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'10', N'J')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'11', N'K')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'12', N'L')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'13', N'M')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'14', N'N')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'15', N'O')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'16', N'P')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'17', N'Q')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'18', N'R')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'19', N'S')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'20', N'T')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'21', N'U')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'22', N'V')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'23', N'NPC')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'24', N'W')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'25', N'X')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'26', N'Особый Монстр')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'27', N'Событие')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'28', N'Именной')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'29', N'Босс')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'31', N'S')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'32', N'Налетчики')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'2', N'B')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'38', N'Падшие Боссы')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'37', N'Разьяренные Боссы')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'36', N'Последователи (ХТЖ Боссы)')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'35', N'Статуя')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'34', N'Эпик Боссы (дем)')
GO

INSERT INTO [dbo].[TP_MonsterClass] ([MClass], [MName]) VALUES (N'33', N'Эпик Мобы (дем)')
GO

