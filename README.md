# Facial Recognition Assistance

![Facial Recognition Demo](https://i.ibb.co/GsF3FjX/webcam.png)
![csv input](https://i.ibb.co/4Y58Cfh/csv.png)

Facial Recognition Assistance is a Python-based facial recognition system designed for access control security. It checks if a person captured via a webcam is present in a database of images. If the person is recognized, the system logs the time and name of the individual in a CSV file. If the person is not recognized, it returns a message indicating that the person is not in the database.

## Features

- Facial recognition using Python and OpenCV.
- Logging of recognized individuals with their name and timestamp.
- Simple and efficient access control system.

## Prerequisites

Before you get started with this project, make sure you have the following dependencies installed:

- Python 3.9

## Getting Started

1) Clone this repository to your local machine:

    ```bash
    git clone https://github.com/dev-diegov/Facial_Recognition_Assistance.git
    ```

2) Navigate to the project directory:
    ```bash
    cd Facial_Recognition_Assistance
    ```

3) You can install the dependencies using pip:

    ```bash
    pip install requeriments.txt
    ```

4) Run the program:

    ```bash
    python facial_recognition.py
    ```
   
## Usage

- When you run the program, it will access your webcam and capture the face of the person in front of the camera.
- The captured face is then compared to the images in the database.
- If a match is found, the system logs the person's name and the timestamp in a CSV file.
- If no match is found, a message indicating that the person is not in the database is displayed.

## Configuration

You can configure the following settings in the config.json file:

- 'path': Path to the folder containing the images of individuals in the database.
- 'log_file': Path to the CSV file where recognized individuals and timestamps are logged.

## Contributing

If you'd like to contribute to this project, please follow these steps:

- Fork the repository on GitHub.
- Clone your fork to your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive messages.
- Push your changes to your fork on GitHub.
- Create a pull request to the original repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- This project was inspired by the need for a simple and effective access control system using facial recognition.

## Contact

If you have any questions or suggestions, please feel free to contact the project author, Diego Donoso Vera.

Happy facial recognition!


You can copy and paste this content into your project's README.md file on GitHub, making sure to update any details and links as needed.
