try:
    import pymysql
    # Use PyMySQL as MySQLdb replacement
    pymysql.install_as_MySQLdb()
except ImportError:
    # If pymysql is not installed, use mysqlclient instead
    pass
