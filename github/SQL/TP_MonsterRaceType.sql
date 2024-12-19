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

 Date: 19/12/2024 01:40:01
*/


-- ----------------------------
-- Table structure for TP_MonsterRaceType
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[TP_MonsterRaceType]') AND type IN ('U'))
	DROP TABLE [dbo].[TP_MonsterRaceType]
GO

CREATE TABLE [dbo].[TP_MonsterRaceType] (
  [MRaceType] int  NULL,
  [mDescFieldW] nvarchar(20) COLLATE Cyrillic_General_CI_AS  NULL,
  [mDesc] nvarchar(35) COLLATE Cyrillic_General_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[TP_MonsterRaceType] SET (LOCK_ESCALATION = TABLE)
GO

EXEC sp_addextendedproperty
'MS_Description', N'DT_Monster --> MRaceType',
'SCHEMA', N'dbo',
'TABLE', N'TP_MonsterRaceType'
GO


-- ----------------------------
-- Records of TP_MonsterRaceType
-- ----------------------------
INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'1', N'eRaceTypeUndead', N'Нежить (Undead)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'2', N'eRaceTypeDragon', N'Дракон (Dragon)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'3', N'eRaceTypeAnimal', N'Животное (Animal)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'4', N'eRaceTypeBug', N'Насекомое (Bug)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'5', N'eRaceTypeMachine', N'Машина (Machine)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'6', N'eRaceTypeHuman', N'Человек (Human)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'7', N'eRaceTypeElf', N'Эльф (Elf)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'8', N'eRaceTypeEtc', N'Прочие (Etc)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'9', N'eRaceTypeDaemon', N'Демон (Daemon)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'10', N'eRaceTypeAngel', N'Ангел (Angel)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'11', N'eRaceTypeDevil', N'Дьявол (Devil)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'12', N'eRaceTypeFullMoon', N'Оборотень (Full Moon)')
GO

INSERT INTO [dbo].[TP_MonsterRaceType] ([MRaceType], [mDescFieldW], [mDesc]) VALUES (N'13', N'eRaceTypeAllNonHuman', N'Все, кроме человека (All Non-Human)')
GO

