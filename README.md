# Advertisement Revenue Predictor - Streamlit Version

A machine learning web application built with **Streamlit** that predicts daily advertisement revenue based on website traffic.

## 🚀 Live Demo
After deployment, your app will be accessible at: `https://your-app-name.streamlit.app`

## 📁 Project Files
```
streamlit-app/
├── app.py              # Streamlit application
└── requirements.txt    # Python dependencies
```

## 🖥️ Local Setup

### Prerequisites
- Python 3.7+
- pip

### Run Locally

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the app:**
```bash
streamlit run app.py
```

3. **Open browser:**
The app will automatically open at `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud (FREE)

### Step-by-Step Deployment:

#### **Step 1: Create GitHub Repository**

1. Go to [GitHub.com](https://github.com) and create a new repository
   - Repository name: `ad-revenue-predictor`
   - Make it Public
   - Don't add README (we already have one)

2. Upload your files:
   - Click "uploading an existing file"
   - Drag and drop both `app.py` and `requirements.txt`
   - Commit changes

#### **Step 2: Deploy on Streamlit Cloud**

1. Go to [share.streamlit.io](https://share.streamlit.io)

2. Sign in with your GitHub account

3. Click **"New app"**

4. Fill in the details:
   - **Repository:** Select `your-username/ad-revenue-predictor`
   - **Branch:** `main` (or `master`)
   - **Main file path:** `app.py`

5. Click **"Deploy"**

6. Wait 2-3 minutes for deployment

7. Your app will be live at: `https://your-app-name.streamlit.app`

#### **Step 3: Share Your App**

- Copy the URL and share it anywhere
- The app is publicly accessible
- No server management needed!

## 📊 How It Works

### User Flow:
1. User enters daily website visitors
2. Clicks "Calculate Revenue"
3. App predicts revenue using Linear Regression
4. Shows daily, monthly, and yearly projections

### Model Logic:
```python
Revenue = 0.5 × Visitors

Example:
5,000 visitors → ₹2,500/day
10,000 visitors → ₹5,000/day
```

## ✨ Features

- 📊 Real-time predictions
- 💰 Monthly and yearly revenue projections
- 📈 Training data visualization
- 🎨 Beautiful gradient UI
- 📱 Mobile responsive
- 🔄 Auto-saves model

## 🛠️ Technologies

- **Framework:** Streamlit
- **ML Library:** scikit-learn
- **Data Processing:** pandas, numpy
- **Deployment:** Streamlit Cloud (FREE)

## 📸 Screenshots

The app includes:
- Input field for visitor count
- Calculate button
- Revenue prediction display
- Monthly/yearly projections
- Sidebar with model information
- Training data table

## 🎓 Assignment Requirements Met

✅ Machine Learning Model (Linear Regression)  
✅ Web Interface (Streamlit UI)  
✅ Backend Logic (Model prediction)  
✅ Deployed on Web (Streamlit Cloud)  
✅ Accessible via Browser (Public URL)  

## 🔧 Troubleshooting

**App not loading?**
- Check if requirements.txt is present
- Verify app.py has no syntax errors
- Make sure repository is public

**Model not training?**
- The model trains automatically on first run
- model.pkl is generated in the app directory

**Deployment failed?**
- Check Streamlit Cloud logs
- Ensure all dependencies are in requirements.txt
- Verify Python version compatibility

## 📝 Notes

- Streamlit Cloud offers **FREE hosting** for public apps
- No credit card required
- Automatic HTTPS
- Apps sleep after inactivity but wake up instantly
- You can deploy multiple apps on free tier

## 🎯 Why Streamlit?

Compared to Flask + HTML:
- ✅ No need to write HTML/CSS/JavaScript
- ✅ Everything in Python
- ✅ Faster development
- ✅ Free hosting included
- ✅ Auto-reload on code changes
- ✅ Built-in widgets and styling

## 📞 Support

For Streamlit deployment help:
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Community](https://discuss.streamlit.io)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

---

**Created for:** ML Capstone Lab Assignment  
**Institution:** KIIT University  
**Deployment:** Streamlit Cloud (FREE)

---

## Quick Deploy Checklist

- [ ] Create GitHub repository
- [ ] Upload app.py and requirements.txt
- [ ] Go to share.streamlit.io
- [ ] Sign in with GitHub
- [ ] Click "New app"
- [ ] Select your repository
- [ ] Set main file as app.py
- [ ] Click Deploy
- [ ] Share your URL! 🎉
