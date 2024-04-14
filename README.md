# FarmAsist #

FarmaAsists is a project aimed at assisting farmers associated with potato crops, to detect  the diseases of those crops and also providing them with relevant measures, to prevent them. 

## Features 

- Accurate Potato Disease Detection
- A chatbot for any Potato Disease related preventions and specific cases

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/FarmaAsists.git
```

2. Install dependencies:

```bash
pip install tensorflow
pip install flask
pip install pandas
pip install numpy
```

## Usage

To start the application, run:

```bash
python app.py
```

Visit `http://localhost:3000` in your web browser to access the application.

## Technologies :
**Frontend:** CSS, HTML, Javascript

**Backend:** Flask

**ML:** Pandas, TensorFlow, Scikit-learn

**Database:** MySQL

## Approach

+---------------------+

| Data Collection     |

+---------------------+

         |
         v
         
+---------------------+

| Data Preprocessing  (using Keras image preprocessing) |
+---------------------+

         |
         v
         
+--------------------------+

| Data Augmentation (Specially in the Healthy category) |

+--------------------------+

         |
         v
         
+----------------------+

| Model Building (DenseNet21 + Autoencoder + CNN + 1 dense layer) |

+----------------------+

         |
         v
         
+--------------------------+

| Model Training & Tuning (Used Dropout layer, Early-stopping, learning-rate scheduler) |

+--------------------------+

         |
         v
         
+--------------------------+

| Model Evaluation (F1 score & accuracy) |

+--------------------------+

For the chatbot, we have used the open-source Google Gemini API.

## Results 
As it is an imbalanced dataset, so we have chosen the F1 score as our evaluation metric.
| Category                           | F1 Score |
|------------------------------------|----------|
| Healthy            | 0.93    |
| Early Blight          | 0.99     |
| Late Blight | 0.98     |

## Video :

https://drive.google.com/file/d/19REm2TT5T5zIQPnLkm11MjdHd3vwAGeV/view?usp=sharing

## Challenges :

Despite encountering unavoidable circumstances and facing a shortage of time, our team persevered through numerous challenges in the development phase. Through collaborative efforts and unwavering determination, we successfully navigated these obstacles and ultimately delivered the application.

## Improvements

**Enhanced UI with React:**

Implementing React for improved frontend interactivity and user experience.

**MySQL Database Connection:**

Resolving unexpected errors hindering registration and login page integration with the MySQL database.

**Advanced ML Models and Hyperparameter Tuning:**

Incorporating ViT and ResNet models, coupled with rigorous hyperparameter tuning, to enhance ML model robustness and accuracy.  

**More types of Vegetables:**

We can train the model on the tomato and pepper-bell image dataset as well.

## Contributing

We welcome contributions from the community! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

