# Database Setup Guide - PostgreSQL Integration

## 🗄️ Database Configuration

Your Fee Management System is now configured to use the **PostgreSQL database** from Render with the following details:

### Database Connection Details
- **Host**: `dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com`
- **Port**: `5432`
- **Database**: `vemu_fee`
- **Username**: `vemu_fee_user`
- **Password**: `SoaqripTGHMX16rb79Jyylq60CiF6Z1Z`

### Connection URLs
- **External URL**: `postgresql://vemu_fee_user:SoaqripTGHMX16rb79Jyylq60CiF6Z1Z@dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com/vemu_fee`
- **Internal URL**: `postgresql://vemu_fee_user:SoaqripTGHMX16rb79Jyylq60CiF6Z1Z@dpg-d31353d6ubrc73c1jfmg-a/vemu_fee`

## 🔧 Changes Made

### 1. Updated Database Configuration
- Modified `main.py` to use PostgreSQL instead of SQLite
- Created `config.py` with database connection details
- Updated both development and production configurations

### 2. Added Required Dependencies
- `psycopg2-binary==2.9.7` - PostgreSQL driver for Python
- Updated `requirements.txt` with proper PostgreSQL support

### 3. Created Database Test Script
- `test_database.py` - Tests database connectivity
- Validates both direct PostgreSQL and Flask-SQLAlchemy connections

## 🚀 How to Run with PostgreSQL

### Step 1: Install Dependencies
```bash
# Run the installation script
install_dependencies.bat

# Or install manually
pip install -r requirements.txt
```

### Step 2: Test Database Connection
```bash
# Test the database connection
python test_database.py
```

### Step 3: Run the Application
```bash
# Start the application
python main.py

# Or use the batch file
run_app.bat
```

## 📊 Database Schema

The application will automatically create the following tables:

### Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    biometric_id VARCHAR(256),
    face_data TEXT,
    auth_method VARCHAR(20)
);
```

### Students Table
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    gender VARCHAR(10),
    category VARCHAR(50) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    branch VARCHAR(50) NOT NULL,
    fee_type VARCHAR(50),
    bill_number VARCHAR(50),
    total_fees NUMERIC(10,2) DEFAULT 0,
    paid_amount NUMERIC(10,2) DEFAULT 0,
    pending_amount NUMERIC(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    biometric_id VARCHAR(256) UNIQUE
);
```

### Transactions Table
```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE NOT NULL,
    student_id INTEGER REFERENCES students(id),
    amount NUMERIC(10,2) NOT NULL,
    fee_type VARCHAR(50) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    utr_number VARCHAR(50),
    bill_number VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pending',
    verification_comment TEXT,
    verified_by INTEGER REFERENCES users(id),
    verified_at TIMESTAMP,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mobile_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Complaints Table
```sql
CREATE TABLE complaints (
    id SERIAL PRIMARY KEY,
    complaint_id VARCHAR(50) UNIQUE NOT NULL,
    student_id INTEGER REFERENCES students(id),
    subject VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    response TEXT,
    responded_by INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔍 Testing Database Connection

### Manual Connection Test
```bash
# Using psql command line
PGPASSWORD=SoaqripTGHMX16rb79Jyylq60CiF6Z1Z psql -h dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com -U vemu_fee_user vemu_fee
```

### Python Test Script
```bash
# Run the database test script
python test_database.py
```

## 🛠️ Troubleshooting

### Common Issues

1. **Connection Timeout**
   - Check your internet connection
   - Verify the database is running on Render

2. **Authentication Failed**
   - Verify username and password are correct
   - Check if the database user has proper permissions

3. **Module Not Found (psycopg2)**
   - Install PostgreSQL driver: `pip install psycopg2-binary`
   - Or run: `install_dependencies.bat`

4. **Database Not Found**
   - Verify the database name `vemu_fee` exists
   - Check if the database is accessible from your IP

### Debug Information

The application will show database connection information on startup:
```
Database Configuration:
  Host: dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com
  Port: 5432
  Database: vemu_fee
  Username: vemu_fee_user
  URL: postgresql://vemu_fee_user:SoaqripTGHMX16rb79Jyylq60CiF6Z1Z@dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com/vemu_fee
```

## 🔒 Security Notes

- Database credentials are stored in `config.py`
- For production, use environment variables
- Consider using connection pooling for better performance
- Enable SSL connections for production use

## 📈 Performance Considerations

- PostgreSQL is more robust than SQLite for production use
- Supports concurrent connections
- Better performance for large datasets
- Built-in backup and recovery features

## 🎯 Next Steps

1. **Test the connection**: Run `python test_database.py`
2. **Start the application**: Run `python main.py`
3. **Verify tables**: Check if tables are created automatically
4. **Test functionality**: Login and create some test data

---

**✅ Your Fee Management System is now ready to use with PostgreSQL!**
