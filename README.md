# CasualHealthcare

A collection of services to make quality healthcare, that can be used for a variety of purposes, utilizing the power of Artificial Intelligence, and paving the future for AI in healthcare.

## Setup

1. Make sure you have `python3` and `pip` installed.
2. Clone this repository OR download the latest stable release on the right.
3. Unzip the folder if it isn't already unzipped.
4. In the terminal, cd to the folder and keep the terminal open.
5. Execute the following command. This command installs all of the needed packages using `pip`

        pip install -r requirements.txt
   
5b. Depending on your OS, you may have to install the tensorflow application, install it as you would usually in your OS

# azh412's Pneumonia detection with Artificial Intelligence (Convolutional Neural Network)

This is PneumoniaDiagnose, an artificially intelligent Neural Network that can detect pneumonia by the means of chest x-rays.

**WARNING:** THIS IS NOT FINISHED, CURRENT ACCURACY IS ≈ 75%

For the best accuracy and performance, use the releases. (On the right)

## Training

1. `cd` to the folder named pneumoniadiagnose/
2. Execute the following command to train the neural network. 

    **NOTE:** If you have multiple versions of Python, you must replace the word `python` with `python3`

        python pneumonia.py trainpneumonia.py train test pneumoniamodel.h5
        
    Be sure to say `yes` when asked to save the trained model.
Now you can start using the Neural Network!

## Usage
Execute the following command, and make sure you replace the word IMAGE with your image name in your filesystem. 

   **NOTE:** If you have multiple versions of Python, you must replace the word `python` with `python3`

        python pneumonia.py pneumoniamodel.h5 IMAGE


If you liked this repository, be sure to `star` it!

Thank you!

-azh
