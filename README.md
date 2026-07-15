# 💳 Credit Card Approval Prediction System

## 📖 Overview

Credit Card Approval Prediction System is an AI-powered Credit Card Approval Prediction application that predicts whether a customer's credit card application will be approved based on applicant details and financial information. The application features a modern, responsive web interface built using Flask, HTML, and CSS, enabling users to receive real-time credit approval predictions through a trained Machine Learning model. It helps banks and financial institutions automate the approval process, improve decision-making, and reduce manual effort.

## 🚀 Features

- 💳 AI-powered credit card approval prediction
- 📊 Machine Learning-based prediction model
- 📝 Accepts applicant details for prediction:
  - Gender
  - Car Ownership
  - Property Ownership
  - Number of Children
  - Annual Income
  - Income Type
  - Education Type
  - Family Status
  - Housing Type
  - Days Birth
  - Days Employed
  - Mobile Phone
  - Work Phone
  - Phone
  - Email
  - Occupation Type
  - Family Members
- ⚡ Instant credit approval prediction
- 💻 Modern responsive web interface
- 📱 Mobile-friendly design
- 🔒 Fast and reliable prediction system
- 🏦 Supports smart financial decision-making

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- NumPy
- Scikit-learn
- Joblib

## 📂 Project Structure

```text
CreditCardApprovalPrediction/
│
├── dataset/
│   ├── application_record.csv
│   └── credit_record.csv
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── app.py
├── test_model.py
├── data_preprocessing.py
├── model.pkl
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

## 📊 Machine Learning Model

| Model |                    Accuracy |

| Random Forest Classifier | 88.04% |

### ⭐ Best Model

**Random Forest Classifier**

## 📁 Dataset

The Credit Card Approval dataset contains:

- Application Records
- Credit Records
- Applicant Information
- Financial Details
- Employment Details

### Input Features

- Gender
- Car Ownership
- Property Ownership
- Number of Children
- Annual Income
- Income Type
- Education Type
- Family Status
- Housing Type
- Days Birth
- Days Employed
- Mobile Phone
- Work Phone
- Phone
- Email
- Occupation Type
- Family Members

### Output

**Credit Card Approval Status**

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Keerthireddy0103/CreditCardApprovalPrediction.git
```

Navigate to the project

```bash
cd CreditCardApprovalPrediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Train the Machine Learning Model

```bash
python test_model.py
```

## 🌐 Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## 📷 Application Screens

## 📈 Model Workflow

- Load the application and credit datasets
- Perform data preprocessing
- Merge the datasets
- Encode categorical features
- Split the dataset into training and testing sets
- Train the Random Forest model
- Evaluate model performance
- Save the trained model
- Integrate the model with Flask
- Generate real-time credit card approval predictions

## 🚀 Deployment

The application is deployed using Render and can be accessed through a public web URL for real-time credit card approval prediction.

**Live Demo:** *https://drive.google.com/file/d/1cRpB8OWsOxHzVwIaPbzJcmj7uBitTFBg/view?usp=drivesdk

## 📌 Future Enhancements

- 📊 Credit score visualization
- 🤖 Explainable AI predictions
- 📱 Mobile application
- 🔐 User authentication
- ☁️ Cloud database integration
- 📄 PDF report generation
- 🌍 Multi-language support

## 👤 Team Members

- Kummithi Keerthi Reddy (Team Lead)
- Aswini Chitreddy (Member)
- Perapogu Mani Kumari (Member)
- Syed Sahil Ahmed (Member)
- Aswini Chitreddy (Member)

## 📄 License

This project is developed for educational purposes as part of an academic Machine Learning project.
