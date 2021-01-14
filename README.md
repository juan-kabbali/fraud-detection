# fraud-detection
python project to detect fraudulent transactions using machine learning algorithms.

## How to setup this project

1. Download the project
    ```bash
    git clone https://github.com/juan-kabbali/fraud-detection.git
    ```
2. Create a virtual environment with python 3.7
3. Install all dependencies
    ```py
    pip install -r requirements.txt
    ```
4. Execute the `main.ipynb` file as a notebook

## Data directory
In this directory we can find out 4 different files containing the data frames used for the analysis.
  
* **light_train.txt**: unbalanced dataset containing 1/10 a tenth part rounded robin from the original dataset 
* **balance_train.txt**: balanced dataset containing all frauds e.i. 5402 and 5402 shuffled non-frauds
* **train.txt** unbalanced dataset for creating our models
* **test.txt** unbalanced dataset for  testing our models
* **transactions.txt** original unbalanced dataset

