-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2017 at 04:09 AM
-- Server version: 5.6.35
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `gis`
--

-- --------------------------------------------------------

--
-- Table structure for table `fields`
--

CREATE TABLE `fields` (
  `id` int(11) NOT NULL,
  `tablename` varchar(40) NOT NULL,
  `field` varchar(40) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `eng_name` varchar(40) DEFAULT NULL,
  `nepl_name` varchar(80) DEFAULT NULL,
  `descrip` varchar(60) DEFAULT NULL,
  `priority` varchar(20) DEFAULT NULL,
  `mykeys` varchar(40) DEFAULT NULL,
  `myvalues` varchar(40) DEFAULT NULL,
  `field_extra` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fields`
--

INSERT INTO `fields` (`id`, `tablename`, `field`, `type`, `eng_name`, `nepl_name`, `descrip`, `priority`, `mykeys`, `myvalues`, `field_extra`) VALUES
(1, 'setuptables', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'setuptables', 'tablename', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'setuptables', 'icon', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'setuptables', 'nepl_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'setuptables', 'panel_class', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'user', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'user', 'username', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'user', 'pwd', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(9, 'user', 'person_id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 'user', 'user_type', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'fields', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, 'fields', 'tablename', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, 'fields', 'field', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, 'fields', 'type', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'fields', 'eng_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, 'fields', 'nepl_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, 'fields', 'descrip', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, 'fields', 'priority', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(19, 'fields', 'mykeys', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, 'fields', 'myvalues', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, 'fields', 'field_extra', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(22, 'file', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(23, 'file', 'cur_id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(24, 'file', 'cur_tablename', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(25, 'file', 'description', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(26, 'file', 'file_type', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(27, 'file', 'file_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(28, 'file', 'size', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(29, 'mymenu', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(30, 'mymenu', 'nepl_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(31, 'mymenu', 'eng_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(32, 'mymenu', 'parent_id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(33, 'mymenu', 'weight', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(34, 'mymenu', 'icon', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(35, 'mymenu', 'href', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(36, 'mymenu', 'hidden_to_user', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(37, 'mytables', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(38, 'mytables', 'tablename', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(39, 'mytables', 'header', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(40, 'mytables', 'subtables', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(41, 'mytables', 'defaultvalues', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(42, 'mytables', 'extra_name', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(43, 'mytables', 'file', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(44, 'mytables', 'form_type', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(45, 'reports', 'id', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(46, 'reports', 'tablename', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(47, 'reports', 'description', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(48, 'reports', 'linecons', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `id` int(11) NOT NULL,
  `cur_id` int(11) NOT NULL,
  `cur_tablename` varchar(40) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `file_type` varchar(20) NOT NULL,
  `file_name` varchar(60) NOT NULL,
  `size` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `mymenu`
--

CREATE TABLE `mymenu` (
  `id` int(11) NOT NULL,
  `nepl_name` varchar(40) DEFAULT NULL,
  `eng_name` varchar(40) DEFAULT NULL,
  `parent_id` int(11) NOT NULL,
  `weight` int(11) DEFAULT NULL,
  `icon` varchar(20) DEFAULT NULL,
  `href` varchar(80) DEFAULT NULL,
  `hidden_to_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Initial Setup';

-- --------------------------------------------------------

--
-- Table structure for table `mytables`
--

CREATE TABLE `mytables` (
  `id` int(11) NOT NULL,
  `tablename` varchar(40) NOT NULL,
  `header` varchar(40) DEFAULT NULL,
  `subtables` varchar(90) DEFAULT NULL,
  `defaultvalues` varchar(40) DEFAULT NULL,
  `extra_name` varchar(40) DEFAULT NULL,
  `file` varchar(20) DEFAULT NULL,
  `form_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='first_time';

--
-- Dumping data for table `mytables`
--

INSERT INTO `mytables` (`id`, `tablename`, `header`, `subtables`, `defaultvalues`, `extra_name`, `file`, `form_type`) VALUES
(1, 'mymenu', 'mymenu', NULL, NULL, NULL, '0', NULL),
(2, 'mytables', 'mytables', NULL, NULL, NULL, '0', NULL),
(3, 'user', 'user', NULL, NULL, NULL, '0', NULL),
(4, 'fields', 'fields', NULL, NULL, NULL, '0', NULL),
(5, 'file', 'file', NULL, NULL, NULL, '0', NULL),
(6, 'reports', 'reports', NULL, NULL, NULL, '0', NULL),
(7, 'setuptables', 'setuptables', NULL, NULL, NULL, '0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `id` int(11) NOT NULL,
  `tablename` varchar(40) NOT NULL,
  `description` varchar(60) DEFAULT NULL,
  `lineicons` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `setuptables`
--

CREATE TABLE `setuptables` (
  `id` int(11) NOT NULL,
  `tablename` int(11) NOT NULL,
  `icon` int(11) DEFAULT NULL,
  `nepl_name` int(11) DEFAULT NULL,
  `panel_class` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `person_id` int(11) DEFAULT NULL,
  `user_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fields`
--
ALTER TABLE `fields`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mymenu`
--
ALTER TABLE `mymenu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mytables`
--
ALTER TABLE `mytables`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `setuptables`
--
ALTER TABLE `setuptables`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fields`
--
ALTER TABLE `fields`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
--
-- AUTO_INCREMENT for table `file`
--
ALTER TABLE `file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mymenu`
--
ALTER TABLE `mymenu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `mytables`
--
ALTER TABLE `mytables`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `setuptables`
--
ALTER TABLE `setuptables`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
