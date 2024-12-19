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

 Date: 19/12/2024 01:40:18
*/


-- ----------------------------
-- Table structure for DT_MonsterLocation
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[DT_MonsterLocation]') AND type IN ('U'))
	DROP TABLE [dbo].[DT_MonsterLocation]
GO

CREATE TABLE [dbo].[DT_MonsterLocation] (
  [MID] int  NOT NULL,
  [MName] varchar(255) COLLATE Cyrillic_General_CI_AS  NULL,
  [Location] varchar(255) COLLATE Cyrillic_General_CI_AS  NULL,
  [LocationLevel] varchar(255) COLLATE Cyrillic_General_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[DT_MonsterLocation] SET (LOCK_ESCALATION = TABLE)
GO

EXEC sp_addextendedproperty
'MS_Description', N'Локации монстров',
'SCHEMA', N'dbo',
'TABLE', N'DT_MonsterLocation'
GO


-- ----------------------------
-- Records of DT_MonsterLocation
-- ----------------------------
INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1634', N'Собиратель рун', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1633', N'Хранитель медной двери', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1635', N'Шаман созданий', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1636', N'Властитель континента', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1719', N'<Охотники На Метеоса>/nСоди', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2474', N'<Саотоник>/nНадгробный Камень', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1710', N'<Хранитель Земли>/nСтониан', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1638', N'Замаскированный наблюдатель', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1637', N'Рогатый надзиратель', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1639', N'Ядовитый вредитель', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1640', N'Хранитель сильного яда', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1711', N'<Хранитель Ветра>/nДарк Ремион', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1643', N'Синий дракон бездны', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1641', N'Хранитель водных врат', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1642', N'Четырехглазый страж', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1644', N'Завоеватель океана', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2475', N'<Осколки Заклинаний>/nИллион', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1713', N'<Хранитель Солнца>/nГохан', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'399', N'Огненный скелет', N'Башня Огня', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'124', N'Скелет-разрушитель', N'Башня Огня', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'87', N'Огненный жук', N'Башня Огня', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'107', N'Огненный упырь', N'Башня Огня', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Башня Огня - 2 ур. Вход', N'Башня Огня', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1457', N'<Исследователь Башни Огня>/nБанеш', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2134', N'Нуиян', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Башня Огня - 4 ур. Вход', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'855', N'Лилит', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'401', N'Огненный демон', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'197', N'Огненный скелет-воин', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'470', N'Туранка-командир', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'493', N'Мудрая ведьма', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2372', N'Искаженный Хватафорс', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'577', N'Хватафорс', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2476', N'<Запечатанная Зона>/n Святая Хаолин', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2447', N'Боец Туранка', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2449', N'Разбившаяся гидра', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2451', N'Сияющая ведьма', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2450', N'Сияющий жрец', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2448', N'Сияющий рыцарь-скелет', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2478', N'<Заклинатель Пламени>/nОгниэль', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'523', N'Пингвин', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'520', N'Толстый пингвин', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'90', N'Белый медведь', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'738', N'Снежный орк', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'501', N'Королевский пингвин', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'739', N'Снежный орк-лучник', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2138', N'<Исследователь Реликвий>/n Харнубо', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Безымянная пещера - 2 ур. Вход', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'527', N'Ящер воды', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'819', N'Йети', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'108', N'Белый слаад', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'741', N'Командир снежных орков', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'121', N'Атараксия', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2139', N'<Исследователь Реликвий>/n Рагондас', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'81', N'Тритон', N'Болото черного дракона', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'418', N'Ящер', N'Болото черного дракона', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'821', N'Рыбоящер', N'Болото черного дракона', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Болото Черного Дракона - 2 ур. Вход', N'Болото черного дракона', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'835', N'Заурус', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'406', N'Гидра', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'104', N'Повелитель иллюзий', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1462', N'<Исследователь Реликвий>/nАнтиох', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2060', N'Безумный убийца', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'92', N'Ламия', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'448', N'Часовой Метеоса', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'450', N'Прислужник Метеоса', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Болото черного дракона - 4 ур. Вход', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1463', N'<Исследователь Реликвий>/nСетус', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2125', N'<Толкователь Слов>/nОбиллион', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2639', N'Смотритель Горизонта полнолуния', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Гробница Короля - 2 ур. Вход', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'516', N'Королева вампиров', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'519', N'Король вампиров', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'825', N'Танцующая с мечом', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Гробница Короля - 3 ур. Вход', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'535', N'Алластиро', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'534', N'Странствующая колдунья', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'820', N'Седрах', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'536', N'Бельжевит', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2386', N'Искаженный Бельжевит', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1306', N'<Заболевший Исследователь>/nХё', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2123', N'<Запечатанная Зона>/nСвятая Гвендельсия', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2149', N'Командир корпуса короля', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2148', N'Маг короля', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2147', N'Ода', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2145', N'Принцесса вампиров', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2146', N'Приходящий мастер', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2126', N'<Команда Раскопок Руин>/nГейл', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'874', N'Личинка', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'881', N'Болотный василиск', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'879', N'Детеныш дракона', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'875', N'Мантис-убийца', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'876', N'Снежный человек', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'882', N'Стражник Метеоса', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'878', N'Тень Метеоса', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'873', N'Червь', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'877', N'Древопаук', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'871', N'Наездница на виверне', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'902', N'<Алхимик>/nАндрей', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2981', N'<Взломщик Сундуков Метеоса>/nКебек', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2105', N'<Глава Нарциссов Метеоса>/nБаса', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1484', N'<Исследователь Реликвий>/nКирия', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1485', N'<Исследователь Эльфов>/nЭланомия', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1792', N'<Караульный>/nЧонликт', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'889', N'<Кладовщик>/nВинс', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1815', N'<Нарцисс>/nЛогея', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1712', N'<Хранитель Воды>/nРыкейн', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Метеоса', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1645', N'Воин огня', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1646', N'Огненная голова', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1647', N'Пироман', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'539', N'Метеос', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1648', N'Огненный тиран', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2526', N'Черный дракон', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'681', N'<Мастер-кузнец>/nДжек', N'Башня Метеоса', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'457', N'Вепрь-воин', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'456', N'Вепрь-лучник', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'106', N'Огненный волк', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'400', N'Огненный скелет-лучник', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'469', N'Туранка-охранник', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'772', N'<Башня Огня>/nТорговец', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Башня Огня - 3 ур. Вход', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Башня Огня', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'468', N'Свирепый туранка', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'466', N'Туранка-воин', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'417', N'Огненная саламандра', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'73', N'Стражник ада', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'105', N'Скелетон ада', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1458', N'<Исследователь Башни Огня>/nКадеш', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'622', N'Файрон', N'Башня Огня', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1459', N'<Исследователь Башни Огня>/nСерафим', N'Башня Огня', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2477', N'<Заклинатель Шторма>/nМолнис', N'Башня Огня', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1479', N'<Темный Жрец>/nДаймос', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'948', N'Райнон', N'Безымянная пещера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1480', N'Груда камней печати', N'Безымянная пещера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'626', N'Дженди', N'Болото черного дракона', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Болото черного дракона - 3 ур. Вход', N'Болото черного дракона', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'855', N'Лилит', N'Болото черного дракона', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'449', N'Прислужница Метеоса', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'451', N'Колдунья', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'827', N'Пазузу', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2383', N'Искаженная черная виверна', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'538', N'Черная виверна', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2120', N'<Запечатанная Зона>/nСвятая Ружина', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Болото черного дракона', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2143', N'Дворянка Метеоса', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2142', N'Личная служанка Метеоса', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2144', N'Меч Метеоса', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2140', N'Рыцарь Пазузу', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2141', N'Скелетон Метеоса', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2124', N'<Исследователь Свойств Воды>/nБеллиса', N'Болото черного дракона', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2611', N'Боец Танатоса', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2615', N'Верховный рыцарь Рарки', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2613', N'Маг Танатоса', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2614', N'Рыцарь-гвардеец Рарки', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2616', N'Снайпер Рарки', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2617', N'Советник Рарки', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2610', N'Солдат Танатоса', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2612', N'Стрелок Танатоса', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2667', N'Лелион', N'Горизонт Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'91', N'Демонесса', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'533', N'Рыцарь Бельжевита', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'825', N'Танцующая с мечом', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1464', N'<Исследователь Реликвий>/nТибстрог', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'623', N'Кабкаб', N'Гробница Короля', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2135', N'Пэйян', N'Гробница Короля', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1466', N'<Исследователь Реликвий>/nКретарис', N'Гробница Короля', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2127', N'<Нависшее Проклятие>/nМагистрат', N'Гробница Короля', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2081', N'<Бог Солнца Сеонум>/nСекретный Камень', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1306', N'<Заболевший Исследователь>/nХё', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1487', N'<Исследователь Реликвий>/nКарнос', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1488', N'<Исследователь Эльфов>/nБарну', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1790', N'<Караульный>/nДакурат', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1791', N'<Караульный>/nЯкрито', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1747', N'<Нарцисс>/nДрагноф', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'427', N'<Страж>/nГибсон', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'425', N'<Страж>/nСит', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'885', N'<Странствующий Торговец>/nБен', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'900', N'<Телепорт>/nЭльф Канесел', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1748', N'<Эльфийский Нарцисс>/nЗафина', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'892', N'Билли', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1486', N'Забытые доспехи воина', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Храм Метеоса - 2 ур. Вход', N'Храм Метеоса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'870', N'Архимаг Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'883', N'Рейнджер Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'882', N'Стражник Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'878', N'Тень Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'869', N'Берсерк Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'872', N'Разрушитель Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'895', N'Страж Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1489', N'<Исследователь Реликвий>/nТерноа', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1490', N'<Исследователь Эльфов>/nКасаноа', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2082', N'<Осколки Заклинаний>/nАндерсен', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1654', N'<Страж Ворот>/nФавейн', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1794', N'<Хранитель>/nРемалокс', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1795', N'<Хранитель>/nФактакс', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1793', N'<Хранитель>/nХетрокс', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1491', N'Магический камень богатства', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2860', N'<Темный Эльф Метеоса>/nМастер Клинков', N'Храм Жрецов Тьмы', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2870', N'<Темный Эльф Метеоса>/nКомандир Разведки', N'Храм Жрецов Тьмы', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2719', N'Дух агрессивного рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2722', N'Дух кочующего ассасина', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2728', N'Дух кочующего мага', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2724', N'Дух кочующего призывателя', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2726', N'Дух кочующего рейнджера', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2720', N'Дух кочующего рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2723', N'Дух молчаливого ассасина', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2012', N'Поверженный страж Метеоса', N'Храм Метеоса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2861', N'<Темный Эльф Метеоса>/nРазведчица', N'Храм Жрецов Тьмы', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2859', N'Зачарованная хризолитовая нага', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2858', N'Зачарованный изумрудный тифон', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2863', N'<Каменноликий>/nБерсерк', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2862', N'<Каменноликий>/nВерховный Колдун', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2864', N'<Каменноликий>/nВоеначальник', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2865', N'<Каменноликий>/nКараульный', N'Храм Жрецов Тьмы', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2706', N'Агрессивный белмон', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2707', N'Агрессивный голиот', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2708', N'Агрессивный келькрон', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2704', N'Агрессивный срендал', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2703', N'Агрессивный тоуду', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2702', N'Агрессивный фашад', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2705', N'Агрессивный эльрон', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2694', N'Дух блуждающего ассасина', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2700', N'Дух блуждающего мага', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2696', N'Дух блуждающего призывателя', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2698', N'Дух блуждающего рейнджера', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2692', N'Дух блуждающего рыцаря', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2695', N'Дух странствующего ассасина', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2701', N'Дух странствующего мага', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2697', N'Дух странствующего призывателя', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2699', N'Дух странствующего рейнджера', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2693', N'Дух странствующего рыцаря', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2734', N'<Страж Зала>/nАлин', N'Крепость Абеллуса', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1813', N'<Нарцисс>/nЛавье', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1742', N'<Нарцисс>/nРасс', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1783', N'<Хранитель>/nСота', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'736', N'Онокентавр', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'111', N'Живучий циклоп', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'397', N'Вурдалак', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'110', N'Повелитель Боли', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1482', N'<Исследователь Реликвий>/nВиллон', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1785', N'<Наемный Торговец>/nМаторис', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1743', N'<Нарцисс>/nРэйвн', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'766', N'Ройо', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1483', N'<Исследователь Реликвий>/nОделла', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1745', N'<Нарцисс>/nЭдди', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'625', N'Ветер', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'656', N'Гигантская оса', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'660', N'Гориш', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'40', N'Призрак зимы', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Логово жуков - 3 ур. Вход', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2119', N'<Осколки Заклинаний>/nБейсон', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2013', N'Викинг-пират', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Пещера древних пиратов - 2 ур. Вход', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1750', N'Бедная Каспер', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1299', N'Камень печати от комнаты Каспер', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1301', N'Камень печати от комнаты рабов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1296', N'Нубиль', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Сундук пиратов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'821', N'Рыбоящер', N'Подводная пещера Эгира', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'406', N'Гидра', N'Подводная пещера Эгира', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'692', N'Ледяная саламандра', N'Подводная пещера Эгира', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Подводная пещера Эгира - 2 ур. Вход', N'Подводная пещера Эгира', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'655', N'Боггарт', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'693', N'Рыцарский скелет-лучник', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2136', N'<Исследователь Реликвий>/nБрейн', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'855', N'Лилит', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'658', N'Птеранодон', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'693', N'Рыцарский скелет-лучник', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'824', N'Астралодон', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2388', N'Искаженный спектр', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'84', N'Спектр', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2137', N'<Исследователь Реликвий>/n Аско', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2482', N'<Служитель Баальбека>/nДемонроза', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2491', N'Торговец зельями Баальбека', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Подземелье нежити - 2 ур. Вход', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'437', N'Скелет-охотник', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'515', N'Опытный скелет-рыцарь', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'131', N'Скелетон', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Подземелье нежити - 3 ур. Вход', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'101', N'Некромант', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'522', N'Кукловод', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'452', N'Людоед', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2385', N'Искаженный король-лич', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'818', N'Король-лич', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2086', N'<Запечатанная Зона>/nЖанро Дантес', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2098', N'<Собиратель Трупов>/nДао', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2486', N'<Разведчик Юпитера>/nЛионд', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2513', N'Маг порталов (Подземелье Юпитера 1 эт)', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1191', N'Дюрахан', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1194', N'Король огров-зомби', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1192', N'Морена', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Хранитель храма жрецов', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2006', N'<Кладовщик>/nБобби', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2122', N'<Осколки Заклинаний>/nМайена', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2035', N'Набор в народную дружину', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2036', N'Отдыхающий эльф', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2624', N'Раненый копейщик', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2029', N'Уставший эльф', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1798', N'Древопаук-мутант', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1799', N'Маг-мутант', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1801', N'Тритон Локсар', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1800', N'Тритон Тиропс', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2729', N'Дух молчаливого мага', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2725', N'Дух молчаливого призывателя', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2727', N'Дух молчаливого рейнджера', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2721', N'Дух молчаливого рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2712', N'Дух одурманенного ассасина', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2718', N'Дух одурманенного мага', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2714', N'Дух одурманенного призывателя', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2716', N'Дух одурманенного рейнджера', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2710', N'Дух одурманенного рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2730', N'Дух разгневанного рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2711', N'Дух страдающего ассасина', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2717', N'Дух страдающего мага', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2713', N'Дух страдающего призывателя', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2715', N'Дух страдающего рейнджера', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2709', N'Дух страдающего рыцаря', N'Крепость Абеллуса', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'473', N'Кукла', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'477', N'Шут', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'103', N'Драконид', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'735', N'Рейвен', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'112', N'Циклоп хаоса', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1481', N'<Исследователь Реликвий>/nТернос', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1741', N'<Нарцисс>/nМигель', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1782', N'<Хранитель>/nВинта', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Лестница древних - 2 ур. Вход', N'Лестница древних', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1784', N'<Наемный Торговец>/nМакурас', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1744', N'<Нарцисс>/nМадок', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Лестница древних - 3 ур. Вход', N'Лестница древних', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'96', N'Драконид-воин', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'737', N'Онокентавр хаоса', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'45', N'Циклоп-разрушитель', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'659', N'Карлик', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'742', N'Сильный вурдалак', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2389', N'Искаженный Урук-хай', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'472', N'Урук-хай', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1779', N'<Генделий Рафельт>/nГлава Гильдии Вольф', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1746', N'<Нарцисс>/nКрисс', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Лестница древних', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'129', N'Жук-гигант', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'657', N'Жук-носорог', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'656', N'Гигантская оса', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1468', N'<Исследователь Реликвий>/nДайджен', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Логово жуков - 2 ур. Вход', N'Логово жуков', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'855', N'Лилит', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Логово жуков', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'662', N'Жук-мутант', N'Логово жуков', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'823', N'Спайк', N'Логово жуков', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2387', N'Искаженная королева горишей', N'Логово жуков', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'661', N'Королева горишей', N'Логово жуков', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Логово жуков', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2611', N'Боец Танатоса', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2615', N'Верховный рыцарь Рарки', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2613', N'Маг Танатоса', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2614', N'Рыцарь-гвардеец Рарки', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2616', N'Снайпер Рарки', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2617', N'Советник Рарки', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2610', N'Солдат Танатоса', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2612', N'Стрелок Танатоса', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2619', N'Кровавый Рарка', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2618', N'Кровавый Танатос', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2622', N'Проекция Рарки', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2620', N'Проекция Танатоса', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Озеро Полной Луны', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1316', N'Глубоководная рыба', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1318', N'Королевская сороконожка', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1314', N'Лангуст', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1313', N'Снимил', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1317', N'Солдат-грабитель', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1321', N'Пират викингов', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1320', N'Пиратка викингов', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1319', N'Раб-призрак', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1796', N'<Коллекционер>/nТокон', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1307', N'<Предатель>/nКайм', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1297', N'Нуив', N'Пещера древних пиратов', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1317', N'Солдат-грабитель', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1337', N'Маг пиратов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1335', N'Мясник пиратов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1336', N'Надзиратель-призрак', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1319', N'Раб-призрак', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1334', N'Тролль-прислужник', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1341', N'Блэр', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1340', N'Каспер', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1338', N'Химера', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1339', N'Хранитель сокровищ', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1797', N'<Коллекционер>/nКанкон', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1300', N'Камень печати от комнаты Блэра', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1298', N'Камень печати от комнаты ликанов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1504', N'Невидимка', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2014', N'Трусливый мясник пиратов', N'Пещера древних пиратов', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'624', N'Саша', N'Подводная пещера Эгира', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Подводная пещера Эгира - 3 ур. Вход', N'Подводная пещера Эгира', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Подводная пещера Эгира', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2459', N'Демон-убийца', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2461', N'Драгун', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2458', N'Падшая кровавая владычица', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2460', N'Пробудившийся кровавый король', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2454', N'Чудаковатый эльвин', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2484', N'<Атакующий Отряд Баальбека>/nАргон', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2515', N'Маг порталов (Подземелье Баальбека 1 эт)', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2468', N'Ларец Баальбека', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Ларец Юпитера/Баальбека (открытый силой)', N'Подземелье Баальбека', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2503', N'Архидемон', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2504', N'Великий змей', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2502', N'Владычица тьмы', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2505', N'Цветок дракона', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2498', N'Эльктан Разрушитель', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2508', N'Потертый древний сундук', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2507', N'Сияющий ларец Баальбека', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Сияющий ларец Баальбека/Юпитера (открытый силой)', N'Подземелье Баальбека', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'507', N'Кровавый скелет', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'402', N'Скелет-лучник', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'404', N'Скелет-рыцарь', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'707', N'Морская змея', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1760', N'Старый дневник исследований', N'Подземелье нежити', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2133', N'Хайян', N'Подземелье нежити', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Подземелье нежити', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2080', N'Жрец короля-лича', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2078', N'Людоед-воин', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2077', N'Маг-нежить', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2079', N'Мясник короля-лича', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2076', N'Некромант отчаяния', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2099', N'<Архимаг Высокого Уровня>/nЭйлин', N'Подземелье нежити', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1288', N'Рак-отшельник', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1308', N'Камень чакры', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1310', N'Призрак Акры', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1309', N'Хонок', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1311', N'Гвардеец', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1312', N'Королевский гвардеец', N'Подземелье Валлефора', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2676', N'Каменный великан', N'Подземелье Валлефора', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2674', N'Каменный защитник', N'Подземелье Валлефора', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2675', N'Небесный дух', N'Подземелье Валлефора', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2673', N'Небесный защитник', N'Подземелье Валлефора', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2672', N'Небесный хранитель', N'Подземелье Валлефора', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2678', N'Защитник земли', N'Подземелье Валлефора', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2681', N'Кобра-солдат', N'Подземелье Валлефора', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2680', N'Ловец тьмы', N'Подземелье Валлефора', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2679', N'Осьминог-шаман', N'Подземелье Валлефора', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2677', N'Хранитель земли', N'Подземелье Валлефора', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2455', N'Древняя валькирия', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2458', N'Падшая кровавая владычица', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2456', N'Слуга бога', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2454', N'Чудаковатый эльвин', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2457', N'Эльсир Хаоса', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2488', N'<Привратник Юпитера>/nФрей', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2480', N'<Служитель Юпитера>/nАнжелика', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2490', N'Торговец зельями Юпитера', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2467', N'Ларец Юпитера', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Ларец Юпитера/Баальбека (открытый силой)', N'Подземелье Юпитера', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2501', N'Архангел', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2502', N'Владычица тьмы', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2500', N'Длань ангела мести', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2498', N'Эльктан Разрушитель', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2499', N'Эрата Пожиратель Душ', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2508', N'Потертый древний сундук', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Сияющий ларец Баальбека/Юпитера (открытый силой)', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2506', N'Сияющий ларец Юпитера', N'Подземелье Юпитера', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2152', N'<Премиум> Асмодеус', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2151', N'<Премиум> Богиня Кали', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1231', N'<Премиум> Гладиатор', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2150', N'<Премиум> Демон-охотник', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1229', N'<Премиум> Ондин', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1232', N'<Премиум> Риттер', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1228', N'<Премиум> Самурай', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1230', N'<Премиум> Слуга Бога', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2155', N'<Премиум> Абиссия', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2153', N'<Премиум> Искаженная Королева Горишей', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1240', N'<Премиум> Искаженный Бельжевит', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1239', N'<Премиум> Искаженный Король-лич', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2154', N'<Премиум> Искаженный Спектр', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1237', N'<Премиум> Искаженный Хватафорс', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1234', N'<Премиум> Королева Личей', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1236', N'<Премиум> Король Огров-зомби', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1233', N'<Премиум> Костяной Дракон', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1238', N'<Премиум> Пробудившийся Кровавый Король', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1235', N'<Премиум> Рахан', N'Премиум подземелье', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1241', N'<Премиум> Алхимик', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1243', N'<Премиум> Геракл', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2156', N'<Премиум> Искаженный Гигант-воин', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2157', N'<Премиум> Искаженный Гигант-шаман', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1245', N'<Премиум> Ноасс', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1244', N'<Премиум> Рыцарь Королевы', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1242', N'<Премиум> Силаирон', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1248', N'<Премиум> Искаженная Королева Личей', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1247', N'<Премиум> Искаженная Черная Виверна', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2160', N'<Премиум> Искаженный Гвардеец Ада', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2158', N'<Премиум> Искаженный Король Огров-зомби', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2159', N'<Премиум> Искаженный Костяной Дракон', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1249', N'<Премиум> Искаженный Рахан', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1246', N'<Премиум> Искаженный Урук-хай', N'Премиум подземелье', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Главный страж Метеоса', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2407', N'Искаженный костяной дракон', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1193', N'Костяной дракон', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Огненный хранитель Хаоса', N'РБ с пираток', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2047', N'<Властитель Руин>/nМинотавр', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2048', N'<Лучник Руин>/nОрк-лучник', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2049', N'<Хранитель Руин>/nВепрь', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1985', N'Верховный жрец Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1992', N'Воин света Танатоса', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1998', N'Голем замка', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1996', N'Земляная виверна', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1991', N'Копейщик Танатоса', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1995', N'Кошмар тьмы', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1994', N'Кровожадный людоед', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1989', N'Лучник Танатоса', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1990', N'Наемный убийца Танатоса', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1984', N'Пехотинец Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1988', N'Разведчик Танатоса', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1987', N'Солдат Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1983', N'Старший офицер Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1986', N'Стрелок Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1993', N'Элементаль тьмы', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1997', N'Этин-разрушитель', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1999', N'Капитан рыцарей Рарки', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2000', N'Танатос', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2026', N'<Боец Рарки>/nОтдыхающий Качес', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2037', N'<Освоение Земель>/nХайзак', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2044', N'Лерион', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2028', N'О полнолунии', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Разлом полнолуния', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2625', N'Раненый старший офицер', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Чудовище полнолуния', N'Руины Полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1803', N'Боец Драграм', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1808', N'Грифон-мутант', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1806', N'Красношипый Фэнсер', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1805', N'Кровожадный скорпион', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1804', N'Огневик Драграм', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1807', N'Падшая виверна', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1802', N'Привратник каменных врат Драграм', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1809', N'Стэгозавр самец', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1811', N'Сумеречный лучник', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1810', N'Сумеречный рыцарь', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1812', N'Сумеречный шаман', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1881', N'Бафомет', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1882', N'Проекция Бафомета', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2084', N'<Бог Земли Хелтес>/nСекретный Камень', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1835', N'<Генделий Рафельт>/nАстральная Проекция', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2608', N'<Исследователь Реликвий>/nЛимб', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1818', N'<Мастер Иллюмина>/nГлава Совета Эарвин', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1868', N'<Пергамент Иллюмины>/nЗаписи О Мутациях', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1819', N'<Прогрессист>/nПредседатель', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1821', N'<Прогрессист>/nПроекция Ронжель', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1867', N'<Стелла Иллюмины>/nЗа Грихентеля', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1866', N'О неизвестной территории', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Темные пещеры - 2 ур. Вход', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'773', N'<Темные Пещеры>/nТорговец', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'404', N'Скелет-рыцарь', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'441', N'Темный страж', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'442', N'Молодой тарантул', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'439', N'Проклятый вампир', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'440', N'Темная ламия', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1453', N'<Изыскатель>/nМарс', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'854', N'Астарот', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'95', N'Горгулья', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'855', N'Лилит', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'444', N'Мудрая колдунья', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'37', N'Ведьма', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'443', N'Огненный скелет-охотник', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'540', N'Гвардеец ада', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2384', N'Искаженный гвардеец ада', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2083', N'<Запечатанная Зона>/nЖанро Дельфор', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1455', N'Окровавленные доспехи', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Тарел', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'391', N'Гиракамеро', N'Алтарь Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'75', N'Бесенок', N'Алтарь Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Алтарь Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2395', N'Искаженный троглодит', N'Берег Ламий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'81', N'Тритон', N'Берег Тритонов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'369', N'Гигантский тритон', N'Берег Тритонов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Берег Тритонов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2060', N'Безумный убийца', N'Деревня кобольдов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'79', N'Бурый медведь', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'78', N'Волк-людоед', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'74', N'Гоблин', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'840', N'Костоглот', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'841', N'Костоглот-шаман', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'80', N'Хобгоблин', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Древний Город Нарту', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'463', N'Орк-боец Варуна', N'Ферма Драконов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'153', N'Орк-воин', N'Ферма Драконов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'405', N'Орк-лучник', N'Ферма Драконов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'460', N'Орк-воин Варуна', N'Ферма Драконов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'33', N'Гарпия', N'Гнездовье гарпий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'363', N'Королева гарпий', N'Гнездовье гарпий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2129', N'Эболлас', N'Гнездовье гарпий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'97', N'Оборотень', N'Красная долина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'740', N'Оборотень-лучник', N'Красная долина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'651', N'Птицелев', N'Красная долина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'505', N'Цербер', N'Лабиринт Манога', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'454', N'Минотавр', N'Лабиринт Манога', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'154', N'Минотавр-воин', N'Лабиринт Манога', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Лабиринт Манога', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'83', N'Орк', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'153', N'Орк-воин', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'405', N'Орк-лучник', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'364', N'Руум', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'775', N'<Лагерь Орков>/nТорговец', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'76', N'Хобгремлин', N'Лес Гремлинов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'389', N'Чабон', N'Лес Гремлинов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'395', N'Детеныш паука', N'Лес пауков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'396', N'Паук', N'Лес пауков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'365', N'Паук-птицеед', N'Лес пауков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'770', N'<Лес Пауков>/nТорговец', N'Лес пауков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный гнолл', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'403', N'Улитка', N'Окрестности деревни Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'648', N'Лепрекон-воин', N'Окрестности деревни Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'396', N'Паук', N'Окрестности деревни Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2382', N'Искаженный гоблин', N'Окрестности деревни Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2393', N'Искаженный кобольд', N'Окрестности деревни Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'843', N'Костяной драйдер', N'Окрестности Деревни Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2391', N'Искаженный костоглот-шаман', N'Окрестности Деревни Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2381', N'Искаженный орк', N'Окрестности Деревни Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'843', N'Костяной драйдер', N'Окрестности деревни Темных земель', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'396', N'Паук', N'Окрестности деревни Темных земель', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Окрестности деревни Темных земель', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'86', N'Скелет', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'402', N'Скелет-лучник', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'85', N'Упырь', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'359', N'Крепкий скелет', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2060', N'Безумный убийца', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2394', N'Искаженный тритон', N'Окрестности Гробницы короля', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'392', N'Жук', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'129', N'Жук-гигант', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'657', N'Жук-носорог', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'705', N'Стальной жук', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Логово Жуков - 1 ур. Вход', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2398', N'Искаженный жук', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'697', N'Мандрагора', N'Окрестности Подводной пещеры Эгира', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'654', N'Василиск', N'Окрестности Подводной пещеры Эгира', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'92', N'Ламия', N'Окрестности Подводной пещеры Эгира', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'703', N'Гигантский василиск', N'Окрестности Подводной пещеры Эгира', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Окрестности Подводной пещеры Эгира', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2401', N'Искаженный оборотень', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'148', N'Серый гремлин', N'Окрестности Темных пещер', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'145', N'Гнолл-воин', N'Оплот Гноллов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'146', N'Гнолл-лучник', N'Оплот Гноллов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'371', N'Шрам', N'Оплот Гноллов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Оплот Гноллов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1817', N'<Генделий Рафельт>/nАлхимик Батус', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2609', N'<Исследователь Реликвий>/nБайрин', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1865', N'<Кладовщик>/nЭносс', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2085', N'<Осколки Заклинаний>/nГейдн', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1891', N'<Прогрессист Иллюмина>/nПроекция Лэндвин', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1892', N'<Прогрессист>/nПроекция Керобека', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1820', N'<Сенат Иллюмина>/nСоветник Керобек', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1836', N'<Торговец Магическими Книгами>/nКентхилл', N'Святые земли Иллюмина', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'130', N'Летучая мышь', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'550', N'Слизь', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'465', N'Тролль-охотник', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'411', N'Пещерная летучая мышь', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'480', N'Гоблин-шахтер', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'708', N'Гремлин-торговец', N'Темные пещеры', N'Уровень: 1')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'481', N'Гоблин-людоед', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'479', N'Гоблин-прислужник', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'437', N'Скелет-охотник', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'88', N'Пещерный паук', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'125', N'Скелет-уничтожитель', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1452', N'<Изыскатель>/nЭрис', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Темные пещеры - 3 ур. Вход', N'Темные пещеры', N'Уровень: 2')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Искаженный торговец', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Темные пещеры - 4 ур. Вход', N'Темные пещеры', N'Уровень: 3')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1454', N'<Изыскатель>/nХарнес', N'Темные пещеры', N'Уровень: 4')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2071', N'Кошмар страха', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2072', N'Кровавый охотник', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2075', N'Охотник гвардейца', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2074', N'Охотничья собака гвардейца', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2073', N'Синяя ведьма', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2097', N'<Исследователь печати>/nЭллиен', N'Темные пещеры', N'Уровень: 5')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'41', N'Молодой древень', N'Аллея Джаратан', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'43', N'Древень', N'Аллея Джаратан', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'459', N'Джаратан', N'Аллея Джаратан', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Аллея Джаратан', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'648', N'Лепрекон-воин', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'649', N'Лепрекон-маг', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'658', N'Птеранодон', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'652', N'Флинд', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'696', N'Флинд-лучник', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'701', N'Флинд мечник', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1470', N'<Исследователь Реликвий>/nТартус', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Алтарь вурдалака', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'92', N'Ламия', N'Берег Ламий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Берег Ламий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Берег Тритонов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'115', N'Кобольд', N'Деревня кобольдов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'209', N'Кобольд-лучник', N'Деревня кобольдов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'362', N'Командир кобольдов', N'Деревня кобольдов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Деревня кобольдов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2391', N'Искаженный костоглот-шаман', N'Долина ветра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'648', N'Лепрекон-воин', N'Древний Город Нарту', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'649', N'Лепрекон-маг', N'Древний Город Нарту', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Древний Город Нарту', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2060', N'Безумный убийца', N'Гнездовье гарпий', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'100', N'Пикси', N'Холм Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'702', N'Королева Мав', N'Холм Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2058', N'Падший владыка', N'Холм Эльфов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'396', N'Паук', N'Храм апостолов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'409', N'Куролиск', N'Храм апостолов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'361', N'Лесной куролиск', N'Храм апостолов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2060', N'Безумный убийца', N'Храм апостолов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'82', N'Троглодит', N'Храм раздора', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Храм раздора', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'694', N'Огр-охотник', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'153', N'Орк-воин', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'405', N'Орк-лучник', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'665', N'Каменный орк-воин', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'453', N'Каменный голем', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'706', N'Огр-воин', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Каменный Молот', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2132', N'Рейндас', N'Лабиринт Манога', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Лагерь орков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2059', N'Стальной судья', N'Лес пауков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'147', N'Болотный гремлин', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'418', N'Ящер', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'145', N'Гнолл-воин', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'146', N'Гнолл-лучник', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'360', N'Куру', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Окрестности Болота черного дракона', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'403', N'Улитка', N'Окрестности Эшборн', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'79', N'Бурый медведь', N'Окрестности Эшборн', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'578', N'Кабалло', N'Окрестности Эшборн', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'734', N'<Администратор Гонок>/nКуру', N'Окрестности Эшборн', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Окрестности Логова жуков', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'840', N'Костоглот', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'841', N'Костоглот-шаман', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'86', N'Скелет', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'418', N'Ящер', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'402', N'Скелет-лучник', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2379', N'Искаженный скелет', N'Окрестности Подземелья нежити', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'486', N'Анфракс', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'474', N'Гигантский краб', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'646', N'Гигантский скорпион', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'97', N'Оборотень', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'740', N'Оборотень-лучник', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'699', N'Ящер огня', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'48', N'Вожак оборотней', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'358', N'Мантикора', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Окрестности Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'119', N'Расхититель гробниц', N'Озеро Времени', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'474', N'Гигантский краб', N'Озеро Времени', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2404', N'Искаженный гигантский краб', N'Озеро Времени', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'646', N'Гигантский скорпион', N'Терраса злодея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'416', N'Гигант-шаман', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'122', N'Гигант-воин', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'120', N'Вождь гигантов', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2402', N'Искаженный гигант-воин', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2403', N'Искаженный гигант-шаман', N'Водопад гигантов', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'34', N'Могучий орк', N'Заброшенная деревня', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'36', N'Могучий орк-лучник', N'Заброшенная деревня', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Заброшенная деревня', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'92', N'Ламия', N'Заброшенный Порт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'82', N'Троглодит', N'Заброшенный Порт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2394', N'Искаженный тритон', N'Заброшенный Порт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2395', N'Искаженный троглодит', N'Заброшенный Порт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'127', N'Зомби', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'410', N'Мертвая гончая', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'86', N'Скелет', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'402', N'Скелет-лучник', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'85', N'Упырь', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Раненый солдат', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'691', N'<Антиквар>/nКрюгер', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1347', N'<Байрон>/nТорговец Очками Хаоса', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1693', N'<Глава Нарциссов Байрона>/nТайгервот', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2748', N'<Инструктор Питомцев>/nИрия', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'684', N'<Мастер Перемещений>/nМинт', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'675', N'<Стражник>/nДжамбо', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'678', N'<Стражник>/nРукер', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'15231', N'<Фермер>/nНойес Уэйтли', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'15230', N'<Фермер>/nУолтер Уэйтли', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'682', N'<Ювелир>/nСпероу', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'304', N'<Алхимик>/nЛюси', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'9998', N'<Ежедневные Задания>/nАнчутка', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2038', N'<Обмен Серебряных Монет>/nБанкир', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1756', N'<Слуга Икрона>/nТренос', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'НПС Маленький дьяволенок', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'302', N'Тоби', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'<Стражник>/nНортон', N'Деревня Кокон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'751', N'<Алхимик>/nКсения', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'749', N'<Антиквар>/nРой', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1694', N'<Глава Нарциссов Родена>/nРостимайн', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'750', N'<Оружейник>/nРуу', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1135', N'<Очки Славы>/nФред', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1345', N'<Роден>/nТорговец Очками Хаоса', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2131', N'Эдельго', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2483', N'<Атакующий Отряд Баальбека>/nБалтус', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2231', N'<Командир Абеллиона>/nКаль', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2353', N'<Продавец Материалов>/nКарл', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2481', N'<Служитель Баальбека>/nЛюцифер', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2356', N'<Стражник Абеллиона>/nКанна', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2354', N'<Стражник Абеллиона>/nМос', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2357', N'<Стражник Абеллиона>/nХилун', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2338', N'<Телепорт>/nГилсон', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2806', N'<Управляющий Ареной>/nПеоний', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2024', N'<Адъютант Рарки>/nВладимор', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2121', N'<Бог Ветра Альтенус>/nСтатуя', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2025', N'<Надзиратель Рарки>/nСинт', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2033', N'<Ресурсы>/nПеревозчик Греин', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2032', N'<Ресурсы>/nСтраж Маргейн', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'<Староста Деревни Отдыха>/nФенон?', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2318', N'Злые мысли Юпитера', N'Небесный остров Эльтер', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2319', N'Командир Баальбека', N'Небесный остров Эльтер', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1001', N'Красная лисица', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1000', N'Молодое дерево', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1002', N'Фламинго', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1003', N'Медуза', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1005', N'Хищный краб', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1013', N'Гвардеец-маг', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1012', N'Гвардеец-мечник', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1007', N'Каннибал', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1010', N'Нага-воительница', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1004', N'Скат', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1006', N'Черепаха', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1015', N'Гвардеец-лучник', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1017', N'Дикарь', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1016', N'Силач', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1009', N'Нага-колдунья', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1008', N'Шаман каннибалов', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1022', N'Лучница акрионцев', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1020', N'Солдат акрионцев', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1023', N'Шаман акрионцев', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1018', N'Командующий копейщиков', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1021', N'Лорд акрионцев', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1014', N'Гвардеец-защитник', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1019', N'Капитан акрионцев', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1011', N'Нага-королева', N'Остров Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Виверна черного ветра', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Вождь первобытных лепреконов', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Гигантская королева птицеедов', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Древний Хватафорс', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Дубобык', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Капитан Йети', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Капитан отчаяния Феликс', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Кровавая мухоловка', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Освобожденный хранитель адских врат', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Скрученный Кириман', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Теса', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Хранитель воды', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'<Старший Научный Сотрудник>/nМамон', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'5116', N'Снежная ведьма', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'5117', N'Искаженный кролик', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'5119', N'Крампус', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'6110', N'Механическая оса', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2390', N'Искаженный зомби', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2379', N'Искаженный скелет', N'Земли мертвых', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1063', N'<Антиквар>/nБрейк', N'Деревня Акра', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'628', N'<Алхимик>/nДжени', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'713', N'<Гонки Драконов>/nБайрон', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1924', N'<Комиссионный Торговец>/nФорор', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'627', N'<Оружейник>/nКорден', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'928', N'<Проповедник Хадеса>/nАльтман', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'677', N'<Стражник>/nДжин', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2806', N'<Управляющий Ареной>/nПеоний', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'15229', N'<Фермер>/nОубед Уэйтли', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'15228', N'<Фермер>/nЭрих Уэйтли', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'634', N'Кванчи', N'Деревня Байрон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'9997', N'<Главный Кошмар> Дрекавак', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1456', N'<Исследователь> Урн', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1777', N'<Слуга Икрона> Гердин', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'307', N'<Торговец Ядами> Джек', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'306', N'Джеймс', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'301', N'Плоц', N'Деревня Изгнанников', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3066', N'<Археолог>/nХайлун', N'Деревня Кокон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'<Особые Перевоплощения>/nГрейс', N'Деревня Кокон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3062', N'<Торговец Припасами>/nДэиль', N'Деревня Кокон', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'752', N'<Мастер Перемещений>/nФасфа', N'Деревня Роден', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2336', N'<Алхимик>/nКейлор', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'1873', N'<Гид По Древу Умений>/nНайт', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2352', N'<Оружейник>/nКорелла', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'934', N'<Продавец Книг Умений>/nКен', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'944', N'<Продавец Магических Книг>/nСвен', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2485', N'<Разведчик Юпитера>/nРэй', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2479', N'<Служитель Юпитера>/nРафаэль', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2355', N'<Стражник Абеллиона>/nКвиэль', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2359', N'<Стражник Абеллиона>/nНиа', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2358', N'<Стражник Абеллиона>/nЭнсо', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2339', N'<Телепорт> Дженис', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'748', N'<Ювелир> Линн', N'Реконструированный город Аббелион', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2002', N'<Алхимик> Поставщик Рарки', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2003', N'<Кладовщик> Склад Рарки', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2023', N'<Привратник Полнолуния> Ривли', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2034', N'<Ресурсы> Ремесленник Мофарэл', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2031', N'<Ресурсы> Страж Марфир', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2027', N'Бессмертный страж', N'Заброшенный город полнолуния', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3041', N'Вождь гремлинов', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Вулканический жук', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Древний железный голем', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Древняя королева Наг', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Императорский пингвин синего льда', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'111236', N'Капитан красных орков', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Командир морозных вендиго', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Ледяной саблезуб', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Скорпион хаоса', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Темный Вулкан', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Хейдан Голубой Луны', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Шаман Рафы', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3047', N'Вождь гноллов Тека', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3022', N'Вождь Оркобольг', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3026', N'Королева пауков-птицеедов', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3051', N'Кровавый наур', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3040', N'Нага-эшби', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3032', N'Освобожденный гвардеец ада', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'3058', N'Прозорливый Хатафорс', N'Остров Демоджар', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Енот - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Кролик - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Летучая мышь - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Лягушка - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Пугало - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2009', N'Гвинейская виверна', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Гремлин - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2007', N'Детеныш орка', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Кабан - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2008', N'Рогатая жаба', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Волк-Людоед - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'0', N'Гоблин - Гвинеи', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'502', N'Циклоп-созерцатель', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'81', N'Тритон', N'Остров Гвинея', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2406', N'Искаженная Королева личей', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2408', N'Искаженный король огров-зомби', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2407', N'Искаженный костяной дракон', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2405', N'Искаженный рахан', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'537', N'Ифрит', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'15300', N'Растущее гигантское растение', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'5115', N'Пингринч', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'5114', N'Элементаль льда', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'579', N'Большой тролль-воин', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'704', N'Король Ракум', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'35', N'Сирена', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2584', N'Захватчик КТ/nАлхимик', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2591', N'Захватчик КТ/nАнгелис', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2587', N'Захватчик КТ/nАсура', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2583', N'Захватчик КТ/nБезжалостная красотка', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2582', N'Захватчик КТ/nБеркора', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2588', N'Захватчик КТ/nБерсерк', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2594', N'Захватчик КТ/nБогиня Кали', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2586', N'Захватчик КТ/nГеракл', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2592', N'Захватчик КТ/nДьяволис', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2589', N'Захватчик КТ/nМонах', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2590', N'Захватчик КТ/nОхотник Левинджер', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2585', N'Захватчик КТ/nПолуночная Гермия', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2581', N'Захватчик КТ/nРыцарь королевы', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2595', N'Захватчик КТ/nСнайпер Биг Свелл', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2593', N'Захватчик КТ/nШут', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'408', N'Виверна', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2399', N'Искаженная ламия', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2400', N'Искаженная мандрагора', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2382', N'Искаженный гоблин', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2392', N'Искаженный гремлин', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2380', N'Искаженный медведь', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'2396', N'Искаженный ящер', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'93', N'Огр', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'99', N'Огр-маг', N'Остров Колфорт', N'')
GO

INSERT INTO [dbo].[DT_MonsterLocation] ([MID], [MName], [Location], [LocationLevel]) VALUES (N'102', N'Черный единорог', N'Остров Колфорт', N'')
GO

