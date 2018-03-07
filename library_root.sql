-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 07, 2018 at 04:43 PM
-- Server version: 5.5.54
-- PHP Version: 5.3.10-1ubuntu3.26

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `library_root`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE IF NOT EXISTS `book` (
  `book_id` int(10) NOT NULL AUTO_INCREMENT,
  `book_name` varchar(150) NOT NULL,
  `book_pubdate` date NOT NULL,
  `book_summary` varchar(250) NOT NULL,
  `book_country` varchar(150) NOT NULL,
  `book_link` varchar(150) NOT NULL,
  `bwriter_id` int(10) NOT NULL,
  PRIMARY KEY (`book_id`),
  KEY `bwriter_id` (`bwriter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `users_id` int(10) NOT NULL AUTO_INCREMENT,
  `users_fname` varchar(150) NOT NULL,
  `users_lname` varchar(150) NOT NULL,
  `users_uname` varchar(150) NOT NULL,
  `users_password` varchar(150) NOT NULL,
  PRIMARY KEY (`users_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `writer`
--

CREATE TABLE IF NOT EXISTS `writer` (
  `writer_id` int(10) NOT NULL AUTO_INCREMENT,
  `writer_name` varchar(150) NOT NULL,
  `writer_dob` date NOT NULL,
  `writer_dod` date NOT NULL,
  `writer_contact` varchar(150) NOT NULL,
  `writer_bio` varchar(255) NOT NULL,
  PRIMARY KEY (`writer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`bwriter_id`) REFERENCES `writer` (`writer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
