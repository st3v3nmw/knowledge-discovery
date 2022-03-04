MLP MULTICLASS CLASSIFIER

risk_data.csv is the data file

INSTALLATION

Install requirements in your venv
    pip install -r requirements.txt

This is needed for plotting the confusion matrix

    sudo apt-get install python3-tk

RUNNING

run preprocess.py ( here you can change for various bins)
run mlp.py for the results

RESULTS

A confusion matrix eg. see (report/sample_output_of_our_mlp.png) and an accuracy percentage (bash output)

great article explaining confusion matrix generated

https://www.analyticsvidhya.com/blog/2020/04/confusion-matrix-machine-learning/


TWEAKING PARAMETERS FOR BETTER RESULTS

change the "bin category settings" in the preprocess.py to generated different datasets and experiment with various bins for the data

the program mlp.py also gives the best parameter which can provide more efficient results for the datasets