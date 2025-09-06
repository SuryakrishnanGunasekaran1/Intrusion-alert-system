-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 08, 2023 at 02:12 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `login_security`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`, `amount`) VALUES
('admin', 'admin', 45500);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `mobile` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `city` varchar(30) NOT NULL,
  `desig` varchar(30) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `pass` varchar(20) NOT NULL,
  `rdate` varchar(20) NOT NULL,
  `fimg` varchar(30) NOT NULL,
  `log_st` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `name`, `mobile`, `email`, `city`, `desig`, `uname`, `pass`, `rdate`, `fimg`, `log_st`) VALUES
(1, 'Dinesh', 9894442716, 'rndittrichy@gmail.com', 'Madurai', 'Software', 'dinesh', '123456', '04-03-2023', 'v1.png', 0);

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `id` int(11) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `filename` varchar(20) NOT NULL,
  `mac_address` varchar(30) NOT NULL,
  `dtime` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`id`, `uname`, `filename`, `mac_address`, `dtime`) VALUES
(1, 'dinesh', 'F1.jpg', '83:69:20:6e:23:6c', '2023-03-05 11:41:09'),
(2, 'dinesh', 'F2.jpg', '83:69:20:6e:23:6c', '2023-03-05 14:06:09'),
(3, 'dinesh', 'F3.jpg', '83:69:20:6e:23:6c', '2023-03-05 14:07:11'),
(4, 'dinesh', 'F4.jpg', '83:69:20:6e:23:6c', '2023-03-06 13:42:15'),
(5, 'dinesh', 'F5.jpg', '83:69:20:6e:23:6c', '2023-03-06 13:49:02'),
(6, 'dinesh', 'F6.jpg', '83:69:20:6e:23:6c', '2023-03-07 15:49:53');

-- --------------------------------------------------------

--
-- Table structure for table `user_files`
--

CREATE TABLE `user_files` (
  `id` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  `upload_file` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_files`
--

