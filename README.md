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
  
* **light_train.txt**: balanced data frame containing 2 673 frauds and 5 000 non-frauds
* **train.txt** unbalanced data frame containing 2 673 frauds and 1 045 902 non-frauds
* **train_chunk.txt** train's unbalanced chunk data frame containing 855 frauds and 263 288 non-frauds
* **transactions.txt** test data frame containing 6 257 and 2 225 112 non-frauds

