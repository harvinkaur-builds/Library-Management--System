-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 04, 2026 at 01:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `book_name` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `book_name`, `author`, `publisher`, `quantity`) VALUES
(4, 'Computer Networks', 'Forouzan', 'McGraw Hill', 7),
(5, 'Data Structures', 'Seymour Lipschutz', 'Schaum', 14),
(6, 'Java Programming', 'Herbert Schildt', 'McGraw Hill', 8),
(7, 'C Programming', 'E. Balagurusamy', 'McGraw Hill', 9),
(8, 'C++ Programming', 'Bjarne Stroustrup', 'Pearson', 7),
(9, 'Artificial Intelligence', 'Stuart Russell', 'Pearson', 5),
(10, 'Machine Learning', 'Tom Mitchell', 'McGraw Hill', 6);

-- --------------------------------------------------------

--
-- Table structure for table `book1`
--

CREATE TABLE `book1` (
  `book_id` int(11) NOT NULL,
  `book_name` varchar(150) NOT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `rating` decimal(5,1) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book1`
--

INSERT INTO `book1` (`book_id`, `book_name`, `author`, `publisher`, `rating`, `price`, `quantity`) VALUES
(1, 'Java Programming', 'herbert schildt', 'mc graw hill', 4.5, 300.00, 7),
(2, 'Introduction to Algorithms', 'Thomas H. Cormen', 'MIT Press', 4.9, 1899.00, 7),
(3, 'Data Structures and Algorithms in Python', 'Michael T. Goodrich', 'Wiley', 4.8, 1599.00, 10),
(4, 'Computer Networks', 'Andrew S. Tanenbaum', 'Pearson', 4.8, 1099.00, 7),
(5, 'Operating System Concepts', 'Abraham Silberschatz', 'Wiley', 4.8, 1399.00, 6),
(6, 'Database System Concepts', 'Abraham Silberschatz', 'McGraw Hill', 4.7, 1250.00, 9),
(7, 'Computer Organization and Design', 'David A. Patterson', 'Morgan Kaufmann', 4.8, 1499.00, 5),
(8, 'Artificial Intelligence: A Modern Approach', 'Stuart Russell', 'Pearson', 4.9, 1799.00, 4),
(9, 'The C Programming Language', 'Brian W.Kernighan', 'Person', 4.9, 799.00, 14),
(10, 'Python Crash Course', 'Eric Matthes', 'No Starch Press', 4.8, 899.00, 11),
(11, 'The Black Maria', 'unknown', 'unknown', 1.0, 52.15, 3),
(12, 'Reasons to Stay Alive', 'unknown', 'unknown', 2.0, 26.41, 2),
(13, 'Olio', 'unknown', 'unknown', 1.0, 23.88, 3);

-- --------------------------------------------------------

--
-- Table structure for table `issue_book`
--

CREATE TABLE `issue_book` (
  `issue_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `issue_book`
--

INSERT INTO `issue_book` (`issue_id`, `student_id`, `book_id`, `issue_date`, `due_date`, `status`) VALUES
(1, 5, 4, '2026-08-04', '2026-08-19', 'Returned'),
(4, 1, 2, '2026-08-04', '2026-08-19', 'Issued'),
(5, 6, 9, '2026-08-04', '2026-08-19', 'Issued'),
(6, 1, 1, '2026-08-04', '2026-08-19', 'Issued'),
(7, 3, 8, '2026-08-04', '2026-08-19', 'Returned'),
(8, 3, 12, '2026-08-04', '2026-08-19', 'Issued');

-- --------------------------------------------------------

--
-- Table structure for table `return_book`
--

CREATE TABLE `return_book` (
  `return_id` int(11) NOT NULL,
  `issue_id` int(11) DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  `fine` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `return_book`
--

INSERT INTO `return_book` (`return_id`, `issue_id`, `return_date`, `fine`) VALUES
(1, 1, '2026-08-04', 0.00),
(2, 7, '2026-08-04', 0.00);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `role_name`) VALUES
(1, 'admin'),
(2, 'student');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  `semester` int(11) DEFAULT NULL,
  `phone` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `user_id`, `name`, `course`, `semester`, `phone`) VALUES
(1, 2, 'Harvin', 'CSE', 7, 2147483647),
(2, 3, 'Simran', 'CSE', 5, 2147483647),
(3, 4, 'Gagan', 'CSE', 7, 687983099),
(4, 5, 'Rahul', 'M.E', 3, 345675328),
(5, 6, 'Rohit', 'C.E', 6, 2147483647),
(6, 7, 'Neha', 'CSE AIML', 6, 2147483647),
(7, 8, 'Harman', 'CSE AIML', 2, 256485890),
(8, 9, 'Sita', 'A.E', 4, 335674388);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `role_id`) VALUES
(1, 'Admin', '12345', 1),
(2, 'Harvin', 'harvin123', 2),
(3, 'Simran', 'simran123', 2),
(4, 'Gagan', 'gagan123', 2),
(5, 'Rahul', 'rahul123', 2),
(6, 'Rohit', 'rohit123', 2),
(7, 'Neha', 'neha123', 2),
(8, 'Harman', 'harman123', 2),
(9, 'Sita', 'sita123', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `book1`
--
ALTER TABLE `book1`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `issue_book`
--
ALTER TABLE `issue_book`
  ADD PRIMARY KEY (`issue_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `issue_book_ibfk_2` (`book_id`);

--
-- Indexes for table `return_book`
--
ALTER TABLE `return_book`
  ADD PRIMARY KEY (`return_id`),
  ADD KEY `issue_id` (`issue_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `book1`
--
ALTER TABLE `book1`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `issue_book`
--
ALTER TABLE `issue_book`
  MODIFY `issue_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `return_book`
--
ALTER TABLE `return_book`
  MODIFY `return_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `issue_book`
--
ALTER TABLE `issue_book`
  ADD CONSTRAINT `issue_book_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `issue_book_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book1` (`book_id`);

--
-- Constraints for table `return_book`
--
ALTER TABLE `return_book`
  ADD CONSTRAINT `return_book_ibfk_1` FOREIGN KEY (`issue_id`) REFERENCES `issue_book` (`issue_id`);

--
-- Constraints for table `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
