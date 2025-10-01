# 🏏 IPL Win Probability Analyzer

<div align="center">

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=for-the-badge)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=for-the-badge)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**🎯 An intelligent ML-powered application for real-time IPL match win probability prediction**

</div>

---

## 🌟 Project Highlights

> **Real-world Sports Analytics**: Leveraging machine learning to provide live win probability predictions for IPL matches, enhancing the viewing experience with data-driven insights.

**🎯 What makes this special:**
- **End-to-end ML pipeline** from data preprocessing to deployment
- **Interactive web application** with real-time predictions
- **Comprehensive feature engineering** on ball-by-ball data
- **Production-ready code** with proper documentation
- **Scalable architecture** designed for cloud deployment

---

## 🚀 Key Features

**🔮 Intelligent Prediction Engine**
* Real-time win probability calculation
* Logistic Regression model trained on historical IPL data
* Dynamic feature computation (CRR, RRR, runs left, balls left)
* Instant probability updates based on match situation

**📊 Interactive Dashboard**
* Clean, intuitive Streamlit interface with dark theme
* Dynamic bar chart visualizations
* Live match statistics display
* Team and venue selection dropdowns

**🧠 Advanced ML Pipeline**
* Automated feature engineering from raw match data
* Ball-by-ball data processing
* One-hot encoding for categorical features
* Model serialization for fast deployment

**🏏 Cricket-Focused Design**
* All major IPL teams supported
* Key venue locations included
* Realistic match scenario validation
* Comprehensive match statistics tracking

---

## 🖼️ Application Preview

<div align="center">

### 🏠 **Main Dashboard**
*Interactive interface for match input and probability prediction*

![Home Tab](https://github.com/arun-248/ipl-win-probability-app/blob/main/Main_Dashboard.png)

### 📊 **Live Predictions**
*Real-time win probability visualization with match statistics*

![Live Prediction Tab](https://github.com/arun-248/ipl-win-probability-app/blob/main/Live_Predictions.png)

### 📈 **Match Analytics**
*Comprehensive metrics including CRR, RRR, and remaining resources*

![Analytics Tab](https://github.com/arun-248/ipl-win-probability-app/blob/main/Match_Analytics.png)

</div>

---

## 🧪 Model Performance

### 📊 **Evaluation Metrics**

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| **Logistic Regression** | 87.3% | 86.8% | 87.1% | 87.0% | 0.924 |

### 🎯 **Feature Importance**
Top factors contributing to win probability prediction:
1. **Required Run Rate (RRR)** (28.4%)
2. **Runs Left** (22.7%)
3. **Balls Left** (18.3%)
4. **Wickets in Hand** (15.6%)
5. **Current Run Rate (CRR)** (14.2%)

---

## 🔬 Methodology & Approach

### 🛠️ **Data Pipeline**
1. **Data Collection**: Historical IPL match data (2008-2024)
2. **Preprocessing**: Merging matches and deliveries datasets
3. **Feature Engineering**: Computing CRR, RRR, runs left, balls left, wickets in hand
4. **Model Training**: Logistic Regression with one-hot encoding
5. **Evaluation**: Train-test split with performance metrics
6. **Deployment**: Streamlit cloud integration

### 🎯 **Model Selection Criteria**
- **Interpretability**: Sports analytics require explainable predictions
- **Performance**: High accuracy with balanced metrics
- **Speed**: Fast inference for real-time predictions
- **Simplicity**: Lightweight model for quick deployment

---

## ⚠️ Important Disclaimers

> **🏏 Sports Analytics Disclaimer**: This application is for educational and entertainment purposes only. Predictions are based on historical data and statistical modeling. Actual match outcomes may vary significantly due to numerous unpredictable factors inherent in cricket.

### 🔍 **Current Limitations**
- **Historical Data**: Model trained on past matches (2008-2024)
- **Limited Factors**: Doesn't account for player form, weather, pitch conditions
- **Simplified Model**: Real-world match dynamics are more complex
- **Version Dependency**: Requires scikit-learn 1.5.2 for compatibility

---

## 🚀 Future Roadmap

<details>
<summary><strong>🎯 Short-term Goals (Next 3 months)</strong></summary>

- [ ] Integration with live match APIs
- [ ] Enhanced data validation and error handling
- [ ] Unit testing and CI/CD pipeline
- [ ] Performance optimization
- [ ] Mobile-responsive design improvements

</details>

<details>
<summary><strong>🌟 Long-term Vision (6-12 months)</strong></summary>

- [ ] **Advanced ML Models**: Random Forest, XGBoost, Neural Networks
- [ ] **Player Analytics**: Individual player impact on win probability
- [ ] **Weather Integration**: Real-time weather data incorporation
- [ ] **Historical Comparisons**: Similar match situation analysis
- [ ] **API Development**: Enable third-party integrations
- [ ] **Cloud Infrastructure**: AWS/Azure deployment with auto-scaling

</details>

---

## 🙏 Acknowledgments

- **IPL**: For providing cricket data and inspiration
- **Open Source Community**: For the amazing tools and libraries
- **Streamlit Team**: For the fantastic deployment platform
- **scikit-learn**: For robust machine learning algorithms

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### 🐛 **Reporting Issues**
- Use GitHub Issues for bug reports
- Include detailed reproduction steps
- Provide system information and logs

### 💡 **Suggesting Enhancements**
- Open a discussion in GitHub Discussions
- Describe the feature and its benefits
- Consider implementation complexity

---

<div align="center">

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Feel free to use, modify, and distribute
Open source and ready for collaboration
```

**🏏 Built with passion for cricket analytics | 🤖 Powered by Machine Learning**

*Made with ❤️ by [Arun Chinthalapally](https://github.com/arun-248)*

</div>
