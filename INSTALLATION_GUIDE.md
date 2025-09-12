# Fee Management System - Installation and Setup Guide

## Issues Fixed

### 1. Permission Error
**Problem**: The application was trying to create directories in the PowerShell system directory, causing permission errors.

**Solution**: 
- Fixed the working directory issue by creating batch and PowerShell scripts
- The application now runs from the correct project directory

### 2. Code Issues Fixed
- **Duplicate return statement** in `/employloginpage` route (line 185)
- **Duplicate import statements** (lines 61-66)
- **Biometric authentication logic errors** - Fixed conditional logic for biometric and face authentication

### 3. Database Configuration
- Fixed SQLite database path configuration
- Ensured proper directory creation for instance and logs folders

## Installation Steps

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install Flask==2.3.3
pip install Flask-SQLAlchemy==3.0.5
pip install Flask-Migrate==4.0.5
pip install Flask-CORS==4.0.0
pip install Werkzeug==2.3.7
pip install requests==2.31.0
pip install python-dotenv==1.0.0
pip install gunicorn==23.0.0
pip install psycopg2-binary==2.9.7
pip install PyMySQL==1.1.0
pip install cryptography==41.0.4
```

### Step 2: Run the Application

#### Option 1: Using Batch File (Windows)
Double-click `run_app.bat` or run:
```cmd
run_app.bat
```

#### Option 2: Using PowerShell Script
Right-click `run_app.ps1` and select "Run with PowerShell" or run:
```powershell
.\run_app.ps1
```

#### Option 3: Manual Command
```bash
cd "c:\Users\prave\Documents\fee_management_system709_(4)[1]\fee management system709 (3)\fee management system709"
python main.py
```

### Step 3: Access the Application
- Open your web browser
- Navigate to: `http://localhost:5000`
- The application will automatically create the database and default users

## Default Users Created

### Admin User
- **Email**: admin@example.com
- **Password**: admin123
- **Role**: admin

### Demo Employee
- **Email**: vemuit@gmail.com
- **Password**: vemuit@2008
- **Role**: employee

### Student Login
- **Password**: vemuit@2008 (for all students)

## Features

### Student Features
- Student login with roll number
- Submit fee transactions
- View payment history
- Submit complaints
- View payment details by academic year

### Employee Features
- Employee login with email/password
- Biometric authentication support
- Face recognition authentication support
- Verify/reject student transactions
- Manage student records
- View all students and statistics

### Admin Features
- All employee features
- User management
- System administration

## API Endpoints

### Authentication
- `POST /api/student/auth` - Student authentication
- `POST /api/employee/auth` - Employee authentication
- `POST /api/employee/register` - Employee registration
- `GET /api/logout` - Logout

### Student Operations
- `POST /api/student/submit-transaction` - Submit fee payment
- `GET /api/student/payment-details/<roll_number>` - Get payment details
- `POST /api/student/complaint` - Submit complaint
- `GET /api/student/transactions/<roll_number>` - Get transaction history
- `GET /api/student/complaints/<roll_number>` - Get complaint history

### Employee Operations
- `POST /api/verify-transaction` - Verify/reject transactions
- `GET /api/students/list` - Get all students
- `POST /api/students/filter` - Filter students
- `POST /api/students` - Add new student
- `POST /api/student/save` - Save student data

## Database Structure

### Tables Created
- `users` - Employee and admin users
- `students` - Student information and fee data
- `transactions` - Fee payment transactions
- `complaints` - Student complaints

## Troubleshooting

### Common Issues

1. **Permission Error**
   - Solution: Use the provided batch/PowerShell scripts or run from the correct directory

2. **Module Not Found**
   - Solution: Install all required packages using pip

3. **Database Error**
   - Solution: The application will create the database automatically on first run

4. **Port Already in Use**
   - Solution: Change the port in main.py or stop other applications using port 5000

### Logs
- Application logs are stored in the `logs/app.log` file
- Database is stored in `instance/fee_management.db`

## Development

### Running in Development Mode
The application runs in debug mode by default. To run in production:
1. Set environment variable: `FLASK_ENV=production`
2. Update database configuration for production database
3. Use a production WSGI server like Gunicorn

### Database Migrations
The application uses Flask-Migrate for database migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Security Notes

- Change default passwords in production
- Use environment variables for sensitive configuration
- Enable HTTPS in production
- Implement proper session management
- Add rate limiting for API endpoints

## Support

If you encounter any issues:
1. Check the logs in `logs/app.log`
2. Verify all dependencies are installed
3. Ensure you're running from the correct directory
4. Check that port 5000 is available
