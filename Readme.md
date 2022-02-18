# Privacy_Policies_text_classifier

This repository contains the implementation of Support Vector Machine (SVM) Machine Learning model to differenciate between main webpage of certain domain and privacy policy webpage of the same domian. It will be also tested in landing pages.

## How it was created

### Generating Dataset

playstore_scrapper.py file was firstly used to get top 100 apps from Google Play Store those will be used to train and test the ML model. Afterwars was also used to get another apps list used for validation (at ./Validation/validation_apps.txt) ignoring repeated apps. This last set was used to validate the ML model.

Once lists were created, get_privacy_policy_text.py was used to recover app's privacy policy text from the published URL in Google Play Store. Texts can be found at policies_top_100_apps folder.

Similarly, get_app_landing_page_text.py was used to recover main app's page text for each app. Texts can be found at text_top_100_apps folder.

Then, join_txt_in_csv.py was used to create a csv with all texts and policies previously recovered (it was used for test-train set and validation set, modify folder and file to choose each one). This csv file is named "ispolicy_annotated.csv", which was afterwards manually annotated introducing "Ispolicy" column, which determines if whether the text belongs to a privacy policy or not.

### Creation of Machine Learning SVM Model

The generation of the model was implemented in IsPolicyClassifierML.ipynb Jupyter Notebook. Generating the trained classifier model "trained_ispolicy_classifier.pkl" and it's tested metrics "Policy_Classifier_Metrics.txt".

Policy_Classifier_traintest_Confussion_Matrix.png refers to the train test set Confussion Matrix while Policy_Classifier_validation_Confussion_Matrix.png refers to the validation set Confussion Matrix.

### Machine Learning SVM Model Metrics

* Train-Test Set:

{'precision': 1.0,
 'recall': 1.0,
 'f1-score': 1.0,
 'NVP': 1.0,
 'specificity': 1.0,
 'f1-score-negative': 1.0,
 'accuracy': 1.0,
 'conf_matrix': [16, 0, 0, 26]}

* 5-Fold Cross Validation:

{'precision': 1.0,
 'recall': 1.0,
 'f1-score': 1.0,
 'NVP': 1.0,
 'specificity': 1.0,
 'f1-score-negative': 1.0,
 'accuracy': 1.0,
 'confusion_matrix': [[13, 0, 0, 20],
  [13, 0, 0, 20],
  [14, 0, 0, 19],
  [14, 0, 0, 19],
  [14, 0, 0, 19]]}

* Validation Set:

{'precision': 1.0,
 'recall': 0.9411764705882353,
 'f1-score': 0.9696969696969697,
 'NVP': 0.9512195121951219,
 'specificity': 1.0,
 'f1-score-negative': 0.975,
 'accuracy': 0.9705882352941176,
 'conf_matrix': [32, 2, 0, 39]}
