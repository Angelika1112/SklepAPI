-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: sql.freedb.tech
-- Generation Time: Cze 09, 2024 at 08:46 AM
-- Wersja serwera: 8.0.36-0ubuntu0.22.04.1
-- Wersja PHP: 8.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `freedb_StoreDjango`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add item', 8, 'add_item'),
(30, 'Can change item', 8, 'change_item'),
(31, 'Can delete item', 8, 'delete_item'),
(32, 'Can view item', 8, 'view_item'),
(33, 'Can add cart item', 9, 'add_cartitem'),
(34, 'Can change cart item', 9, 'change_cartitem'),
(35, 'Can delete cart item', 9, 'delete_cartitem'),
(36, 'Can view cart item', 9, 'view_cartitem'),
(37, 'Can add order summary', 10, 'add_ordersummary'),
(38, 'Can change order summary', 10, 'change_ordersummary'),
(39, 'Can delete order summary', 10, 'delete_ordersummary'),
(40, 'Can view order summary', 10, 'view_ordersummary');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$6asa5M373g4OLRgAX7Ydiv$+3kMbXNCDHexIKiSTCKJxa41i2vfCe9gahA5vXVJfP0=', '2024-06-09 08:42:48.956306', 1, 'Admin', '', '', 'admin@sklepapi.pl', 1, 1, '2024-06-09 08:42:00.007098'),
(2, 'pbkdf2_sha256$720000$XP1kaGyC3CGSOz9k3KfVek$ADcJXT1oSrtGGAuCAusl2f7dDfeet8k0sHHZS0mmDzs=', NULL, 0, 'ZwyklyUser', '', '', '', 0, 1, '2024-06-09 08:45:28.369295');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-06-09 08:45:28.612843', '2', 'ZwyklyUser', 1, '[{\"added\": {}}]', 4, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(9, 'storeapp', 'cartitem'),
(7, 'storeapp', 'category'),
(8, 'storeapp', 'item'),
(10, 'storeapp', 'ordersummary');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-06-08 19:46:19.192442'),
(2, 'auth', '0001_initial', '2024-06-08 19:46:20.192858'),
(3, 'admin', '0001_initial', '2024-06-08 19:46:20.440481'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-06-08 19:46:20.480034'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-06-08 19:46:20.505005'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-06-08 19:46:20.699693'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-06-08 19:46:20.802693'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-06-08 19:46:20.861233'),
(9, 'auth', '0004_alter_user_username_opts', '2024-06-08 19:46:20.886249'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-06-08 19:46:20.974884'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-06-08 19:46:20.996888'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-06-08 19:46:21.021916'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-06-08 19:46:21.123334'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-06-08 19:46:21.223097'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-06-08 19:46:21.280146'),
(16, 'auth', '0011_update_proxy_permissions', '2024-06-08 19:46:21.362484'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-06-08 19:46:21.458237'),
(18, 'sessions', '0001_initial', '2024-06-08 19:46:21.601950'),
(19, 'storeapp', '0001_initial', '2024-06-08 19:46:21.784676'),
(20, 'storeapp', '0002_alter_category_id_alter_item_id', '2024-06-08 19:46:22.177491'),
(21, 'storeapp', '0003_cartitem', '2024-06-08 19:46:22.239050'),
(22, 'storeapp', '0004_alter_cartitem_cartid', '2024-06-08 19:46:22.261857'),
(23, 'storeapp', '0005_ordersummary_alter_cartitem_cartid', '2024-06-08 19:46:22.378196');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('s83928h7wjrzjt8br1luxlsmtj0n2mgj', '.eJxVjMsOgjAUBf-la9Nw-5DWpXu-gdwXgpqSUFgZ_11JWOj2zMx5mR63dey3qks_ibkYMKffjZAfWnYgdyy32fJc1mUiuyv2oNV2s-jzerh_ByPW8VtnRSUCwIznHBIhuCQg1LiYaGiylzYG8ZHQMwDFkELjUjuoMnsd2Lw_9dk4gw:1sGE8W:rtYqUpdLfhzFW6cp-8OQI0SDkzrBq7ADG-M8kT4YmEc', '2024-06-23 08:42:48.980477');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `storeapp_cartitem`
--

CREATE TABLE `storeapp_cartitem` (
  `id` bigint NOT NULL,
  `cartId` varchar(36) NOT NULL,
  `itemId` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `storeapp_cartitem`
--

INSERT INTO `storeapp_cartitem` (`id`, `cartId`, `itemId`) VALUES
(8, '2f1e2e59-5417-45fe-8206-9aa6c59f96b6', 2),
(9, '2f1e2e59-5417-45fe-8206-9aa6c59f96b6', 2),
(10, '2f1e2e59-5417-45fe-8206-9aa6c59f96b6', 2),
(11, '2f1e2e59-5417-45fe-8206-9aa6c59f96b6', 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `storeapp_category`
--

CREATE TABLE `storeapp_category` (
  `id` int NOT NULL,
  `name` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `storeapp_category`
--

INSERT INTO `storeapp_category` (`id`, `name`) VALUES
(1, 'Makijaż'),
(2, 'Włosy'),
(3, 'Pielęgnacja');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `storeapp_item`
--

CREATE TABLE `storeapp_item` (
  `id` int NOT NULL,
  `name` varchar(25) NOT NULL,
  `quantity` int NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `imageUrl` varchar(200) NOT NULL,
  `category_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `storeapp_item`
--

INSERT INTO `storeapp_item` (`id`, `name`, `quantity`, `price`, `imageUrl`, `category_id`) VALUES
(1, 'Podkład', 7, 60.00, 'https://img.freepik.com/darmowe-zdjecie/fundament-brandingu-produktu-martwa-natura_23-2149665122.jpg?t=st=1717921671~exp=1717925271~hmac=b47fd3601e426a4436ab679eeb97d4edfb6f42af03f2fe12609a63c1b05a7a7', 1),
(2, 'Błyszczyk', 11, 39.99, 'https://img.freepik.com/darmowe-zdjecie/uklad-balsamu-do-ust-z-jasnym-niebem-pod-wysokim-katem_23-2149681508.jpg?t=st=1717921968~exp=1717925568~hmac=f2c38bbdc81b3d528a7a0598c40fbfe8af6bd7d481fc638c889', 1),
(3, 'Róż', 30, 40.50, 'https://img.freepik.com/darmowe-zdjecie/owalny-pedzel-i-kompaktowy-puder-do-twarzy-na-bialym-tle_23-2148074004.jpg?t=st=1717922073~exp=1717925673~hmac=79a19b2ca4d937be13d107378b002805c7a7ce30296cf1a4a', 1),
(4, 'Farba', 25, 15.99, 'https://img.freepik.com/darmowe-zdjecie/widok-z-boku-kobieta-w-salonie-fryzjerskim_23-2150668447.jpg?t=st=1717922191~exp=1717925791~hmac=04f2ee458523e2e8ce930be32b90ea65c7288aa6426a2254d066c3e277d8e92', 3);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `storeapp_ordersummary`
--

CREATE TABLE `storeapp_ordersummary` (
  `id` int NOT NULL,
  `itemList` varchar(200) NOT NULL,
  `totalPrice` decimal(5,2) NOT NULL,
  `firstName` varchar(15) NOT NULL,
  `lastName` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `street` varchar(25) NOT NULL,
  `homeNumber` varchar(10) NOT NULL,
  `zipCode` varchar(6) NOT NULL,
  `phoneNumber` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `storeapp_ordersummary`
--

INSERT INTO `storeapp_ordersummary` (`id`, `itemList`, `totalPrice`, `firstName`, `lastName`, `city`, `street`, `homeNumber`, `zipCode`, `phoneNumber`) VALUES
(1, '{1:3,2:4}', 339.96, 'Angelika', 'Olszewska', 'Warszawa', 'Warszawska', '12', '12-345', '123456789');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indeksy dla tabeli `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indeksy dla tabeli `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indeksy dla tabeli `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indeksy dla tabeli `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indeksy dla tabeli `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indeksy dla tabeli `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indeksy dla tabeli `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indeksy dla tabeli `storeapp_cartitem`
--
ALTER TABLE `storeapp_cartitem`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `storeapp_category`
--
ALTER TABLE `storeapp_category`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `storeapp_item`
--
ALTER TABLE `storeapp_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `storeapp_item_category_id_5cb0a744_fk` (`category_id`);

--
-- Indeksy dla tabeli `storeapp_ordersummary`
--
ALTER TABLE `storeapp_ordersummary`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `storeapp_cartitem`
--
ALTER TABLE `storeapp_cartitem`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `storeapp_category`
--
ALTER TABLE `storeapp_category`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `storeapp_item`
--
ALTER TABLE `storeapp_item`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `storeapp_ordersummary`
--
ALTER TABLE `storeapp_ordersummary`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `storeapp_item`
--
ALTER TABLE `storeapp_item`
  ADD CONSTRAINT `storeapp_item_category_id_5cb0a744_fk` FOREIGN KEY (`category_id`) REFERENCES `storeapp_category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
