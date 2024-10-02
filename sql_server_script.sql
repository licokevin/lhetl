USE [master]
GO
/****** Object:  Database [LH]    Script Date: 10/2/2024 10:17:16 AM ******/
CREATE DATABASE [LH]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'LH', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\LH.mdf' , SIZE = 73728KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'LH_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\LH_log.ldf' , SIZE = 139264KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [LH] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [LH].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [LH] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [LH] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [LH] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [LH] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [LH] SET ARITHABORT OFF 
GO
ALTER DATABASE [LH] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [LH] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [LH] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [LH] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [LH] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [LH] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [LH] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [LH] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [LH] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [LH] SET  DISABLE_BROKER 
GO
ALTER DATABASE [LH] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [LH] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [LH] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [LH] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [LH] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [LH] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [LH] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [LH] SET RECOVERY FULL 
GO
ALTER DATABASE [LH] SET  MULTI_USER 
GO
ALTER DATABASE [LH] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [LH] SET DB_CHAINING OFF 
GO
ALTER DATABASE [LH] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [LH] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [LH] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [LH] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'LH', N'ON'
GO
ALTER DATABASE [LH] SET QUERY_STORE = ON
GO
ALTER DATABASE [LH] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [LH]
GO
/****** Object:  Table [dbo].[db_customers_df]    Script Date: 10/2/2024 10:17:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[db_customers_df](
	[customer_id] [varchar](max) NULL,
	[customer_unique_id] [varchar](max) NULL,
	[customer_zip_code_prefix] [bigint] NULL,
	[customer_city] [varchar](max) NULL,
	[customer_state] [varchar](max) NULL,
	[geolocation_lat] [float] NULL,
	[geolocation_lng] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[db_order_items]    Script Date: 10/2/2024 10:17:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[db_order_items](
	[order_id] [varchar](max) NULL,
	[order_item_id] [bigint] NULL,
	[product_id] [varchar](max) NULL,
	[seller_id] [varchar](max) NULL,
	[shipping_limit_date] [varchar](max) NULL,
	[price] [float] NULL,
	[freight_value] [float] NULL,
	[total_price] [float] NULL,
	[delivery_time] [bigint] NULL,
	[profit_margin] [float] NULL,
	[customer_id] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[db_order_purchase_date]    Script Date: 10/2/2024 10:17:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[db_order_purchase_date](
	[order_purchase_timestamp] [varchar](max) NULL,
	[order_delivered_customer_date] [varchar](max) NULL,
	[delivery_time] [bigint] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[db_products]    Script Date: 10/2/2024 10:17:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[db_products](
	[product_id] [varchar](max) NULL,
	[product_category_name] [varchar](max) NULL,
	[product_name_lenght] [varchar](max) NULL,
	[product_description_lenght] [float] NULL,
	[product_photos_qty] [float] NULL,
	[product_weight_g] [varchar](max) NULL,
	[product_length_cm] [varchar](max) NULL,
	[product_height_cm] [float] NULL,
	[product_width_cm] [varchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[db_sellers]    Script Date: 10/2/2024 10:17:16 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[db_sellers](
	[seller_id] [varchar](max) NULL,
	[seller_zip_code_prefix] [bigint] NULL,
	[seller_city] [varchar](max) NULL,
	[seller_state] [varchar](max) NULL,
	[geolocation_lat] [float] NULL,
	[geolocation_lng] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [LH] SET  READ_WRITE 
GO
