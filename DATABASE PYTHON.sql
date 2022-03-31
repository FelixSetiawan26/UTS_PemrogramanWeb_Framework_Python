-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2022 at 11:19 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uts_python`
--
CREATE DATABASE IF NOT EXISTS `uts_python` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `uts_python`;

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `nim` varchar(10) NOT NULL,
  `nama_mahasiswa` varchar(100) NOT NULL,
  `jurusan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`nim`, `nama_mahasiswa`, `jurusan`) VALUES
('32190034', 'Felix Setiawan', 'Teknik Informatika'),
('32190036', 'Josef Christian Adi Putra', 'Budaya Bahasa Inggris'),
('32190040', 'Andry', 'Teknik Mesin'),
('32190041', 'Kelvin Chandra', 'Teknik Informatika'),
('32190042', 'Eufrasia Paskasius', 'Sistem Informasi'),
('32190045', 'Ferdyan Erick', 'Teknik Industri'),
('32190048', 'Kevin Kusuma', 'Teknik Mesin'),
('32190049', 'Jamal Permana', 'Teknik Industri'),
('32190051', 'Ignatius Arya Praditya', 'Ilmu Komunikasi'),
('32190052', 'Samuel Sulianto', 'Teknik Informatika'),
('32190061', 'Alvin Wiryawan', 'Psikologi'),
('32190062', 'Hoki Saputra', 'Psikologi'),
('32190069', 'Christian Bernard', 'Budaya Bahasa Tionghoa'),
('32190090', 'Martinus Suryadi', 'Ilmu Komunikasi'),
('32190096', 'Budy Haryono', 'Psikologi'),
('32190097', 'Reynaldo Krisno', 'Teknik Informatika'),
('32190098', 'Ferry Gunawan', 'Sistem Informasi'),
('32190105', 'Persan Raj', 'Desain Komunikasi Visual');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `kode_buku` varchar(5) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `stok` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`kode_buku`, `judul`, `stok`) VALUES
('B001', 'Kamus Besar Bahasa Indonesia', '81'),
('B002', 'Kamus Inggris - Indonesia', '43'),
('B003', 'Kamus Mandarin - Indonesia', '99'),
('B004', 'Laskar Pelangi', '103'),
('B005', 'Sang Pemimpi', '490'),
('B006', 'Nanti Kita Cerita Tentang Hari Ini', '104'),
('B007', 'Filosofi Teras', '379'),
('B008', 'Manusia Setengah Salmon', '29'),
('B009', 'Moga Bunda Disayang Allah', '74'),
('B010', 'Babi Nge.Sot', '72'),
('B011', 'Habis Gelap Terbitlah Terang', '1038'),
('B012', 'Laut Bercerita', '19'),
('B013', 'Pagi di Amerika Single Edition', '42'),
('B014', 'Pengantar Matematika Ekonomi', '92'),
('B015', 'Matematika Terapan', '83');

-- --------------------------------------------------------

--
-- Table structure for table `kembali`
--

CREATE TABLE `kembali` (
  `kode_kembali` varchar(5) NOT NULL,
  `kode_buku` varchar(5) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `tgl_kembali` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kembali`
--

INSERT INTO `kembali` (`kode_kembali`, `kode_buku`, `nim`, `tgl_kembali`) VALUES
('K001', 'B011', '32190090', '2022-03-30'),
('K002', 'B012', '32190069', '2022-04-09'),
('K003', 'B006', '32190062', '2022-03-14'),
('K004', 'B010', '32190096', '2022-04-10'),
('K005', 'B007', '32190105', '2021-11-18');

-- --------------------------------------------------------

--
-- Table structure for table `pinjam`
--

CREATE TABLE `pinjam` (
  `kode_pinjam` varchar(5) NOT NULL,
  `kode_buku` varchar(5) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `tgl_pinjam` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pinjam`
--

INSERT INTO `pinjam` (`kode_pinjam`, `kode_buku`, `nim`, `tgl_pinjam`) VALUES
('P001', 'B004', '32190049', '2022-03-30'),
('P002', 'B011', '32190097', '2022-03-20'),
('P003', 'B010', '32190034', '2022-03-31'),
('P004', 'B006', '32190051', '2022-03-31'),
('P005', 'B010', '32190105', '2022-12-23');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `nama` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`nama`, `email`, `password`) VALUES
('Administrator', 'admin123@gmail.com', 'admin123'),
('Reynaldo Krisno', 'rey@gmail.com', 'rey123'),
('Felix Setiawan', 's32190034@student.ubm.ac.id', 'felix123'),
('Samuel Sulianto', 'samuel@gmail.com', 'samuel123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`nim`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`kode_buku`);

--
-- Indexes for table `kembali`
--
ALTER TABLE `kembali`
  ADD PRIMARY KEY (`kode_kembali`),
  ADD KEY `kode_buku` (`kode_buku`),
  ADD KEY `nim` (`nim`);

--
-- Indexes for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD PRIMARY KEY (`kode_pinjam`),
  ADD KEY `nim` (`nim`),
  ADD KEY `kode_buku` (`kode_buku`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `kembali`
--
ALTER TABLE `kembali`
  ADD CONSTRAINT `kembali_ibfk_1` FOREIGN KEY (`kode_buku`) REFERENCES `buku` (`kode_buku`),
  ADD CONSTRAINT `kembali_ibfk_2` FOREIGN KEY (`nim`) REFERENCES `anggota` (`nim`);

--
-- Constraints for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD CONSTRAINT `pinjam_ibfk_1` FOREIGN KEY (`nim`) REFERENCES `anggota` (`nim`),
  ADD CONSTRAINT `pinjam_ibfk_2` FOREIGN KEY (`kode_buku`) REFERENCES `buku` (`kode_buku`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
