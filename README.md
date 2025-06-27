# Rainfall Prediction Web Application

A Django-based web application that predicts rainfall using machine learning. The application uses a trained Random Forest model to predict whether it will rain based on temperature, humidity, and wind speed inputs.

## 🌧️ Features

- **Interactive Web Interface**: User-friendly form to input weather parameters
- **Real-time Predictions**: Instant rainfall predictions with probability scores
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Machine Learning Integration**: Uses a pre-trained Random Forest classifier
- **Visual Results**: Beautiful charts and icons to display prediction results
- **Input Validation**: Client and server-side validation for all inputs
- **Error Handling**: Comprehensive error management and user feedback

## 🔧 Technologies Used

- **Backend**: Django 5.2.3, Python 3.10+
- **Machine Learning**: scikit-learn, pandas, joblib
- **Frontend**: HTML5, CSS3, Bootstrap 5.1.3
- **Icons**: Font Awesome 6.0
- **Database**: SQLite (default Django database)

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher installed
- pip (Python package installer)
- A trained Random Forest model saved as `rainfall_model.pkl`

## 🚀 Installation

### 1. Clone or Download the Project

```bash
# If using Git
git clone <repository-url>
cd rainfall_prediction

# Or create a new directory and copy files
mkdir rainfall_prediction
cd rainfall_prediction
```

### 2. Install Required Packages

```bash
pip install django scikit-learn pandas joblib
```

### 3. Set Up Django Project

```bash
# Create Django project
django-admin startproject rainfall_predictor .

# Create the prediction app
python manage.py startapp prediction

# Apply database migrations
python manage.py migrate
```

### 4. Add Your Model File

Copy your trained `rainfall_model.pkl` file to the project root directory:

```bash
# Copy your model file
copy "path/to/your/rainfall_model.pkl" .
```

## 📁 Project Structure

```
rainfall_prediction/
├── manage.py
├── rainfall_model.pkl              # Your trained ML model
├── db.sqlite3                      # Django database
├── README.md                       # This file
├── rainfall_predictor/             # Main Django project
│   ├── __init__.py
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
└── prediction/                     # Django app for predictions
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py                    # Main application logic
    ├── urls.py                     # App URL patterns
    ├── forms.py                    # Django forms
    ├── tests.py
    ├── migrations/
    └── templates/
        └── prediction/
            ├── base.html           # Base template
            ├── predict.html        # Prediction form
            └── result.html         # Results display
```

## ⚙️ Configuration

### Django Settings

The main configuration is in `rainfall_predictor/settings.py`:

- **SECRET_KEY**: Generate a new secret key for production
- **DEBUG**: Set to `False` in production
- **INSTALLED_APPS**: Includes the `prediction` app
- **ML_MODEL_PATH**: Path to your trained model file

### Model Requirements

Your `rainfall_model.pkl` should be a scikit-learn RandomForestClassifier that:
- Accepts 3 features: `[temperature, humidity, windspeed]` (in this exact order)
- Returns binary predictions: `0` (no rain) or `1` (rain)
- Supports `predict_proba()` method for probability estimates

## 🎯 Usage

### 1. Start the Development Server

```bash
python manage.py runserver
```

### 2. Access the Application

Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```

### 3. Make Predictions

1. **Enter Weather Data**:
   - Temperature (°C): Range -50 to 60
   - Humidity (%): Range 0 to 100
   - Wind Speed (km/h): Range 0 to 200

2. **Submit the Form**: Click "Predict Rainfall"

3. **View Results**: See the prediction with probability percentages

### 4. Example Input Values

```
Temperature: 25.0°C
Humidity: 80.0%
Wind Speed: 15.0 km/h
```

## 🔍 How It Works

### Machine Learning Pipeline

1. **Data Input**: User enters temperature, humidity, and wind speed
2. **Data Validation**: Django forms validate input ranges and types
3. **Model Loading**: Application loads the pre-trained Random Forest model
4. **Prediction**: Model processes the input and returns prediction + probabilities
5. **Results Display**: User sees formatted results with visual indicators

### Model Integration

The application integrates with your ML model through:

```python
# Load the model
model = joblib.load('rainfall_model.pkl')

# Make prediction
input_data = [[temperature, humidity, windspeed]]
prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]
```

## 🎨 User Interface

### Design Features

- **Modern Gradient Design**: Beautiful purple gradient background
- **Responsive Layout**: Bootstrap-based responsive design
- **Interactive Elements**: Hover effects and smooth transitions
- **Visual Feedback**: Icons and progress bars for results
- **Form Validation**: Real-time input validation with helpful messages

### Pages

1. **Home/Prediction Page** (`/`): Main form for inputting weather data
2. **Results Page** (`/result/`): Displays prediction results and probabilities

## 🛠️ Development

### Adding New Features

1. **Custom Models**: Replace `rainfall_model.pkl` with your own trained model
2. **Additional Features**: Modify forms and views to include more weather parameters
3. **Styling**: Customize CSS in the templates for different themes
4. **Database**: Add models to store prediction history

### Testing

```bash
# Run Django tests
python manage.py test

# Test with sample data
python manage.py shell
>>> from prediction.views import load_model
>>> model = load_model()
>>> model.predict([[25.0, 80.0, 15.0]])
```

## 🚨 Common Issues & Solutions

### Model Not Found Error
```
Error: Could not load the prediction model.
```
**Solution**: Ensure `rainfall_model.pkl` is in the project root directory.

### Import Errors
```
ModuleNotFoundError: No module named 'sklearn'
```
**Solution**: Install required packages:
```bash
pip install scikit-learn pandas joblib
```

### Migration Warnings
```
You have unapplied migrations
```
**Solution**: Run migrations:
```bash
python manage.py migrate
```
